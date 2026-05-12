# 2026-05-12 下午 · Δ Calibration(handoff 之後新進資料)

> 抓取時間:2026-05-12 下午
> 來源:Jira REST API(jira.navman.co.nz)/ Outlook(pokai.huang@mitacmdt)/ NotebookLM「神達VMX」notebook(44 個來源)
> 目的:對照 morning handoff 寫的 137 票 snapshot,看下午到目前為止有哪些 Jira / Email / 會議錄音的新訊號。

---

## 📊 Jira Δ vs 2026-05-12 morning snapshot

### 狀態變動(同樣 137 票)— 1 個
- **[VMX-7407](https://jira.navman.co.nz/jira/browse/VMX-7407)** New → **Resolved** · @righter.song · 5/12 13:25 · `Implement error handling for UVC cameras that do not support RAW frame output`(Single SKU CDR 上不支援 RAW Frame 的 UVC Camera 不再 stop recording)

### 5/12 同日新建 ticket — 27 個

#### 🔴 Lens Cover / Rollover / Blurring 線(直接連客戶 commitment)
- **[VMX-7459](https://jira.navman.co.nz/jira/browse/VMX-7459) New** · @lucy.sw.yen · `Disable Lens Cover Event` — **PreCise 客戶**用 VisionMax portal,需要 cover driver-facing camera 的 toggle(Configuration tab)
- **[VMX-7462](https://jira.navman.co.nz/jira/browse/VMX-7462) Open** · @lucy.sw.yen · `[UI/GUI] Rollover Event` — Rollover event UI/GUI 設計(承接 [VMX-7419](https://jira.navman.co.nz/jira/browse/VMX-7419) `[API] new event type: rollover` Resolved 5/7)
- **[VMX-7441](https://jira.navman.co.nz/jira/browse/VMX-7441) New** · @mori.jhang · `The Blurry feature can be turned on or off via the API in the portal` — Master Portal 加 switch 控制特定 Fleet 能否透過 API 設定 Blurring(VMX-7458 的 parent task)
- **[VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) New** · @pokai.huang · `[VisionMax] [GUI] Blurring control UI on Master/Fleet Portal for non-API customers` — Auto Sense 等 2,000+ VisionMax web UI 客戶用,Master/Fleet Portal 必須有 Blurring control UI(extends VMX-7441)
- 對外 commitment:對 **Cary / Wendy / Elvis(MiTAC AU)** 線 — Master Portal Blurring switch + UI 已交設計稿(Lucy 5/12 11:45 AM:Management > Fleet > Configurations > Device Settings > Enable Video Privacy Masking)

#### 🟠 AZUGA SmartLink 連續 ticket(hsinyi.chang 主開)
- **[VMX-7315](https://jira.navman.co.nz/jira/browse/VMX-7315) In Progress** · @hsinyi.chang · `New API implementation for AZUGA requirement`(2026-04-13 created)
- **[VMX-7329](https://jira.navman.co.nz/jira/browse/VMX-7329) New** · @hsinyi.chang · `[AZUGA SmartLink] ENGINE_ON / ENGINE_OFF - 引擎啟閉事件`
- **[VMX-7335](https://jira.navman.co.nz/jira/browse/VMX-7335) New** · @hsinyi.chang · `[AZUGA SmartLink] ACCIDENT_DETECTION - 撞擊事件(含 10Hz NMEA G-sensor)`
- **[VMX-7354](https://jira.navman.co.nz/jira/browse/VMX-7354) In Progress** · @jack.fl.chen · `[AZUGA SmartLink] event / trip 新增 vehicle 欄位上傳`
- **[VMX-7373](https://jira.navman.co.nz/jira/browse/VMX-7373) New** · @hsinyi.chang · `GPS 未定位時相關欄位(事件 / GPS)內容處理規則`

#### 🟢 VisionAgent (iOS/AOS) 連續 fix(james.cw.chou + lucy.sw.yen)
- **[VMX-7447](https://jira.navman.co.nz/jira/browse/VMX-7447) In Progress** · @james.cw.chou · `[VisionAgent] [AOS] Notice Modal GUI Style Issue`
- **[VMX-7449](https://jira.navman.co.nz/jira/browse/VMX-7449) Resolved** · @lucy.sw.yen · `[VisionAgent] [AOS] Device List 難控制`
- **[VMX-7454](https://jira.navman.co.nz/jira/browse/VMX-7454) Resolved** · @lucy.sw.yen · `[VisionAgent] [AOS] 載入更多資料時的畫面閃爍`

#### 🔵 5/12 同日 Resolved(對外可講「✅ 已 ship」)
- **[VMX-7287](https://jira.navman.co.nz/jira/browse/VMX-7287) Resolved** · @lynn.yl.huang · `[K265][Region] Build VisionMax 2026Q1 Region (260420)` — K265 2026Q1 region build 完成,對 Vinicius(Platform Science)5/12 OTA 直接生效
- **[VMX-7326](https://jira.navman.co.nz/jira/browse/VMX-7326) Resolved** · @leo.tsai · `[Crashlytics] EngineManager.notifyShutdown - AssertionError`
- **[VMX-7388](https://jira.navman.co.nz/jira/browse/VMX-7388) Resolved** · @elvis.tran · `Request for inventory report with simcard ICCID`
- **[VMX-7395](https://jira.navman.co.nz/jira/browse/VMX-7395) Resolved** · @spencer.su · `[API] 調整 coach able 判斷條件`
- **[VMX-7460](https://jira.navman.co.nz/jira/browse/VMX-7460) Resolved** · @cary.lo · `MAU Device Provisioning: SEEING MACHINE AU US Master`
- **[VMX-7463](https://jira.navman.co.nz/jira/browse/VMX-7463) Resolved** · @spencer.su · `[API] [Permission] device controller actionSd`
- **[VMX-7103](https://jira.navman.co.nz/jira/browse/VMX-7103) Closed** · @elvis.tran · `Camera not recording new trips / reporting to the server`(2026-01-20 created)

#### 🟡 5/12 新 Bug / Issue
- **[VMX-7461](https://jira.navman.co.nz/jira/browse/VMX-7461) New** · @elvis.tran · `Camera is not uploading any trips or event videos`
- **[VMX-7464](https://jira.navman.co.nz/jira/browse/VMX-7464) New** · @chiehli.wang · `Implement a Cloud Worker responsible for overlaying and rendering CDR videos with debug logs`
- **[VMX-7465](https://jira.navman.co.nz/jira/browse/VMX-7465) New** · @neil.kuo · `Error in assigning device to fleet`(同 [HAWK-584](https://jira.navman.co.nz/jira/browse/HAWK-584))
- **[VMX-7466](https://jira.navman.co.nz/jira/browse/VMX-7466) Open** · @hsinyi.chang · `Add video duration info to SD card video filename`
- **[VMX-7467](https://jira.navman.co.nz/jira/browse/VMX-7467) New** · @jack.fl.chen · `Test Lab: OBD2 / SmartCableVehicleData simulator dashboard`
- **[VMX-7468](https://jira.navman.co.nz/jira/browse/VMX-7468) New** · @leo.tsai · `Improve the IOSix dongle firmware update process`
- **[VMX-7355](https://jira.navman.co.nz/jira/browse/VMX-7355) New** · @lynn.yl.huang · `[K265][MAU] Base Image OTA upgrade failure`
- **[VMX-7380](https://jira.navman.co.nz/jira/browse/VMX-7380) New** · @luke.cheng · `改善 Add to Coaching Material Switch 可否被使用的邏輯`
- **[VMX-7387](https://jira.navman.co.nz/jira/browse/VMX-7387) New** · @spencer.su · `Add the Video Cradle and Video Hub information to the Configuration tab`
- **[VMX-7390](https://jira.navman.co.nz/jira/browse/VMX-7390) New** · @luke.cheng · `Simcard ICCID history is showing recall history`
- **[HAWK-450](https://jira.navman.co.nz/jira/browse/HAWK-450) New** · @steve.rudzik · `Firmware updates delay current installations/activations - any ideas to circumvent?`(2025-11-11 created — 半年前 reopen 5/12)

---

## 📧 Outlook Δ(handoff 之後新進信件)

### 5/12 上午 5 封新信
1. **lucy.sw.yen [JIRA] VMX-7441**(11:47)— Lucy 在 ticket 內 cc Kenny:「此 7458 與 Master 層級所做的改動,我在 Management > Fleet > Configurations > Device Settings 新增一個設定項目:Enable Video Privacy Masking。請先 review 這個設計是否合乎需求」+ Screenshot 2026-05-12 at 11.41.25 AM.png (577×361)。**Action**:Kenny 需 review 設計稿
2. **jimmy.jy.huang AI Deployment Weekly Meeting**(11:04)— 確認 5/12(週二)11:00-13:00 在 A0512 開會 · 受邀:Eric H / Vincent Ho / Joy Qiu / Jack Liu / Brian / Chiehli / Jonathan / Kenny · 會前要更新工作項目最新狀態到 [Google Sheet](https://docs.google.com/spreadsheets/d/1DKQByU7Z...)。**Action**:Kenny 已參加(會議結束時間 13:00)
3. **anila.hsu(MIC)2026/04 新進同仁宜睿電子禮券 APP 綁定**(10:46)— HR 通知,需綁定 Edenred App。公司編號 `MITACMGW` + 員工編號 + 生日後 4 碼。**Action**:Kenny HR 雜事,非工作項
4. **lucy.sw.yen [JIRA] VMX-7458**(10:33)— Lucy 問 Kenny:「Is this the same task as VMX-7441?」(Kenny 5/12 10:51/10:54 已在 ticket 內回覆:7458 extends 7441,7441 = Master 層 switch、7458 = Fleet 層 UI 加一層)
5. **righter.song RE: VisionMax Account Device Listing**(10:08)— 給 **Vinicius(Platform Science)**:K265 OTA profile 已設好,請保持 K265 連網,OTA 下載完後 ACC OFF 即可更新。對外:K265 2026Q1 region 5/12 開始 push(配 [VMX-7287](https://jira.navman.co.nz/jira/browse/VMX-7287) Resolved)

### 5/11 晚間 新信(handoff 沒涵蓋)
6. **simon.wu(NA Regional Sales Director, MITAC AOTBC | Magellan)RE: Fleet portal manual draft 1**(5/11 23:52)— 對 Brian 的 Fleet Portal 手冊 R02 draft 給 page-by-page review:
   - Page 5 Map Overview / Page 15 App Display / Pages 25-26 Distracted(speed ≥ 20 km/h 才觸發)/ Page 30 Device Usage / 拼字一致化:log-in→login, live-view→live view, start-up→startup, shut-down→shutdown
   - **Event Map 要進 user guide**(Phil Soung 寫的版本還沒加)— **Event Map 功能要回歸 Fleet Portal**(luke.cheng 5/11 14:20 已附 2 張 screenshot,Map view + Video view 雙 view)
7. **Vinicius Francisquinho Re: Vision Max APIs**(5/11 22:03)— 對 Kenny 5/11 02:31 交付的 JS Live View lib V1.0.4(`https://www.visionmaxfleet.com/lib/vmRTC/1.0.4/...`)回:「Thanks, I will start running some tests with it」 — **handoff 內「Vinicius Live View JS lib 待回」項可結案,Vinicius 已收貨+開始測試**

### 5/9 仍 active(handoff 已寫,但補一筆)
- **brian.chienlee FW: Honeywell MiddleEast CDR opportunity**(5/9 10:09)— Brian forward Stark Yang(Director)5/8 23:27 的 mail loop:5月份 6K 量 single batch 銷售討論;Stark 要求 Kenny 等內部 5/11 開會討論。Brian 點名:Spencer / Mori / Pokai。**Status**:已有 `case-learning/honeywell-me-cdr-opportunity.md`

---

## 🎙️ NotebookLM「神達VMX」新資料(44 個來源)

### 5/11 AI Weekly 完整內容 → 已寫進 [`meetings/ai-weekly-internal-roundup.md`](../meetings/ai-weekly-internal-roundup.md)(series 檔)

> **2026-05-12 校正**:Kenny 規則「每週循環會議用 **series 檔**追加,不每場開新 HTML」。`meetings/ai-weekly-internal-roundup.md` 是內部 AI Weekly 系列的 SSOT,5/11 + 5/7 + 未來新場都進這個檔。Model 11P/11L/26/V14 對應 / 6/2 Fix Version 三大死線 / 5/15 Beta 前置 / Regression Risk 全部在那邊。

### 新增的 NotebookLM 來源(repo 對應 meeting note 狀態)
- 🎙️ **5-11 ai weekly meeting.m4a** → ✅ 已 ingest 進 `meetings/ai-weekly-internal-roundup.md` § 2026-05-11
- ❌ **5-10 Syncup with MAU for API questions** — 5/10 MAU API 同步會議錄音,**repo 沒 meeting note**(待還原)
- ❌ **5-8 Chat for API with MAU** — 5/8 Chat for API,可能跟 `meetings/2026-05-08_syncup-cary-elvis_meeting-record.md` 同場(待確認;若是同場則 supersede)

### 跟 Blurring 相關的 ticket NotebookLM 提到
- **[VMX-7025](https://jira.navman.co.nz/jira/browse/VMX-7025)**:用來下載特定影片進行 Blurring 測試與追溯(repo 沒這票 — 不在 137 內)

---

## 🚀 Action Items(下次 session / Kenny 接手)

1. **Lucy 5/12 11:45 設計稿 review** — VMX-7441 Master Portal Blurring switch 設計(Management > Fleet > Configurations > Device Settings > Enable Video Privacy Masking)
2. **Vinicius JS lib V1.0.4 測試 follow-up** — 收 Vinicius 測試結果回饋(他 5/11 22:03 確認開始測試)
3. **AI Weekly Sheet 自己工作項更新** — Jimmy 5/12 11:04 信要求,每次會議前更新
4. **5/10 MAU sync meeting note** — 從 NotebookLM 音檔還原 → `meetings/2026-05-10_mau-api-syncup.md`(待做)
5. **5/11 AI Weekly meeting note** — 從 NotebookLM 音檔還原 → `meetings/2026-05-11_ai-weekly.md`(待做)
6. **6/2 Fix Version 全名單對外口徑** — LDWS API + Lens Cover + Model 26 全要在 6/2 release,內部要對 Sue / Lucy / Eric / Jieli 確認 ETA
7. **Event Map 回歸 Fleet Portal** — luke.cheng 5/11 提的 Phil Soung 手冊更新工作(Map view + Video view 雙 view 已有 screenshot)
8. **Honeywell MiddleEast CDR 5/11 內部會** — 已過了 5/11,需 Kenny 補充會議結果(若有)

---

## 📌 引用快查

- 完整 Jira snapshot(164 票 = 137 舊 + 27 新):`jira_data/jira_tickets_snapshot_2026-05-12T15.json`
- 原 morning snapshot:`jira_data/jira_tickets_snapshot_2026-05-12.json`
- Outlook 抓取人:Kenny 本機 Outlook (classic) + 新 Outlook for Windows(同步)
- NotebookLM URL:https://notebooklm.google.com/notebook/a3aad3ec-ecf3-4468-a0d9-13a6a18359c7(notebook 名「神達VMX」,44 個來源)
- 抓取方式:Chrome MCP(Browser 1, Kenny 本機)→ Jira REST API + Outlook computer-use + NotebookLM Chrome MCP
