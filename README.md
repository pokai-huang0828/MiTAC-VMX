# MiTAC-KennyHuang Workspace

> Kenny Huang(黃柏凱)在 MiTAC VMX 評估期(2026-04 起)的工作目錄。
> 收容:portal 知識資產、客戶案件追蹤、會議紀錄、NotebookLM 同步、簡報模板、PM 教材。
> 最後更新:2026-05-08
> ⭐ **若你是接手 Claude session**:先讀本檔 + [`knowledge/README.md`](knowledge/README.md) + `~/.claude/.../memory/MEMORY.md`

---

## 一頁總覽

| 項目 | 值 |
|------|---|
| 入職時間 | 2026-04 評估期 |
| 角色 | VMX Product Manager |
| 測試設備 | MioEYE K245(L3024290010,401 events) |
| 主力案件 | Brian portal task(已交付) + Platform Science / Connect Source |
| 簡報基底(2026-05-05 起) | `MDT_2026_powerpoint_template.pptx` |
| AI Roadmap 對外版 | `MiAI Roadmap Introduce 2026024.pptx`(7 張) |

---

## 資料夾結構

| 路徑 | 用途 | 重點 |
|------|------|-----|
| **[`knowledge/`](knowledge/README.md)** ⭐ | 結構化知識庫(source of truth) | 43 份 md / 6 大分類:Product / Org / Systems / PM Frameworks / Workflows / Calibration |
| **[`websiteview/`](websiteview/index.html)** ⭐⭐ | **Mission Control** v2 — 三層 IA(NOW / CASES / KNOWLEDGE)+ Hero KPI gauge + Cabinet Grotesk / Satoshi 字型 | landing / Knowledge Hub / Case Hub(含 Honeywell + Weekly Summary tab)/ Portal Briefing / Architecture |
| **[`weekly-summary/`](weekly-summary/2026-05-11_week-of-may-8.md)** ⭐ | 每週對齊摘要(email + Jira + repo Δ) | 5/11 起每週一上工前 · 對應 case-hub Weekly tab |
| [`case-learning/`](case-learning/) | 客戶案件追蹤(.md 來源) | Connect Source / Platform Science / **Honeywell ME(新)** |
| [`meetings/`](meetings/) | 會議筆記 | Video Safety / Q2 Review / AI Weekly / Sync-up |
| [`VMX_images/`](VMX_images/) | Portal 截圖 | Fleet 21 張 + Master 8 張 |
| [`portal_reference/`](portal_reference/) | Brian portal task 原始交付歸檔 | 客戶版 pptx + 架構版 PDF + 草稿 md |
| `EVO_image_update/` | 韌體更新流程文件 | `.gitignore` 排除 binary,只留 process.md |
| `MDT_2026_powerpoint_template.pptx` | 官方簡報模板(6 layouts, 16:9) | — |
| `MiAI Roadmap Introduce 2026024.pptx` | AI Roadmap 對外版(7 張) | — |

---

## 三層真相框架(對外講不同版)

| 層 | 入口 | 對誰講 |
|----|------|-------|
| **KB**(已 ship 事實) | `https://service.visionmaxfleet.com/portal/en/kb/vm` | 客戶可具體承諾 |
| **AI Sheet**(內部進行中) | [VMX Features Tracking Table](https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit?gid=339075798) | PM 內部判斷 |
| **MiAI Roadmap**(對外規劃) | `MiAI Roadmap Introduce 2026024.pptx` | 客戶 / 主管 |

**衝突處理**:對外用 Roadmap、對內用 Sheet、實際是否能用看 KB。詳見 [knowledge/04_pm-frameworks/three-truth-layers.md](knowledge/04_pm-frameworks/three-truth-layers.md)。

⚠️ AI Sheet hidden row = **團隊已決定不做**,不是 PM 介入空間。CSV export 會把 hidden 一起拉,以 sheet UI 可見性為準。

---

## 進行中工作

| 主題 | 文件 |
|------|-----|
| VMX-7404 ADAS Failure 追蹤 | [knowledge/06_calibration-log/vmx-7404-tracking.md](knowledge/06_calibration-log/vmx-7404-tracking.md) |
| Coffee chat 待問清單(Brian / Mori / Jimmy / Spencer / Lucy / Tony) | [knowledge/02_organization-map/coffee-chat-questions.md](knowledge/02_organization-map/coffee-chat-questions.md) |
| AI Team 16 件逐行 5/7 狀態 + Brian 1on1 talking points | [knowledge/06_calibration-log/ai-team-row-by-row-status-2026-05-07.md](knowledge/06_calibration-log/ai-team-row-by-row-status-2026-05-07.md) |
| AI 工作計畫 × Jira filter 36457 對齊 + 10 票 comment 深掘 | [knowledge/06_calibration-log/ai-tab-jira-alignment-2026-05-07.md](knowledge/06_calibration-log/ai-tab-jira-alignment-2026-05-07.md) |
| 2026-05-07 AI Weekly 會議重大訊號(17x 客訴 / LDWS Pending / Lens Cover 雙軌) | [meetings/2026-05-07_ai-weekly_meeting-record.md](meetings/2026-05-07_ai-weekly_meeting-record.md) |
| 已校正的 VMX 事實(別再答錯) | [knowledge/06_calibration-log/critical-facts-log.md](knowledge/06_calibration-log/critical-facts-log.md) |

---

## 工作流入口

### Web Hub(本機開)
打開 [`websiteview/index.html`](websiteview/index.html) — Mission Control v2,三層 IA(NOW / CASES / KNOWLEDGE)。**全 static HTML,直接編輯**,無 Python build script。

### HTML 結構(2026-05-11 起 v2 static)
- 每頁 = 一個 .html + 對應 css/ + js/(都在 `websiteview/css/` 和 `websiteview/js/`)
- 直接 edit HTML / CSS / JS,**不再用 Python 生成**
- 字型升級:Cabinet Grotesk(heading)+ Satoshi(body),Fontshare CDN
- 主要檔案:
  - `websiteview/index.html` + `css/index.css` — Mission Control 入口
  - `websiteview/knowledge.html` + `css/knowledge.css` + `js/knowledge.js` — Knowledge Hub(43 文件 6 分類)
  - `websiteview/case-hub.html` + `css/case-hub.css` — 5 tab(Honeywell / PS / CS / PM / Weekly)
  - `weekly-summary/*.md.html` + `css/weekly-summary.css` + `js/weekly-summary.js` — 每週 summary
- 舊 build script `_build_*.py` 已全部移除

### 簡報製作
- **PPT 路線**:拷貝 `MDT_2026_powerpoint_template.pptx`,從 6 個 layout 插入 slide
- **HTML 路線**:#5B9BD5 / #4472C4 / #ED7D31 + Calibri(舊主題)或 Cabinet Grotesk / Satoshi(新主題 v2)
- SOP 見 [knowledge/05_workflows/html-presentation-pipeline.md](knowledge/05_workflows/html-presentation-pipeline.md)
- portal-briefing / portal-architecture 兩個 slide deck 仍是 static(2026-05-11 前由 python build,現已 freeze)

### Jira(MiTAC R&D)
- 入口:`https://jira.navman.co.nz/jira/`
- VMX 全 open issues filter:`https://jira.navman.co.nz/jira/issues/?filter=36457`

### NotebookLM
- 入口:`https://notebooklm.google.com/notebook/a3aad3ec-ecf3-4468-a0d9-13a6a18359c7`

### Portal
- Master:`portal.visionmaxfleet.com`(經銷商視角)
- Fleet:`www.visionmaxfleet.com`(客戶視角,Kenny 名下 K245)
- KB:`service.visionmaxfleet.com/portal/en/kb/vm`(已讀完核心 9 篇)

---

## .gitignore 規則

所有 dotfiles / dotfolders(`.claude/`、`.vscode/` 等個人 IDE / 工具設定)整體排除,只保留 `.gitignore` 本身。`image_update/*` 與 `EVO_image_update/*` 排除(韌體大檔不入 repo),保留 `EVO_image_update/EVO image update process.md`(流程文件)。Python `__pycache__/` 與 `*.pyc` 排除。

---

## 接手指南(若你是接手 Kenny 的人)

1. 先讀本檔(README.md)+ [knowledge/README.md](knowledge/README.md)
2. 用 Live Server 開 [`websiteview/index.html`](websiteview/index.html),從 Knowledge Hub 開始翻
3. 開 [`websiteview/case-hub.html`](websiteview/case-hub.html)(3 tab),先看「PM 策略洞察」tab 拿框架,再看兩個客戶案
4. 找 Brian 對齊主管期待
5. 評估期可見度從 [VMX-7404 ADAS Failure](knowledge/06_calibration-log/vmx-7404-tracking.md) 入手最快
