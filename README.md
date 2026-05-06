# MiTAC-KennyHuang Workspace

> Kenny Huang(黃柏凱)在 MiTAC VMX 評估期(2026-04 起)的工作目錄。
> 收容:portal 知識資產、客戶案件追蹤、會議紀錄、NotebookLM 同步、簡報模板、PM 教材。
> 最後更新:2026-05-06

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
| **[`knowledge/`](knowledge/README.md)** ⭐ | 結構化知識庫(source of truth) | 6 大 folder:Product / Org / Systems / PM Frameworks / Workflows / Calibration |
| [`portal_reference/`](portal_reference/) | Brian portal task 主交付 | HTML 客戶簡報 25 張 + PDF 複刻 55 張 |
| [`Case_learning/`](Case_learning/) | 客戶案件追蹤 | Connect Source / Platform Science / case hub |
| [`meetings/`](meetings/) | 會議筆記 | Video Safety / Q2 Review |
| [`VMX_images/`](VMX_images/) | Portal 截圖 | Fleet 16 張 + Master 8 張 |
| `EVO_image_update/` | 韌體更新流程文件 | `.gitignore` 排除 binary,只留 process.md |
| [`docs/`](docs/) | Repo-level meta 文件 | git history 清理評估等 |
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
| AI Team 15 件 active tasks(2026-05-05 截圖) | [knowledge/06_calibration-log/ai-team-sheet-snapshot-2026-05-05.md](knowledge/06_calibration-log/ai-team-sheet-snapshot-2026-05-05.md) |
| 已校正的 VMX 事實(別再答錯) | [knowledge/06_calibration-log/critical-facts-log.md](knowledge/06_calibration-log/critical-facts-log.md) |

---

## 工作流入口

### 簡報製作
- **PPT 路線**:拷貝 `MDT_2026_powerpoint_template.pptx`,從 6 個 layout 插入 slide
- **HTML 路線**:`#5B9BD5` / `#4472C4` / `#ED7D31` + Calibri,SOP 見 [knowledge/05_workflows/html-presentation-pipeline.md](knowledge/05_workflows/html-presentation-pipeline.md)

⚠️ `portal_reference/*.html` 與 `Case_learning/case-learning-hub.html` 仍是舊 navy 配色,下次重做時換成 MDT 2026 模板色票。

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

`image_update/*` 與 `EVO_image_update/*` 排除(韌體大檔不入 repo),保留 `EVO_image_update/EVO image update process.md`(流程文件)。`.claude/worktrees/` 排除本機暫存。

> Repo 體積偏大(`.git` 140 MB / 工作樹 31 MB),原因與處理方式見 [docs/git-history-cleanup-assessment.md](docs/git-history-cleanup-assessment.md)。

---

## 接手指南(若你是接手 Kenny 的人)

1. 先讀本檔(README.md)+ [knowledge/README.md](knowledge/README.md)
2. 讀 `portal_reference/vmx_portal_client_briefing.html` 了解 portal 全貌
3. 開 `Case_learning/case-learning-hub.html`(3 tab),先看「PM 策略洞察」tab 拿框架,再看兩個客戶案
4. 找 Brian 對齊主管期待
5. 評估期可見度從 [VMX-7404 ADAS Failure](knowledge/06_calibration-log/vmx-7404-tracking.md) 入手最快
