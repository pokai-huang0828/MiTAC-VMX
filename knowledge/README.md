# Knowledge Base — Kenny Huang VMX PM

> Kenny 的 PM 評估期知識庫,結構化來自:KB / Sheet / Jira / 會議錄音 / Coffee chat / Hub 第三 tab 自萃取框架。
> 整理日期:2026-05-06(初版)
> 最新狀態同步:**2026-05-11 Weekly**(含 QBR KPI 100K / Honeywell ME 新案 / Lens Cover **6 月 release**(HAWK-582 單軌)/ Vinicius Live View JS lib / Plan Type ↔ 啟用層級議題)
> ⭐ **本週 Summary**:[`weekly-summary/2026-05-11_week-of-may-8.md`](../weekly-summary/2026-05-11_week-of-may-8.md)(含 47 票 VMX pending 180d triage + 48 票 HAWK opened 分組 + 對外 Δ 校正表)

🌐 **[在瀏覽器開啟 Knowledge Hub →](../websiteview/knowledge.html)**(static v2,離線可用,6 分類 + 搜尋 Ctrl+K + sticky TOC)
🏠 [Mission Control](../websiteview/index.html) — 三層 IA(NOW / CASES / KNOWLEDGE)

**直接編輯 HTML / CSS / JS** — 無 build script(2026-05-11 起改 static)。
- HTML:`websiteview/knowledge.html`
- CSS:`websiteview/css/knowledge.css`
- JS:`websiteview/js/knowledge.js`(scroll spy + 搜尋 filter)
- 新增 / 刪除 .md 文件後,要手動更新 `knowledge.html` 內對應 `<a class="doc-card">` 卡片。

---

## 🔗 上游資料源

| 來源 | 連結 / 路徑 | 性質 |
|------|------------|-----|
| **VMX Knowledge Base** | https://service.visionmaxfleet.com/portal/en/kb/vm | ✅ 已 ship 的官方事實 |
| Request Tracker Sheet | https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit | 內部進行中 |
| AI 工作計畫 Sheet | 同上 (gid=339075798) | AI team 內部追蹤 |
| Jira | https://jira.navman.co.nz/jira/ | RD ticket 事實狀態 |
| MiAI Roadmap (對外) | `../MiAI Roadmap Introduce 2026024.pptx` | 客戶 / 主管版 |
| case-learning Hub | `../websiteview/case-hub.html` | 客戶案 + PM 框架 |
| Portal HTML Briefings | `../websiteview/portal-briefing.html` + `../websiteview/portal-architecture.html` | 客戶簡報用 |

---

## 📁 Folder 結構

| Folder | 內容 | 何時用 |
|--------|------|-------|
| **[01_product-knowledge/](01_product-knowledge/)** | KB cheatsheet / 機種 / Events / Voice / Roadmap | 對客戶 / RD 講具體 spec 前查 |
| **[02_organization-map/](02_organization-map/)** | 內部利害關係人 / 客戶 / Coffee chat 待問 | 寫信 / 找人前查 |
| **[03_systems-architecture/](03_systems-architecture/)** | Portal 雙層 / Plan Type / Server AI 架構 | 對客戶 demo / 解釋 demo 前查 |
| **[04_pm-frameworks/](04_pm-frameworks/)** | 三層真相 / 承諾層次 / 4 條核心原則 | 寫 proposal / 跟 Brian 對話前查 |
| **[05_workflows/](05_workflows/)** | HTML 簡報 SOP / MDT 模板 / Sheet sweeper | 動手做東西前查 |
| **[06_calibration-log/](06_calibration-log/)** | 已校正事實 / Sheet vs Jira mismatch 紀錄 | 確認自己沒講錯話 |

---

## 三層真相 — 進入 KB 前的閱讀準則

```
┌─────────────────────────────────────────┐
│  KB         → 已 ship 的事實              │   對客戶可具體承諾
├─────────────────────────────────────────┤
│  Sheet      → 內部進行中                  │   PM 內部判斷依據
├─────────────────────────────────────────┤
│  Roadmap    → 對外規劃故事                │   客戶 / 主管的版本
└─────────────────────────────────────────┘
```

**衝突處理**:對外用 Roadmap、對內用 Sheet、實際是否能用看 KB。

詳見 [04_pm-frameworks/three-truth-layers.md](04_pm-frameworks/three-truth-layers.md)。

---

## 🚦 快速指南

### 「我要對客戶講 X 功能」
1. 開 KB(https://service.visionmaxfleet.com/portal/en/kb/vm)搜 X
2. 沒找到 → 看 [06_calibration-log](06_calibration-log/) 有沒有寫「狀態待釐清」
3. 還沒釐清 → 不要承諾,改用「Roadmap planned, 內部測試中」(Yawning / Smoking 都這狀態)

### 「我要找對的人問 X」
- 看 [02_organization-map/stakeholders.md](02_organization-map/stakeholders.md)
- 已準備好的問題:[02_organization-map/coffee-chat-questions.md](02_organization-map/coffee-chat-questions.md)

### 「我要做新簡報」
- 開 [05_workflows/html-presentation-pipeline.md](05_workflows/html-presentation-pipeline.md)
- PPT 路線:套 `../MDT_2026_powerpoint_template.pptx`
- HTML 路線:套 `#5B9BD5 / #4472C4 / #ED7D31` + Calibri

### 「我要應對 Brian 戰略議題」
- [04_pm-frameworks/](04_pm-frameworks/) 全部讀過一次
- 關鍵:VMX/BMS 同步翻案 / Beta 模式 / Sunset Plan(舊 Playback 案)

---

## 知識更新原則

1. **新事實 / 校正** → 寫進 [06_calibration-log/](06_calibration-log/),不要直接改舊文件
2. **新會議洞察** → 寫進 `../meetings/YYYY-MM-DD_*` + 把戰略議題抽出到 04 / 06
3. **客戶案 update** → 進 `../case-learning/`
4. **Sheet / Jira 變動** → 截圖驗證 visible rows,不信 CSV export

⚠️ **這個資料夾是 source of truth 的整理層,不是原始資料層**。原始資料在 `../meetings/`、`../portal_reference/`、`../case-learning/`,以及 NotebookLM 線上(notebook id `a3aad3ec-ecf3-4468-a0d9-13a6a18359c7`)。

---

## 版本

| 日期 | 變動 |
|------|------|
| 2026-05-06 | 初版建立,整合 13 條 Claude memory + Hub 第三 tab + 5/6 Q2 Review 會議洞察 |
| 2026-05-07 | 5/7 AI Weekly 大量校正:Yawning 灰階模型 + VMX-7432 對應 / Eating 17x 客訴(ID 6652)/ LDWS YOLO device-side Pending / Lens Cover 雙軌(Azuga vs BMS)/ Speed Sign Flip 重訓 / Spencer = Cloud lead(原 Adonis 誤認) |
