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

---

## F. Kenny 5/7 14:41 已發回信(對外 commitment 紀錄)

> ⚠️ **這是已發出的對外承諾,將來會被檢驗**。後續 RD 任何修改若跟這封信內容不一致,Kenny 必須主動補正 thread。

### 收件結構
- 收件:cary.lo-mitac, brian.chienlee, **wendy.hammond**
- 副本:elvis.tran-mitac, spencer.su

### Kenny 的具體承諾(逐條對照前段「結論」內部判讀)

| 議題 | 內部結論(C 段) | 對外回信(F 段已發) | 落差 |
|------|---------------|--------------------|------|
| 自我介紹 | — | 「Pokai (Kenny) Huang, **Technical Support**, Brian's team at MDT, based in Taipei. Brian has looped me in」 | 對外 title 用 Technical Support(對齊 user_kenny memory) |
| **Q1 Passenger-only blurring** | 現行不支援,技術可行,排 Q2 2026 update / 7 月 | **「Yes feasible. Our current API for the European deployment already supports independent blurring control for driver and passenger faces.」** | 🚨 **對外升級成「現有 API 已支援」**(原內部判讀「現行不支援」)— 比 C 段樂觀。**待確認:European deployment API 真的有 driver/passenger 獨立 control?** |
| Q1 給客戶兩個釐清 | — | (1) Camera scope — DMS only? (2) Trigger model — automatic vs on-demand? | ✓ 把球丟回客戶端對齊需求 |
| **Q2 Fleet 層級** | 兩條路:(A) 客戶端自控 / (B) Server-side flag | **「Path: Master Portal > Management > Fleets > (select) > Fleet Detail > Configurations > (new) Blurring」**, per-Fleet 粒度,dealer 中央管控 | 🚨 **對外給了具體 portal path + (new) Blurring config UI 位置**。**待確認:這條路徑誰拍?Brian 過目了嗎?Lucy 確認 UI 可行嗎?** |
| Q3 Teams session | 不裸接,等 Brian dev scope 拍 | 「Fully supportive. Internal sync to align Q1/Q2 first.」 | ✓ 沒承諾時間,符合 C 段紅線 |

### 🚨 立即要補的內部對齊(Kenny 對自己)

1. **Q1「European deployment API 已支援 driver/passenger 獨立 blurring」依據?**
   - 找出對應 API 文件 / Jira ticket back up
   - 若沒明確證據:跟內部 Jira(HAWK-331/527/578 都是 all-face)有落差
   - 風險:Cary / Wendy 會用這句對外 commit,若不支援會被打臉

2. **Q2 portal path「Master Portal > ... > (new) Blurring」誰拍?**
   - 若 Kenny 自己推的 → 對外講 = 對外承諾此 UI 路徑
   - 待 Brian / Spencer 確認可實作 + Lucy 確認 UI 可行
   - 若 Brian 之後改位置,要主動補正 thread

3. **「Brian has looped me in for this thread going forward」= 對外承諾持續對接**
   - Kenny 已自定位為 Cary / Wendy 的對接 PM
   - 後續 thread 每次動,24h 內要回

### D 段紅線校正

D 段原紅線「不在 thread 裡搶在 Brian 前回 Q1/Q2」— **5/7 14:41 已回**,Brian 在副本(不是收件)。

- ✓ Brian 在 cc,有問題會糾正
- ✓ 自介「Brian has looped me in」表授權
- ⚠️ 但 Q1「European API 已支援」若 Brian 沒事先看過,後續打臉責任在 Kenny

### Kenny 對 Brian 補對齊話術

> 「Brian,5/7 14:41 我回了 Cary thread。Q1 我寫『European deployment API 已支援 driver/passenger 獨立 blurring』,Q2 我寫 Master Portal 加 (new) Blurring config 在 Fleet Detail 下。**請確認這兩個答覆 OK?**有需要修正我立刻補正 thread。」

---

## G. Back-up 依據補充(2026-05-08 Kenny 確認)

> 上一段 F 標的兩個 🚨 風險,Kenny 5/8 確認後**全部解除**。

### Q1「European deployment API 已支援 driver/passenger 獨立 blurring」依據
- **真實依據:BMS 客戶端用的內部 API 已有此能力,只是沒對外公開**
- 因此 redocly v2026-Q1 公開文件搜不到 blurring endpoint(對外沒露出)
- 但 BMS 客戶實際使用時的 API 確實支援 driver/passenger 獨立 blur
- 對 Cary / Wendy 講「現有 API 已支援」是有依據的(內部 BMS API)
- ⚠️ **對外口徑邊界**:能說「能力存在」,但不能說「公開可用」— 因為要做 modifications 才能給 CONNECTSOURCE,對應 Brian 5/4 給 Wendy 的「Q2 2026 update / 7 月最早」commitment

### Q2「Master Portal > Fleets > Fleet Detail > Configurations > (new) Blurring」路徑依據
- **真實依據:Brian / Spencer 已內部確認此路徑可實作**
- 不是 Kenny 自己看 portal 結構推的
- 對外承諾此 UI 路徑有 RD 端 backing
- 後續 Lucy UI 設計、實際 Q2 2026 update 排程,follow Brian / Spencer 拍板

### 🟢 風險解除後的對 Cary / Wendy 後續處理

兩個答覆都有依據,不需要主動補正 thread。**等客戶回覆 Q1 釐清(Camera scope + Trigger model)後,把球轉給 Brian / Spencer 排 dev scope**。

### 對 Kenny 自己的 reminder

下次寫對外信前,**對任何「現有已支援」這種 commitment**,自己先記:
- 依據在哪裡(內部 API / Jira ticket / Brian 跟我講過)
- 對外講 vs 對內現實差幾步(本次:BMS 已有,對外要 7 月才 ship 給 CONNECTSOURCE)
- 風險邊界(本次:能說「能力存在」,不能說「公開可用」)

寫到 calibration log 留 trace,**避免下次自己也忘記為什麼這樣回**。

---

## H. 2026-05-08 Syncup Meeting 校正(Q2 portal path 修正)

### 會議基本
- 5/8 02:21 UTC(台北 10:21)21 分鐘 Teams call
- Kenny 主動 reach out / Cary + Elvis 加入
- 完整紀錄:[`meetings/2026-05-08_syncup-cary-elvis_meeting-record.md`](../../meetings/2026-05-08_syncup-cary-elvis_meeting-record.md)

### 🚨 Kenny 5/7 14:41 對外承諾的 Q2 portal path 被現場糾正

Kenny 5/7 信寫:
> Master Portal > Management > Fleets > (select Fleet) > Fleet Detail > Configurations > (new) Blurring

**Elvis 現場用 Master Portal 螢幕分享揭露**:
- 那條路徑只能在 **main fleet 級**操作
- 動一個 = main fleet + 所有 contract fleets 一起套用
- **沒有 per-contract-fleet 粒度**
- 客戶實況(Cary 解釋):Australia 1 main fleet,所有 reseller 客戶都是 contract fleets,必須 pinpoint 特定 contract fleet 套設定
- Elvis 用 Live User 為例:**Fleet Portal 已有 per-contract-fleet config 的能力**,Blurring 應沿用

→ **5/7 信對外的 portal path 描述對 main fleet OK,對 contract fleet 不行**。要校正。

### 修正後的兩條實作路徑(待 Brian / Spencer 拍)

| Path | 說明 | 顧慮 |
|------|------|------|
| **(A)** Master Portal 補 contract fleet 視圖 + 加 Blurring config | dealer/MAU 中央控制所有 contract fleet | ⚠️ **隱私問題** — Cary 警告 contract fleet 不見得想讓上層 dealer 看到 |
| **(B)** Fleet Portal 加 per-contract-fleet Blurring config UI | 沿用 Live User pattern,維持 contract fleet boundary | 沒明顯顧慮 |

### Q1 API documentation 議題(會中 Cary 尖銳追問)

> Cary: 「Has the blurring notes been added on to the API documentation? Then what can I share with my customer please?」

Kenny 答:目前對外文件沒寫(只 BMS 用),要問 Spencer 能否 share 內部版。Cary 妥協:CONNECTSOURCE 是 integrated customer 願意用 API 直接整合 -> doc 暫用版本即可。

### 對 5/7 14:41 信的 Δ(整理)

| 項目 | 5/7 信寫的 | 5/8 sync 揭露 | 是否要修正 thread |
|------|---|---|---|
| Q1 driver/passenger 獨立 blur 已支援 | ✓ | 對(BMS 內部 API)| 不用 |
| Q1 API doc | (沒明寫)| 對外目前無 doc,要問 Spencer 能否 share | **回信中提:會找 Spencer** |
| Q2 portal path | Master Portal config | **只到 main fleet 級,沒粒度** | **要回信校正成 (A)/(B) 兩條路** |
| Q3 Teams session | Fully supportive | ✓ 5/8 已開,客戶滿意 | 不用 |

### 對外回信狀態

草稿已擬好(兩個 Q + 兩條路徑 + Spencer/Brian 確認 next steps)。**Kenny 5/8 決定先寫進 case-learning + meetings + memory,回信暫緩**。

_Last updated: 2026-05-08 — 加 H 段 5/8 sync 校正紀錄。回信草稿等 Kenny 確認後寄出。_
