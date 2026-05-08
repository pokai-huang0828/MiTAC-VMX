#!/usr/bin/env python3
"""Build knowledge/index.html — single self-contained HTML hub of all knowledge/*.md files.

Usage:
    python3 knowledge/_build_index.py

Features:
    - 8 tabs:總覽 / 6 分類 / 待釐清(自動掃描)
    - 重要性 ★ 評分;Sidebar 可伸縮 + 拖曳 resize
    - URL/VMX-/HAWK- 自動超連結
    - 內部 .md 連結改走 hub 內路由(看 preview,不開原始碼)
    - 上一頁按鈕、響應式 layout、過場動畫
"""
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

HERE = Path(__file__).parent  # knowledge/
REPO_ROOT = HERE.parent
OUT = REPO_ROOT / "websiteview" / "knowledge.html"

# Category metadata: folder prefix → (display name, icon)
CATEGORIES = {
    "01_product-knowledge":   ("產品知識",       "🔧"),
    "02_organization-map":    ("組織與利害關係人", "👥"),
    "03_systems-architecture": ("系統架構",       "🏛"),
    "04_pm-frameworks":       ("PM 框架",         "📐"),
    "05_workflows":           ("工作流 SOP",      "⚙️"),
    "06_calibration-log":     ("校正紀錄",        "🎯"),
}

# Importance per filename (1-5 stars). README handled separately (priority 0, top).
PRIORITY = {
    # 01_product-knowledge
    "kb-cheatsheet.md":         5,
    "machines-spec.md":         5,
    "adas-dms-events.md":       5,
    "voice-alerts.md":          4,
    "diagnostics.md":           4,
    "miai-roadmap-2026.md":     4,
    "kb-full-catalog.md":       3,
    "safety-score.md":          3,
    "sales-faq.md":             3,
    "storage-mechanism.md":     2,
    "visionagent-app.md":       2,
    # 02_organization-map
    "coffee-chat-questions.md": 5,
    "stakeholders.md":          5,
    # 03_systems-architecture
    "portal-architecture.md":   5,
    "plan-types.md":            5,
    "server-ai-architecture.md": 4,
    "master-portal-operations.md": 3,
    "vehicle-classification.md": 3,
    # 04_pm-frameworks
    "three-truth-layers.md":    5,
    "core-principles.md":       5,
    "commitment-framework.md":  5,
    "internal-comm-gap.md":     4,
    "tech-client-comm.md":      4,
    "ui-change-management.md":  3,
    # 05_workflows
    "html-presentation-pipeline.md": 5,
    "mdt-2026-template.md":     5,
    "sheet-jira-sync-sweeper.md": 4,
    "customer-onboarding.md":   4,
    "troubleshooting.md":       4,
    "memory-system.md":         3,
    # 06_calibration-log
    "critical-facts-log.md":    5,
    "vmx-7404-tracking.md":     5,
    "ai-team-sheet-snapshot-2026-05-05.md": 4,
    "sheet-jira-mismatches.md": 4,
    "roadmap-vs-internal.md":   4,
}

PENDING_KEYWORDS = [
    "待釐清", "待確認", "待問", "待補", "待動作",
    "待對齊", "待裁示",
    "TBD", "TODO",
]
PENDING_RE = re.compile("|".join(re.escape(k) for k in PENDING_KEYWORDS))

# Jira ticket patterns. Linked to MiTAC R&D Jira host.
JIRA_HOST = "https://jira.navman.co.nz/jira/browse"
JIRA_RE = re.compile(r"\b(VMX|HAWK|BMS)-(\d+)\b")

# Bare URL pattern (used as a fallback when magiclink doesn't catch one)
URL_RE = re.compile(r"(?<![\"'>=])\bhttps?://[^\s<>'\"`]+", re.IGNORECASE)

MD_EXTENSIONS = [
    "extra",
    "sane_lists",
    "smarty",
    "toc",
    "pymdownx.tilde",
    "pymdownx.superfences",
    "pymdownx.magiclink",  # auto-link bare URLs (https://… etc.)
]

MD_EXTENSION_CONFIGS = {
    "pymdownx.magiclink": {
        "hide_protocol": False,
        "repo_url_shortener": False,
    },
}


def md_to_html(text: str) -> str:
    md = markdown.Markdown(
        extensions=MD_EXTENSIONS,
        extension_configs=MD_EXTENSION_CONFIGS,
        output_format="html5",
    )
    return md.convert(text)


def slugify(s: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", s, flags=re.UNICODE).strip("-")
    return s.lower() or "doc"


def extract_pending(text: str) -> list[dict]:
    items = []
    for i, line in enumerate(text.splitlines(), start=1):
        m = PENDING_RE.search(line)
        if not m:
            continue
        clean = line.strip()
        if len(clean) > 220:
            clean = clean[:217] + "…"
        items.append({"line_no": i, "line": clean, "keyword": m.group(0)})
    return items


def get_priority(filename: str) -> int:
    if filename == "README.md":
        return 0
    return PRIORITY.get(filename, 3)


def collect_doc_registry() -> dict:
    """First pass: build {basename: (cat_id, doc_id)} so we can rewrite cross-doc .md links."""
    registry = {}
    for folder in sorted(HERE.iterdir()):
        if not folder.is_dir() or folder.name not in CATEGORIES:
            continue
        for md_file in folder.glob("*.md"):
            doc_id = slugify(f"{folder.name}--{md_file.stem}")
            registry[md_file.name] = (folder.name, doc_id)
    return registry


# Track external .md files referenced by hub (resolved to absolute paths)
# so we can generate companion preview HTML for them. Populated by post_process_html.
EXTERNAL_MD_REFS: set[Path] = set()


def post_process_html(rendered: str, registry: dict) -> str:
    """Apply transforms with a single BS4 parse:
    1. Internal .md links → in-app hash routes (so click shows preview, not raw md).
    2. Bare VMX-/HAWK-/BMS- ticket text → Jira links.
    3. Rewrite ../../ paths → ../ (source markdown lives 2 levels deep at
       knowledge/<cat>/X.md, but output html lives 1 level deep at
       websiteview/knowledge.html, so ../../ would escape repo root).
    4. External .md links (outside knowledge/) → companion .html preview
       (Kenny rule: md must always render as preview, never raw text).
    """
    soup = BeautifulSoup(rendered, "html.parser")

    # 1. Rewrite anchors pointing to .md files (any subpath, any anchor)
    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Strip query/anchor for file matching
        m = re.match(r"^([^?#]+\.md)(?:[?#].*)?$", href, flags=re.IGNORECASE)
        if not m:
            continue
        basename = m.group(1).split("/")[-1]
        if basename in registry:
            cat_id, doc_id = registry[basename]
            a["href"] = f"#{cat_id}/{doc_id}"
            classes = a.get("class", [])
            if "internal-doc-link" not in classes:
                classes.append("internal-doc-link")
            a["class"] = classes
            a["data-cat"] = cat_id
            a["data-doc"] = doc_id

    # 3. Rewrite ../../ → ../ for href and src (depth correction)
    for tag in soup.find_all(["a", "img", "script", "link"]):
        for attr in ("href", "src"):
            v = tag.get(attr)
            if not v:
                continue
            if v.startswith("../../"):
                tag[attr] = "../" + v[len("../../"):]

    # 4. External .md links → companion .html preview
    # After step 1+3, internal .md were converted to hash routes; remaining .md
    # links are external (meetings/, case-learning/ etc). Rewrite to .html and
    # track for preview generation.
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
            continue
        m = re.match(r"^([^?#]+\.md)((?:[?#]).*)?$", href, flags=re.IGNORECASE)
        if not m:
            continue
        md_path = m.group(1)
        suffix = m.group(2) or ""
        # Resolve from output location (websiteview/) to absolute path
        abs_md = (REPO_ROOT / "websiteview" / md_path).resolve()
        if not abs_md.exists():
            continue
        try:
            abs_md.relative_to(REPO_ROOT)
        except ValueError:
            continue
        EXTERNAL_MD_REFS.add(abs_md)
        # Rewrite href: foo.md → foo.md.html
        a["href"] = md_path + ".html" + suffix

    # 5. Folder-only links (e.g., "01_product-knowledge/") → hash routes
    # In source markdown, knowledge/README.md links to sibling category folders;
    # in rendered hub these should jump to the category's first doc.
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(("http://", "https://", "#", "mailto:", "javascript:")):
            continue
        # Normalize: strip leading ./ and trailing /
        normalized = href.lstrip("./").rstrip("/")
        if normalized in CATEGORIES:
            a["href"] = f"#{normalized}"
            classes = a.get("class", [])
            if "internal-doc-link" not in classes:
                classes.append("internal-doc-link")
            a["class"] = classes
            a["data-cat"] = normalized
            # Set data-doc to first doc id (README) so click handler works
            doc_id = slugify(f"{normalized}--README")
            a["data-doc"] = doc_id

    # 2. Auto-link Jira tickets in plain text (skip text already inside <a>/<code>)
    SKIP_PARENTS = {"a", "code", "pre"}
    text_nodes = list(soup.find_all(string=True))
    for tn in text_nodes:
        if tn.parent and tn.parent.name in SKIP_PARENTS:
            continue
        # Ascend to check ancestor
        parent = tn.parent
        skip = False
        while parent is not None:
            if getattr(parent, "name", None) in SKIP_PARENTS:
                skip = True
                break
            parent = parent.parent
        if skip:
            continue
        s = str(tn)
        if not JIRA_RE.search(s):
            continue
        # Build replacement nodes
        new_nodes = []
        last = 0
        for m in JIRA_RE.finditer(s):
            if m.start() > last:
                new_nodes.append(s[last:m.start()])
            ticket = m.group(0)
            link = soup.new_tag(
                "a",
                href=f"{JIRA_HOST}/{ticket}",
                target="_blank",
                rel="noopener",
            )
            link["class"] = ["ext-link", "jira-link"]
            link.string = ticket
            new_nodes.append(link)
            last = m.end()
        if last < len(s):
            new_nodes.append(s[last:])
        # Replace
        for n in reversed(new_nodes):
            tn.insert_after(n)
        tn.extract()

    # 3. Mark external links so we can give them a visual hint + open in new tab
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("http://") or href.startswith("https://"):
            classes = a.get("class", [])
            if "ext-link" not in classes:
                classes.append("ext-link")
            a["class"] = classes
            if not a.get("target"):
                a["target"] = "_blank"
            if not a.get("rel"):
                a["rel"] = "noopener"

    return str(soup)


DOC_FILE_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · Knowledge Hub</title>
<link rel="stylesheet" href="../css/shared.css">
<link rel="stylesheet" href="../css/knowledge.css">
<style>
  body {{ background: var(--bg); margin: 0; padding: 0; height: auto; overflow: auto; }}
  .doc-standalone-topbar {{
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: #fff; padding: 12px 24px;
    display: flex; align-items: center; gap: 14px; flex-wrap: wrap;
  }}
  .doc-standalone-topbar a.back {{
    color: rgba(255,255,255,0.92); text-decoration: none; font-size: 13px;
    background: rgba(255,255,255,0.15); padding: 5px 11px; border-radius: 6px;
  }}
  .doc-standalone-topbar a.back:hover {{ background: rgba(255,255,255,0.28); }}
  .doc-standalone-topbar .heading {{
    font-weight: 600; font-size: 15px; letter-spacing: 0.2px;
  }}
  .doc-standalone-topbar .filename {{
    margin-left: auto; font-size: 12px; opacity: 0.78;
    font-family: 'SF Mono', Consolas, monospace;
  }}
  .doc-standalone-meta {{
    max-width: 920px; margin: 0 auto;
    padding: 14px 32px 0;
    font-size: 12px; color: var(--text-muted);
  }}
  main.doc-standalone {{
    max-width: 920px; margin: 0 auto; padding: 18px 32px 24px;
  }}
  .doc-prevnext {{
    max-width: 920px; margin: 0 auto;
    padding: 0 32px 80px;
    display: flex; justify-content: space-between; gap: 16px;
    border-top: 1px solid var(--border); padding-top: 24px;
  }}
  .doc-prevnext a {{
    flex: 1; max-width: 48%;
    padding: 12px 16px; border-radius: 8px;
    background: var(--card); border: 1px solid var(--border);
    text-decoration: none; color: var(--text);
    transition: all 0.15s var(--ease);
  }}
  .doc-prevnext a:hover {{
    border-color: var(--primary); transform: translateY(-1px);
    box-shadow: var(--shadow);
  }}
  .doc-prevnext a.next {{ text-align: right; margin-left: auto; }}
  .doc-prevnext .label {{
    display: block; font-size: 10px; font-weight: 700;
    color: var(--text-muted); text-transform: uppercase;
    letter-spacing: 1px; margin-bottom: 4px;
  }}
  .doc-prevnext .doc-name {{
    font-size: 14px; font-weight: 600; color: var(--primary);
  }}
</style>
</head>
<body>
<header class="doc-standalone-topbar">
  <a class="back" href="../knowledge.html#{cat_id}/{doc_id}" title="返回 Knowledge Hub">← Knowledge Hub</a>
  <span class="heading">{cat_icon} {cat_name} · {title}</span>
  <span class="filename">{filename}</span>
</header>
<div class="doc-standalone-meta">最後更新:{last_updated}</div>
<main class="doc-standalone">
  <div class="doc-content">
{rendered_html}
  </div>
</main>
<nav class="doc-prevnext">
{prevnext_html}
</nav>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image preview">
  <button class="lightbox-close" type="button" aria-label="Close preview" onclick="document.getElementById('lightbox').classList.remove('is-open')">×</button>
  <img alt="">
  <div class="lightbox-caption"></div>
</div>
<script src="../js/lightbox.js" defer></script>
</body>
</html>
"""


def _prevnext_block(prev_doc: dict | None, next_doc: dict | None) -> str:
    parts = []
    if prev_doc:
        parts.append(
            f'  <a class="prev" href="{prev_doc["id"]}.html" rel="prev">'
            f'<span class="label">← 上一篇</span>'
            f'<span class="doc-name">{html.escape(prev_doc["title"])}</span></a>'
        )
    else:
        parts.append('  <span></span>')
    if next_doc:
        parts.append(
            f'  <a class="next" href="{next_doc["id"]}.html" rel="next">'
            f'<span class="label">下一篇 →</span>'
            f'<span class="doc-name">{html.escape(next_doc["title"])}</span></a>'
        )
    else:
        parts.append('  <span></span>')
    return "\n".join(parts)


def write_doc_file(docs_dir: Path, doc_id: str, title: str, cat_id: str,
                    cat_name: str, cat_icon: str, filename: str,
                    rendered_html: str, last_updated: str,
                    prev_doc: dict | None = None,
                    next_doc: dict | None = None) -> None:
    """Each knowledge doc → its own websiteview/docs/<doc_id>.html with
    last-updated stamp + prev/next nav baked in."""
    page = DOC_FILE_TEMPLATE.format(
        title=html.escape(title),
        cat_id=cat_id,
        doc_id=doc_id,
        cat_name=html.escape(cat_name),
        cat_icon=cat_icon,
        filename=html.escape(filename),
        last_updated=html.escape(last_updated),
        rendered_html=rendered_html,
        prevnext_html=_prevnext_block(prev_doc, next_doc),
    )
    (docs_dir / f"{doc_id}.html").write_text(page, encoding="utf-8")


def _plain_text(rendered_html: str) -> str:
    """Strip HTML tags → plain text for search index."""
    return BeautifulSoup(rendered_html, "html.parser").get_text(" ", strip=True)


def build():
    registry = collect_doc_registry()
    categories: list[dict] = []
    pending_groups: list[dict] = []

    docs_dir = REPO_ROOT / "websiteview" / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    n_doc_files = 0

    for folder in sorted(HERE.iterdir()):
        if not folder.is_dir() or folder.name not in CATEGORIES:
            continue
        display, icon = CATEGORIES[folder.name]
        docs = []
        cat_pending: list[dict] = []
        md_files = list(folder.glob("*.md"))
        md_files.sort(key=lambda p: (
            0 if p.name == "README.md" else 1,
            -get_priority(p.name),
            p.name,
        ))
        # First pass: collect doc metadata + rendered html in memory so we can
        # compute prev/next links (each doc needs to know its neighbours).
        rendered_docs: list[dict] = []
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")
            doc_id = slugify(f"{folder.name}--{md_file.stem}")
            m = re.search(r"^# (.+)$", text, flags=re.MULTILINE)
            title = m.group(1).strip() if m else md_file.stem
            priority = get_priority(md_file.name)
            pending = extract_pending(text)
            rendered = md_to_html(text)
            rendered = post_process_html(rendered, registry)
            mtime = datetime.fromtimestamp(md_file.stat().st_mtime)
            rendered_docs.append({
                "doc_id": doc_id,
                "title": title,
                "filename": md_file.name,
                "priority": priority,
                "pending": pending,
                "rendered": rendered,
                "last_updated": mtime.strftime("%Y-%m-%d"),
                "search_text": _plain_text(rendered)[:8000],  # cap to avoid bloat
            })

        # Second pass: write doc files with prev/next links + accumulate JSON
        for i, rd in enumerate(rendered_docs):
            prev_doc = (
                {"id": rendered_docs[i - 1]["doc_id"], "title": rendered_docs[i - 1]["title"]}
                if i > 0 else None
            )
            next_doc = (
                {"id": rendered_docs[i + 1]["doc_id"], "title": rendered_docs[i + 1]["title"]}
                if i < len(rendered_docs) - 1 else None
            )
            write_doc_file(
                docs_dir, rd["doc_id"], rd["title"],
                cat_id=folder.name, cat_name=display, cat_icon=icon,
                filename=rd["filename"], rendered_html=rd["rendered"],
                last_updated=rd["last_updated"],
                prev_doc=prev_doc, next_doc=next_doc,
            )
            n_doc_files += 1
            docs.append({
                "id": rd["doc_id"],
                "filename": rd["filename"],
                "title": rd["title"],
                "priority": rd["priority"],
                "pending_count": len(rd["pending"]),
                "last_updated": rd["last_updated"],
                "text": rd["search_text"],  # for full-text search filter
                # rendered html lives in docs/<doc_id>.html — fetched on click
            })
            if rd["pending"]:
                cat_pending.append({
                    "doc_id": rd["doc_id"],
                    "filename": rd["filename"],
                    "title": rd["title"],
                    "items": rd["pending"],
                })
        categories.append({
            "id": folder.name,
            "name": display,
            "icon": icon,
            "docs": docs,
        })
        if cat_pending:
            pending_groups.append({
                "category_id": folder.name,
                "category_name": display,
                "category_icon": icon,
                "files": cat_pending,
            })

    overview_md = HERE / "README.md"
    if overview_md.exists():
        overview_html = post_process_html(
            md_to_html(overview_md.read_text(encoding="utf-8")), registry
        )
        overview_mtime = datetime.fromtimestamp(overview_md.stat().st_mtime)
        write_doc_file(
            docs_dir, "overview-readme",
            title="Knowledge Base 總覽",
            cat_id="overview", cat_name="總覽", cat_icon="🏠",
            filename="knowledge/README.md",
            rendered_html=overview_html,
            last_updated=overview_mtime.strftime("%Y-%m-%d"),
        )
        n_doc_files += 1

    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "categories": categories,
        "pending_groups": pending_groups,
        "pending_total": sum(
            sum(len(f["items"]) for f in g["files"]) for g in pending_groups
        ),
    }

    OUT.write_text(render_template(payload), encoding="utf-8")
    total_docs = sum(len(c["docs"]) for c in categories)
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    print(f"  {len(categories)} categories, {total_docs} docs")
    print(f"  pending items: {payload['pending_total']}")
    print(f"  per-doc files in websiteview/docs/: {n_doc_files}")

    # Generate companion .html preview for external .md files referenced from hub
    # (Kenny rule: md must always render as preview, not raw text)
    n_previews = generate_external_md_previews()
    print(f"  external .md previews: {n_previews}")


EXTERNAL_PREVIEW_TEMPLATE = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  :root {{
    --mdt-blue: #5B9BD5;
    --mdt-blue-dark: #2E5C8A;
    --mdt-orange: #ED7D31;
    --mdt-orange-dark: #C25E1B;
    --mdt-text: #2c3e50;
    --mdt-text-muted: #5a6c7d;
    --mdt-text-light: #95a5a6;
    --mdt-border: #e1e8ed;
    --mdt-card: #fff;
    --mdt-bg: #F4F6FA;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: "Calibri", -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft JhengHei", sans-serif;
    background: var(--mdt-bg);
    color: var(--mdt-text);
    margin: 0;
    line-height: 1.7;
  }}
  .topbar {{
    background: linear-gradient(135deg, var(--mdt-blue) 0%, var(--mdt-blue-dark) 100%);
    color: #fff;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
  }}
  .topbar .back {{
    color: rgba(255,255,255,0.9); text-decoration: none; font-size: 13px;
    padding: 5px 10px; border-radius: 6px; background: rgba(255,255,255,0.15);
  }}
  .topbar .back:hover {{ background: rgba(255,255,255,0.28); }}
  .topbar .source-path {{
    margin-left: auto; font-size: 12px; opacity: 0.75; font-family: ui-monospace, monospace;
  }}
  main {{
    max-width: 920px; margin: 0 auto; padding: 32px 28px 80px;
  }}
  main h1 {{ color: var(--mdt-blue-dark); border-bottom: 3px solid var(--mdt-orange); padding-bottom: 8px; margin-top: 0; }}
  main h2 {{ color: var(--mdt-blue-dark); border-left: 4px solid var(--mdt-orange); padding-left: 12px; margin-top: 32px; }}
  main h3 {{ color: var(--mdt-blue); margin-top: 24px; }}
  main blockquote {{
    border-left: 4px solid var(--mdt-orange); background: #FFF7EE;
    margin: 16px 0; padding: 10px 16px; border-radius: 0 6px 6px 0;
  }}
  main code {{
    background: #eef2f7; padding: 2px 6px; border-radius: 4px;
    font-family: ui-monospace, "Cascadia Code", monospace; font-size: 0.92em;
  }}
  main pre {{
    background: #1e293b; color: #e2e8f0; padding: 16px; border-radius: 8px;
    overflow-x: auto; line-height: 1.5;
  }}
  main pre code {{ background: transparent; color: inherit; padding: 0; }}
  main table {{
    border-collapse: collapse; width: 100%; margin: 14px 0; background: #fff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }}
  main th, main td {{
    border: 1px solid var(--mdt-border); padding: 8px 12px; text-align: left;
    font-size: 14px; vertical-align: top;
  }}
  main th {{ background: var(--mdt-blue); color: #fff; font-weight: 600; }}
  main tr:nth-child(even) td {{ background: #f8fafc; }}
  main a {{ color: var(--mdt-blue); text-decoration: none; border-bottom: 1px dotted var(--mdt-blue); }}
  main a:hover {{ color: var(--mdt-orange); border-bottom-color: var(--mdt-orange); }}
  main ul, main ol {{ padding-left: 1.6em; }}
  main li {{ margin: 4px 0; }}
  main hr {{ border: none; border-top: 1px solid var(--mdt-border); margin: 28px 0; }}
  .footer {{
    text-align: center; padding: 20px; font-size: 12px;
    color: var(--mdt-text-light); border-top: 1px solid var(--mdt-border);
  }}
</style>
</head>
<body>
<header class="topbar">
  <a class="back" href="{back_url}" title="返回 Knowledge Hub">← Knowledge Hub</a>
  <strong>📄 {title}</strong>
  <span class="source-path">{source_path}</span>
</header>
<main>
{body_html}
</main>
<footer class="footer">由 <code>knowledge/_build_index.py</code> 從 <code>{source_path}</code> 自動產生 · MDT 2026 Theme</footer>
</body>
</html>
"""


def generate_external_md_previews() -> int:
    """For each external .md referenced from hub, generate companion .html preview."""
    count = 0
    for md_path in sorted(EXTERNAL_MD_REFS):
        out_path = md_path.with_name(md_path.name + ".html")
        try:
            md_text = md_path.read_text(encoding="utf-8")
        except Exception:
            continue
        # Title from first H1, fallback to stem
        m = re.search(r"^# (.+)$", md_text, flags=re.MULTILINE)
        title = m.group(1).strip() if m else md_path.stem
        body_html = md_to_html(md_text)
        # Compute back URL: from out_path back to websiteview/knowledge.html
        try:
            rel = Path("..") / OUT.relative_to(REPO_ROOT)
            # We want path from out_path's parent to OUT
            import os
            back_url = os.path.relpath(OUT, start=out_path.parent).replace("\\", "/")
        except Exception:
            back_url = "../websiteview/knowledge.html"
        try:
            source_rel = md_path.relative_to(REPO_ROOT).as_posix()
        except ValueError:
            source_rel = md_path.name
        page = EXTERNAL_PREVIEW_TEMPLATE.format(
            title=html.escape(title),
            back_url=html.escape(back_url),
            source_path=html.escape(source_rel),
            body_html=body_html,
        )
        out_path.write_text(page, encoding="utf-8")
        count += 1
    return count


def render_template(payload: dict) -> str:
    # Pretty-print JSON so the source HTML is readable (was a single mega-line).
    # `</` is escaped to `<\/` so a stray closing tag inside any string field
    # cannot terminate the surrounding <script> block prematurely.
    data_json = json.dumps(payload, ensure_ascii=False, indent=2)
    data_json = data_json.replace("</", "<\\/")
    return TEMPLATE.replace("__DATA_JSON__", data_json).replace(
        "__GENERATED_AT__", html.escape(payload["generated_at"])
    )


# --- HTML template ---------------------------------------------------------

TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kenny VMX Knowledge Hub</title>
<link rel="stylesheet" href="css/shared.css">
<link rel="stylesheet" href="css/components.css">
<link rel="stylesheet" href="css/knowledge.css">

</head>
<body>

<header class="topbar">
  <div class="topbar-brand-flex">
    <button class="sidebar-toggle" id="sidebarToggle" title="收合 / 展開 sidebar (Ctrl+B)">☰</button>
    <a class="topbar-back-link" href="index.html" title="返回 Web Hub">← Web Hub</a>
    <h1>📚 Kenny VMX <span class="accent">Knowledge Hub</span></h1>
  </div>
  <div class="meta">
    <span class="topbar-meta-info">產生於 __GENERATED_AT__</span>
    <input type="search" id="searchBox" placeholder="搜尋文件名稱…" autocomplete="off">
  </div>
</header>

<nav class="tabs" id="tabs"></nav>

<div class="layout" id="layout">
  <aside class="sidebar" id="sidebar">
    <div class="resize-handle" id="resizeHandle"></div>
  </aside>
  <main class="content" id="content"></main>
</div>

<script id="hub-data" type="application/json">
__DATA_JSON__
</script>

<script>
(function () {
  const data = JSON.parse(document.getElementById("hub-data").textContent);
  const tabsEl    = document.getElementById("tabs");
  const sidebarEl = document.getElementById("sidebar");
  const contentEl = document.getElementById("content");
  const searchEl  = document.getElementById("searchBox");
  const layoutEl  = document.getElementById("layout");
  const toggleEl  = document.getElementById("sidebarToggle");
  const handleEl  = document.getElementById("resizeHandle");

  const PENDING_RE = /(待釐清|待確認|待問|待補|待動作|待對齊|待裁示|TBD|TODO)/g;

  // Pseudo-categories
  const overviewCat = {
    id: "overview", name: "總覽", icon: "🏠",
    docs: [{
      id: "overview-readme",
      filename: "knowledge/README.md",
      title: "Knowledge Base 總覽",
      priority: 0,
      pending_count: 0,
    }],
  };
  const pendingCat = { id: "pending", name: "待釐清", icon: "📌", docs: [], isPending: true };
  const allCats = [overviewCat, ...data.categories, pendingCat];

  // ─── Per-doc HTML loader (each doc lives in docs/<id>.html) ───
  const docHtmlCache = Object.create(null);
  let loadToken = 0;

  async function loadDocHtml(docId) {
    if (docHtmlCache[docId] != null) return docHtmlCache[docId];
    try {
      const res = await fetch(`docs/${docId}.html`);
      if (!res.ok) throw new Error("HTTP " + res.status);
      const text = await res.text();
      const dom = new DOMParser().parseFromString(text, "text/html");
      const node = dom.querySelector(".doc-content");
      const html = node
        ? node.innerHTML
        : `<div class="empty">⚠️ docs/${docId}.html 缺少 .doc-content 節點</div>`;
      docHtmlCache[docId] = html;
      return html;
    } catch (e) {
      return `<div class="empty">⚠️ 無法載入 <code>docs/${docId}.html</code>(${e.message})。<br>若以 <code>file://</code> 開啟,fetch 會被瀏覽器擋。請改用本機伺服器:<br><code>python -m http.server</code> 或 VS Code Live Server。</div>`;
    }
  }

  let activeCatId = allCats[0].id;
  let activeDocId = allCats[0].docs[0] ? allCats[0].docs[0].id : null;

  // ─── Sidebar persistence ───
  const savedW = parseInt(localStorage.getItem("hub-sidebar-w") || "0", 10);
  if (savedW >= 180 && savedW <= 600) {
    document.documentElement.style.setProperty("--sidebar-w", savedW + "px");
  }
  if (localStorage.getItem("hub-sidebar-collapsed") === "1") {
    layoutEl.classList.add("sidebar-collapsed");
  }

  // ─── Helpers ───
  function pendingCount() { return data.pending_total || 0; }
  function categoryCount(cat) { return cat.isPending ? pendingCount() : cat.docs.length; }
  function renderStars(n) { return n ? "★".repeat(n) + "☆".repeat(5 - n) : ""; }
  function escapeHtml(s) { return String(s).replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c])); }
  function escapeAttr(s) { return escapeHtml(s); }

  // ─── Tabs ───
  function buildTabs() {
    tabsEl.innerHTML = "";
    allCats.forEach((cat) => {
      const t = document.createElement("div");
      t.className = "tab" + (cat.id === activeCatId ? " active" : "") + (cat.isPending ? " pending-tab" : "");
      const cnt = categoryCount(cat);
      t.innerHTML = `<span class="icon">${cat.icon}</span>${cat.name}` +
        (cnt > 0 ? `<span class="count">${cnt}</span>` : "");
      t.onclick = () => selectCategory(cat.id);
      tabsEl.appendChild(t);
    });
  }

  // ─── Sidebar ───
  function buildSidebar() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { sidebarEl.innerHTML = `<div class="resize-handle" id="resizeHandle"></div>`; return; }

    let inner;
    if (cat.isPending) {
      inner = `<div class="sidebar-header">${cat.icon} ${cat.name}（${pendingCount()} 條)</div><ul>`;
      data.pending_groups.forEach((g) => {
        const total = g.files.reduce((s,f)=>s+f.items.length,0);
        inner += `<li><a class="group-link" data-cat="${g.category_id}" href="#${g.category_id}">
          <span class="row-title"><span class="row-title-text">${g.category_icon} ${escapeHtml(g.category_name)}</span><span class="pending-badge">${total}</span></span>
          <span class="filename">${g.files.length} 檔</span>
        </a></li>`;
      });
      inner += `</ul>`;
    } else {
      inner = `<div class="sidebar-header">${cat.icon} ${cat.name} (${cat.docs.length})</div><ul>`;
      cat.docs.forEach((d) => {
        const stars = d.priority > 0 ? `<span class="stars">${renderStars(d.priority)}</span>` : "";
        const badge = d.pending_count > 0 ? `<span class="pending-badge">${d.pending_count}</span>` : "";
        inner += `
          <li>
            <a href="#${activeCatId}/${d.id}" data-id="${d.id}" class="${d.id === activeDocId ? "active" : ""}" data-title="${escapeAttr(d.title)}" data-filename="${escapeAttr(d.filename)}">
              <span class="row-title">
                <span class="row-title-text">${escapeHtml(d.title)}</span>
                ${stars}${badge}
              </span>
              <span class="filename">${escapeHtml(d.filename)}</span>
            </a>
          </li>`;
      });
      inner += `</ul>`;
    }
    sidebarEl.innerHTML = inner + `<div class="resize-handle" id="resizeHandle"></div>`;

    sidebarEl.querySelectorAll("a[data-id]").forEach((a) => {
      a.onclick = (e) => { e.preventDefault(); selectDoc(a.dataset.id); };
    });
    sidebarEl.querySelectorAll(".group-link").forEach((a) => {
      a.onclick = (e) => { e.preventDefault(); selectCategory(a.dataset.cat); };
    });
    bindResizeHandle();
    applySearchFilter();
  }

  // ─── Content ───
  async function buildContent() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { contentEl.innerHTML = `<div class="empty">未選擇分類</div>`; return; }

    if (cat.isPending) { buildPendingContent(); contentEl.scrollTop = 0; return; }

    const doc = cat.docs.find((d) => d.id === activeDocId);
    if (!doc) { contentEl.innerHTML = `<div class="empty">未選擇文件</div>`; return; }

    // Stale-fetch guard: each call gets a token; later clicks invalidate earlier loads.
    const myToken = ++loadToken;
    contentEl.innerHTML = `<div class="empty">載入 ${escapeHtml(doc.title)}…</div>`;

    const docHtml = await loadDocHtml(doc.id);
    if (myToken !== loadToken) return; // user already moved on

    const stars = doc.priority > 0
      ? `<span class="stars" title="重要性 ${doc.priority}/5">${renderStars(doc.priority)}</span>`
      : "";
    const pendingPill = doc.pending_count > 0 ? `<span class="pending-pill">${doc.pending_count} 待釐清</span>` : "";
    const canBack = navHistory.length > 1;

    const lastUpdated = doc.last_updated
      ? `<span class="last-updated" title="檔案最後修改日期">📅 ${escapeHtml(doc.last_updated)}</span>`
      : "";

    contentEl.innerHTML = `
      <article class="doc-wrapper">
        <div class="doc-meta">
          <span class="left">
            <button class="back-btn" id="backBtn" ${canBack ? "" : "disabled"} title="回到上一頁 (Alt+←)">← 上一頁</button>
            ${cat.icon} ${escapeHtml(cat.name)} ${stars} ${pendingPill}
          </span>
          <span class="meta-right">${lastUpdated} <span class="filename">${escapeHtml(doc.filename)}</span></span>
        </div>
        <div class="doc-content">${docHtml}</div>
      </article>
    `;
    contentEl.scrollTop = 0;
    bindBackButton();
    bindInternalLinks();
  }

  function buildPendingContent() {
    const canBack = navHistory.length > 1;
    let html = `<div class="pending-page">`;
    html += `
      <div class="back-btn-row"><button class="back-btn" id="backBtn" ${canBack ? "" : "disabled"} title="回到上一頁 (Alt+←)">← 上一頁</button></div>
      <div class="pending-summary">
        共 <strong>${pendingCount()}</strong> 條待釐清項目,
        分布於 ${data.pending_groups.length} 個分類、${data.pending_groups.reduce((s,g)=>s+g.files.length,0)} 個文件中。
        <br><small>關鍵字:待釐清 / 待確認 / 待問 / 待補 / 待動作 / 待對齊 / 待裁示 / TBD / TODO。點檔名跳到原文。</small>
      </div>
    `;
    data.pending_groups.forEach((g) => {
      const groupTotal = g.files.reduce((s, f) => s + f.items.length, 0);
      html += `<section class="pending-group">`;
      html += `<h3>${g.category_icon} ${escapeHtml(g.category_name)} <span class="group-count">${groupTotal}</span></h3>`;
      g.files.forEach((f) => {
        const docHash = `${g.category_id}/${f.doc_id}`;
        html += `<div class="pending-file">`;
        html += `<h4><a href="#${docHash}" class="jump" data-cat="${g.category_id}" data-doc="${f.doc_id}">${escapeHtml(f.title)}</a> <span class="count">${f.items.length}</span> <code>${escapeHtml(f.filename)}</code></h4>`;
        html += `<ul>`;
        f.items.forEach((it) => {
          const escaped = escapeHtml(it.line).replace(PENDING_RE, "<mark>$1</mark>");
          html += `<li><span class="ln">L${it.line_no}</span>${escaped}</li>`;
        });
        html += `</ul></div>`;
      });
      html += `</section>`;
    });
    if (pendingCount() === 0) html += `<div class="empty">🎉 沒有待釐清項目</div>`;
    html += `</div>`;
    contentEl.innerHTML = html;
    contentEl.querySelectorAll("a.jump").forEach((a) => {
      a.onclick = (e) => { e.preventDefault(); selectCatDoc(a.dataset.cat, a.dataset.doc); };
    });
    bindBackButton();
  }

  // ─── Click handler for internal .md links rewritten by the build ───
  function bindInternalLinks() {
    contentEl.querySelectorAll("a.internal-doc-link").forEach((a) => {
      a.onclick = (e) => {
        e.preventDefault();
        const cat = a.dataset.cat;
        const doc = a.dataset.doc;
        if (cat && doc) selectCatDoc(cat, doc);
      };
    });
  }

  // ─── Back button ───
  const navHistory = []; // stack of {catId, docId}
  function pushHistory() {
    const top = navHistory[navHistory.length - 1];
    if (top && top.catId === activeCatId && top.docId === activeDocId) return;
    navHistory.push({ catId: activeCatId, docId: activeDocId });
    if (navHistory.length > 100) navHistory.shift();
  }
  function bindBackButton() {
    const btn = document.getElementById("backBtn");
    if (btn) btn.onclick = goBack;
  }
  function goBack() {
    if (navHistory.length < 2) return;
    navHistory.pop();              // remove current
    const prev = navHistory[navHistory.length - 1];
    activeCatId = prev.catId;
    activeDocId = prev.docId;
    syncHash();
    buildTabs(); buildSidebar(); buildContent();
  }

  // ─── Routing ───
  function syncHash() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (cat && cat.isPending) location.hash = activeCatId;
    else location.hash = `${activeCatId}/${activeDocId || ""}`;
  }
  function selectCategory(catId) {
    activeCatId = catId;
    const cat = allCats.find((c) => c.id === activeCatId);
    activeDocId = (cat && !cat.isPending && cat.docs[0]) ? cat.docs[0].id : null;
    pushHistory();
    syncHash();
    buildTabs(); buildSidebar(); buildContent();
  }
  function selectDoc(docId) {
    activeDocId = docId;
    pushHistory();
    syncHash();
    buildSidebar(); buildContent();
  }
  function selectCatDoc(catId, docId) {
    activeCatId = catId;
    activeDocId = docId;
    pushHistory();
    syncHash();
    buildTabs(); buildSidebar(); buildContent();
  }

  // Build a doc-id → search-text lookup once, so input filter is fast.
  const docTextById = (() => {
    const map = Object.create(null);
    allCats.forEach((cat) => {
      (cat.docs || []).forEach((d) => {
        if (d.text) map[d.id] = d.text.toLowerCase();
      });
    });
    return map;
  })();

  function applySearchFilter() {
    const q = (searchEl.value || "").trim().toLowerCase();
    sidebarEl.querySelectorAll("li").forEach((li) => {
      const a = li.querySelector("a");
      if (!a) return;
      const docId = a.dataset.id || "";
      const haystack = (
        (a.dataset.title || "") + " " +
        (a.dataset.filename || "") + " " +
        a.textContent + " " +
        (docTextById[docId] || "")
      ).toLowerCase();
      li.classList.toggle("hidden", !!q && haystack.indexOf(q) === -1);
    });
  }

  function fromHash(initial) {
    const h = location.hash.replace(/^#/, "");
    if (!h) return;
    const [catId, docId] = h.split("/");
    const cat = allCats.find((c) => c.id === catId);
    if (!cat) return;
    activeCatId = cat.id;
    if (cat.isPending) { activeDocId = null; return; }
    if (docId) {
      const doc = cat.docs.find((d) => d.id === docId);
      if (doc) activeDocId = doc.id;
    } else {
      activeDocId = cat.docs[0] ? cat.docs[0].id : null;
    }
  }

  // ─── Sidebar resize ───
  function bindResizeHandle() {
    const handle = document.getElementById("resizeHandle");
    if (!handle) return;
    handle.addEventListener("mousedown", (e) => {
      e.preventDefault();
      handle.classList.add("dragging");
      document.body.classList.add("resizing");
      const startX = e.clientX;
      const startW = sidebarEl.getBoundingClientRect().width;
      function onMove(ev) {
        let w = startW + (ev.clientX - startX);
        w = Math.max(180, Math.min(600, w));
        document.documentElement.style.setProperty("--sidebar-w", w + "px");
      }
      function onUp() {
        document.removeEventListener("mousemove", onMove);
        document.removeEventListener("mouseup", onUp);
        handle.classList.remove("dragging");
        document.body.classList.remove("resizing");
        const finalW = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--sidebar-w"), 10);
        if (finalW) localStorage.setItem("hub-sidebar-w", String(finalW));
      }
      document.addEventListener("mousemove", onMove);
      document.addEventListener("mouseup", onUp);
    });
  }

  // ─── Sidebar toggle ───
  toggleEl.onclick = () => {
    layoutEl.classList.toggle("sidebar-collapsed");
    localStorage.setItem("hub-sidebar-collapsed", layoutEl.classList.contains("sidebar-collapsed") ? "1" : "0");
  };

  // ─── Init ───
  fromHash(true);
  pushHistory();
  buildTabs();
  buildSidebar();
  buildContent();

  searchEl.addEventListener("input", applySearchFilter);
  window.addEventListener("hashchange", () => {
    fromHash(false);
    pushHistory();
    buildTabs(); buildSidebar(); buildContent();
  });

  document.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
    // Ctrl+B → toggle sidebar
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "b") {
      e.preventDefault();
      toggleEl.click();
      return;
    }
    // Alt+← → back
    if (e.altKey && e.key === "ArrowLeft") {
      e.preventDefault();
      goBack();
      return;
    }
    const n = parseInt(e.key, 10);
    if (n >= 1 && n <= allCats.length) selectCategory(allCats[n - 1].id);
  });
})();
</script>

<div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image preview">
  <button class="lightbox-close" type="button" aria-label="Close preview" onclick="document.getElementById('lightbox').classList.remove('is-open')">×</button>
  <img alt="">
  <div class="lightbox-caption"></div>
</div>
<script src="js/lightbox.js" defer></script>

</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(build())
