# 內部利害關係人地圖

## MiTAC 端

| 領域 | 人 | 職責 / 關鍵議題 |
|------|---|----------------|
| **Software Head** | **Brian** | VisionMax / Cloud / Camera App / AI 整體;團隊 ~20 人;Jira dashboard 主導者 |
| **High-level KPI 拍板** | **Steve** | **5/8 QBR 揭露**:VMX 2026 全年 subscription KPI = **100,000 台**,目前差 15K(Brian 5/9 信)。Kenny 不直接對接,**內部 KPI 不對外** |
| **Video Telematics Director** | **Stark Yang(楊永吉)** | 5/8 23:27 啟動 Honeywell ME CDR 新案,負責戰略 + tier pricing 拍板。也在 Vinicius / PS 案 thread 內監督 |
| **HW PM** | **Kevin Yhwang(王耀賢)** | Honeywell ME 案 sample / cable / mounting kit |
| **Marketing PM** | **Phil Soung(宋介恂)** | 5/8 14:34 出 VisionMax Fleet Portal R02 draft 1.pdf 第一版 manual(9MB),下週開始做 Master Portal manual。Kenny 要 review |
| **RD 對外技術 PM** | **Conant Ho(何肇峯)** | PS 案技術窗口;sample equipment 訂單對接;SDK / CDR roadmap 對外 share |
| **RD inventory / FW Engineer** | **Righter Song(宋祐全)** | 設備 inventory + image flashing 限制(K265 LM 版 SD update 限制 = 他揭露)|
| **Account Sales Manager** | **Paul Lee(李世博)** | PS 主對接 sales;Honeywell ME 主對接 sales(Stark 點 task)|
| Camera App | Hsinyi, Jack, Leo | 設備端錄影 / UI / 紅色按鍵 |
| AI Inference | **Jimmy**, Vincent, Eric | ADAS / DMS 模型、訓練、validation。**5/7:Vincent 角色擴大,加入飲食誤判 7000+ Edge case 重訓主導** |
| AI Inference 補 | Jieli, Andy, **Jay** | Yawning / Quantatec / Lens Cover / DMS Golden Case / Speed Sign 重訓(Jay 5/7) |
| **Cloud / API team lead** | **Spencer** | **校正(5/7):Spencer 是 Cloud / API team lead,扛睜眼率 API 全鏈路驗證 6/2**(原 memory 誤把 Adonis 當 Cloud lead)|
| Cloud Backend 一般 | Neil | Event API / DB / portal serving |
| MiDM / OTA | RD 主管 | 韌體推送 / config(**最高風險區**:Custom ID 派錯設備變磚) |
| 硬體規格 | **Mori** | K-series / G-Sensor / 200Hz / 紅色按鍵 / Rollover detection([VMX-7194](https://jira.navman.co.nz/jira/browse/VMX-7194))|
| 測試車隊 | **Elvis** | NAVMAN-AU,新功能驗證 / 開 Smoking accuracy 單([VMX-7324](https://jira.navman.co.nz/jira/browse/VMX-7324))|
| **Server AI 應用層** | **Adonis** | Server AI confidence threshold / blurring on-demand / pre_event_message / Add box around event([VMX-5909](https://jira.navman.co.nz/jira/browse/VMX-5909))— **不是 Cloud lead** |
| **Webservice / Blurring API** | **chiehli.wang(王傑立)**| [HAWK-573](https://jira.navman.co.nz/jira/browse/HAWK-573) / [HAWK-577](https://jira.navman.co.nz/jira/browse/HAWK-577) / [HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578) / SQS retention 改 14 天(5/6 ping spencer.su)/ Health check 機制 |
| Front-end | **Lucy** | UI 設計 / 軌跡顏色 / Severity 等級 / **Yawning UI toggle = [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(5/6 開)** / Rollover UI |
| Speed Sign 模型 | **woody.lee** | [VMX-7430](https://jira.navman.co.nz/jira/browse/VMX-7430)(exit ramp)/ [VMX-7431](https://jira.navman.co.nz/jira/browse/VMX-7431)(LED sign)5/6 新開 |
| MiTAC AU 業務端 | **Wendy Hammond** | wendy.hammond@mitac.com.au · MiTAC AU(澳洲)· 跟 Cary 同部門 · 4/30 起信推 HQ「BMS feature 應跨 reseller reusable」· 5/5 訴求「conception stage 早期介入」· thread = "RE: VMX Roadmap Update and Explanation \<PASSENGER BLURRING\>" |
| GA 分析 | Luke / Sacer | 5/6 起 Lucy 用同一 GA 帳號 |
| 韌體 / Akamai 中介 | Tony | OTA #11 真因 — 跟 Akamai 之間轉述 |

## 海外客戶

| 客戶 | 整合方式 | 對接人 | 重點 |
|------|---------|--------|------|
| **Azuga** | Custom SDK | (待補) | 21 個新 API 排隊 / SmartLink 系列 ticket |
| **Bridgeron** | API integration | (待補) | 整合會議每週 |
| **Mainfreight** | Web Platform 測試 | (待補) | 測試中 |
| **BMS** | API + 客製 | (待補) | 雙版本同步戰略對象 / 200Hz / Smoking config / [VMX-6920](https://jira.navman.co.nz/jira/browse/VMX-6920) ✅ Closed 2026-03-09 (Jimmy) |
| **Platform Science (Vinicius)** | 評估中 | Vinicius (Engineering Director) · vinicius.francisquinho@platformscience.com · cc 內部 paul.sp.lee / conant.ho / righter.song / stark.yang / brian.chienlee | US · 5/7 已成功 connect VisionMax(原以為 cable 問題,實為 APN)· **5/7 testing plan**:Evo K265 + 2 side cam + 1 rear cam + InCab Display,後續測 **K165 single lens** + K245 Video Hub(K246 Orion future)· 在等 cable 資訊訂購 sample equipment |
| **CONNECTSOURCE** | 評估中 | Cary Lo (MiTAC AU) + Wendy Hammond (MiTAC AU 業務端) | Passenger blurring 需求 · 起源 = Wendy 4/30 信推 BMS feature reusable / Brian 5/4 承諾 Q2 2026 update,7月給 CONNECTSOURCE / 5/7 Cary 跟進 |
| **Quantatec** | 客製 | (待補) | Camera obstruction 系列([VMX-6983](https://jira.navman.co.nz/jira/browse/VMX-6983) / 7427) |
| **Webfleet / Bridgestone / Azuga(三客戶聯動)** | BMS Hawk 平台 | Sebastian Schneider (Webfleet), Martin Rothe (Webfleet), Jakob Mund (Bridgestone), Sirphi Manivannan (Azuga) | **[HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) Lens Cover detection 改設計**(取消 speed/calibration 限制),**Eric H 5/8 13:38 確認 6 月 release**。三客戶共用同一 Improvement,Flow 1 Bridgestone 偏好 |
| **Honeywell MiddleEast(新案)** | CDR 採購 + white-label VMX portal | Honeywell ME 端待補 | **2026-05-08 23:27 啟動**:K220 × 1 + K265 × 1 樣機(5/11),後續 K220 × 4 + K265 × 4 set。第一單 5 月 6K pcs。要做 white-label Honeywell logo VMX portal + 機殼貼紙。Kenny 對接 VMX setup 線 |
| **HDFE** | (待補) | (S 那邊) | 2026-05-06 抱怨 Q1 Events Page UI 變動 |
| **LB Technology** | (待補) | (待補) | Plow PTO / Posted Speed Alert |
| **Rastrac** | (待補) | (待補) | False Speed Event([VMX-7317](https://jira.navman.co.nz/jira/browse/VMX-7317))|
| **Seeing Machines** | (待補) | (待補) | Rollover detection 需求([VMX-7194](https://jira.navman.co.nz/jira/browse/VMX-7194)) |
| **Suvio** | 評估中 | (待補) | 影像 + 客製語音 |
| **DSNY** | (待補) | (待補) | Camera Pilot Project / RTR+Camera |

## 每週固定會議

| 會議 | 時段 | 性質 | 重點 |
|------|------|------|------|
| **Azuga AI weekly** | 每週三 15:30 – 17:00 | 客戶端 | 5/6 揭露 Lens Cover 標準版規格 / 飲食誤判少數提及 |
| **內部 AI weekly** | 每週二、四 10:00 – 12:00 | 內部 | 🆕 **5/11 最新場揭露**:Model 11P/11L/26/V14 對應 + **6/2 Fix Version** 三大死線(LDWS API + Lens Cover + Model 26)+ 5/15 Beta 前置 → 詳細在 [`meetings/ai-weekly-internal-roundup.md`](../../meetings/ai-weekly-internal-roundup.md)(series 檔,新場追加 H2 不開新 dated 檔)|
| **Field-side requirements sync** = **Quater tracking review** = **Q2 Tasks meeting**(同一場三個名稱)| 隔週三 10:00 – 12:00 | 跨團隊 | Quarter 追蹤 / Q2 Tasks 進度 |
| **Bridgestone (BMS) 整合** | 隔週二 15:30 – 17:00 | 客戶端 | BMS 雙版本同步戰略對齊 → ⚠️ **5/11 校正**:已從雙軌 → 單軌(<a href="https://jira.navman.co.nz/jira/browse/HAWK-582" target="_blank">HAWK-582</a>),Eric H 5/8 confirmed 6 月 release |
| ~~Q2 Tracker review(Brian 主持,5/6)~~ | — | ❌ 已過期(5/6 已開) | 結論已記在 [meetings/2026-05-06_q2-request-review_meeting-record.md](../../meetings/2026-05-06_q2-request-review_meeting-record.md) |
