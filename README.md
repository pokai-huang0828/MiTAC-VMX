# MiTAC-KennyHuang Workspace

> Kenny Huang(黃柏凱)在 MiTAC VMX 評估期(2026-04 起)的工作目錄。
> 收容:portal 知識資產、客戶案件追蹤、會議紀錄、NotebookLM 同步、簡報模板、PM 教材。
> 最後更新:2026-05-05

---

## 1. 一頁總覽

| 項目 | 值 |
|------|---|
| 入職時間 | 2026-04 評估期 |
| 角色 | VMX Product Manager |
| 測試設備 | MioEYE K245(L3024290010,401 events) |
| 目前主力 | Brian portal task(已交付) + Platform Science / Connect Source 客戶案 |
| 工作 IDE | VS Code,git tracked,連 GitHub repo |
| 簡報基底(2026-05-05 起) | `MDT_2026_powerpoint_template.pptx` |
| AI Roadmap 對外版 | `MiAI Roadmap Introduce 2026024.pptx`(7 張) |

---

## 2. 資料夾結構

| 路徑 | 用途 | 重點 |
|------|------|-----|
| **`knowledge/`** ⭐ | **結構化知識庫**(2026-05-06 整理) | 6 大 folder:Product / Org / Systems / PM Frameworks / Workflows / Calibration |
| `portal_reference/` | Brian portal task 主交付 | HTML 客戶簡報 25 張 + PDF 複刻 55 張 |
| `Case_learning/` | 客戶案件追蹤 | Connect Source / Platform Science / case hub |
| `meetings/` | 會議筆記 | Video Safety / Q2 Review |
| `神達VMX/` | NotebookLM 同步資料 | 36 sources / notes / metadata |
| `VMX_images/` | Portal 截圖 | Fleet 16 張 + Master 8 張 |
| `EVO_image_update/` | 韌體更新流程 | base + region + QPST + driver(.gitignore 排除) |
| `MDT_2026_powerpoint_template.pptx` | 官方簡報模板 | 6 layouts,16:9 |
| `MiAI Roadmap Introduce 2026024.pptx` | AI Roadmap 對外版 | 7 張(2023-2027 4 tiers) |

### 📚 knowledge/ 子結構

| Folder | 用途 |
|--------|------|
| [01_product-knowledge/](knowledge/01_product-knowledge/) | KB cheatsheet / 機種 / Events / Voice / Roadmap |
| [02_organization-map/](knowledge/02_organization-map/) | 內部利害關係人 + 客戶 + Coffee chat 待問 |
| [03_systems-architecture/](knowledge/03_systems-architecture/) | Portal 雙層 / Plan Type / Server AI 架構 |
| [04_pm-frameworks/](knowledge/04_pm-frameworks/) | 三層真相 / 承諾層次 / 4 條核心原則 / UI 變更管理 |
| [05_workflows/](knowledge/05_workflows/) | HTML SOP / MDT 模板 / Sheet sweeper / Memory 系統 |
| [06_calibration-log/](knowledge/06_calibration-log/) | 已校正事實 / Sheet vs Jira mismatch / Roadmap vs 內部 |

→ **入口**:[knowledge/README.md](knowledge/README.md)

---

## 3. 核心交付(主要產出)

### Brian Portal Task(已完成)

```
portal_reference/
├── vmx_portal_client_briefing.html  ⭐ 25 張中文客戶簡報(可現場 demo)
├── vmx_portal_client_briefing.md    同內容 markdown 5 部分
├── vmx_architecture_replica.html    ⭐ 55 張英文 PDF 複刻(海外客戶用)
├── VMX_Master_Fleet_Customer_Intro.pptx  PPT 版
├── source_arch.pdf                  原始 VisionMax 架構文件
```

⚠️ 兩份 HTML 還是舊 navy `#003B71` theme — 下次重做要換成 MDT 2026 模板色票(`#5B9BD5` / `#4472C4` / `#ED7D31`)。

### 客戶案件(進行中)

```
Case_learning/
├── case-learning-hub.html              ⭐ 3-tab dashboard(2026-04 – 2026-05 範圍)
├── CONNECTSOURCE-PASSENGER-BLURRING.md Connect Source × passenger blurring 信件追蹤
└── Vinicius-PLATFORM SCIENCE.md        Platform Science Vision Max APIs 整合案
```

`case-learning-hub.html` 三個 tab:

| Tab | 內容 |
|-----|------|
| **Platform Science**(US 客戶) | 專案總覽 / 關係人 / 時間軸 / 技術資訊 / 待辦事項 / 商機與風險 / PM 分析 |
| **CONNECTSOURCE**(passenger blurring 需求) | 事件總覽 / 關係人 / 商業規模 / 時間軸 / **衝突分析** / 待辦事項 / PM 建議 |
| **PM 策略洞察**(跨案例) | 跨案例洞察 / **承諾層次框架** / 技術型客戶溝通 / **內部溝通斷層** / 核心原則 |

→ 第三個 tab 是 Kenny 兩個案件交手後萃取的 PM 框架,評估期內最有價值的個人沉澱。

⚠️ Hub 用 navy `#1a3a5c` theme,跟兩份 portal HTML 同樣是舊配色 — 下次重做要一起換成 MDT 2026 模板色。

### 會議紀錄(進行中)

```
meetings/
├── 2026-04-29_VideoSafety_deep-analysis.md  深度分析(499 行)
└── 2026-04-29_VideoSafety_per-person.md     按人切版(230 行)
```

### NotebookLM 同步(36 sources)

`神達VMX/` 整套同步從 NotebookLM 抓下來的內部訓練 / 會議錄音 / 規格書 / coffee chat 文字稿。包含:
- Brian / Mori coffee chat 逐字稿
- VMX internal training(2026-04-23)
- Azuga / Bridgeron / Field-side / AI weekly 會議
- MiAI Function Test Manual / K-Series Datasheet
- 職涯戰略分析 / 新人 PM 實戰破局指南

---

## 4. 三層真相框架(對外講不同版)

| 層 | 入口 | 對誰講 |
|----|------|-------|
| **KB**(已 ship 事實) | `https://service.visionmaxfleet.com/portal/en/kb/vm` | 客戶可具體承諾 |
| **AI Sheet**(內部進行中) | [VMX Features Tracking Table > AI 工作計畫](https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit?gid=339075798) | PM 內部判斷 |
| **MiAI Roadmap**(對外規劃) | `MiAI Roadmap Introduce 2026024.pptx`(本目錄) | 客戶 / 主管 |

**衝突處理**:對外用 Roadmap、對內用 Sheet、實際是否能用看 KB。

⚠️ AI Sheet 上 hidden row = 目前不使用,**不要當「沒人扛 = PM 介入空間」**。CSV export 會把 hidden 一起拉,以 sheet UI 可見性為準。

---

## 5. 進行中工作 Top 3

### A. VMX-7404 ADAS Failure(評估期最大籌碼)
- 8/10 設備 ADAS AI Health = ADAS Failure(包含 Kenny 的 K245 L3024290010)
- 真因(2026-05-05 校正):**30 km/h × 3 mins** 行駛條件門檻沒滿足 → 市區走停會反覆觸發
- Evidence:Trip 7028714(均速 ~25 km/h,缺 ADAS Started)vs Trip 7079470(有 ADAS Started)同韌體
- 待動作:把 evidence 寫成 Jira comment 貼進 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)

### B. Coffee Chat 待問清單

詳細列表見 `.claude/projects/.../memory/project_portal_walkthrough.md` 第 10 段。

**Jimmy(MiAI lead)**
- Smoking 真實狀態(KB 沒寫 / sheet hidden / Roadmap 列 Basic / 4 個 Jira open)
- Burning ADAS / Burning DMS 是什麼意思
- Eating & Drinking(HAWK-562)— Roadmap 標 2027 為何已動?
- Face Not Found Issue 跟 VMX-7404 ADAS Failure 是否同根因

**Mori(硬體)**
- K145c / K220 / K245 / K245c / K265 各跑哪顆 Qualcomm chip(對應 Roadmap Tier)
- Harsh Acceleration / Rollover G 值門檻(memory 缺這 2 個)
- 紅色按鍵語音不一致 / Private Mode 切換按法 / 各機種 frame rate

**Brian**
- Pro / Suspend 完整定價、「13 cams / 47 cams」含義
- Contract Fleet 真實定義(Portal 上有 tab 但 PDF 未列)
- Roadmap vs Sheet 同步缺口(Smoking / VLM 兩處衝突)

**Spencer**
- Server-side AI 進度(Edge+Server / Server VLM / Edge VLM 各 stage 時程)
- Contract Fleet RBAC spec
- AI debug overlay 對客戶開關策略

### C. AI Team Sheet 真實 Active Tasks(15 件,2026-05-05 截圖驗證)

| Row | Task | PIC | JIRA |
|-----|------|-----|------|
| 4 | Yawning Detection | Jieli | VMX-7309 |
| 5 | Eyes Detection | Jieli | VMX-7309 |
| 9 | Blurring Footage | Vincent | HAWK-331 / VMX-6391 |
| 10 | LDWS Server AI | Eric | VMX-6722 / VMX-7101 |
| 30 | VLM | — | (sheet 標 2026 Q3) |
| 31 | Quantatec 鏡頭遮擋 | Jieli | VMX-6983 |
| 35 | Face Not Found Issue | Jimmy | — |
| 44 | Add box around event | Jay, Adonis | VMX-5909 |
| 45 | Server AI 統計資料釐清 | Vincent, Jimmy | — |
| 46 | Camera height 不穩定 | Jay, Vincent | HAWK-501 |
| 48 | Pedestrian Detect | Vincent | HAWK-570 |
| 49 | Eating & Drinking | Jimmy | HAWK-562 |
| 50 | Rastrac False Speed | Jonathan | VMX-7317 |
| 51 | Request event blurry | Adonis | HAWK-573 |
| 52 | Blurring on-demand fails | Adonis | HAWK-577 |

---

## 6. 工作流入口

### 簡報製作
- **PPT 路線**:拷貝 `MDT_2026_powerpoint_template.pptx`,從 6 個 layout 插入 slide
- **HTML 路線**:用模板色票重做(`#5B9BD5` / `#4472C4` / `#ED7D31` + Calibri)。SOP 詳見 `.claude/projects/.../memory/reference_html_pipeline.md`

### Jira(MiTAC R&D)
- 入口:`https://jira.navman.co.nz/jira/`
- VMX 全 open issues filter:`https://jira.navman.co.nz/jira/issues/?filter=36457`(253 筆,2026-05-05)
- Kenny 主追:VMX-7404(ADAS Failure)

### NotebookLM
- 入口:`https://notebooklm.google.com/notebook/a3aad3ec-ecf3-4468-a0d9-13a6a18359c7`
- 同步資料夾:本目錄 `神達VMX/`

### Portal
- Master:`portal.visionmaxfleet.com`(經銷商視角)
- Fleet:`www.visionmaxfleet.com`(客戶視角,Kenny 名下 K245)
- KB:`service.visionmaxfleet.com/portal/en/kb/vm`(已讀完核心 9 篇)

### 個人訓練筆記
- Google Doc:[VisionMax 平台產品常見問題](https://docs.google.com/document/d/1KYAsFw5oJKWq9jb0aZ3s93ANzaILrA4Jw5dYK5551HQ/edit)(11.7 MB)

---

## 7. 重要事實校正歷史(別再答錯)

詳見 `.claude/projects/.../memory/feedback_vmx_facts.md`。重點:

- 機種:**K145c / K220 / K245 / K245c / K265**(沒有 K165)
- ADAS 範圍:**FCW / LDW / Stop and Go / Tailgating**(不含 yawning / phone / smoking)
- ADAS 基礎計算門檻:**30 km/h × 3 mins**(2026-05-05 校正,之前 60 是錯的)
- DMS 全域門檻:**20 km/h**
- 紅色按鍵:接電話 + Manual event + Server callback + 格化 SD(**沒 panic event**)
- FCW 語音 = **"Keep distance"**(不是 "Frontal Collision Warning")
- G-Sensor 6 種:Harsh Acceleration / Braking / Cornering / Driving Impact / Parking Impact / Rollover
- TW 客戶 Traffic Sign 只能承諾 **Speed Limit**;Stop / School / Railway 沒支援
- MMF(Mobility Map Function)還沒上線

---

## 8. .gitignore 規則

`EVO_image_update/*` 排除(韌體大檔不入 repo),保留 `EVO_image_update/EVO image update process.md`(流程文件)。

---

## 9. 如果你是接手 Kenny 的人

1. 先讀本檔(README.md)
2. 讀 `portal_reference/vmx_portal_client_briefing.html` 了解 portal 全貌
3. 開 `Case_learning/case-learning-hub.html`(3 tab),先看「PM 策略洞察」tab 拿框架,再看兩個客戶案
4. 找 Brian 對齊主管期待
5. 評估期可見度從 VMX-7404 ADAS Failure 入手最快
