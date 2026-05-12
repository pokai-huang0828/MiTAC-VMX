# 01 Product Knowledge

VMX 產品事實層 — 機種、事件、語音、Roadmap。對客戶 / RD 講具體 spec 前先在這裡查。

## 文件

- **[kb-full-catalog.md](kb-full-catalog.md)** ⭐ — KB 全 60+ 篇 catalog + 校正(2026-05-06 掃)
- **[kb-cheatsheet.md](kb-cheatsheet.md)** — KB 核心 9 篇摘要 + 連結
- **[sales-faq.md](sales-faq.md)** ⭐ — 客戶 RFP 標準題 8 題答題 SOP(KB deep read)
- **[machines-spec.md](machines-spec.md)** — K-series 5 機種 + Chip mapping + RFID/QR mapping
- **[adas-dms-events.md](adas-dms-events.md)** — ADAS / DMS / G-Sensor 完整事件 + 觸發 threshold
- **[voice-alerts.md](voice-alerts.md)** ⭐ — In-cabin voice alerts 完整 11 類(KB deep read)
- **[safety-score.md](safety-score.md)** ⭐ — Driver Scorecard 公式 + 5,000 km 滾動視窗
- **[diagnostics.md](diagnostics.md)** ⭐ — Diagnostics Q&A + Master Portal 監控
- **[visionagent-app.md](visionagent-app.md)** ⭐ — VisionAgent 技術人員 app(跟 Fleet Mobile App 不同)
- **[storage-mechanism.md](storage-mechanism.md)** ⭐ — SD Card + Internal Flash 完整 overwrite 規則
- **[miai-roadmap-2026.md](miai-roadmap-2026.md)** — Tier × Chip × Model × Year 完整對應

## ⚠️ 三層真相提醒

本層內容 **以 KB 為準**。Roadmap 寫但 KB 狀態不一致的功能,實際狀態如下(2026-05-07 校正):

- **Yawning** — 仍在開發中,還沒給客戶用,效果不如預期。**5/7 補:夜間嘴部辨識不佳 → 加灰階模型 + 考慮改辨識整張臉。UI toggle 對應 [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(Lucy)**
- **Smoking** — KB 標 (in development),已開發但 sheet 隱藏 / 客戶端沒主動 promo
- **Eating/Drinking** — 對外 Roadmap 2027,但 **5/7 揭露 BMS 客訴量是過去 17 倍(ID 6652),6/15 前 7000+ Edge case 緊急重訓**
- **LDWS** — Server-side Q1 已 deploy,**device-side YOLO Lane Detection 改善 5/7 Pending 暫緩**
- 對外口徑統一:「**Roadmap planned, 內部開發 / 測試中**」,不對客戶承諾上線時間。

