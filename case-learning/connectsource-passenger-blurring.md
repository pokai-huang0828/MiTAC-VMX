# 事件記錄：CONNECTSOURCE × Passenger Blurring 需求

> 信件主旨：`RE: VMX Roadmap Update and Explanation <PASSENGER BLURRING>`
> 記錄範圍：2026/04 – 2026/05/04
> 記錄人：Pokai Huang (pokai.huang@mitacmdt.com)

---

## 1. 事件背景

澳洲 MiTAC 經銷商（產品品牌名：**CONNECTSOURCE**）接獲一個馬來西亞車隊業者的合作需求。該客戶因當地隱私法規及工會規定，要求在行車記錄器影像中自動模糊乘客臉部，此即 **Passenger Blurring（乘客模糊化）** AI 功能。

Wendy（澳洲業務窗口）向 MiTAC VisionMax 產品端（Brian）反映此需求，並詢問功能上線時程，引發內部關於路線圖透明度、功能開發優先順序與成本分攤的討論。

---

## 2. 主要關係人

| 姓名 | 角色 |
|---|---|
| **Wendy Hammond** | MiTAC AU 業務(wendy.hammond@mitac.com.au)— 5/8 解密身份,代 reseller 客戶端傳達需求 |
| **Cary Lo** | MiTAC AU 業務 / Account Manager — 跟 Wendy 同部門,5/8 sync-up 主對話人 |
| **Elvis Tran** | MiTAC AU PM — 5/8 sync-up 加入,負責 release notes review,5/8 技術糾正 Q2 portal path |
| Brian Chienlee(李健) | VisionMax 解決方案負責人(MiTAC HQ 產品端) |
| Spencer Su(蘇家弘) | Cloud / API team lead(HQ)— Q1 API doc / Q2 portal 路徑可實作性 owner |
| **Pokai (Kenny) Huang** | Technical Support, Brian's team @ Taipei — 5/7 對外回信 / 5/8 主動 reach out 開 sync,目前 MiTAC AU 線**主對接 PM** |

---

## 3. 商業規模

| 項目 | 數字 |
|---|---|
| 馬來西亞客戶硬體台數 | 1,165 台裝置 |
| 預估連線數 | 1,000 個連線 |
| 合約期限 | 36 個月 |
| 潛在收益（Wendy 估算） | ~$216,000 USD（約 $6/月/連線） |
| Passenger Blurring AWS 額外成本 | $700 USD/月 |
| AWS 成本（36 個月合計） | ~$25,200 USD |
| 淨收益估算（扣除 AWS 成本） | ~$190,800 USD |

> 財務上具備可行性，前提是 $6/月/連線的定價模型已涵蓋 AWS 成本分攤。

---

## 4. 時間軸

### 早期需求提出（2026/04 初）
- Wendy 向 Brian 提出馬來西亞客戶的 Passenger Blurring 需求
- 說明合約規模（1,165 台、1,000 連線、36 個月）以及功能背景（隱私法規與工會要求）

### 2026/04/24 — 財務與功能可行性討論
- **Cary Lo** 提出財務問題：
  - 1,165 台 HW 每月產生約 $1,165 USD 的基礎收益
  - Passenger Blurring AWS 成本 $700/月 是否已計入定價模型？
  - 車隊規模是否符合 Passenger Blurring 功能的適用條件？
- **Brian** 回覆：
  - 確認 AWS 額外成本為 $700/月
  - 說明此功能原為 **BMS 客戶** 開發的原型，整合至 CONNECTSOURCE 環境需要**額外開發工作**，不能直接套用
  - 預計目標時程：**Q2 2026（七月）**

### 2026/05/04 — 路線圖透明度衝突浮上檯面
- **Wendy** 表達對 MiTAC 路線圖缺乏透明度的不滿：
  - 長期沒有召開路線圖同步會議
  - 業務端無法對客戶做出有效承諾
  - 要求 Brian 提供更明確的時程資訊
- **Brian** 回覆：
  - 分享 **AI Feature Roadmap 簡報**：https://docs.google.com/presentation/d/1FIkUrx_-f1ouI3j0Tne7HdjuW1nTgnBST7GvNwcPuo/edit?usp=sharing
  - 分享 **需求管理追蹤表（Google Sheets）**：https://docs.google.com/spreadsheets/d/1DXCf8yU7ZrtzVdMEPSxHgmDb7cPKIFDK/edit?gid=639348744
  - 說明 Passenger Blurring 功能已排入 Q2 2026 路線圖，七月為目標
  - 強調 feature 為 BMS 設計，CONNECTSOURCE 需要額外 modifications，Q2 2026 update / 7 月最早

### 2026/05/07 — Cary 加碼兩個技術可行性問題 + 客戶 session 請求

**Cary 5/7 11:22 信件**（收件人：Brian、Wendy、Pokai；副本：Elvis Tran、Spencer Su）：

> Can I confirm that the below is achievable, given BMS implementation.
> - Blurring to be applied to passengers only with the driver's face as is.
> - Blurring to be applied to a certain Fleet or Contract Fleet?
> Is it possible to have a customer session on teams on this topic?

**內部對照（Pokai 分析，完整版於 plan 檔）**：

- **Q1 passenger-only**：redocly v2026-Q1 沒 blurring API；Jira HAWK-331 / 527 / 578 全是 all-face；**現行不支援駕乘區分**；BMS DMS 結果可餵 blur 模組是可行路徑，但需新 ticket
- **Q2 fleet-level**：現行為 caller 端 on-demand；**沒有 server-side fleet gating**；兩條路 — 客戶端自控（快） vs VMX 加 server flag（Q2 2026）
- **Q3 Teams session**：應開，但前置必須先在內部把 Q1/Q2 dev scope 拍版，免得在客戶面前 over-promise
- 對 Cary 不應搶在 Brian 之前回 "Yes" — Cary 信中 quick reply 提示 "Yes, that is correct."/"Yes, it can."/"Yes." 三選項，**這正是要警戒的點**

完整分析：`~/.claude/plans/https-outlook-cloud-microsoft-mail-categ-glimmering-sky.md`

### 2026/05/07 下午 — Kenny 寄出回信（v6 final）

跟 Spencer 確認 Q1 / Q2 真實狀態後寄出。決策摘要：

**Q1**：揭露「歐洲 API 已支援 driver/passenger 分開」，請客戶確認鏡頭範圍 + 觸發模式
**Q2**：提議實作位置 `Master Portal › Management › Fleets › Fleet Detail › Configurations › (new) Blurring`，per-Fleet 粒度，dealer 端集中管理
**Q3**：先內部 sync 對齊再排客戶 Teams call

收件人：Cary、Brian、Wendy；副本：Elvis Tran、Spencer Su

實際寄出版本與後續追蹤：`knowledge/06_calibration-log/cary-passenger-blurring-reply-draft-2026-05-07.md`

**已知風險點（待 Cary 回覆後處理）**：
- Q1 camera scope 簡化成只問 DMS，沒對比 ADAS → 需追問
- Q2 確認題拿掉留「Once confirmed」帶過 → 需追問是否真的要 Master Portal 集中
- 寄出前未先 DM Brian preview → 看 Brian 後續是否有調整意見

---

## 5. 衝突核心分析

### 5.1 業務端 vs 產品端的期望落差

| 面向 | Wendy（業務端）的期望 | Brian（產品端）的現實 |
|---|---|---|
| 功能時程 | 盡快上線，可對客戶承諾 | 需額外開發，Q2 2026 / 七月 |
| 功能範圍 | CONNECTSOURCE 可直接使用 | 需針對 CONNECTSOURCE 重新整合 |
| 資訊頻率 | 定期路線圖同步 | 被動回應，沒有主動推播機制 |
| 承諾精度 | 具體日期 | 「Q2 / 七月」（粗粒度） |

### 5.2 根本問題診斷

1. **資訊不對稱是主因**：業務端不知道路線圖，只能被動等待。Wendy 的情緒反應背後是系統性的溝通斷裂，不是個人關係問題。

2. **功能原型 ≠ 可交付功能**：Passenger Blurring 對 BMS 可用，但對 CONNECTSOURCE 需要重新整合。這個差異沒有在早期被清楚傳達，導致業務端誤判功能的就緒程度。

3. **承諾時程粒度不足**：「Q2 2026 / 七月」對業務端太粗，客戶端無法據此規劃。更有效的說法應是：「六月確認可行性、七月開始整合測試、Q3 正式上線」。

4. **成本歸屬未釐清**：$700/月的 AWS 成本是否計入 $6/月/連線的定價？若未涵蓋，CONNECTSOURCE 的報價結構需要重新評估。

---

## 6. 待辦事項（Action Items）

### Brian / VisionMax 產品端
- [ ] 提供 Passenger Blurring 的具體里程碑節點（不只說「七月」），讓業務端可以管理客戶預期
- [ ] 確認 $6/月/連線的定價模型是否已包含 $700/月 AWS 成本分攤
- [ ] 建立定期 roadmap sync 機制（建議每季一次），確保澳洲業務端有常態資訊流

### Wendy / CONNECTSOURCE 業務端
- [ ] 向馬來西亞客戶溝通功能時程：Q2 2026 / 七月為目標，但需等 Brian 提供更細的里程碑確認

### Cary Lo / 商務端
- [ ] 確認 1,165 台裝置是否符合 Passenger Blurring 功能的最小部署規模條件
- [ ] 釐清 AWS 成本分攤是否已反映在 CONNECTSOURCE 現行定價結構中
- [ ] **（5/7 新加）** 等 Brian 拍 Q1/Q2 dev scope 後再排 Teams customer session

### 2026/05/07 新增（待 Brian 拍板）
- [ ] **Q1 passenger-only blurring** dev scope 評估：BMS DMS 結果如何餵給 blur 模組？需新開 spike ticket
- [ ] **Q2 fleet-level blurring 開關** 路線抉擇：客戶端自控（馬上可做）vs VMX server-side gating（Q2 2026 update）
- [ ] **Teams customer session prep**：scope 對齊後再訂時間，禁止裸接客戶

---

## 7. 參考資料

- AI Feature Roadmap 簡報：https://docs.google.com/presentation/d/1FIkUrx_-f1ouI3j0Tne7HdjuW1nTgnBST7GvNwcPuo/edit?usp=sharing
- 需求管理追蹤表（Google Sheets）：https://docs.google.com/spreadsheets/d/1DXCf8yU7ZrtzVdMEPSxHgmDb7cPKIFDK/edit?gid=639348744

---

## 8. PM 觀察與建議

### 短期（立即可做）
Brian 應在下次回信中把「七月」轉化為可驗證的里程碑：
> 「預計六月底確認整合方案可行性，七月啟動開發，Q3 結束前提供 CONNECTSOURCE 測試版本。任何變動我會提前通知。」

這句話的關鍵不在日期，而在「任何變動我會提前通知」——這才是 Wendy 真正需要的承諾。

### 中期（流程改善）
建立 **VisionMax Roadmap Sync** 定期會議（每季一次），澳洲、台灣業務端與產品端共同參與，輸出一頁簡報說明：
- 已上線功能
- 進行中的功能（含預計里程碑）
- 規劃中但未承諾的功能

### 長期（定價結構）
若 Passenger Blurring 成為標準功能，需在 CONNECTSOURCE 的定價模型中明確將 AWS 成本納入，避免每次都需要個案討論。

---

_Last updated: 2026/05/07 下午 — Kenny 寄出 v6 回信。Q1/Q2 都答「可行」，請客戶補確認。後續追蹤檔：`knowledge/06_calibration-log/cary-passenger-blurring-reply-draft-2026-05-07.md`。_

_Earlier 2026/05/07：補入 Cary 5/7 11:22 新提兩個問題（passenger-only / fleet-level）+ Teams session 請求。對照 HAWK-527 description 發現 driver_blurry/passenger_blurry 已是分開 flag，redocly 沒文件化（→ memory `feedback_jira_first_not_redocly.md`）。_

_Previous: 2026/05/05 — 初版建立，記錄 2026/04–05 信件串內容。_

---

## 2026-05-08 後續校正(Kenny 5/7 14:41 回信的 back-up 確認)

### Q1「European deployment API 已支援 driver/passenger 獨立 blurring」依據

**真實依據:BMS 客戶端內部 API 已支援,只是沒對外公開**。

- redocly v2026-Q1 公開 API doc 沒露出 blurring endpoint(對外保留)
- 但 BMS 客戶實際使用的內部 API 確實有 driver/passenger 獨立 blur control
- 5/7 對 Cary / Wendy 講「現有 API 已支援」是有依據的(內部 BMS API)
- 對應 HAWK-527 description 中 driver_blurry / passenger_blurry 分開 flag 的觀察 ✓

**對外口徑邊界**:
- ✓ 「能力存在」可以講
- ❌ 「公開可用」不能講 — 要 modifications + Q2 2026 update + 7 月 ship 給 CONNECTSOURCE
- 對齊 Brian 5/4 給 Wendy 的 commitment

### Q2「Master Portal > Management > Fleets > (select Fleet) > Fleet Detail > Configurations > (new) Blurring」路徑

**真實依據:Brian / Spencer 內部已確認此路徑可實作**。

- 不是 Kenny 自己看 portal 結構推的
- 對外承諾此 UI 路徑有 RD 端 backing
- 後續 Lucy UI 設計 + Brian / Spencer 拍 Q2 2026 update 排程

### 風險解除狀態

| 風險 | 狀態 |
|------|------|
| Q1 對外升級成「現有已支援」沒依據 | 🟢 解除(BMS 內部 API 真的有)|
| Q2 portal path 自推沒驗證 | 🟢 解除(Brian/Spencer 已確認)|
| 是否要主動補正 thread | ❌ 不需要 — 兩答覆都成立 |

### 等客戶下一步

等 Cary / Wendy 回覆 Q1 的兩個釐清:
1. **Camera scope**:DMS (Driver facing) only?
2. **Trigger model**:automatic blurring on every uploaded event,or on-demand only when they request a specific event clip?

收到後球轉給 Brian / Spencer 排 dev scope。

_Last updated: 2026-05-08 — Q1 BMS API back-up + Q2 portal path 由 Brian/Spencer 確認。風險解除,thread 不需主動補正。_

---

## 2026-05-08 Sync-up Meeting(Kenny + Cary + Elvis,21 分鐘)

### 起源
Kenny 5/7 14:41 回信 thread 後,客戶端有疑問。Kenny **主動 reach out** 開 Teams call 釐清(= 5/7 信中承諾的 Q3 Teams session 實際發生)。

### 重大發現

#### 🚨 Q2 Portal path 不夠精細 — Elvis 現場糾正

Kenny 5/7 信寫的:
> Master Portal > Management > Fleets > (select Fleet) > Fleet Detail > Configurations > (new) Blurring

Elvis 在會議中用螢幕分享確認:
- 那條 Master Portal 路徑**只能控制整個 main fleet 級**
- 一動 = 影響 main fleet + 所有 contract fleet 一起,**沒粒度**
- 客戶結構:Australia 1 fleet + 各 reseller 客戶當 contract fleets,**必須能 pinpoint 特定 contract fleet**
- Fleet Portal 已有 per-contract-fleet config 的能力(以 **Live User** 為例),Blurring 應沿用同 pattern

→ 5/7 信中對外承諾的 portal path **不滿足客戶實際需求**,要校正。

#### 兩條未來實作路徑

| Path | 說明 | 顧慮 |
|------|------|------|
| **(A)** Master Portal 補 contract fleet 視圖 | dealer/MAU 中央管控所有 contract fleet | ⚠️ Cary 警告隱私問題 — contract fleet 不見得想讓上層看到 |
| **(B)** Fleet Portal 加 Blurring config UI 在 per-contract-fleet 層級 | 沿用 Live User pattern,維持 contract fleet 邊界 | 沒明顯顧慮,跟客戶現有操作模式一致 |

→ 兩條路都要帶回給 Brian / Spencer 評估,Kenny 在 thread 會明確點出兩個方向。

#### Q1 API documentation 議題

Cary 在會中尖銳追問:「**Has the blurring notes been added on to the API documentation? Then what can I share with my customer please?**」

Kenny 答:目前對外文件沒寫(只給 BMS),要問 Spencer 能否提供。Cary 妥協:CONNECTSOURCE 是 integrated customer,願意用 API 直接整合暫用,不一定要等前端 UI。

→ Action:**問 Spencer 能否 share blurring API doc 給 CONNECTSOURCE 對外**(暫用版本)。

### Cary / Elvis 對 Kenny 的接納

- Cary 開頭:「Brian and Spencer are under star, they go just 'yes' — you reaching out is so refreshing」
- 結尾:「**we will be stalking you**」(以後直接 ping Kenny,跳過 Brian/Spencer)
- → Kenny 已成為 MiTAC AU 線(Cary + Elvis + Wendy)的**主對接 PM**

### Action Items(從會議掉出來)

#### P0(24h 內)→ 5/11 早上實況
- [x] **回 thread 校正 Q2 portal path** — ✅ 5/11 早上 Kenny 經 Spencer alignment 後在 Teams 提 Option A/B 兩個 model
- [x] 跟 Spencer 確認 Blurring API doc 能否 share — 🟡 Spencer aligned,**仍等 Brian sign-off**
- [x] 跟 Brian + Spencer 對齊 (A)/(B) 走哪條路 — ✅ Spencer 端 OK · ⏳ 等 Brian QPR 後拍板

---

## 6. 2026-05-11 早上 · Teams thread + Cary 拍板 Option B

> 詳見:[`meetings/2026-05-11_morning_cary-elvis-teams-thread.md`](../meetings/2026-05-11_morning_cary-elvis-teams-thread.md)

### 6.1 Spencer 重新框架的兩個 model(等於 5/8 (A)/(B) 順序對調)

| Spencer 提的 | 對應 5/8 sync | 拍板 |
|------------|--------------|-----|
| Option A — Two-tier delegated control(Master 持 entitlement,delegate 給 Fleet)| ≈ 5/8 sync 的 **(B)** Fleet Portal UI | ❌ 未選 |
| **Option B — Centralised control at Master**(Master 直接控所有 Blurring permission 含 Contract Fleet 層級)| ≈ 5/8 sync 的 **(A)** Master Portal 補視圖 | ✅ **Cary 拍板** |

### 6.2 Cary 拍 Option B 理由(立場翻轉)

> "this will potentially incur an extra fee, thus the SI need to be able to have full control which fleet they would like to push this feature out to."

- **billing 控制 > 5/8 提的隱私顧慮** — 5/8 Cary 還警告 Master 視圖會「alarming」,但今天反向選 Centralised
- 推測:內部討論後確認「extra fee 由誰收 / 誰決定推」才是核心商業問題,隱私可用 BMS 既有「Master 預設 on,Fleet 不顯示開關」mitigate

### 6.3 🆕 新需求 · Monthly subscription report

> "It will also be great, if we can have this appear on the monthly subscription report. So we know how many devices under each master account has this feature implemented."

- 訊號:Cary / Wendy 已把 Blurring 當成**下一輪 monetization tier**,SI 要 billing visibility
- 對 MiTAC HQ 意義:Blurring 不只 feature,**是新 subscription tier 上升的依據**
- 待動作:跟 Spencer 細談 monthly subscription report 加 Blurring 啟用裝置數的可行性(Jira 哪張單?新單?)

### 6.4 Q1 API doc share — 重大新限制揭露

Spencer 透過 Kenny 傳達:
> "even once the document is shared, the customer will not be able to call the API yet, because the endpoint has not been opened on our current VisionMax environment. It will only be enabled after our internal validation is completed."

- **doc sharing 跟 endpoint open 是兩件事** — 即使 Brian 同意 share doc,客戶**仍不能 call**
- 暫時對外口徑:「Blurring function is on our roadmap」(等 Brian 同意才講)
- 待動作:準備「能 share 但不能 call」的 wording 給 Cary 對外用

### 6.5 今天 2pm 計畫 · Q1 API sync

- Kenny + Elvis(可能 Cary)— 14:00 台灣時間
- 同 Teams group meeting link
- Stark 另有 call shortly(不在本 group)

---

## 7. 更新後的 Action Items(2026-05-11 morning 之後)

#### 🔥 P0(今天剩下時間)
- [ ] **2pm Q1 API sync 跟 Elvis(可能 Cary)** — 同 Teams group
- [ ] Brian QPR 結束後 confirm:API doc share / Option B 拍板 / Endpoint open 時程
- [ ] 寫正式 email reply,把 Spencer preliminary + Brian 最終 position 一起發

#### 📅 P1(本週)
- [ ] 跟 Spencer 細談 monthly subscription report 加 Blurring 欄位的可行性
- [ ] Critical Facts log 加 Option B 拍板紀錄 + endpoint 未 open 限制
- [ ] 把 5/11 morning thread 同步給 Wendy(她不在這個 Teams group)

#### 🎯 P2(下個 sync 前)
- [ ] Monthly subscription report 加 Blurring 欄位若進 sprint,排優先級
- [ ] Endpoint open 條件「internal validation」具體 criteria + 預估完成日

_Last updated: 2026-05-11 早上 — 補 5/11 Teams thread + Cary 拍板 Option B + monthly report 新需求 + endpoint 未 open 限制 + 2pm Q1 API sync 安排。_

---

## 8. 2026-05-11 下午 14:00 · Cary / Elvis / Brian sync · Q2 scope 拍板

> 詳見:[`meetings/2026-05-11_afternoon_cary-elvis-sync.md`](../meetings/2026-05-11_afternoon_cary-elvis-sync.md)

### 8.1 Q2 Scope 最終拍板(Brian take over 釐清)

| Scope | 內容 | 時程 |
|-------|------|------|
| **Q2 In Scope** | BMS Blurring 整合進 VisionMax cloud + Release API doc 給 Connect Source | Staging end of June / Production end of July |
| **Q2 Out of Scope** | UI on Master/Fleet Portal(Auto Sense 用)— 要 GUI design,是 long term | 不在 Q2 |
| **Post-Q2** | Monthly subscription report 加 Blurring tracking | "Future planning" — Brian's call |

### 8.2 Connect Source 走 API only · 不需要 UI portal toggle

Brian 拍板:
> "if they use the API they could use the API to blurring any video they want... we don't need to consider is the customer is under the free or subly."

→ **Connect Source 走 API 整合,不分 fleet vs contract fleet permission**。API 自己可控任何 video / fleet。

### 8.3 Option B 拍板的真實意義(早上 vs 下午對齊)

| 早上 Spencer 框架 | 下午 Brian 釐清 |
|----------------|---------------|
| Option A delegated / Option B centralised(UI 視角) | Option A 跟 B 在 API 層 **是同一條 flow**(Kenny 在會議裡有講出來,但太晚太含糊) |
| Cary 選 Option B = Master 中央控制 UI | **Connect Source 不需要任何 UI**(API only)· Auto Sense 需要 UI 是另案 |
| 隱含「Master Portal 有 toggle」 | Master 端 entitlement 是 backend 設,**只能 API 層呈現** |

### 8.4 Jira tickets(已開 · 2026-05-11)

| Ticket | Summary | Type | Priority | Component | Assignee | Due / Timeline |
|--------|---------|------|----------|-----------|---------|---------------|
| [**VMX-7457**](https://jira.navman.co.nz/jira/browse/VMX-7457) | [API] Integrate BMS Blurring functionality into VisionMax cloud(含 API doc share to MAU 作為 AC) | Task | 2 - Medium | *Fleet/Master backend API | **Spencer** | **Due 30/Jun/2026**(staging)· Production end of July |
| [**VMX-7458**](https://jira.navman.co.nz/jira/browse/VMX-7458) | [VisionMax] [GUI] Blurring control UI on Master/Fleet Portal for non-API customers | Task | 2 - Medium | *Fleet/Master frontend | **Kenny**(自己 own scoping)| Q2 feasibility · 實作 long-term |
| _(暫不開 ticket)_ | Monthly subscription report — Blurring enablement & usage tracking | — | — | — | — | Post-Q2 production · 等真實需求落地再開新單 |

#### 為什麼 #4(Monthly report)暫不開 ticket
- **參考舊單**:[VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427) "Improve reporting function #107" — Elvis 2025/06/05 開,目前 assign Spencer,但**這張是更大的 events reporting 改造**(需要 Time Series DB migration,Brian 4/20 acknowledge 但未排入 sprint)
- VMX-6427 ≠ Blurring monthly report 的對應位置 — overlap 但不是同一件事
- **決策(2026-05-11)**:Blurring monthly report 等 Production deploy 後(end of July 後)有具體 SI usage 資料時再開新單,不疊在 VMX-6427 上
- **對 Cary 口徑**:「Tracked as future enhancement post-Q2 production, will scope once we have real usage data」

#### Kenny 在 VMX-7457 / 7458 的 2 個 sharp 處理
1. **#1+#2 合併在 VMX-7457**:cloud integration + API doc share 同票,doc share 寫進 AC,不分兩張避免並行追蹤負擔
2. **VMX-7458 把 pattern reference 改精準**:從「Live User」改成「**Driver-Facing Camera Live View**」— 對 Lucy / GUI team 更明確

#### VMX-7457 內 2 個 deliverable 不同 timeline(Kenny 5/11 加 comment 釐清)

合併同票會讓票面 Due date(30/Jun/26)誤導 — 看似 doc share 也要等到 6 月底。**Kenny 在 VMX-7457 加 comment 標清楚 2 個 deliverable 不同 commitment**:

| Deliverable | Timeline | 對 Cary commitment |
|------------|----------|------------------|
| **A · API documentation share to MAU – Connect Source** | **本週 post-QPR** · 等 Brian sign-off | 「receive doc this week」(本週收到 doc)· cover note 必須標 "doc share ≠ endpoint live" |
| **B · Cloud integration**(ticket main scope) | **Staging 30/Jun/2026** · Production end of July(post-DQE)| 「Q2 release notes summary by end of June」(對外發給客戶前先 review) |

→ Endpoint cannot be called live against production until Deliverable B validation completes — Cary 已 briefed。

→ **Comment 已加進 VMX-7457**,Brian / Spencer 一讀就知道兩條 timeline 不同 · 後續對 Cary 任何承諾都 traceable 在 ticket 上。

### 8.5 對 MAU 的 commitment 更新

| Cary 5/11 早上要的 | 2pm 結論 |
|------------------|---------|
| ① 確認 Option B(per-fleet billing 控制) | ✅ 走 API · per-fleet/contract-fleet 在 API 層自然支援 |
| ② Monthly subscription report 加啟用裝置數 | 🕐 開 Ticket #4 · post-Q2 future planning · 不能消失 |
| ③ 2pm Q1 API sync | ✅ 已開 · Q2 scope 鎖定 |
| (Elvis 加碼)未來 deployment 前 notify · Q2 release notes 提早給 | ✅ Kenny commit · end of June 給 release notes |

### 8.6 Action Items(2pm 結束後)

#### 🔥 P0 · 今天剩下時間
- [ ] **Cary follow-up email**(把今天 dismiss 掉的 monthly report 救回來)· cc Brian / Spencer / Wendy / Elvis
- [ ] Brian / Spencer 1-on-1 ping · review 今天會議的 execution gap

#### 📅 P1 · 本週
- [ ] 開 4 張 Jira ticket(§ 8.4)
- [ ] 跟 Spencer 拿 endpoint open production 的 concrete ETA
- [ ] Q1 release notes 對 MAU 客戶部署前先安排(Cary 5/11「don't surprise」訊號)
- [ ] update knowledge(critical-facts / changelog / case-hub.html · 已執行)

#### 🎯 P2 · End of June 前
- [ ] Q2 release notes summary 給 Cary(對外發給客戶之前)
- [ ] GUI team kick-off(Ticket #3 Auto Sense UI 可行性)
- [ ] Connect Source SI 端 integration 進度追蹤

### 8.7 Kenny 自評:Execution gap

**真實問題**:準備層(Kenny 版 / Cary 版 HTML / sound-bites)極完整 → 但會議現場幾乎沒 deploy。Brian 進場 take over 5 分鐘把所有事情講完,**主導權失分**。

**下次 protocol**:T-30min pre-game drill 內化(verbatim 念 sound-bite / 指圖練習 / 念 DON'T SAY)· 會議室只帶 Cary 版 · 手機備 Kenny 版(緊急廁所看)· Kenny 版 **不帶進會議室**(INTERNAL banner 被旁邊主管看到尷尬)。

_Last updated: 2026-05-11 下午 · 補 § 8 2pm sync 結論 + Q2 scope 拍板 + Jira queue + Kenny 執行 gap 自評。_

---

## § 8.8 · 2026-05-11 傍晚 · Brian 攔下 Cary follow-up email

### 事件

2pm sync 後 Kenny 起草了一封 follow-up email 給 Cary / Elvis(cc Wendy / Brian / Spencer)— 內容包含:
- Q1 + Q2 兩個原始 5/7 問題的 ✅ Confirmed 答案
- VMX-7457 / VMX-7458 ticket link
- 4 條 commitment timeline(doc share 本週 / staging 30/Jun / production end-Jul / Q2 release notes end-Jun)
- Monthly subscription report 救球段(tracked as post-Q2 future enhancement)

**Brian 5/11 傍晚 review 後說「不要發」**,Kenny 接受並暫停。

### 推測 Brian 攔下的可能原因

| 可能性 | 訊號 |
|--------|------|
| A · Brian 想自己發 | 維持 Connect Source 對外主導 · 不把主導權回給 Kenny 書面動作 |
| **B · 不想對 Cary 紙上 commit 時程** | "doc this week / staging 30/Jun / production end-Jul" 寫成 email → 萬一延誤客戶有紙本追責 |
| **C · 內部還沒完全對齊** | QPR 未走完 · Spencer endpoint 條件未鎖死 · 不想 Kenny 先 lock in |

→ **最大概率 B + C 混合**(Brian 反射動作 = 別在 spec / timeline 鎖死前留書面 trail)

### Kenny 後續動作

1. **Teams 短訊 ping Brian**(已執行 / 待執行):
   - Q1: Brian 自己發,還是這 thread 先 hold?
   - Q2: 若 hold,什麼 trigger 後再 communicate(doc sign-off / staging deploy / other)?

2. **準備好「Cary / Wendy chase」的口頭答覆模板**(沒書面 trail 不代表 Kenny 沒記住結論)

3. **不要主動再寫 follow-up email**,等 Brian 動作或明確授權

### Email draft 存底(沒發但留 record)

完整 draft(中英對照)備份在 `weekly-summary/2026-05-11_blurring-followup-email-draft.md`(若未來 Brian 授權發,直接拿)。Email 涵蓋:
- Subject: "Confirmed · Passenger Blurring Q1 + Q2 — Implementation Summary"
- Q1 ✅ Confirmed feasible(driver/passenger 區分 BMS API 已支援)
- Q2 ✅ Confirmed feasible at API level(三層 inheritance + override)
- Jira tickets VMX-7457 / VMX-7458
- 4 條 commitment timeline
- Monthly report future enhancement 救球段

### Implication(Kenny 心裡要記)

| 沒發的後果 | 影響 |
|----------|------|
| Cary 早上 monthly report 球 | 沒救回來 · 她下次會 chase |
| 2pm 拍板的 4 條 commitment | 只有口頭印象 · Cary / Wendy / Brian 都可能忘細節 |
| Wendy 完全不知道 2pm 結論 | 她下次 ping 你問「最後決定什麼」, 你只能口頭 forward |

→ **這些不是 Kenny 的鍋**(Brian 攔下),但 Kenny 腦中要記「Cary / Wendy 任何時候 chase, 我有準備好答案」。

### 校正紀錄(2026-05-11 傍晚 v2 · Brian 二次回應後校正)

**Kenny 二次 ping Brian 後**,Brian 回:**「不用那麼麻煩, 他看我 Jira 寫清楚了」**

→ 校正之前的推測(B+C 混合,Brian 不想留書面 trail)成更精準的解讀:

| 我之前推測(過度保守)| Brian 真實立場(更 relaxed)|
|---------------------|--------------------------|
| Brian 不想在 spec/timeline 鎖死前對客戶留書面 trail | **Jira ticket 寫清楚 = 對外 commitment 已建立 · external email 是 redundant** |
| 「未來對外發 commitment 文件前先 Brian sign-off」| **內部 Jira / case file 寫清楚 = SSOT 已建立 · 對外只在客戶要書面 audit 時才寫** |
| 等於 Kenny 動作被 gate | **Brian 對 Kenny 的開單質量肯定**(特別是 VMX-7457 拆 Deliverable A/B 那個 comment 動作有效) |

### Kenny 拿到的 3 個訊號

1. **書面工作 > 口頭工作** — 今天 2pm 會議 execution gap 的失分,被 Jira 開單質量補回一半
2. **MDT 文化內 SSOT = ticket** — 不需要重複做 external 文件
3. **客戶 chase 時口頭 / Teams 回答**根據 Jira 內容即可,不用 wait Brian sign-off email

### Cary / Wendy chase 時的口頭答覆模板

預期本週內會收到 chase(「Q1+Q2 最後決定?」/「doc 何時給?」/「monthly report 你們會做嗎?」)。
直接照 § 8.8 email draft 內容口頭 / Teams 回:

| 客戶問什麼 | Kenny 怎麼答 |
|----------|------------|
| "Q1 (driver/passenger blur) 確認嗎?" | "Confirmed feasible at API level. BMS API already supports it. For Connect Source, your SI calls the API specifying scope." |
| "Q2 (per fleet / contract fleet) 確認嗎?" | "Confirmed feasible at API level. Three-layer inheritance — Master → Fleet → Contract Fleet, with API override at any layer. Connect Source has full programmatic control." |
| "doc 什麼時候給?" | "This week, post Brian's sign-off after QPR. I'll ping you the moment it's ready." |
| "endpoint 什麼時候 live?" | "Production end of July, post-DQE. Staging end of June. I'll confirm exact date once Spencer's internal validation lands." |
| "monthly subscription report?" | "Tracked as future enhancement post-Q2 production. Data foundation is in VMX-7457 (every API call logged). We'll scope the format with you once we have real usage data flowing — happy to revisit format after July." |
| "你 5/8 提的兩條 portal path 路徑(A/B)?" | "After deeper RD alignment, the per-Contract-Fleet control you needed is fully supported at the API level today. Auto Sense's UI track is separate — long-term." |

→ 這些答覆**跟 Jira / Brian 立場一致**,客戶任何時候 chase 都答得出來。

_Last updated: 2026-05-11 傍晚 v2 · 校正 § 8.8 Brian 二次回應 + Kenny 學到 + chase 時口頭答覆模板。_
