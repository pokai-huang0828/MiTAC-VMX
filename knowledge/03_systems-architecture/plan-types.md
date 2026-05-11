# Plan Type 商業模型

> 來源:PDF Subscription Plans for TSP

## 4 種 Plan

| Plan | 功能 | 定價(per device/month) | Edge 行為 |
|------|------|----------------------|----------|
| **Standard** | Sensor Event + VMX VT Cloud + GPS+Video | $5(13 cams) / $7(47 cams) | 強制關閉 MiAI |
| **Advanced** | + ADAS Event Detection | $7(13 cams) / $9(47 cams) | 釋放前向 AI,禁 DMS |
| **Pro** | + DMS Event Detection(全 AI) | (待補) | 全 AI |
| **Suspend** | (PDF 未列) | — | 帳號暫停 |

## 待 Coffee Chat 釐清(Brian)

- ⚠️ Pro 完整定價
- ⚠️ Suspend 細節
- ⚠️ **「13 cams / 47 cams」含義**(攝影機數?分群?)

---

## 2026-05-11 新議題:Plan Type ↔ 啟用層級對應

### 議題來源

1. **Platform Science (Vinicius)** 5/8 反映 EVO (K265) ADAS 和 DMS 沒啟動,但 Righter 說 K265 (L1225380005) AI function 看起來 OK,K265 已分配給 "Platform Science" fleet → **推測差在 plan type 沒對到 ADAS/DMS 啟用層級**
2. **Honeywell ME CDR** 5/11 開案要做 white-label VMX portal,Plan Type 對應 ADAS/DMS / Live View / Privacy Mode 等啟用是第一個必須確認的設定點

### 待 Brian / Spencer 對齊的問題

- Plan Type 切換是否需要 device firmware reflash,還是 cloud-side 即時生效?
- Standard / Advanced / Pro 之間切換的 grace period?
- Plan Type 影響的具體 feature list(對應 [adas-dms-events.md](../01_product-knowledge/adas-dms-events.md))需要 KB 對齊

### Contract Fleet 配置議題(5/8 Sync-up Cary/Elvis 衍生)

兩張 Jira ticket 是這個議題在 Jira 上的位置(pending 180+ 天):

| Jira | Title | 對應 Plan Type 影響 |
|------|-------|-------------------|
| [VMX-5908](https://jira.navman.co.nz/jira/browse/VMX-5908) | Contract fleet 的 Webhook 處理 | 影響 contract fleet 的 Event 推送 channel |
| [VMX-6586](https://jira.navman.co.nz/jira/browse/VMX-6586) | Group main fleet and contract fleets together | 影響 Master Portal 是否看得到 contract fleet,跟「Master Portal Blurring config 只到 main fleet 級」同根 |

→ **這兩張票如果優先級升上去,5/8 Sync-up 提的 per-contract-fleet config (A)/(B) 路徑就有 owner 了**。Kenny 可建議 Brian / Spencer 排進現 sprint。

### Honeywell ME 案會驗證的設定

White-label Honeywell logo + sample import 是第一個實案,Kenny 應該記錄:
- Plan Type 選擇對應「測試 fleet」應該是哪一級
- Login logo 替換是 Master Portal 自助開關還是後端 config
- 機殼 sticker / login logo 兩個 white-label 元素的 SOP

詳見 [case-learning/honeywell-me-cdr-opportunity.md](../../case-learning/honeywell-me-cdr-opportunity.md)。

_2026-05-11 update:加 Plan Type ↔ 啟用層級對應 / Contract Fleet 配置議題 / Honeywell 驗證設定 三段。_
