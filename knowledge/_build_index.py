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


def post_process_html(rendered: str, registry: dict) -> str:
    """Apply two transforms with a single BS4 parse:
    1. Internal .md links → in-app hash routes (so click shows preview, not raw md).
    2. Bare VMX-/HAWK-/BMS- ticket text → Jira links.
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


def build():
    registry = collect_doc_registry()
    categories: list[dict] = []
    pending_groups: list[dict] = []

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
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")
            doc_id = slugify(f"{folder.name}--{md_file.stem}")
            m = re.search(r"^# (.+)$", text, flags=re.MULTILINE)
            title = m.group(1).strip() if m else md_file.stem
            priority = get_priority(md_file.name)
            pending = extract_pending(text)
            rendered = md_to_html(text)
            rendered = post_process_html(rendered, registry)
            docs.append({
                "id": doc_id,
                "filename": md_file.name,
                "title": title,
                "priority": priority,
                "pending_count": len(pending),
                "html": rendered,
            })
            if pending:
                cat_pending.append({
                    "doc_id": doc_id,
                    "filename": md_file.name,
                    "title": title,
                    "items": pending,
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
    overview_html = ""
    if overview_md.exists():
        overview_html = post_process_html(
            md_to_html(overview_md.read_text(encoding="utf-8")), registry
        )

    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "categories": categories,
        "overview_html": overview_html,
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


def render_template(payload: dict) -> str:
    data_json = json.dumps(payload, ensure_ascii=False)
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
<style>
  /* Page-specific tokens (colors / fonts come from shared.css) */
  :root {
    --sidebar-w:      300px;
    --ease:           var(--mdt-ease);
  }

  html, body { height: 100%; overflow: hidden; }

  body {
    background: var(--bg);
    color: var(--text);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
  }

  /* ─── Topbar ─── */
  .topbar {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: #fff;
    padding: 12px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--shadow);
    z-index: 50;
    flex-shrink: 0;
    gap: 12px;
  }
  .topbar h1 { font-size: 19px; font-weight: 600; letter-spacing: 0.3px; white-space: nowrap; }
  .topbar h1 .accent { color: #FFD9A8; }
  .topbar .meta { font-size: 13px; color: rgba(255,255,255,0.85); display: flex; gap: 14px; align-items: center; }
  .topbar input[type="search"] {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 13px;
    width: 220px;
    font-family: inherit;
    transition: width 0.2s var(--ease), background 0.2s;
  }
  .topbar input[type="search"]::placeholder { color: rgba(255,255,255,0.7); }
  .topbar input[type="search"]:focus { outline: 2px solid var(--accent); width: 280px; background: rgba(255,255,255,0.22); }

  /* ─── Tabs ─── */
  .tabs {
    display: flex;
    background: var(--tab-inactive);
    border-bottom: 2px solid var(--primary);
    padding: 0 16px;
    overflow-x: auto;
    flex-shrink: 0;
    z-index: 40;
  }
  .tab {
    padding: 11px 18px;
    cursor: pointer;
    font-weight: 500;
    color: var(--text-muted);
    border-bottom: 3px solid transparent;
    transition: color 0.18s, background 0.18s, border-color 0.25s var(--ease);
    white-space: nowrap;
    user-select: none;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .tab:hover { color: var(--primary); background: rgba(91,155,213,0.08); }
  .tab.active {
    background: var(--tab-active-bg);
    color: var(--primary);
    border-bottom-color: var(--accent);
    font-weight: 600;
  }
  .tab .count {
    font-size: 11px;
    background: rgba(68,114,196,0.15);
    color: var(--primary);
    padding: 2px 7px;
    border-radius: 10px;
    font-weight: 500;
    transition: background 0.18s, color 0.18s;
  }
  .tab.active .count { background: var(--accent); color: #fff; }
  .tab.pending-tab.active { border-bottom-color: var(--pending); color: var(--pending); }
  .tab.pending-tab .count { background: rgba(220,38,38,0.12); color: var(--pending); }
  .tab.pending-tab.active .count { background: var(--pending); color: #fff; }

  /* ─── Layout ─── */
  .layout {
    display: grid;
    grid-template-columns: var(--sidebar-w) 1fr;
    flex: 1;
    min-height: 0;
    transition: grid-template-columns 0.25s var(--ease);
  }
  .layout.sidebar-collapsed { grid-template-columns: 0 1fr; }

  /* ─── Sidebar ─── */
  .sidebar {
    background: var(--card);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    overflow-x: hidden;
    position: relative;
    transition: transform 0.25s var(--ease);
    min-width: 0;
  }
  .layout.sidebar-collapsed .sidebar { transform: translateX(-100%); pointer-events: none; }

  .sidebar-header {
    padding: 14px 18px 8px;
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
  }
  .sidebar ul { list-style: none; padding: 4px 0; }
  .sidebar li a {
    display: block;
    padding: 9px 18px 9px 14px;
    color: var(--text);
    text-decoration: none;
    font-size: 13.5px;
    border-left: 3px solid transparent;
    transition: background 0.12s, border-color 0.12s, color 0.12s;
    position: relative;
  }
  .sidebar li a:hover {
    background: rgba(91,155,213,0.1);
    border-left-color: var(--primary-light);
  }
  .sidebar li a.active {
    background: rgba(237,125,49,0.08);
    border-left-color: var(--accent);
    color: var(--primary);
    font-weight: 600;
  }
  .sidebar li a .row-title { display: flex; align-items: center; gap: 8px; flex-wrap: nowrap; min-width: 0; }
  .sidebar li a .row-title-text {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    flex: 1;
    min-width: 0;
  }
  .sidebar li a .stars { color: var(--star); font-size: 11px; letter-spacing: -1px; flex-shrink: 0; }
  .sidebar li a .pending-badge {
    background: var(--pending);
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    padding: 1px 6px;
    border-radius: 8px;
    flex-shrink: 0;
  }
  .sidebar li a .filename {
    display: block;
    font-size: 11px;
    color: var(--text-muted);
    font-family: 'SF Mono', Consolas, monospace;
    margin-top: 2px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  /* Sidebar drag handle */
  .resize-handle {
    position: absolute;
    top: 0; right: -3px;
    width: 6px;
    height: 100%;
    cursor: col-resize;
    z-index: 5;
    transition: background 0.15s;
  }
  .resize-handle:hover, .resize-handle.dragging { background: rgba(91,155,213,0.35); }
  body.resizing { cursor: col-resize !important; user-select: none; }
  body.resizing .layout { transition: none; }

  /* ─── Toggle button ─── */
  .sidebar-toggle {
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    width: 32px; height: 32px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    display: flex; align-items: center; justify-content: center;
    transition: background 0.15s, transform 0.2s var(--ease);
  }
  .sidebar-toggle:hover { background: rgba(255,255,255,0.28); }
  .layout.sidebar-collapsed ~ * .sidebar-toggle { transform: rotate(180deg); }

  /* ─── Content ─── */
  .content {
    background: var(--bg);
    padding: 24px 32px;
    overflow-y: auto;
    overflow-x: hidden;
    min-width: 0;
  }
  .doc-wrapper {
    background: var(--card);
    padding: 28px 36px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    max-width: 980px;
    margin: 0 auto;
    animation: fadeUp 0.25s var(--ease);
  }
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .doc-meta {
    font-size: 12px;
    color: var(--text-muted);
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }
  .doc-meta .left { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
  .doc-meta .stars { color: var(--star); font-size: 14px; letter-spacing: 1px; }
  .doc-meta .filename {
    font-family: 'SF Mono', Consolas, monospace;
    background: var(--code-bg);
    padding: 2px 8px;
    border-radius: 4px;
  }
  .doc-meta .pending-pill {
    background: var(--pending);
    color: #fff;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 10px;
  }
  .doc-meta .back-btn {
    background: var(--code-bg);
    border: 1px solid var(--border);
    color: var(--primary);
    padding: 4px 10px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 12px;
    font-family: inherit;
    transition: all 0.15s;
  }
  .doc-meta .back-btn:hover { background: var(--primary); color: #fff; border-color: var(--primary); }
  .doc-meta .back-btn:disabled { opacity: 0.4; cursor: not-allowed; background: var(--code-bg); color: var(--text-muted); }

  /* ─── Markdown content ─── */
  .doc-content {
    word-wrap: break-word;
    overflow-wrap: anywhere;
  }
  .doc-content h1 {
    color: var(--primary);
    font-size: 26px;
    font-weight: 700;
    margin: 0 0 16px;
    padding-bottom: 8px;
    border-bottom: 3px solid var(--accent);
  }
  .doc-content h2 {
    color: var(--primary);
    font-size: 20px;
    margin: 28px 0 12px;
    padding-left: 12px;
    border-left: 4px solid var(--accent);
  }
  .doc-content h3 { color: var(--primary-light); font-size: 16px; margin: 20px 0 10px; }
  .doc-content h4 { color: var(--text); font-size: 15px; margin: 16px 0 8px; }
  .doc-content p { margin: 10px 0; }
  .doc-content ul, .doc-content ol { margin: 10px 0 10px 24px; }
  .doc-content li { margin: 4px 0; }
  .doc-content code {
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 4px;
    font-family: 'SF Mono', Consolas, monospace;
    font-size: 13px;
    color: var(--accent);
    word-break: break-word;
  }
  .doc-content pre {
    background: #1E293B;
    color: #E8EEF7;
    padding: 14px 18px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 12px 0;
    font-size: 13px;
  }
  .doc-content pre code { background: transparent; color: inherit; padding: 0; font-size: inherit; word-break: normal; }
  .doc-content blockquote {
    border-left: 4px solid var(--primary-light);
    background: rgba(91,155,213,0.08);
    padding: 10px 16px;
    margin: 12px 0;
    color: var(--text);
  }
  /* Wrap tables in scroll container */
  .doc-content table {
    border-collapse: collapse;
    width: 100%;
    margin: 14px 0;
    font-size: 14px;
    display: block;
    overflow-x: auto;
    max-width: 100%;
  }
  .doc-content th, .doc-content td {
    border: 1px solid var(--border);
    padding: 8px 12px;
    text-align: left;
    word-break: break-word;
  }
  .doc-content th { background: var(--primary); color: #fff; font-weight: 600; }
  .doc-content tr:nth-child(even) td { background: rgba(91,155,213,0.04); }
  .doc-content a { color: var(--primary); text-decoration: none; border-bottom: 1px dashed var(--primary-light); transition: color 0.12s, border-color 0.12s; }
  .doc-content a:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .doc-content a.ext-link::after {
    content: " ↗";
    font-size: 0.85em;
    color: var(--text-muted);
  }
  .doc-content a.jira-link {
    background: rgba(91,155,213,0.12);
    padding: 0 5px;
    border-radius: 3px;
    border-bottom: 0;
    font-family: 'SF Mono', Consolas, monospace;
    font-size: 0.95em;
  }
  .doc-content a.jira-link:hover { background: rgba(237,125,49,0.18); color: var(--accent); }
  .doc-content a.internal-doc-link {
    color: var(--primary);
    border-bottom: 1px solid var(--primary-light);
  }
  .doc-content a.internal-doc-link::before {
    content: "📄 ";
    margin-right: 1px;
  }
  .doc-content a.internal-doc-link:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .doc-content hr { border: 0; border-top: 1px solid var(--border); margin: 24px 0; }
  .doc-content strong { color: var(--primary); }

  /* ─── Pending tab ─── */
  .pending-page { max-width: 980px; margin: 0 auto; animation: fadeUp 0.25s var(--ease); }
  .pending-page .pending-summary {
    background: linear-gradient(135deg, rgba(220,38,38,0.06), rgba(237,125,49,0.06));
    border: 1px solid rgba(220,38,38,0.18);
    color: var(--text);
    padding: 14px 18px;
    border-radius: 8px;
    font-size: 14px;
    margin-bottom: 20px;
  }
  .pending-page .pending-summary strong { color: var(--pending); font-size: 18px; }
  .pending-group {
    background: var(--card);
    border-radius: 8px;
    box-shadow: var(--shadow);
    padding: 16px 22px;
    margin-bottom: 16px;
  }
  .pending-group h3 {
    color: var(--primary);
    font-size: 17px;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 2px solid var(--accent);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .pending-group h3 .group-count {
    margin-left: auto;
    font-size: 12px;
    background: rgba(220,38,38,0.12);
    color: var(--pending);
    padding: 2px 9px;
    border-radius: 10px;
  }
  .pending-file { margin: 10px 0 16px; padding-left: 4px; }
  .pending-file h4 {
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 8px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }
  .pending-file h4 a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    border-bottom: 1px dashed var(--primary-light);
    transition: color 0.12s;
  }
  .pending-file h4 a:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .pending-file h4 .count {
    background: rgba(220,38,38,0.10);
    color: var(--pending);
    padding: 1px 7px;
    border-radius: 8px;
    font-size: 11px;
  }
  .pending-file ul { list-style: none; margin: 0; }
  .pending-file li {
    background: var(--code-bg);
    border-left: 3px solid var(--pending);
    padding: 8px 12px;
    margin: 6px 0;
    font-size: 13.5px;
    border-radius: 0 4px 4px 0;
    line-height: 1.5;
    word-break: break-word;
    transition: transform 0.12s var(--ease), box-shadow 0.12s;
  }
  .pending-file li:hover {
    transform: translateX(2px);
    box-shadow: 0 1px 4px rgba(220,38,38,0.15);
  }
  .pending-file li .ln {
    color: var(--text-muted);
    font-family: 'SF Mono', Consolas, monospace;
    font-size: 11px;
    margin-right: 8px;
  }
  .pending-file li mark {
    background: rgba(220,38,38,0.18);
    color: var(--pending);
    font-weight: 600;
    padding: 0 3px;
    border-radius: 2px;
  }

  .empty { text-align: center; color: var(--text-muted); padding: 80px 20px; }
  li.hidden { display: none; }

  /* ─── Responsive ─── */
  @media (max-width: 1100px) {
    :root { --sidebar-w: 260px; }
    .doc-wrapper { padding: 22px 26px; }
    .content { padding: 18px 22px; }
  }
  @media (max-width: 820px) {
    :root { --sidebar-w: 220px; }
    .topbar h1 { font-size: 16px; }
    .topbar input[type="search"] { width: 130px; }
    .topbar input[type="search"]:focus { width: 180px; }
    .tab { padding: 9px 12px; font-size: 13px; }
  }
  @media (max-width: 640px) {
    .layout {
      grid-template-columns: 1fr;
    }
    .sidebar {
      position: fixed;
      top: 100px;
      left: 0;
      width: 280px;
      height: calc(100vh - 100px);
      z-index: 30;
      transform: translateX(-100%);
      box-shadow: 4px 0 20px rgba(0,0,0,0.1);
    }
    .layout.sidebar-open .sidebar { transform: translateX(0); }
    .layout.sidebar-collapsed .sidebar { transform: translateX(-100%); }
    .resize-handle { display: none; }
    .doc-wrapper { padding: 18px; }
    .content { padding: 12px; }
    .topbar { padding: 10px 12px; }
    .topbar h1 { font-size: 15px; }
    .topbar .meta { gap: 6px; }
    .doc-meta { font-size: 11px; }
  }

  @media print {
    .topbar, .tabs, .sidebar, .resize-handle { display: none; }
    .layout { display: block; }
    .content { overflow: visible; max-height: none; padding: 0; }
    .doc-wrapper { box-shadow: none; padding: 0; max-width: none; animation: none; }
  }
</style>
</head>
<body>

<header class="topbar">
  <div style="display:flex;align-items:center;gap:10px;">
    <button class="sidebar-toggle" id="sidebarToggle" title="收合 / 展開 sidebar (Ctrl+B)">☰</button>
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

<script id="hub-data" type="application/json">__DATA_JSON__</script>

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
      html: data.overview_html,
    }],
  };
  const pendingCat = { id: "pending", name: "待釐清", icon: "📌", docs: [], isPending: true };
  const allCats = [overviewCat, ...data.categories, pendingCat];

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
  function buildContent() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { contentEl.innerHTML = `<div class="empty">未選擇分類</div>`; return; }

    if (cat.isPending) { buildPendingContent(); contentEl.scrollTop = 0; return; }

    const doc = cat.docs.find((d) => d.id === activeDocId);
    if (!doc) { contentEl.innerHTML = `<div class="empty">未選擇文件</div>`; return; }

    const stars = doc.priority > 0
      ? `<span class="stars" title="重要性 ${doc.priority}/5">${renderStars(doc.priority)}</span>`
      : "";
    const pendingPill = doc.pending_count > 0 ? `<span class="pending-pill">${doc.pending_count} 待釐清</span>` : "";
    const canBack = navHistory.length > 1;

    contentEl.innerHTML = `
      <article class="doc-wrapper">
        <div class="doc-meta">
          <span class="left">
            <button class="back-btn" id="backBtn" ${canBack ? "" : "disabled"} title="回到上一頁 (Alt+←)">← 上一頁</button>
            ${cat.icon} ${escapeHtml(cat.name)} ${stars} ${pendingPill}
          </span>
          <span class="filename">${escapeHtml(doc.filename)}</span>
        </div>
        <div class="doc-content">${doc.html}</div>
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
      <div style="margin-bottom:12px"><button class="back-btn" id="backBtn" ${canBack ? "" : "disabled"} title="回到上一頁 (Alt+←)">← 上一頁</button></div>
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

  function applySearchFilter() {
    const q = (searchEl.value || "").trim().toLowerCase();
    sidebarEl.querySelectorAll("li").forEach((li) => {
      const a = li.querySelector("a");
      if (!a) return;
      const haystack = ((a.dataset.title || "") + " " + (a.dataset.filename || "") + " " + a.textContent).toLowerCase();
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

</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(build())
