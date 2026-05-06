#!/usr/bin/env python3
"""Build knowledge/index.html — single self-contained HTML hub of all knowledge/*.md files.

Usage:
    python3 knowledge/_build_index.py

Output:
    knowledge/index.html  (self-contained, no external assets at runtime)
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

# Category metadata: folder prefix → (display name, accent color, icon)
CATEGORIES = {
    "01_product-knowledge":   ("產品知識",       "🔧"),
    "02_organization-map":    ("組織與利害關係人", "👥"),
    "03_systems-architecture": ("系統架構",       "🏛"),
    "04_pm-frameworks":       ("PM 框架",         "📐"),
    "05_workflows":           ("工作流 SOP",      "⚙️"),
    "06_calibration-log":     ("校正紀錄",        "🎯"),
}

MD_EXTENSIONS = [
    "extra",            # tables, fenced_code, etc.
    "sane_lists",
    "smarty",
    "toc",
    "pymdownx.tilde",
    "pymdownx.superfences",
]


def md_to_html(text: str) -> str:
    """Render markdown text to HTML fragment."""
    md = markdown.Markdown(extensions=MD_EXTENSIONS, output_format="html5")
    return md.convert(text)


def slugify(s: str) -> str:
    s = re.sub(r"[^\w一-鿿-]+", "-", s, flags=re.UNICODE).strip("-")
    return s.lower() or "doc"


def build():
    categories: list[dict] = []

    # Category index built from folder structure
    for folder in sorted(HERE.iterdir()):
        if not folder.is_dir():
            continue
        if folder.name not in CATEGORIES:
            continue
        display, icon = CATEGORIES[folder.name]
        docs = []
        # README first if present, then other files alphabetically
        md_files = sorted(folder.glob("*.md"), key=lambda p: (p.name != "README.md", p.name))
        for md_file in md_files:
            text = md_file.read_text(encoding="utf-8")
            doc_id = f"{folder.name}--{md_file.stem}"
            # Use first H1 as title; fallback to filename
            m = re.search(r"^# (.+)$", text, flags=re.MULTILINE)
            title = m.group(1).strip() if m else md_file.stem
            docs.append({
                "id": slugify(doc_id),
                "filename": md_file.name,
                "title": title,
                "html": md_to_html(text),
            })
        categories.append({
            "id": folder.name,
            "name": display,
            "icon": icon,
            "docs": docs,
        })

    # Top-level knowledge/README.md goes into a "總覽" tab
    overview_md = HERE / "README.md"
    overview_html = md_to_html(overview_md.read_text(encoding="utf-8")) if overview_md.exists() else ""

    payload = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "categories": categories,
        "overview_html": overview_html,
    }

    OUT.write_text(render_template(payload), encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes)")
    total_docs = sum(len(c["docs"]) for c in categories)
    print(f"  {len(categories)} categories, {total_docs} docs")


def render_template(payload: dict) -> str:
    data_json = json.dumps(payload, ensure_ascii=False)
    # Escape closing script tag inside JSON to prevent breakout
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
    --primary:        #4472C4;  /* MDT 2026 primary */
    --primary-light:  #5B9BD5;  /* MDT 2026 secondary blue */
    --accent:         #ED7D31;  /* MDT 2026 orange */
    --bg:             #F4F6FA;
    --card:           #FFFFFF;
    --border:         #DDE3EC;
    --text:           #1E293B;
    --text-muted:     #64748B;
    --code-bg:        #F1F5F9;
    --tab-active-bg:  #FFFFFF;
    --tab-inactive:   #E8EEF7;
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
    padding: 16px 28px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: var(--shadow);
    position: sticky;
    top: 0;
    z-index: 50;
  }
  .topbar h1 {
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0.3px;
  }
  .topbar h1 .accent { color: #FFD9A8; }
  .topbar .meta {
    font-size: 13px;
    color: rgba(255,255,255,0.85);
    display: flex;
    gap: 16px;
    align-items: center;
  }
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
  }
  .tab {
    padding: 12px 20px;
    cursor: pointer;
    font-weight: 500;
    color: var(--text-muted);
    border-bottom: 3px solid transparent;
    transition: all 0.15s;
    white-space: nowrap;
    user-select: none;
    font-size: 14px;
  }
  .tab:hover { color: var(--primary); background: rgba(91,155,213,0.08); }
  .tab.active {
    background: var(--tab-active-bg);
    color: var(--primary);
    border-bottom-color: var(--accent);
    font-weight: 600;
  }
  .tab .icon { margin-right: 6px; }
  .tab .count {
    margin-left: 6px;
    font-size: 11px;
    background: rgba(68,114,196,0.15);
    color: var(--primary);
    padding: 2px 6px;
    border-radius: 10px;
    font-weight: 500;
  }
  .tab.active .count { background: var(--accent); color: #fff; }

  /* Layout */
  .layout {
    display: grid;
    grid-template-columns: 280px 1fr;
    gap: 0;
    min-height: calc(100vh - 110px);
  }

  /* Sidebar */
  .sidebar {
    background: var(--card);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    max-height: calc(100vh - 110px);
    position: sticky;
    top: 110px;
  }
  .sidebar-header {
    padding: 16px 20px 8px;
    font-size: 11px;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.8px;
    border-bottom: 1px solid var(--border);
  }
  .sidebar ul { list-style: none; }
  .sidebar li a {
    display: block;
    padding: 9px 20px;
    color: var(--text);
    text-decoration: none;
    font-size: 13.5px;
    border-left: 3px solid transparent;
    transition: all 0.1s;
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
  .sidebar li a .filename {
    display: block;
    font-size: 11px;
    color: var(--text-muted);
    font-family: 'SF Mono', Consolas, monospace;
    margin-top: 2px;
  }

  /* Content */
  .content {
    background: var(--bg);
    padding: 32px 48px;
    overflow-y: auto;
    max-height: calc(100vh - 110px);
  }
  .doc-wrapper {
    background: var(--card);
    padding: 36px 48px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    max-width: 960px;
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
  }
  .doc-meta .filename {
    font-family: 'SF Mono', Consolas, monospace;
    background: var(--code-bg);
    padding: 2px 8px;
    border-radius: 4px;
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
  .doc-content h3 {
    color: var(--primary-light);
    font-size: 16px;
    margin: 20px 0 10px;
  }
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
  .doc-content pre code {
    background: transparent;
    color: inherit;
    padding: 0;
    font-size: inherit;
  }
  .doc-content blockquote {
    border-left: 4px solid var(--primary-light);
    background: rgba(91,155,213,0.08);
    padding: 10px 16px;
    margin: 12px 0;
    color: var(--text);
  }
  .doc-content table {
    border-collapse: collapse;
    width: 100%;
    margin: 14px 0;
    font-size: 14px;
  }
  .doc-content th, .doc-content td {
    border: 1px solid var(--border);
    padding: 8px 12px;
    text-align: left;
  }
  .doc-content th {
    background: var(--primary);
    color: #fff;
    font-weight: 600;
  }
  .doc-content tr:nth-child(even) td { background: rgba(91,155,213,0.04); }
  .doc-content a { color: var(--primary); text-decoration: none; border-bottom: 1px dashed var(--primary-light); }
  .doc-content a:hover { color: var(--accent); border-bottom-color: var(--accent); }
  .doc-content hr { border: 0; border-top: 1px solid var(--border); margin: 24px 0; }
  .doc-content strong { color: var(--primary); }

  /* Empty state */
  .empty {
    text-align: center;
    color: var(--text-muted);
    padding: 80px 20px;
  }

  /* Hidden via search */
  li.hidden { display: none; }

  /* Responsive */
  @media (max-width: 900px) {
    .layout { grid-template-columns: 1fr; }
    .sidebar { position: static; max-height: none; border-right: 0; border-bottom: 1px solid var(--border); }
    .content { padding: 20px; }
    .doc-wrapper { padding: 20px; }
    .topbar { flex-direction: column; gap: 8px; align-items: flex-start; }
    .topbar input[type="search"] { width: 100%; }
  }

  /* Print */
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

  // Build "overview" pseudo-category at the front
  const overviewCat = {
    id: "overview",
    name: "總覽",
    icon: "🏠",
    docs: [{
      id: "overview-readme",
      filename: "knowledge/README.md",
      title: "Knowledge Base 總覽",
      html: data.overview_html,
    }],
  };
  const allCats = [overviewCat, ...data.categories];

  let activeCatId = allCats[0].id;
  let activeDocId = allCats[0].docs[0].id;

  function buildTabs() {
    tabsEl.innerHTML = "";
    allCats.forEach((cat) => {
      const t = document.createElement("div");
      t.className = "tab" + (cat.id === activeCatId ? " active" : "");
      t.innerHTML = `<span class="icon">${cat.icon}</span>${cat.name}<span class="count">${cat.docs.length}</span>`;
      t.onclick = () => selectCategory(cat.id);
      tabsEl.appendChild(t);
    });
  }

  function buildSidebar() {
    const cat = allCats.find((c) => c.id === activeCatId);
    if (!cat) { sidebarEl.innerHTML = ""; return; }
    sidebarEl.innerHTML = `
      <div class="sidebar-header">${cat.icon} ${cat.name} (${cat.docs.length})</div>
      <ul>
        ${cat.docs.map((d) => `
          <li>
            <a href="#" data-id="${d.id}" class="${d.id === activeDocId ? "active" : ""}" data-title="${escapeAttr(d.title)}" data-filename="${escapeAttr(d.filename)}">
              ${escapeHtml(d.title)}
              <span class="filename">${escapeHtml(d.filename)}</span>
            </a>
          </li>`).join("")}
      </ul>
    `;
    sidebarEl.querySelectorAll("a").forEach((a) => {
      a.onclick = (e) => {
        e.preventDefault();
        selectDoc(a.dataset.id);
      };
    });
    applySearchFilter();
  }

  function buildContent() {
    const cat = allCats.find((c) => c.id === activeCatId);
    const doc = cat ? cat.docs.find((d) => d.id === activeDocId) : null;
    if (!doc) {
      contentEl.innerHTML = `<div class="empty">未選擇文件</div>`;
      return;
    }
    contentEl.innerHTML = `
      <article class="doc-wrapper">
        <div class="doc-meta">
          <span>${cat.icon} ${escapeHtml(cat.name)}</span>
          <span class="filename">${escapeHtml(doc.filename)}</span>
        </div>
        <div class="doc-content">${doc.html}</div>
      </article>
    `;
    contentEl.scrollTop = 0;
  }

  function selectCategory(catId) {
    activeCatId = catId;
    const cat = allCats.find((c) => c.id === activeCatId);
    activeDocId = cat && cat.docs[0] ? cat.docs[0].id : null;
    location.hash = `${activeCatId}/${activeDocId || ""}`;
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
      const haystack = (a.dataset.title + " " + a.dataset.filename).toLowerCase();
      li.classList.toggle("hidden", !!q && haystack.indexOf(q) === -1);
    });
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));
  }
  function escapeAttr(s) { return escapeHtml(s); }

  function fromHash() {
    const h = location.hash.replace(/^#/, "");
    if (!h) return;
    const [catId, docId] = h.split("/");
    const cat = allCats.find((c) => c.id === catId);
    if (!cat) return;
    activeCatId = cat.id;
    if (docId) {
      const doc = cat.docs.find((d) => d.id === docId);
      if (doc) activeDocId = doc.id;
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

  // Keyboard: 1-7 for tab switching
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
