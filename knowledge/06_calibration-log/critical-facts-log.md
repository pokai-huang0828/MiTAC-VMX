# 已校正的關鍵 VMX 事實

> 🎯 **SSOT** — 所有「過去答錯後校正」的事實在這裡。其他檔提到這些事實時只能 link,不要複製。
>
> 過去 Claude / 對話中答錯後修正的事實。**對 RD / 客戶 / 內部講話前先看這份**。
> 索引:[`00_index/ssot-map.md`](../00_index/ssot-map.md) | Changelog:[`00_index/changelog.md`](../00_index/changelog.md) | Jira 即時狀態:[`00_index/jira-snapshot.md`](../00_index/jira-snapshot.md)(2026-05-12 抓 137 票)

## AI Model 版本對應 + 6/2 Fix Version 死線(2026-05-12 下午從 5/11 AI Weekly 錄音揭露 via NotebookLM)

### 4 個現役 / 規劃中 AI Model
- **Model 11P**:原本用於「嘴部 (Mouth)」辨識的分類模型 → 現正被修改為「全臉 (Full Face) 打哈欠 (Yawning)」辨識
- **Model 11L**:舊版的 DMS(含安全帶)分類模型 — **將被 Model 26 取代**
- **Model 26**:新導入的 DMS 分類 + Detect 模型架構,**準確度優於 11L**,預計掛 6/2 Fix Version 上線
- **V14**:先前用於影像模糊化 (Blurring) 的舊模型版本(對應 [HAWK-527](https://jira.navman.co.nz/jira/browse/HAWK-527) / [HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578) Blurring 修問題的舊基礎,對外仍是「2026-05-06 已 fix」口徑)

### 6/2 Fix Version(2026-06-02)— 三個必上 deliverable
- **LDWS API** — 之前 [VMX-7375](https://jira.navman.co.nz/jira/browse/VMX-7375) Pending,5/7 AI Weekly 講過暫緩,但 5/11 AI Weekly **重新掛 6/2**(後續需從 Jira 確認 transition 狀態)
- **BMS 鏡頭遮蔽拆分**([HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) Lens Cover,Eric H 2026-05-08 13:38 confirmed `planned for the next release in June`,handoff 已記)
- **新版 DMS 模型(Model 26)** — Yawning + 安全帶 + Distraction 統一架構,**必須在 6/2 Fix Version 發布**

### 5/15(15 號)Beta 測試前置死線
- **要求外部 API / 模組需在此之前 ready** — 等於 Kenny 對 Cary / Elvis / Wendy / MiTAC AU 的 commitment 都要在 5/15 前確認 API 規格凍結

### Regression Risk(NotebookLM 自動 PM 建議)
- 6/2 同時上 Model 26(DMS 底層替換)+ 11P(嘴部→全臉)+ V14 → vNext(Blurring)— **三個 model 同時動,Regression Bug 高風險**
- 動作建議:跟 QA 團隊(Righter / Richard)擬 Regression Test Plan 鎖「Head 邏輯」+「Model 26」雙重路徑;UI 團隊敲「打哈欠開關」Figma 設計

- 校正人:Kenny + NotebookLM 自動摘要(5/11 AI Weekly 錄音 + 4 個 source 交叉)
- 應用:對 Brian / Jimmy / Vincent / Eric H 提 6/2 release 時用 Model 26 / 11P / V14 三個 model 區分,**不能再講「DMS 模型」這個籠統字**

## Jira 本週新 Resolved/Closed(2026-05-12 全 137 ticket comment ingest 揭露)

### 已 deploy / Resolved(對外可講「✅ 已 ship」)
- **[VMX-7239](https://jira.navman.co.nz/jira/browse/VMX-7239) Closed 5/11(Vincent)**:`Add handheld object classification model for phone usage feature` — 飲食誤判 17x 客訴改善 sub-feature
- **[VMX-7419](https://jira.navman.co.nz/jira/browse/VMX-7419) Resolved 5/7(Spencer)**:`[API] new event type: rollover` — Mori 200Hz Rollover API **已 release**。對外可講「Rollover event API 已 ship」
- **[VMX-7381](https://jira.navman.co.nz/jira/browse/VMX-7381) Resolved 5/8(Lucy)**:VisionAgent iOS / AOS 無法刪除 Event — james.cw.chou 5/8 提 patch
- **[VMX-6925](https://jira.navman.co.nz/jira/browse/VMX-6925) Resolved 5/5(jay.qiu)**:`[MMF] Partial Map Update` — andrew 5/5「**已完成 Partial map update 功能**」(MMF 全 feature 仍未上線,但 partial update 可用)
- **[VMX-7346](https://jira.navman.co.nz/jira/browse/VMX-7346) Resolved 4/24(Vincent)**:`[ServerAI] pre_event_message 加 cdr 版號` — chiehli 4/20 加 `app_version` 欄位
- **[HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578) Resolved 5/6(Luís)**:VisionMax PROD 不 blurring 修 — chiehli 5/6 SQS retention 14d 配套部署
- **[HAWK-527](https://jira.navman.co.nz/jira/browse/HAWK-527) Resolved 5/6(Vincent)**:`Blurring not reliable` — Sebastian 5/6 確認 fixed

### 已 Closed
- **[VMX-6920](https://jira.navman.co.nz/jira/browse/VMX-6920) Closed 3/9(Jimmy)**:`[DMS] Smoking 新參數` — 已 deploy 2 個月,stakeholders.md BMS 列已校正
- **[HAWK-331](https://jira.navman.co.nz/jira/browse/HAWK-331) Closed 4/22(Luís)**:`Blurring (face, background, license plate)` — 主案結束,follow-up ticket 已開

### 設計完但未 ship
- **[VMX-6353](https://jira.navman.co.nz/jira/browse/VMX-6353) Resolved 5/7(Mori)**:`[MMF] Map Data Update Flow Design` ⚠️ **Design 完成,不是 MMF 上線**。對客戶仍維持「MMF 還沒上線、不要承諾」口徑

### 進行中但有重要進展(對外應更新口徑)
- **[HAWK-577](https://jira.navman.co.nz/jira/browse/HAWK-577) Open 5/11(chiehli)**:`Blurring on-demand fails when not all event media ready` — root cause 5/4 已定位
- **[VMX-7254](https://jira.navman.co.nz/jira/browse/VMX-7254) In Progress 5/5(Spencer)**:`Cloud integration for rollover` — hsinyi 5/4 加 `tiltAngleThresholdDeg` + `samplePercentageThreshold` 2 個參數

- 校正人:Kenny + Jira REST API 全量抓取(透過 Chrome MCP 連 jira.navman.co.nz,2026-05-12 第一次完整 ticket comment ingest)
- 應用:對 Brian / Mori / Lucy / Spencer / Vincent / Sebastian 提對應功能時,**用「✅ 已 ship」**
- 完整 137 ticket 即時狀態:[`websiteview/docs/00_index/jira-snapshot.html`](../../websiteview/docs/00_index/jira-snapshot.html)

## Jira `New` status 含意(2026-05-12 大規模發現)
- 全 hub 提到的 137 ticket 中:**93 個 (68%) 是 New status**
- 但其中**多數實際已做完**,只是 RD 沒按 transition button(Open → Resolved)— 已記錄在「[VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722) LDWS transition discipline gap」段
- **判斷規則**:`status=New` + `Updated > 90 days ago` = 大概率已 deploy 但 transition 漏按 / 或永久 stale
- 應用:看 ticket 真實狀態,**讀 Updated 日期 + Comment 內容**,不要只看 status
- 提案 Brian:Q2 做一輪 ticket triage,把這些「New 但已做完」全 transition 掉

## VMX subscription KPI:100K(目前差 15K)(2026-05-09 QBR 揭露)
- 來源:Brian 2026-05-09 10:07 信「VisionMax 2026 Q1 QBR」內明寫
- **Steve 今年底 KPI = 100,000 台**,目前進度估**還差 15K**
- 等於目前 ≈ 85K,要再簽 15K 才能達標
- QBR Deck:`https://docs.google.com/presentation/d/1UWin65dXNCtp_ExzP1_pCF9Upzu4tQOp`
- 對外應用:**不要對任何客戶 quote 這個數字**(內部 KPI),只對 Brian / Spencer / Mori / Spencer 線講
- 對內應用:Kenny 自己工作如果跟 QBR deck 列的 projects 沒對齊,Brian 信中明說「請最好再來和我確認一下」

## [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) Lens Cover 設計修正:單軌即可滿足客戶(2026-05-11 校正)
- ❌ 之前理解(memory `project_meeting_2026-05-07_ai_weekly.md`):RD 緊急雙軌維護(Azuga 標準版解除車速、BMS 版車速 > 0 才啟動)
- ✅ **[HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) 揭露**:Webfleet (Sebastian Schneider) 報告,Bridgestone (Jakob Mund) 確認偏好 Flow 1(ignition ON + 無移動就偵測),**spec 改成取消 speed ≥ 20 km/h + DMS calibration 完成兩個 dependency**
- **Eric H (謝翔宇) 2026-05-08 13:38 comment 確認**:`The feature is planned for the next release in June`
- 校正後現狀:**不是「雙軌維護」,是改設計後單軌即可滿足三客戶(Webfleet / Bridgestone / Azuga)**
- 對外應用:6 月 release 可以對 Cary / Wendy(MiTAC AU 線)提,passenger blurring 是同 pattern 案,客戶會問
- Jira link:`https://jira.navman.co.nz/jira/browse/HAWK-582`

## BMS 客戶端 API 有 driver/passenger 獨立 blurring 能力(2026-05-08 校正)
- ❌ 之前以為:redocly v2026-Q1 沒 blurring endpoint = blurring 沒 driver/passenger 區分
- ✅ **正確**:**BMS 客戶端內部 API 已支援 driver/passenger 獨立 blurring control,只是沒對外公開**
- 校正日:2026-05-08
- 校正人:Kenny(回覆 Cary 5/7 thread 後內部確認)
- 應用:對 Cary / Wendy 講「現有 API 已支援」有依據,但**邊界**是「能力存在」≠「公開可用」(要 Q2 2026 update 才能 ship 給 CONNECTSOURCE)
- 跟 Brian 5/4 給 Wendy 的「Q2 2026 update / 7 月最早 ship」commitment 一致

## Master Portal Blurring config UI 路徑(2026-05-08 兩次校正 → 2026-05-11 Cary 拍板 Option B)
- ⚠️ **v1 (5/8 早上)Brian/Spencer 確認可實作**:`Master Portal > Management > Fleets > (select Fleet) > Fleet Detail > Configurations > (new) Blurring`
- 🚨 **v2 (5/8 下午)Sync-up Elvis 現場糾正**:這條路徑**只能控制整個 main fleet 級**,一動 = 影響 main + 所有 contract fleets,**沒 per-contract-fleet 粒度**
- 客戶實況:Australia 1 fleet + 各 reseller 客戶當 contract fleets,**必須 pinpoint 特定 contract fleet**
- **v3 (5/11 早上)Spencer 重新框架兩個 model**:
  - **Option A — Two-tier delegated**:Master 持 overall entitlement,delegate 給 Fleet,Fleet 自己決定 Contract Fleet 開關(≈ 5/8 (B) Fleet Portal UI)
  - **Option B — Centralised at Master**:Master 直接控所有 Blurring permission 含 Contract Fleet 層級,Fleet 不 manage(≈ 5/8 (A) Master 補視圖)
- ✅ **2026-05-11 Cary 拍板:Option B(Centralised at Master)**
  - 立場翻轉理由:**feature 可能 incur extra fee → SI 要 full control which fleet 推**(billing 控制 > 隱私顧慮)
  - 同時提新需求:**monthly subscription report 加「每 master account 下啟用裝置數」**(billing tracking)
- ⏳ 待 Brian QPR 後 confirm 拍板
- 詳見:`meetings/2026-05-11_morning_cary-elvis-teams-thread.md` + `case-learning/connectsource-passenger-blurring.md` § 6

## Connect Source = API only / Auto Sense = UI(Q2 不做)(2026-05-11 下午 Brian 拍板)
- ✅ **Connect Source(MAU 客戶)**:已 API integrated · **走 API only,不需要 UI portal toggle** · API 可控任何 video / 任何 fleet · contract fleet 不需要在 portal 端做 permission
- 🕐 **Auto Sense(MAU 客戶)**:用 VMX web UI(2000+ devices)· 要 GUI design 才能加 Blurring 控制 · **Q2 不做**(long term)
- ✅ **Q2 scope 拍板**:(1) Integrate BMS Blurring into VMX cloud · (2) Release API doc 給 Connect Source
- 🕐 **Monthly subscription report 加 Blurring tracking**:Brian「not the target for now, future planning」· **暫不開 ticket** · Production deploy 後有真實 usage 資料再開新單 · 舊單 [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427)(events reporting infra)不對等
- 📅 **時程**:Staging end of June · Production end of July · Q2 release notes end of June 給 Cary(對外發布前)
- 對外應用:對 MAU 講「Connect Source 走 API,Q2 可 ship;Auto Sense 走 UI 是另案 long term」· **不要把 Connect Source 跟 Auto Sense 的方案混講**
- 來源:Brian 2026-05-11 14:00 sync(Cary / Elvis 在場)
- **Jira tickets(2026-05-11 開)**:
  - [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) — Cloud API integration + doc share(Spencer · Due 30/Jun/26 staging)
    - **2 個 deliverable 不同 timeline**(Kenny 5/11 加 comment 釐清):
      - A · **API doc share**:本週 post-QPR(對 Cary commit「本週收 doc」)· cover note 必須標 "doc share ≠ endpoint live"
      - B · **Cloud integration**:Staging 30/Jun · Production end of July post-DQE(對 Cary commit「end of June 給 Q2 release notes summary」)
  - [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) — GUI feasibility for non-API customers(Kenny · long-term)
  - [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427)(舊單,事實 reference,**不當作 Blurring monthly report 對應位置**)

## Option A vs Option B 在 API 層是同一條 flow(2026-05-11 下午 Kenny 講出但太晚)
- 🚨 **5/11 早上 Spencer 給的 Option A(delegated)/ Option B(centralised at Master)是 UI 視角的框架**
- ✅ **下午 Brian 拍板**:在 API 層,A 跟 B 是**同一條 flow** — 因為 API 本來就可以控任何 fleet 任何粒度 · UI 視角的差異在 API 層消失
- 對外應用:**未來討論 Blurring per-fleet 控制,直接用 inheritance + override + on-demand 模型講**,不要回去用 UI Option A/B 框架(已 superseded)
- 對 Cary 線:後續 follow up 不要再提 5/11 早上的 Option A/B,直接講「API 路徑 + inheritance model」

## Jira ticket = SSOT,external email follow-up 通常 redundant(2026-05-11 傍晚 calibration)
- 🎯 **真實 calibration**(經 Brian 5/11 傍晚二次澄清後校正):
- **事件**:Kenny 2pm sync 後起草 follow-up email 給 Cary(Q1/Q2 ✅ Confirmed + ticket link + 4 條 commitment timeline + monthly report 救球段)→ Brian 第一次回「不要發」→ Kenny 再 ping 確認 → **Brian「不用那麼麻煩,他看我 Jira 寫清楚了」**
- **Brian 真實立場**:
  - Jira ticket 寫清楚 = **對外 commitment 已建立**(內部 SSOT)
  - External email 重複 Jira 內容 = **redundant overhead**
  - 客戶 chase 時:口頭 / Teams 回答即可,不需要 email 留書面 trail
  - 對 Kenny 開單質量肯定(特別是 [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) 加 comment 拆 Deliverable A/B 那個動作)
- **新規則**:
  - 內部 ticket / case file 寫清楚 = commitment 已建立 · 不需要再做 external 書面文件重複
  - 對外發 email 只在「客戶看不到 Jira + 需要書面 visibility 給上級 audit」時做
  - 客戶 chase 時口頭 / Teams 回答(根據 Jira 內容)即可
- **Kenny 學到的**:
  - **書面工作 > 口頭工作**(MDT 文化內 net positive)
  - 把 Jira / case file / changelog 寫精細 = 對 Brian 來說「Kenny 有 own」訊號
  - 但 Kenny 心裡要存好 chase 時的口頭答覆 mental model
- 適用情境(同樣不發 external email):
  - timeline / scope 確認類(Jira 內有時)· spec 澄清類(ticket comment 內有時)· 對客戶承諾 audit 類
- **要發 email 的情境**(這個沒變):
  - 客戶看不到 Jira 但要書面 visibility 給他們上級 audit · 跨組織正式宣告 · 真實必須留書面 trail 的法務/商務 commitment
- email draft 不丟掉 → 存在 `case-learning/connectsource-passenger-blurring.md` § 8.8 · 未來 Brian 授權時可直接拿(可能性低)
- 來源:Brian 5/11 傍晚二次回應「不用那麼麻煩, 看我 Jira 寫清楚了」

## Blurring API doc share ≠ endpoint open(2026-05-11 揭露)
- 🚨 **重大限制**:即使 Brian 同意 share API doc 給 CONNECTSOURCE,客戶**仍不能 call API**
- 原因:**endpoint 還沒在現 VisionMax 環境 open**,要 internal validation 完成才開
- 對外口徑:**「Blurring function is on our roadmap」**(等 Brian agree 才能講)
- 對內待動作:跟 Brian 確認 internal validation 完成 criteria + 預估 endpoint open 日期
- 應用:對任何客戶提 Blurring API 都要兩段式說明 — (1) doc 可給 (2) 但 endpoint 未開,**不要讓客戶以為「拿到 doc = 馬上可用」**
- 來源:Spencer 5/11 早上經 Kenny 傳達(QPR 期間 alignment)

## 對外 cost / 數字 commitment framing 防身術(2026-05-13 三輪校正後固化)
- 🚨 **觸發情境**:5/13 給 Elvis Passenger Blurring 訊息經過 v1 → v2 → v3 三輪修訂才安全寄出 — 任何包含 cost / 倍數 / 美金數字的對外訊息都適用以下 6 條
- **修訂歷程**:
  - **v1 ❌**:錯引 AWS Rekognition Video API ($0.10/min) 作為 cost 錨點 → MiTAC 用**自家 AI**,不是 Rekognition,客戶點公開定價連結會發現對不上,credibility 受損
  - **v2 ✅**:校正為 MiTAC 自家 AI(內部 proprietary)+ AWS S3 storage($0.023/GB)+ bandwidth(杯水車薪)
  - **v3 ✅**:Storage 倍數重算 — **1.8× 不是 10×**(因原始檔本來就會存,只有 blurred copy 隨 trigger 倍增)· AI 處理量 10× 是物理事實,但 cost scaling 是黑盒不能對外承諾倍數
- **6 條 framing 規則**(下次任何類似情境直接套):
  1. **「Mechanism (factual)」段標** — 把確定的事實跟假設清楚切開
  2. **「A hypothetical to illustrate」段標** — 假設條件外顯(例:「假設 1,000 連線 × 5 events/day」),客戶可說「我們其實是 30%」→ 自然修正不打臉
  3. **「scales meaningfully higher」** — 給方向不給具體倍數。**絕對不要寫「~10×」這種數字**,除非有 Brian/Spencer 正式 quote backing
  4. **「subject to Spencer's quote」/「subject to Brian's confirmation」** — 把報價權責交回正確的人,自己不在現場拍數字
  5. **引用 source 用原話** — 例「separate commercial arrangement」是 Brian 4/24 信件原話,寫進訊息有 source 不憑空
  6. **弱點轉設計理由** — 例「BMS 不可見 = 為何我們開 Step 3 control point」,把「我們不知道」轉成「所以才有這個機制」
- **最大坑**:把**內部假設當成事實**寫進外部訊息(例如把 AI 處理量 10× 當成 cost 10×;把 AWS 公開定價當成我們的成本)
- **預先 grep 自查**(寫完訊息 before send):
  - 是否引用某個外部服務的定價?(若是,先確認我們是否真的用那個服務)
  - 任何具體倍數 / 美金數字,問自己「這個數字有 Brian/Spencer 書面 quote 嗎?」沒有的話就改 "meaningfully higher" / "subject to formal quote"
  - grep 訊息找「~Nx」「$N」「per X」這些 token,每個都要對得回 source
- 來源:Kenny 2026-05-13 Elvis Passenger Blurring 對話三輪修訂 · 完整 case 在 `case-learning/connectsource-passenger-blurring.md` § 9 + memory `feedback_external_cost_framing.md`

## 機種列表(2026-05-08 再校正)
- ❌ v1 之前答:K245 / K265 / K165
- ⚠️ v2 校正(2026-04):K145c / K220 / K245 / K245c / K265(認為沒有 K165)
- ✅ **v3 真相(2026-05-08 Outlook Vinicius 5/7 信件揭露)**:**K165 真的存在** — Vinicius 在 5/7 11:02 AM 給 Paul Lee 的 testing plan 中明確要求測 K165(single lens dashcam,某些客戶 single lens 是 requirement)。
  - 所以 K-series 完整應為:**K145c / K165 / K220 / K245 / K245c / K265**(可能還有 K246 Orion 未來機種,Vinicius 也提到)
- 校正人:Vinicius Francisquinho (Platform Science) 5/7 testing plan
- 重要:**對 Vinicius / Platform Science 不要再說「沒有 K165」**;K165 = 單鏡頭 dashcam 版本
- 待動作:跟 Mori 確認 K165 完整 spec(chip / 鏡頭 / 算力)+ 為什麼之前 memory 說沒有

## 紅色按鍵功能
- ❌ 之前答:Panic + 雙擊取消 + 長按重啟 + factory reset
- ✅ **正確**:接聽電話 + Manual event + Server callback + 格化 SD(**沒 panic event**)
- 校正人:Kenny

## FCW 語音
- ❌ 之前答:"Frontal Collision Warning"
- ✅ **正確**:`"Keep distance"`
- 校正人:Kenny

## 疲勞分類
- ❌ 之前答:單一 Fatigue event
- ✅ **正確**:細分 Yawning / Nodding off / Sleepy 三個子事件
- 註:Yawning 真實狀態 → 看 [roadmap-vs-internal.md](roadmap-vs-internal.md)

## ADAS 範圍 vs DMS(初版校正)
- ❌ 之前答:ADAS 含 yawning / phone / smoking
- ✅ **正確**:DMS 是另一回事;ADAS 範圍詳細看下方 5/6 KB 校正

## ADAS 觸發時間 / Calibration 條件
- ❌ 之前答:60 km/h × 3 分鐘
- ✅ **正確**:**30 km/h × 3 分鐘 + 平坦少彎**
- 校正日:2026-05-05
- 校正人:Kenny
- 重要:**沒滿足就觸發 ADAS Failure**,語音 `"Can't detect the road level, ADAS off"`
- 應用:**[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 根因**,市區走停會反覆觸發

## G-Sensor 事件數
- ❌ 之前答:4 種(Harsh Braking / Cornering / Driving Impact / Parking Impact)
- ✅ **正確**:**6 種**(+ Harsh Acceleration + Rollover)
- 校正日:2026-05-05(MiAI Roadmap 揭露)
- 註:Harsh Acc / Rollover G 值門檻 ⚠️ 待 Mori 確認

## VLM Roadmap 時程
- ❌ 之前答:2H'2027(對內)
- ✅ **正確**:對內 Sheet 寫 2026 Q3,**對外用 Roadmap 2027**(Kenny 裁示)
- 校正日:2026-05-05

## AI sheet 隱藏 row 是「PM 介入空間」
- ❌ 之前答:hidden row + No PIC = PM 該扛
- ✅ **正確**:**hidden row = 團隊已決定不做**,別扛
- 校正日:2026-05-05
- 校正人:Kenny

## Yawning 真實狀態(2026-05-06 / 5/7 兩次校正)
- ❌ 之前答:Roadmap Basic tier 已有
- ✅ **5/6 會議揭露**:還沒給客戶用,內部測試中,效果不如預期。Fatigue config 下要加獨立 enable/disable 子選項
- ✅ **5/7 AI weekly 補**:夜間嘴部辨識效果不佳,加入「灰階(Grayscale)」影像重新訓練,並考慮 Server 端從「辨識嘴巴」改為「辨識整張臉」
- 對外口徑:「Roadmap planned, 內部測試中」**不能說「已有」**
- Yawning UI toggle 真實對應 ticket:**[VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)**(Lucy 5/6 開,assignee)

## Brian #11 OTA 17 個月 ticket 性質
- ❌ 之前答:stale(Brian 拖延)
- ✅ **正確**:**不是內部 stale,是 Akamai CDN 設定問題**
- 校正日:2026-05-06
- 校正人:會議錄音(Brian 自己說)
- 重要:**別在 Brian 面前主動提這個 ticket**

## #154 Server AI lane departure 為什麼 API 沒釋出(2026-05-07 再校正)
- ❌ v1 之前答:RD 沒做完
- ⚠️ v2(5/6 會議錄音 Brian 自評):「Q1 已 merge 但 label 沒設好,Brian filter 時漏 pick」
- ✅ **v3 真相(2026-05-07 讀 [VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722) comments + sub-tasks)**:[VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722) **本身有 label `vmx_2026Q2`**,sub-tasks 全 closed/resolved + jimmy 3/11 留「Server AI 已完成並 deploy 到 prod」+ parent ticket 仍 NEW。**不是 label 漏 pick,是 transition discipline gap** — RD 寫 comment 沒按 Open→Resolved button
- 校正日:2026-05-07(Comment 深掘後)
- 重要:**對 Brian 提 process improvement 從「transition 紀律」切入,不是「label 紀律」**
- 補充:**LDWS 5/7 完整故事**:Server-side([VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722))Q1 確實 deploy。但 device 端 YOLO Lane Detection 改善是 5/7 AI weekly 決議 Pending 暫緩 + 開新 ticket(編號待釐清)— 這是另一條工作

## ADAS 範圍(2026-05-06 KB 校正)
- ❌ 之前答:只含 FCW / LDW / Stop and Go / Tailgating
- ✅ **正確**:**FCWS / LDWS / Tailgating / Rolling Stop / Stop & Go(已 ship)+ Speed Sign(in development)**
- 校正人:KB 2026-05-06
- 註:詳細 5/7 補充 Speed Sign Flip 重訓在 [feedback_vmx_facts.md] memory

## Smoking 在 KB 真實狀態(2026-05-06 校正)
- ❌ 之前答:狀態待釐清
- ✅ **正確**:**KB 上 Smoking 標 (in development)**。對外可講「開發中」有官方依據
- 校正日:2026-05-06
- 註:Sheet row 隱藏 / Jira 多單 open 是內部狀態,不影響對外口徑
