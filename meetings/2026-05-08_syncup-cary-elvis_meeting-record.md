# 2026-05-08 Syncup — Kenny / Cary / Elvis(MiTAC AU)

> **時間**:2026-05-08 凌晨 2:21 UTC(= 2026-05-08 早上 10:21 台北 GMT+8)· 21 分 28 秒
> **參與**:pokai.huang (Kenny - MDT) / cary.lo-mitac (MiTAC AU) / elvis.tran-mitac (MiTAC AU PM)
> **形式**:Teams call · Kenny camera off
> **來源**:Teams 自動 transcript(`Syncup meeting .docx`)+ recording(`.mp4`)
> **整理人**:Kenny

---

## 一頁總覽

| 項目 | 內容 |
|------|------|
| 起源 | Kenny 5/7 14:41 回信 thread(Q1/Q2/Q3 對外答覆)後,Cary/Wendy 端有疑問,Kenny 主動 reach out 開會釐清 |
| 性質 | = Kenny 5/7 信中承諾的 **Q3 Teams session 實際發生** |
| 兩個焦點議題 | (1) Passenger-only blurring API 文件 share / (2) Per-contract-fleet config 路徑 |
| 重大發現 | 🚨 **Kenny 5/7 對外承諾的 Master Portal config path 不夠精細** — Elvis 現場糾正 |
| 客戶 acceptable 暫解 | 用 API 直接整合(CONNECTSOURCE 是 integrated customer)|
| Cary 對 Kenny 評價 | 「very refreshing」/「we will be stalking you」(後續會直接 ping)|

---

## A. 議程逐項紀錄

### A1. 自我介紹 / 破冰(0:06–1:13)
- Kenny camera off(在辦公室),Elvis 預告會加入
- Cary 開玩笑:「沒化妝啊?」
- Kenny 自我介紹:「Pokai (Kenny) Huang, Technical Support, Brian's team at MDT, 入職幾週」
- Elvis: 「Welcome」
- Cary: 「Brian and Spencer 都太忙,you reaching out is so refreshing」← **建立 Kenny 為對外主要對話窗口的關鍵 moment**

### A2. Q1 — Passenger-only blurring(driver as-is)(1:43–10:43)

**Kenny 答**:
- 「BMS 已有 blurring functions,Master Portal default on」
- 「Front-end fleet control 暫時沒有,但跟 Brian/Spencer 同步過 = doable + 排在下個 update」

**Cary 重述確認**:
> 「You are saying currently available through API but your team is working on an update down the track to allow fleet admin to enable IT on the front end VMX portal」

→ Kenny 確認 yes。

**Elvis 補背書**:
> 「You'll be getting the request from Europe as well to ensure there's GDPR compliance, so will be a standard request moving forward」

→ 歐洲端也會 demand 同樣功能,不是 CONNECTSOURCE one-off。

**ADAS 範圍補充(Cary 提)**:
> 「In API notes that Brian sent in the past, you can actually select which camera to be on and off, and the gradient of the blurring as well」

→ Kenny 確認:driver-facing / road-facing 都已有 API,blur 區域 / ratio 也可調。

**API 文件問題(9:23 起,Cary 尖銳追問)**:
- Cary: 「Has the blurring notes been added on to the API documentation?」
- Kenny: 「No, 只給 BMS, 沒對外文件化」
- Cary: 「**Then what can I share with my customer please?**」
- Kenny: 「暫時不能對外 share, 等我們準備好 API 才能適當 share」
- Cary 妥協:「OK, they're integrated customer, happy to use API for the time being」
- Kenny 承諾:「會問 Spencer 能否提供 API documentation share 出來」

### A3. Q2 — Per-fleet vs Per-contract-fleet config(11:02–16:32)

**Kenny 開頭(對應 5/7 信內容)**:
- 「Master Portal 控制所有 fleet」
- 「在 Fleet Detail > Configurations 加 Blurring 開關」

**Elvis 糾正(11:47–12:44)**:
> 「Master portal doesn't show you the contract fleet. Fleet A 是 main fleet,Fleet B 和 C 是 contract fleet。要 access B 和 C 必須在 Fleet Portal 看,under Fleet A。
> Currently you can change certain settings for each contract fleet already, which I mentioned about the **live user**.」

→ **Elvis 用 Live User 做 reference**:Fleet Portal 已有 per-contract-fleet 細項 config 的能力,Blurring 應沿用這個 pattern。

**Kenny 分享螢幕看 Master Portal 確認(12:44–14:38)**:
- 在 Master Portal > Management > Fleets > Fleet Detail > Configurations 看
- 開螢幕跟 Elvis 對著看
- Elvis 點明:「But when you do it for that, that will only apply to the main fleet — actually apply to **all main fleet and contract fleet**」
- Elvis: 「If you want granular per-contract-fleet, IT has to be done in the Fleet Portal」
- Kenny: 「Got IT, that's the gap」← **5/7 信對外承諾的 portal path 不夠精細,被現場糾正**

**客戶實況(Cary 解釋,15:23–16:16)**:
> 「This particular customer is integrated, currently 只有一個 fleet (Australia),所有 reseller 客戶都是 contract fleets。
> 將來客戶會分區(Malaysia 一個 fleet + Malaysian 客戶當 contract fleet,等等)。
> They need to **pinpoint particular contract fleet** to apply settings on/off.」

→ **per-contract-fleet 是硬性需求**,不是 nice-to-have。

### A4. 兩條未來實作路徑討論(16:32–17:45)

Kenny 提出 alternative:
- 「Master Portal 也可以加 contract fleets 視圖」

Cary 警告(隱私):
> 「That will be alarming, but yeah, it could be cool — privacy issues like if the contract fleet doesn't want the master to know about them.」

結論:兩個方向都帶回給 Brian / Spencer 評估:
- **(A)** Master Portal 補 contract fleet 視圖 — 隱私顧慮
- **(B)** Fleet Portal 加 Blurring config UI 在 per-contract-fleet 層級 — 沿用 Live User pattern

### A5. Spencer release notes review(20:05–20:46)

- Elvis 問:「Will Spencer transfer the task to you to review our release notes for final approval?」
- Kenny: 「目前 permission 受限,但會被加進 CC email / Jira / drew(?)」
- Elvis: 「OK 理解」

### A6. 結尾互動(20:48–21:17)

- Kenny: 「歡迎 Teams 直接 ping 我」
- Cary: 「**It's too late now. You approached US on Teams and now we've got your name and we will be stalking you.**」(會繼續找你)
- Kenny: 「That's great」
- 互道感謝結束

---

## B. 對 5/7 14:41 對外承諾的 Δ 校正

| 項目 | 5/7 信寫的 | 5/8 sync 揭露 | 動作 |
|------|---|---|---|
| Q1 driver/passenger 獨立 blur | 「API for European deployment 已支援」 | ✅ 對(BMS 內部 API)| 不用補 |
| Q1 API 文件 | (沒明寫)| Cary 要 doc share, Kenny 答暫無對外文件 | 跟 Spencer 確認能否 share |
| **Q2 Portal path** | 「Master Portal > Management > Fleets > Fleet Detail > Configurations > (new) Blurring」 | ⚠️ **只到 main fleet 級,沒粒度** — 不能滿足客戶 per-contract-fleet 需求 | **要回 thread 校正成 (A) 補 Master Portal 視圖 vs (B) Fleet Portal 加 UI 兩條路** |
| Q3 Teams session | 「Fully supportive」 | ✅ 5/8 已開,客戶滿意 | 不用補 |

---

## C. Action Items

### 🔥 Kenny 自己(P0,24h 內)
- [ ] **回 Cary / Wendy thread 校正 Q2 portal path** — 不能裝沒事,Elvis 現場糾正了。雙路徑(Master 補視圖 vs Fleet Portal 加 UI)帶進信中
- [ ] 跟 **Spencer** 確認:**Blurring API documentation 能否 share** 給 CONNECTSOURCE 對外用(暫用,在 front-end UI 出來前)
- [ ] 跟 **Brian + Spencer** 對齊:contract-fleet-level Blurring config 走哪條路
  - (A) Master Portal 補 contract fleet 視圖(處理隱私)
  - (B) Fleet Portal 加 per-contract-fleet UI(沿用 Live User pattern)

### 📅 本週(P1)
- [ ] 把 5/8 會議結論寫進 `case-learning/connectsource-passenger-blurring.md`
- [ ] 把 5/8 會議結論寫進 `knowledge/06_calibration-log/cary-passenger-blurring-2026-05-07.md`(加 H 段 5/8 校正)
- [ ] 建 memory `project_meeting_2026-05-08_cary-elvis_syncup.md`
- [ ] Kenny 對外定位:Cary / Elvis / Wendy 主對接 PM(Brian / Spencer 退到後援)

### 🎯 下個 sync 前(P2)
- [ ] Brian / Spencer 拍板 Q2 走 (A) 還是 (B)
- [ ] 若走 (B),跟 Lucy 對 Fleet Portal UI 設計

---

## D. 戰略觀察 / 軟資訊

### Cary 對 Kenny 的接納度
- 開頭:「very refreshing」(對 Kenny 主動 reach out 的肯定)
- 結尾:「we will be stalking you」(從現在開始會直接 ping Kenny,跳過 Brian / Spencer)
- → **Kenny 已成為 MiTAC AU 線(Cary + Elvis + Wendy)的主對接 PM**,不是 Brian backup

### Cary / Elvis 的工作風格
- Cary:玩咖型 + 直接(「沒化妝」「we will be stalking you」「mandarin = 食物 + 幼稚園程度」)
- Elvis:技術型 + 銳利糾正(直接點出 Kenny 5/7 portal path 的問題,不留情面但不挑釁)
- → 這兩位對 Kenny 開放但會持續 challenge,**回信不能含糊**,要明確 commitment + 明確時程

### Brian / Spencer 對 Kenny 的授權
- Cary 開頭:「Brian and Spencer are under star at the moment so they go just yes」← 暗示 Brian / Spencer 給的回應太短沒釐清
- → Kenny 補位空間:把模糊的 yes 變成具體可執行 plan,這是 Kenny 在 Brian 團隊內可建立差異化的點

### 隱私議題首次浮現
- Cary 在 Master Portal 補 contract fleet 視圖時警告隱私
- → 這是 **Master/Fleet 雙 portal 架構的長期戰略議題**,跟 Brian 先前 BMS/VMX 同步戰略翻案放一起評估

---

## E. 跨檔案連結

- 5/7 對外承諾紀錄:[`knowledge/06_calibration-log/cary-passenger-blurring-2026-05-07.md`](../knowledge/06_calibration-log/cary-passenger-blurring-2026-05-07.md)
- CONNECTSOURCE 案件主檔:[`case-learning/connectsource-passenger-blurring.md`](../case-learning/connectsource-passenger-blurring.md)
- Wendy 身份解密:`~/memory/reference_wendy_hammond_identity.md`
- 三層真相 / Roadmap vs Internal:[`knowledge/06_calibration-log/roadmap-vs-internal.md`](../knowledge/06_calibration-log/roadmap-vs-internal.md)
- 對外回信草稿:**等 Kenny 確認後再發**(暫不寄出)
