# Server AI 架構演進

> 來源:MiAI Roadmap 2026-04-24 Slide 5

## 4 階段架構演進

| 階段 | 架構 | Strengths | 預期 |
|------|------|-----------|------|
| 1 | **Edge AI**(目前) | Real-time / Low latency / Offline / Privacy | 受限於設備算力 |
| 2 | **Edge AI + Server AI** | 二次驗證,降 FP / 借 server 算力 | 提升精度 |
| 3 | **Edge AI + Server VLM** | 全影片語意理解 / 處理複雜混合行為 | 大幅降 FP/FN |
| 4 | **Edge VLM**(終局) | Real-time semantic on-device / 不依賴網路 | 終極形態 |

**Expected Overall Accuracy Improvement: 20% ~ 40%**(視場景)

## 已開的 Server AI Jira tickets(對應 Stage 2/3)

| Jira | 主題 | PIC |
|------|------|-----|
| [VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722) | Server-side LDWS model(防 FP)| Eric / Spencer |
| [VMX-6703](https://jira.navman.co.nz/jira/browse/VMX-6703) | Configurable Server AI Response Time | (待補) |
| [VMX-7346](https://jira.navman.co.nz/jira/browse/VMX-7346) | ServerAI pre_event_message 加 cdr 版號 | Adonis |
| [VMX-7099](https://jira.navman.co.nz/jira/browse/VMX-7099) | Migrate IOSix service to AZUGA server | (待補) |
| [VMX-6453](https://jira.navman.co.nz/jira/browse/VMX-6453) | Server Model Research - Phone Usage | (待補) |
| [HAWK-397](https://jira.navman.co.nz/jira/browse/HAWK-397) / [VMX-6724](https://jira.navman.co.nz/jira/browse/VMX-6724) | Server AI phone texting | Jieli |
| RFQ0749-689 | Backend 動態覆寫 confidence threshold | Adonis |

## 影片三版本架構(Q2-Q3 PM 級議題)

未來同一影片可能同時存在三版本:
1. **原始 video**
2. **模糊版本**(Server AI 後製,demand request 模式)
3. **Debug view**(AI 視角)

對 PM:
- 模糊在 Master/MAU 加 API 開關([VMX-7088](https://jira.navman.co.nz/jira/browse/VMX-7088) / 文件需 Lucy 配合 UI 設計)
- 模糊不在 fleet portal 上顯示(維持 API 操作)
- **缺一個「任務完成主動通知」UI 機制**(目前缺,未來補)

## ⚠️ Brian 戰略翻案 — VMX/BMS 同步(2026-05-06 揭露)

過去:VisionMax 不給 fleet 改 AI 參數 / BMS 給改 → 兩套 codebase

未來:**兩邊同步實作**,VMX 也開放給 fleet 改;API 加保護避免亂改參數

時程:6 個月內會發生的架構決策

PM 跟進:API 文件對齊 / Fleet portal UI 加開關 / 客戶溝通(從「不能改」變「能改」要小心訊息)
