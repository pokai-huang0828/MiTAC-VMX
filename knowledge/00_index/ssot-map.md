# SSOT Map · 概念 ↔ 主檔 索引

> SSOT = Single Source of Truth。**每個事實只在一個檔詳寫,其他地方只引用 + link**。
> 這份就是「我要找 X 概念的 master,該去哪個檔」對照表。
>
> 改概念時:**只改 master 一份,其他引用處透過 link 自動同步**(別複製貼上)。

---

## 🏭 產品事實

| 概念 | SSOT 主檔 | 摘要引用處 |
|-----|---------|-----------|
| K-series 機種 spec(K145c / K165 / K220 / K245 / K245c / K265 / K246 Orion) | [`01_product-knowledge/machines-spec.md`](../01_product-knowledge/machines-spec.md) | critical-facts-log(校正歷史)/ case-learning/* |
| ADAS / DMS / G-Sensor / Map / OBD-II 完整事件 | [`01_product-knowledge/adas-dms-events.md`](../01_product-knowledge/adas-dms-events.md) | roadmap-vs-internal(對外口徑)/ sales-faq |
| 紅色按鍵功能(接聽電話 / Manual event / Server callback / 格化 SD) | [`01_product-knowledge/voice-alerts.md`](../01_product-knowledge/voice-alerts.md) + `kb-cheatsheet.md` | critical-facts-log(校正歷史) |
| Voice Alerts 完整清單 | [`01_product-knowledge/voice-alerts.md`](../01_product-knowledge/voice-alerts.md) | — |
| Storage Overwrite 機制(SD + Internal Flash) | [`01_product-knowledge/storage-mechanism.md`](../01_product-knowledge/storage-mechanism.md) | sales-faq |
| Safety Score / Driver Scorecard | [`01_product-knowledge/safety-score.md`](../01_product-knowledge/safety-score.md) | — |
| VisionAgent App | [`01_product-knowledge/visionagent-app.md`](../01_product-knowledge/visionagent-app.md) | — |
| Diagnostics(Master Portal Diagnostics 頁) | [`01_product-knowledge/diagnostics.md`](../01_product-knowledge/diagnostics.md) | vmx-7404-tracking |
| KB 60+ 篇完整 catalog | [`01_product-knowledge/kb-full-catalog.md`](../01_product-knowledge/kb-full-catalog.md) | kb-cheatsheet(精選 9 篇) |
| MiAI Roadmap 2026 對外版 | [`01_product-knowledge/miai-roadmap-2026.md`](../01_product-knowledge/miai-roadmap-2026.md) | roadmap-vs-internal(對外 vs 內部) |
| Sales-Level FAQ 對外口徑 | [`01_product-knowledge/sales-faq.md`](../01_product-knowledge/sales-faq.md) | — |

## 👥 組織

| 概念 | SSOT 主檔 | 摘要引用處 |
|-----|---------|-----------|
| Stakeholder map(MiTAC / 海外客戶) | [`02_organization-map/stakeholders.md`](../02_organization-map/stakeholders.md) | case-learning/* |
| Coffee chat 問題清單 | [`02_organization-map/coffee-chat-questions.md`](../02_organization-map/coffee-chat-questions.md) | — |

## 🏛 系統架構

| 概念 | SSOT 主檔 | 摘要引用處 |
|-----|---------|-----------|
| Portal 雙層架構(Master / Fleet)+ 26 頁 walkthrough | [`03_systems-architecture/portal-architecture.md`](../03_systems-architecture/portal-architecture.md) | case-learning/honeywell-me-cdr-opportunity |
| Plan Type 商業模型(Standard / Advanced / Pro / Suspend) | [`03_systems-architecture/plan-types.md`](../03_systems-architecture/plan-types.md) | case-learning/*(PS / Honeywell) |
| Master Portal 操作層(8 篇 KB 整理) | [`03_systems-architecture/master-portal-operations.md`](../03_systems-architecture/master-portal-operations.md) | troubleshooting |
| Server AI 架構演進(4 階段) | [`03_systems-architecture/server-ai-architecture.md`](../03_systems-architecture/server-ai-architecture.md) | miai-roadmap-2026 / roadmap-vs-internal |
| Vehicle Classification + Camera Height | [`03_systems-architecture/vehicle-classification.md`](../03_systems-architecture/vehicle-classification.md) | — |

## 📐 PM 框架

| 概念 | SSOT 主檔 |
|-----|---------|
| 三層真相(KB / Sheet / Roadmap) | [`04_pm-frameworks/three-truth-layers.md`](../04_pm-frameworks/three-truth-layers.md) |
| 承諾層次框架 | [`04_pm-frameworks/commitment-framework.md`](../04_pm-frameworks/commitment-framework.md) |
| 4 條核心 PM 原則 | [`04_pm-frameworks/core-principles.md`](../04_pm-frameworks/core-principles.md) |
| 技術型客戶溝通 | [`04_pm-frameworks/tech-client-comm.md`](../04_pm-frameworks/tech-client-comm.md) |
| 內部溝通斷層 | [`04_pm-frameworks/internal-comm-gap.md`](../04_pm-frameworks/internal-comm-gap.md) |
| UI Change Management | [`04_pm-frameworks/ui-change-management.md`](../04_pm-frameworks/ui-change-management.md) |

## ⚙️ Workflows / SOP

| 概念 | SSOT 主檔 |
|-----|---------|
| Data ingestion workflow(user 給資料 → Claude 整理進 .md → 更新 HTML) | [`05_workflows/data-ingestion-workflow.md`](../05_workflows/data-ingestion-workflow.md) |
| HTML 簡報製作 | [`05_workflows/html-presentation-pipeline.md`](../05_workflows/html-presentation-pipeline.md) |
| MDT 2026 PPT 模板 | [`05_workflows/mdt-2026-template.md`](../05_workflows/mdt-2026-template.md) |
| Sheet × Jira 雙週 sweeper | [`05_workflows/sheet-jira-sync-sweeper.md`](../05_workflows/sheet-jira-sync-sweeper.md) |
| Customer onboarding | [`05_workflows/customer-onboarding.md`](../05_workflows/customer-onboarding.md) |
| Troubleshooting checklist | [`05_workflows/troubleshooting.md`](../05_workflows/troubleshooting.md) |
| Claude memory system | [`05_workflows/memory-system.md`](../05_workflows/memory-system.md) |

## 🎯 校正事實表

| 概念 | SSOT 主檔 | 對應引用處 |
|-----|---------|-----------|
| 已校正關鍵 VMX 事實(別再答錯) | [`06_calibration-log/critical-facts-log.md`](../06_calibration-log/critical-facts-log.md) | weekly-summary / case-learning |
| Roadmap(對外)vs 內部現實 不一致紀錄 | [`06_calibration-log/roadmap-vs-internal.md`](../06_calibration-log/roadmap-vs-internal.md) | adas-dms-events |
| Sheet ↔ Jira mismatch 紀錄 | [`06_calibration-log/sheet-jira-mismatches.md`](../06_calibration-log/sheet-jira-mismatches.md) | sheet-jira-sync-sweeper |
| [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure 追蹤(評估期籌碼) | [`06_calibration-log/vmx-7404-tracking.md`](../06_calibration-log/vmx-7404-tracking.md) | diagnostics / weekly-summary |

## 📅 時序事件

| 概念 | SSOT 主檔 |
|-----|---------|
| 本週對齊狀態 | `weekly-summary/<latest>.md`(每週新檔)|
| 會議紀錄 | `meetings/YYYY-MM-DD_<topic>.md` |
| 歷史 snapshot | `knowledge/archive/YYYY-MM-DD_<topic>.md` |

## 📋 客戶案件

| 案件 | SSOT 主檔 | 狀態 | 對應 Jira(2026-05-11)|
|-----|---------|-----|-------------------|
| Honeywell ME CDR(新案 5/8 啟動) | [`case-learning/honeywell-me-cdr-opportunity.md`](../../case-learning/honeywell-me-cdr-opportunity.md) | 🆕 NEW | (待開 Honeywell setup ticket)|
| Platform Science / Vinicius | [`case-learning/vinicius-platform-science.md`](../../case-learning/vinicius-platform-science.md) | 🟢 ACTIVE | Live View JS lib(Brian 5/9 承諾)· camera-side video without download 開放問題 |
| CONNECTSOURCE / Cary / Wendy / MAU | [`case-learning/connectsource-passenger-blurring.md`](../../case-learning/connectsource-passenger-blurring.md) | 🟢 ACTIVE · **Q2 scope 已鎖定**(2026-05-11 Brian 拍板)| [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) Cloud API + doc share(Spencer · Due 30/Jun)· [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) GUI feasibility long-term(Kenny)|

## 📋 Jira tickets 對應主檔

| Jira | 案件 / 議題 | 主檔 SSOT |
|------|----------|---------|
| [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) | CONNECTSOURCE Blurring · Cloud API integration + doc share(Spencer · Due 30/Jun/26 staging · Production end-Jul) | `case-learning/connectsource-passenger-blurring.md` § 8.4 |
| [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) | Auto Sense / non-API customers · Blurring UI feasibility(Kenny · long-term)| `case-learning/connectsource-passenger-blurring.md` § 8.4 |
| [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) | ADAS Failure(評估期主力)· 8/10 設備 health failure | `knowledge/06_calibration-log/vmx-7404-tracking.md` |
| [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427)(reference 舊單,不對等)| Improve reporting function #107 · events reporting infra(非 Blurring monthly report 對應位置)| `case-learning/connectsource-passenger-blurring.md` § 8.4 註腳 |

## 🎯 Calibration rules(critical-facts-log 內 SSOT)

| Rule | 來源 | 主檔 |
|------|------|------|
| **Jira ticket = SSOT,external email follow-up 通常 redundant** | Brian 2026-05-11 傍晚二次回應 | `06_calibration-log/critical-facts-log.md` |
| Blurring API doc share ≠ endpoint open | Spencer 2026-05-11 揭露 | `06_calibration-log/critical-facts-log.md` |
| Option A vs Option B 在 API 層是同一條 flow | Brian 2026-05-11 下午 take over | `06_calibration-log/critical-facts-log.md` |
| Connect Source = API only / Auto Sense = UI(Q2 不做) | Brian 2026-05-11 下午拍板 | `06_calibration-log/critical-facts-log.md` |

---

## 更新規則

新增一個概念到 SSOT map:
1. 在對應分類找位置插入一行
2. 寫概念名稱 + 主檔 link + 主要引用處
3. 在 changelog.md 加一行 `STRUCT · ssot-map · 加 <X> 概念`
