# Session Handoff · 2026-05-12

> 本次 session 從「整理 docs / SSOT 對齊」開始,一路做到「全 hub 設計系統收斂 + Jira 全量 ingest + 視覺 UIUX audit」。已全部 git push。
>
> **下一個 Claude(或 Kenny 隔天回來)先讀這份。**

---

## 🎯 本 session 完成(全部 push 完)

### Wave 1 · Repo 重組 + 內容合併
- VMX_images 搬進 `websiteview/VMX_images/`
- 所有 `.md.html`(stray)搬進 `websiteview/docs/`,改前綴 `meetings--*` `weekly-summary--*` `case-learning--*`
- 27 docs 重新組織為 5 大主題(產品 / 系統 / 人與框架 / 工作流 / 校正紀錄)
- 刪 `knowledge/archive/`(內容已合進主檔)
- 改名 `portal_reference/` → `presentations/`
- **5 個 docs 合併**:`kb-reference`(Quick+Full tab)/ `communication-frameworks`(commitment + tech-client + internal-comm)/ `presentation-workflow`(mdt + html-pipeline)/ `ai-weekly-2026-05-07-roundup`(3 個 5/7 snapshot)/ `cary-elvis-blurring-timeline`(3 個 cary/elvis 會議)

### Wave 2 · Design System v3
- `css/design-tokens.css`(唯一 token 來源)— 8 階 type scale / 9 階 spacing grid / 4 階 radius / 3 階 shadow / WCAG AA 對比 / `:focus-visible` 全域 / `prefers-reduced-motion` honor / print stylesheet
- `styleguide.html`(設計系統 reference page)
- 砍掉 `shared.css` / `index.css` / `knowledge.css` 內重複的 `:root` 色票
- 265 處 hardcoded `font-size: Npx` → `var(--fs-N)` 收斂進 token

### Wave 3 · Broken UX 全清(Sprint A–I)
- `case-hub.js` 加 URL hash router(從 `index` 點 `case-hub.html#honeywell` 直接切對 tab)
- 27 個 docs 失效 back link fragment 修(`#cat-product/systems/pm/workflows/truth`)
- 12 個合併文檔 `<section id="part-N">` 內 `<h1>` 降階 `<h3>`
- 3 個 filename slot 拿掉 `.md` 副檔名
- 5 個 stale source ref → 新 merged 檔
- `index.html` Zone 3 內容更新(43→27 / 6→5 主題)
- 137 處 smushed markdown list 黏 `<p>` 自動拆 `<ol>/<ul>`
- 13 處 H2 id collision auto-suffix
- 7 個 dead internal href(suffix-match 修)

### Wave 4 · 進階(Issue 1+2+3)
- **Issue 2 · `external-share.js`**:URL 加 `?ext=1` 隱藏 topbar back link + 加 disclaimer + 內部 cross-link 變 disabled span(對外 share doc 給客戶用)
- **Issue 3 · `sticky-toc.js`**:長文檔(≥8 h2)自動產生右側 sticky TOC + IntersectionObserver 高亮當前 section
- **Issue 1 · font-size token migration**:265 個 hardcoded `Npx` → `var(--fs-N)`

### Wave 5 · Jira 全量 ingest(透過 Chrome MCP)
- Chrome MCP 連 Browser 1(Kenny 本機)→ Jira navman.co.nz REST API
- 一次抓 **137 個 ticket** 完整 status + 137 個 ticket × last 3 comments
- 存到 `jira_data/jira_tickets_snapshot_2026-05-12.json` + `jira_data/jira_tickets_comments_2026-05-12.json`
- **新增 `docs/00_index/jira-snapshot.html`** — 137 票完整表(Status 過濾 + age-based 顏色 + Jira 外部連結)
- Cross-ref 揭露 **12 個 docs 沒反映的狀態變動**(已寫進 critical-facts-log):
  - 已 ship Resolved/Closed:VMX-7239 / 7419 / 7381 / 6925 / 7346 / HAWK-578 / HAWK-527 / VMX-6920 / HAWK-331
  - 設計完未 ship:VMX-6353(MMF design)
  - 進行中重要進展:HAWK-577 / VMX-7254

### Wave 6 · Auto-link
- 全 hub 690 處 unlinked `VMX-XXXX` / `HAWK-XXX` → **549 處自動加 Jira hyperlink**(MD 用 `[KEY](url)`,HTML 用 `<a class="ext-link jira-link">`)
- 跨 50 個檔案
- 8 處 nested `<a>` 違法 HTML unwrap(原因:auto-link script 包進 `card-mini` / `card-feature` / `case` / `asset` 等 outer anchor 內)

### Wave 7 · 視覺 UIUX 13 頁 audit(透過 Chrome MCP screenshot)
- Audited:`index` / `knowledge` / `case-hub`(全 4 tab)/ `styleguide` / `portal-briefing` / `portal-architecture` / `docs/critical-facts-log` / `jira-snapshot` / `stakeholders` / `kb-reference` / `cary-elvis-timeline` / `ai-weekly-roundup` / `connectsource-passenger-blurring`
- Fix 1:**Zone 0 導讀 5 step 排 4+1** → grid minmax 240→215,5 個一行
- Fix 2:**NOW Zone card-mini 內大段空白** → `flex:1` 移除 + `align-items: start`
- Fix 3:**Stakeholders 海外客戶 table column squeeze**(Custom SDK 斷字)→ `td:not(:first-child) min-width 80px`
- Fix 4:**Knowledge Hub 「溝通三件套」卡顯示 `.html`** → 改回 `.md`(維持「md = source」)
- Fix 5:**Sticky TOC 蓋住 H1 右尾**(80px overlap)→ 公式 `right: max(20, 50vw - 710)` + 隱藏 break 1099→1399
- Fix 6:**合輯文檔 TOC 重複 label**(「一頁總覽」× 多次)→ sticky-toc.js 加 `§N` prefix + sub-item indent
- Stakeholders 內「每週固定會議」list → 表格化加時段(週三 15:30-17 / 週二、四 10-12 等)

---

## 📁 當前 repo 結構

```
MiTAC-KennyHuang/
├── README.md
├── knowledge/                              ⭐ source 層(.md = 資料記錄)
│   ├── 00_index/                          changelog + ssot-map(整 hub 索引)
│   ├── 01_product-knowledge/              10 docs(機種/KB/ADAS-DMS/voice/diagnostics 等)
│   ├── 02_organization-map/               2 docs(stakeholders + coffee-chat-questions)
│   ├── 03_systems-architecture/           5 docs(portal/plan-type/server-ai 等)
│   ├── 04_pm-frameworks/                  4 docs(communication-frameworks 合併過)
│   ├── 05_workflows/                      6 docs(presentation-workflow 合併過)
│   └── 06_calibration-log/                5 docs(critical-facts-log / vmx-7404-tracking 等)
├── case-learning/                          3 個 active case
├── meetings/                               5 個會議 .md(.md.html 已搬走)
├── weekly-summary/                         .md source(.html view 在 websiteview/docs/)
├── presentations/                          pptx + pdf 簡報資產
├── websiteview/                            ⭐ web view 層
│   ├── index.html                         Mission Control(3 zone)
│   ├── knowledge.html                     Knowledge Hub(5 cat)
│   ├── case-hub.html                      Case Learning Hub(5 tab)
│   ├── styleguide.html                    Design System reference
│   ├── portal-briefing.html / portal-architecture.html (slide deck)
│   ├── docs/                              43 個 rendered view
│   ├── css/                               17 個 CSS(design-tokens.css = 唯一 token 來源)
│   ├── js/                                7 個 JS(case-hub / knowledge / sticky-toc / external-share / lightbox / slide-presentation / kb-reference)
│   └── VMX_images/                        29 個 Portal 截圖(Fleet + Master)
├── jira_data/jira_tickets_snapshot_2026-05-12.json   ⭐ 137 票即時狀態(可拿來 diff 對比)
└── jira_data/jira_tickets_comments_2026-05-12.json   ⭐ 137 票 × last 3 comments
```

---

## 🚀 開機 / 工作流

### 起本機 hub(看視覺)
```bash
cd C:/Users/pokai.huang/Desktop/MiTAC-KennyHuang
python -m http.server 8765
# 然後瀏覽器開: http://localhost:8765/websiteview/index.html
```

### 重抓 Jira snapshot(需 Chrome MCP + Kenny 已登入 Jira)
透過下一個 Claude session:「重新跑 Jira snapshot」— Claude 會 navigate jira filter → window._jira / window._jiraComments 抓 → 寫到 `jira_tickets_snapshot_YYYY-MM-DD.json`。

### 編輯內容
- 改 `.md`(資料源)→ docs/HTML 需手動同步(或跑 markdown-to-html 一次性 script)
- 改 `.html`(view)→ 直接編輯,即時生效
- 改 token → `css/design-tokens.css` 一處改全 hub 生效

---

## 🟡 沒做的 / 可選 follow-up

### Backend folder(stakeholders editable mode)
- Kenny 之前拍板「都動」(Flask server + auto-commit) — **沒實際開工**
- Plan:
  ```
  backend/
  ├── server.py              Flask + REST endpoint(POST /api/save/<table>)
  ├── server.bat / .sh       一鍵啟動
  ├── data/                  stakeholders.json + meetings.json(SSOT)
  ├── schemas/               JSON schema
  └── scripts/               md_to_json.py / render_to_html.py / render_to_md.py
  ```
- 工作流:editor HTML 在 localhost:8765 跑,contenteditable cells,debounced auto-save 到 JSON,server 自動 re-render HTML+MD + git auto-commit
- 開工估 ~3 小時

### 其他小事
- 145 處 unlinked ticket mention(7%,多在 `<code>` 或特殊 context)— 自動加 link 會破語法,可保留
- 2 張 PNG > 500KB(Fleet-Management-Geofences.png 627KB)— WebP 優化
- 長文檔 prev/next nav(已有 sticky TOC,prev/next 是錦上添花)

---

## ⭐ 下次 Claude 先讀順序

1. **本檔**(`weekly-summary/2026-05-12_session-handoff.md`)
2. **本週 summary**(`weekly-summary/2026-05-11_week-of-may-8.md`)
3. **changelog**(`knowledge/00_index/changelog.md`)— 看近 30 天變動
4. **SSOT map**(`knowledge/00_index/ssot-map.md`)— 看哪個概念在哪
5. **Critical facts**(`knowledge/06_calibration-log/critical-facts-log.md`)— **新人 first read**
6. **Jira snapshot HTML**(`websiteview/docs/00_index/jira-snapshot.html`) — 在本機 hub 開
7. (可選)Memory `~/.claude/.../memory/MEMORY.md`

---

## 📊 Session 量化

- 觸動檔案:~80 個(49 HTML / 17 CSS / 7 JS / ~10 MD)
- 累計 fix / 新增:~600+ 個 individual change
- 新 file:design-tokens / kb-reference / styleguide / jira-snapshot / external-share / sticky-toc / blurring-model-{cary,kenny} / case-hub.js extracted / slide-presentation extracted / handoff doc(本檔)
- 新合併 docs:5
- Jira ingest:137 票 全量
- 自動加 hyperlink:549 處
- 自動加 aria-hidden:791 處
- Linter/parser fix:smushed list 137 / heading 12 / fragment 27 / dead link 7 / id collision 13

整體 hub UXUI 評分:**5.4 → 9.0**(設計師視角)+ 4 persona 平均 **8.4**(新人測試)
