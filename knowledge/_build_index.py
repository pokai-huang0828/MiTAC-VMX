#!/usr/bin/env python3
"""Build knowledge/index.html — single self-contained HTML hub of all knowledge/*.md files.

Usage:
    python3 knowledge/_build_index.py

Output:
    knowledge/index.html  (self-contained, no external assets at runtime)

Features:
    - 7 + 1 tabs:總覽 / 6 分類 / 待釐清(自動掃描)
    - 重要性 ★ 評分,Sidebar 依重要性排序
    - Pending 計數 badge(待釐清/待確認/待問/待補/待動作/TBD/TODO)
    - URL hash 路由、鍵盤 1-8 切 tab、文件名搜尋
"""
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown

HERE = Path(__file__).parent
OUT = HERE / "index.html"

# Category metadata: folder prefix → (display name, icon)
CATEGORIES = {
    "01_product-knowledge":   ("產品知識",       "🔧"),
    "02_organization-map":    ("組織與利害關係人", "👥"),
    "03_systems-architecture": ("系統架構",       "🏛"),
    "04_pm-frameworks":       ("PM 框架",         "📐"),
    "05_workflows":           ("工作流 SOP",      "⚙️"),
    "06_calibration-log":     ("校正紀錄",        "🎯"),
}

# Importance rating per filename (1-5 stars). README handled separately.
# Higher = more important = sorted earlier within its category.
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

# Pending keywords — lines containing any of these will be extracted into the
# "待釐清" tab.
PENDING_KEYWORDS = [
    "待釐清", "待確認", "待問", "待補", "待動作",
    "待對齊", "待裁示",
    "TBD", "TODO",
]
PENDING_RE = re.compile("|".join(re.escape(k) for k in PENDING_KEYWORDS))

MD_EXTENSIONS = [
    "extra",
    "sane_lists",
    "smarty",
    "toc",
    "pymdownx.tilde",
    "pymdownx.superfences",
]


def md_to_html(text: str) -> str:
    md = markdown.Markdown(extensions=MD_EXTENSIONS, output_format="html5")
    return md.convert(text)


def slugify(s: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", s, flags=re.UNICODE).strip("-")
    return s.lower() or "doc"


def extract_pending(text: str) -> list[dict]:
    """Find lines containing any pending keyword. Return list of {line_no, line, keyword}."""
    items = []
    for i, line in enumerate(text.splitlines(), start=1):
        m = PENDING_RE.search(line)
        if not m:
            continue
        # Strip leading list markers / whitespace for cleaner display
        clean = line.strip()
        # Keep brevity but allow context — limit to 220 chars
        if len(clean) > 220:
            clean = clean[:217] + "…"
        items.append({"line_no": i, "line": clean, "keyword": m.group(0)})
    return items


def get_priority(filename: str) -> int:
    """Return priority 0 (README, top) or 1-5 stars. Unknown → 3."""
    if filename == "README.md":
        return 0
    return PRIORITY.get(filename, 3)


def build():
    categories: list[dict] = []
    pending_groups: list[dict] = []  # for "待釐清" tab

    for folder in sorted(HERE.iterdir()):
        if not folder.is_dir() or folder.name not in CATEGORIES:
            continue
        display, icon = CATEGORIES[folder.name]
        docs = []
        cat_pending: list[dict] = []
        md_files = list(folder.glob("*.md"))
        # Sort: README first (priority 0), then by descending priority, then by filename
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
            docs.append({
                "id": doc_id,
                "filename": md_file.name,
                "title": title,
                "priority": priority,
                "pending_count": len(pending),
                "html": md_to_html(text),
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

    # Top-level knowledge/README.md → "總覽" tab
    overview_md = HERE / "README.md"
    overview_html = md_to_html(overview_md.read_text(encoding="utf-8")) if overview_md.exists() else ""

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
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    total_docs = sum(len(c["docs"]) for c in categories)
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
<style>
  /* MDT 2026 palette */
  :root {
    --primary:        #4472C4;
    --primary-light:  #5B9BD5;
    --accent:         #ED7D31;
    --bg:             #F4F6FA;
    --card:           #FFFFFF;
    --border:         #DDE3EC;
    --text:           #1E293B;
    --text-muted:     #64748B;
    --code-bg:        #F1F5F9;
    --tab-active-bg:  #FFFFFF;
    --tab-inactive:   #E8EEF7;
    --pending:        #DC2626;
    --star:           #F59E0B;
    --shadow:         0 2px 12px rgba(68,114,196,0.10);
    --shadow-hover:   0 4px 20px rgba(68,114,196,0.18);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: Calibri, "Segoe UI", -apple-system, BlinkMacSystemFont, "Microsoft JhengHei", "PingFang TC", sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    line-height: 1.6;
  }

  /* Header */
  .topbar {
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: #fff;
    padding: 14px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--shadow);
    position: sticky;
    top: 0;
    z-index: 50;
  }
  .topbar h1 { font-size: 20px; font-weight: 600; letter-spacing: 0.3px; }
  .topbar h1 .accent { color: #FFD9A8; }
  .topbar .meta { font-size: 13px; color: rgba(255,255,255,0.85); display: flex; gap: 16px; align-items: center; }
  .topbar input[type="search"] {
    background: rgba(255,255,255,0.15);
    border: 1px solid rgba(255,255,255,0.3);
    color: #fff;
    padding: 6px 10px;
    border-radius: 6px;
    font-size: 13px;
    width: 220px;
    font-family: inherit;
  }
  .topbar input[type="search"]::placeholder { color: rgba(255,255,255,0.7); }
  .topbar input[type="search"]:focus { outline: 2px solid var(--accent); }

  /* Tabs */
  .tabs {
    display: flex;
    background: var(--tab-inactive);
    border-bottom: 2px solid var(--primary);
    padding: 0 16px;
    overflow-x: auto;
    position: sticky;
    top: 56px;
    z-index: 40;
  }
  .tab {
    padding: 11px 18px;
    cursor: pointer;
    font-weight: 500;
    color: var(--text-muted);
    border-bottom: 3px solid transparent;
    transition: all 0.15s;
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
  }
  .tab.active .count { background: var(--accent); color: #fff; }
  .tab.pending-tab.active { border-bottom-color: var(--pending); color: var(--pending); }
  .tab.pending-tab .count {
    background: rgba(220,38,38,0.12);
    color: var(--pending);
  }
  .tab.pending-tab.active .count { background: var(--pending); color: #fff; }

  /* Layout */
  .layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 0;
    min-height: calc(100vh - 100px);
  }

  /* Sidebar */
  .sidebar {
    background: var(--card);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    max-height: calc(100vh - 100px);
    position: sticky;
    top: 100px;
  }
  .sidebar-header {
    padding: 14px 18px 8px;
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid var(--border);
  }
  .sidebar ul { list-style: none; }
  .sidebar li a {
    display: block;
    padding: 9px 18px 9px 14px;
    color: var(--text);
    text-decoration: none;
    font-size: 13.5px;
    border-left: 3px solid transparent;
    transition: all 0.1s;
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
  .sidebar li a .row-title {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: nowrap;
    overflow: hidden;
  }
  .sidebar li a .row-title-text {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    flex: 1;
  }
  .sidebar li a .stars {
    color: var(--star);
    font-size: 11px;
    letter-spacing: -1px;
    flex-shrink: 0;
  }
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

  /* Content */
  .content {
    background: var(--bg);
    padding: 28px 40px;
    overflow-y: auto;
    max-height: calc(100vh - 100px);
  }
  .doc-wrapper {
    background: var(--card);
    padding: 32px 44px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    max-width: 980px;
    margin: 0 auto;
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
  .doc-meta .left { display: flex; align-items: center; gap: 10px; }
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

  /* Markdown content styles */
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
  .doc-content pre code { background: transparent; color: inherit; padding: 0; font-size: inherit; }
  .doc-content blockquote {
    border-left: 4px solid var(--primary-light);
    background: rgba(91,155,213,0.08);
    padding: 10px 16px;
    margin: 12px 0;
    color: var(--text);
  }
  .doc-content table { border-collapse: collapse; width: 100%; margin: 14px 0; font-size: 14px; }
  .doc-content th, .doc-content td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; }
  .doc-content th { background: var(--primary); color: #fff; font-weight: 600; }
  .doc-content tr:nth-child(even) td { background: rgba(91,155,213,0.04); }
  .doc-content a { color: var(--primary); text-decoration: none; border-bottom: 1px dashed var(--primary-light); }
  .doc-content a:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .doc-content hr { border: 0; border-top: 1px solid var(--border); margin: 24px 0; }
  .doc-content strong { color: var(--primary); }

  /* Pending tab dedicated layout */
  .pending-page { max-width: 980px; margin: 0 auto; }
  .pending-page .pending-summary {
    background: linear-gradient(135deg, rgba(220,38,38,0.06), rgba(237,125,49,0.06));
    border: 1px solid rgba(220,38,38,0.18);
    color: var(--text);
    padding: 16px 20px;
    border-radius: 8px;
    font-size: 14px;
    margin-bottom: 24px;
  }
  .pending-page .pending-summary strong { color: var(--pending); font-size: 18px; }
  .pending-group {
    background: var(--card);
    border-radius: 8px;
    box-shadow: var(--shadow);
    padding: 18px 24px;
    margin-bottom: 18px;
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
  .pending-file {
    margin: 10px 0 18px;
    padding-left: 4px;
  }
  .pending-file h4 {
    font-size: 13px;
    color: var(--text-muted);
    margin-bottom: 8px;
    font-weight: 500;
  }
  .pending-file h4 a {
    color: var(--primary);
    text-decoration: none;
    font-weight: 600;
    border-bottom: 1px dashed var(--primary-light);
  }
  .pending-file h4 a:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .pending-file h4 .count {
    background: rgba(220,38,38,0.10);
    color: var(--pending);
    padding: 1px 7px;
    border-radius: 8px;
    font-size: 11px;
    margin-left: 6px;
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

  @media (max-width: 900px) {
    .layout { grid-template-columns: 1fr; }
    .sidebar { position: static; max-height: none; border-right: 0; border-bottom: 1px solid var(--border); }
    .content { padding: 18px; }
    .doc-wrapper { padding: 18px; }
    .topbar { flex-direction: column; gap: 8px; align-items: flex-start; }
    .topbar input[type="search"] { width: 100%; }
    .tabs { top: 88px; }
  }

  @media print {
    .topbar, .tabs, .sidebar { display: none; }
    .layout { grid-template-columns: 1fr; }
    .content { max-height: none; padding: 0; }
    .doc-wrapper { box-shadow: none; padding: 0; max-width: none; }
  }
</style>
</head>
<body>

<header class="topbar">
  <div>
    <h1>📚 Kenny VMX <span class="accent">Knowledge Hub</span></h1>
  </div>
  <div class="meta">
    <span>產生於 __GENERATED_AT__</span>
    <input type="search" id="searchBox" placeholder="搜尋文件名稱…" autocomplete="off">
  </div>
</header>

<nav class="tabs" id="tabs"></nav>

<div class="layout">
  <aside class="sidebar" id="sidebar"></aside>
  <main class="content" id="content"></main>
</div>

<script id="hub-data" type="application/json">__DATA_JSON__</script>

<script>
(function () {
  const data = JSON.parse(document.getElementById("hub-data").textContent);
  const tabsEl = document.getElementById("tabs");
  const sidebarEl = document.getElementById("sidebar");
  const contentEl = document.getElementById("content");
  const searchEl = document.getElementById("searchBox");

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
  const pendingCat = {
    id: "pending", name: "待釐清", icon: "📌",
    docs: [], // virtual; rendered specially
    isPending: true,
  };

  const allCats = [overviewCat, ...data.categories, pendingCat];

  let activeCatId = allCats[0].id;
  let activeDocId = allCats[0].docs[0] ? allCats[0].docs[0].id : null;

  function pendingCount() { return data.pending_total || 0; }

  function categoryCount(cat) {
    if (cat.isPending) return pendingCount();
    return cat.docs.length;
  }

  function renderStars(n) {
    if (!n) return "";
    return "★".repeat(n) + "☆".repeat(5 - n);
  }

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

  function buildSidebar() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { sidebarEl.innerHTML = ""; return; }

    if (cat.isPending) {
      // Sidebar shows the pending source files grouped by category
      let html = `<div class="sidebar-header">${cat.icon} ${cat.name}（${pendingCount()} 條)</div><ul>`;
      data.pending_groups.forEach((g) => {
        html += `<li><a class="group-link" data-cat="${g.category_id}" data-doc="" href="#${g.category_id}">${g.category_icon} ${escapeHtml(g.category_name)}<span class="filename">${g.files.length} 檔 · ${g.files.reduce((s,f)=>s+f.items.length,0)} 條</span></a></li>`;
      });
      html += "</ul>";
      sidebarEl.innerHTML = html;
      sidebarEl.querySelectorAll(".group-link").forEach((a) => {
        a.onclick = (e) => {
          e.preventDefault();
          // Clicking a group jumps to the source category, first doc
          selectCategory(a.dataset.cat);
        };
      });
      applySearchFilter();
      return;
    }

    sidebarEl.innerHTML = `
      <div class="sidebar-header">${cat.icon} ${cat.name} (${cat.docs.length})</div>
      <ul>
        ${cat.docs.map((d) => {
          const stars = d.priority > 0 ? `<span class="stars">${renderStars(d.priority)}</span>` : "";
          const badge = d.pending_count > 0 ? `<span class="pending-badge">${d.pending_count}</span>` : "";
          return `
            <li>
              <a href="#" data-id="${d.id}" class="${d.id === activeDocId ? "active" : ""}" data-title="${escapeAttr(d.title)}" data-filename="${escapeAttr(d.filename)}">
                <span class="row-title">
                  <span class="row-title-text">${escapeHtml(d.title)}</span>
                  ${stars}
                  ${badge}
                </span>
                <span class="filename">${escapeHtml(d.filename)}</span>
              </a>
            </li>`;
        }).join("")}
      </ul>
    `;
    sidebarEl.querySelectorAll("a[data-id]").forEach((a) => {
      a.onclick = (e) => {
        e.preventDefault();
        selectDoc(a.dataset.id);
      };
    });
    applySearchFilter();
  }

  function buildContent() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { contentEl.innerHTML = `<div class="empty">未選擇分類</div>`; return; }

    if (cat.isPending) {
      buildPendingContent();
      contentEl.scrollTop = 0;
      return;
    }

    const doc = cat.docs.find((d) => d.id === activeDocId);
    if (!doc) {
      contentEl.innerHTML = `<div class="empty">未選擇文件</div>`;
      return;
    }
    const stars = doc.priority > 0
      ? `<span class="stars" title="重要性 ${doc.priority}/5">${renderStars(doc.priority)}</span>`
      : "";
    const pendingPill = doc.pending_count > 0
      ? `<span class="pending-pill">${doc.pending_count} 待釐清</span>`
      : "";
    contentEl.innerHTML = `
      <article class="doc-wrapper">
        <div class="doc-meta">
          <span class="left">${cat.icon} ${escapeHtml(cat.name)} ${stars} ${pendingPill}</span>
          <span class="filename">${escapeHtml(doc.filename)}</span>
        </div>
        <div class="doc-content">${doc.html}</div>
      </article>
    `;
    contentEl.scrollTop = 0;
  }

  function buildPendingContent() {
    let html = `<div class="pending-page">`;
    html += `
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
    if (pendingCount() === 0) {
      html += `<div class="empty">🎉 沒有待釐清項目</div>`;
    }
    html += `</div>`;
    contentEl.innerHTML = html;
    contentEl.querySelectorAll("a.jump").forEach((a) => {
      a.onclick = (e) => {
        e.preventDefault();
        activeCatId = a.dataset.cat;
        activeDocId = a.dataset.doc;
        location.hash = `${activeCatId}/${activeDocId}`;
        buildTabs(); buildSidebar(); buildContent();
      };
    });
  }

  function selectCategory(catId) {
    activeCatId = catId;
    const cat = allCats.find((c) => c.id === activeCatId);
    if (cat && !cat.isPending) {
      activeDocId = cat.docs[0] ? cat.docs[0].id : null;
      location.hash = `${activeCatId}/${activeDocId || ""}`;
    } else {
      activeDocId = null;
      location.hash = activeCatId;
    }
    buildTabs(); buildSidebar(); buildContent();
  }

  function selectDoc(docId) {
    activeDocId = docId;
    location.hash = `${activeCatId}/${activeDocId}`;
    buildSidebar(); buildContent();
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

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
  }
  function escapeAttr(s) { return escapeHtml(s); }

  function fromHash() {
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

  // Init
  fromHash();
  buildTabs();
  buildSidebar();
  buildContent();

  searchEl.addEventListener("input", applySearchFilter);
  window.addEventListener("hashchange", () => {
    fromHash();
    buildTabs(); buildSidebar(); buildContent();
  });

  // Keyboard 1-N for tab switching (1-8 with overview + 6 + pending)
  document.addEventListener("keydown", (e) => {
    if (e.target.tagName === "INPUT" || e.target.tagName === "TEXTAREA") return;
    const n = parseInt(e.key, 10);
    if (n >= 1 && n <= allCats.length) {
      selectCategory(allCats[n - 1].id);
    }
  });
})();
</script>

</body>
</html>
"""


if __name__ == "__main__":
    sys.exit(build())
