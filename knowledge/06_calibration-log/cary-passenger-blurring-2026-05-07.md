# Calibration Log — Cary 5/7 Passenger Blurring Update

> 日期：2026-05-07
> 來源：Outlook → Important!!! category → cary.lo-mitac 5/7 11:22
> 主旨：RE: VMX Roadmap Update and Explanation <PASSENGER BLURRING>
> 性質：Cary（MiTAC AU 商務）代客戶向 Brian 提兩個技術可行性問題 + 一個 Teams session 請求

---

## TL;DR — 三個發現

1. 🚨 **Cary 兩個問題對照內部資料都不能無腦 yes**：redocly v2026-Q1 沒 blurring API 公開；Jira HAWK-331/527/578 系列都是「all-face blur」、無駕乘區分；fleet-level 開關現行也不存在
2. 🚨 **Cary 信件 quick reply 給三個 yes 選項**（"Yes, that is correct."/"Yes, it can."/"Yes."）— 客戶在現場、希望快回，**這就是 Brian 5/4 警告的「BMS 為原型 + 需 modifications」雷區**
3. ⚠️ **CONNECTSOURCE 案 4/24 起立的 5 件 P1 todo 5/7 一件都沒結** — 老問題未解又疊新規格

---

## A. Cary 5/7 提問原文

```
HI Brian
Can I confirm that the below is achievable, given BMS implementation.
- Blurring to be applied to passengers only with the driver's face as is.
- Blurring to be applied to a certain Fleet or Contract Fleet?
Is it possible to have a customer session on teams on this topic?
Many thanks.
Cheers, Cary
```

收件人：Brian、Wendy、Pokai
副本：Elvis Tran (MiTAC AU PM)、Spencer Su

---

## B. 三個對照來源

### B1. visionmax.redocly.app（v2026-Q1 公開 API doc）

| 查詢 | 結果 |
|------|------|
| Blurring endpoint | **沒有任何公開 endpoint** |
| `videoClip` / `GetVideoDetail` 是否有 blur 參數 | 沒有 |
| Fleet config 區是否有 blurring 開關 | 沒有 |

→ 公開 API 看不到 blurring 任何控制能力。

### B2. Jira Filter 36457 + AI tab 對齊（5/7 校正日誌）

從 `06_calibration-log/ai-tab-jira-alignment-2026-05-07.md`：

| Jira | Summary | Status | 範圍 |
|------|---------|--------|------|
| HAWK-331 | Blurring (face / **background** / **license plate**) | CLOSED 2/5 | all-face,沒駕乘區分 |
| HAWK-527 | Blurring not reliable | RESOLVED 4/1 | all-face |
| HAWK-578 | VisionMax PROD not blurring | RESOLVED 5/4 | all-face |
| HAWK-577 | Blurring on-demand fails | OPEN | 確認是 on-demand API call 模式 |
| VMX-6391 | AI New Feature: Blurring | RESOLVED 12/10/25 | 原始實作 |

→ Blurring 在內部存在，但全部都是 all-face、on-demand call 模式。**沒有 driver/passenger 區分，沒有 fleet-level gating。**

### B3. Brian 4/29 4:11 PM 信中親口確認

> "**This is not included in the features that have already been developed.**
> This API does not require any special permissions and it is the same as all other APIs.
> If the customer has this requirement, **it will need to be implemented separately**."

→ Brian 自己已說過「不在現有功能裡」、「需另外開發」、「API 沒特殊權限」。Cary 5/7 兩問其實是把同樣問題用更具體的規格再問一次。

---

## C. 結論（內部用，不對外）

### Q1 passenger-only blurring（駕駛保留）
- 現行：**不支援**
- 技術可行性：**可行**（BMS 有 DMS 知道駕駛座位置 → 可推駕駛臉 → blur 模組排除駕駛區）
- 實作成本：**新 spike ticket + RD scope** → 排入 Q2 2026 update / 7 月最早

### Q2 fleet / contract-fleet 層級套用
- 現行：**沒有 server-side gating**，blurring 是 caller-responsibility on-demand call
- 兩條路：
  - **(A)客戶端自控**：CONNECTSOURCE 在自己 dispatch logic 只對特定 fleet 觸發 blur API → 馬上可做
  - **(B)VMX server-side flag**：需 RD 排程，跟 Q1 一起綁 Q2 2026 update
- 推薦：先 (A) 救急、(B) 排正式路線圖

### Q3 Teams customer session
- 應開，**但禁止裸接** — Brian dev scope 沒拍前不訂時間
- 進會議前要：(1) Q1/Q2 內部 scope 對齊；(2) 對外故事一致；(3) Brian 在場主答

---

## D. 動作清單

### 立即（24h 內）
- [x] 完成本 calibration log + 更新 case-learning 主檔
- [ ] 給 Brian 內部 DM 三點摘要（**等使用者明示後才發** — auto-mode 不主動發訊息）

### 本週
- [ ] Brian 拍 Q1/Q2 dev scope（PM 端追蹤）
- [ ] 若 Brian 同意，幫忙開兩張 spike ticket（**不抓 Eric/Vincent/Jimmy 名字** — 等 Brian 指派）
- [ ] CONNECTSOURCE 4/24 起 5 件 P1 todo 全沒結（**老問題**），下一輪同步要拉出來逼進度

### 紅線提醒
- ❌ 不在 thread 裡搶在 Brian 前回 Q1/Q2
- ❌ 不在 dev scope 沒拍前訂 Teams session 時間
- ❌ 對 Cary 講「現有沒能力」這種內部判讀（那是 Brian 該講的對外故事）

---

## E. 跨檔案連結

- 完整分析：`~/.claude/plans/https-outlook-cloud-microsoft-mail-categ-glimmering-sky.md`
- 案件主檔（已更新時間軸 + Action Items）：`case-learning/connectsource-passenger-blurring.md`
- Jira 對齊佐證：`knowledge/06_calibration-log/ai-tab-jira-alignment-2026-05-07.md`
- API 文件（v2026-Q1）：https://visionmax.redocly.app/
