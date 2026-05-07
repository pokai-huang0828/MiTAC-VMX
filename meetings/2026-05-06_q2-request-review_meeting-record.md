# 2026-05-06 Q2 Request Management Review — 會議完整紀錄

- **日期**:2026-05-06(Tue)
- **主持**:Brian(Software Head)
- **性質**:Q2 Request Management Tracker review + 即時客訴處理
- **整理視角**:Kenny PM 角度,逐 item + 戰略洞察
- **來源**:會議錄音 transcript + Sheet 變動 diff + Jira 交叉驗證
- **整理人**:Kenny Huang(黃柏凱)

---

## 一頁總覽

| 項目 | 數字 |
|------|------|
| Sheet visible 變動 | 28 → 55(filter 放鬆) |
| Status 變動 | 12 筆 |
| Q1 同步缺口收尾 | **4 件 Resolved**(VMX-6754 / 7029 / 7161 / 7162) |
| 新增 ticket | 4 筆(#205~#209) |
| 推進的關鍵 | Rollover Discussion → In Process / Mori 接 |
| Header 推遲 | Q1 Deadline 4/2 → **Q2 Deadline 6/30** |
| 緊急 hotfix | Single SKU + UVC crash(Simon 跳腳) |

---

## Part A — 議程處理順序(逐 item)

### A1. #126 Yawning Detection(HAWK-332)

**狀態**:Q1 → Q2(承認延期)

**會議紀錄**:
- 客戶端**還沒放出去**,目前都關起來
- 內部測試效果不如預期,需要更多 RD 內部測試
- 要在 user TR(test)賬號上開,看正常開車情況下會不會誤觸發(例如講話)
- 自己內部要做 false positive 觀察

**重要決策**:
- **Fatigue config 下要加獨立 enable/disable 子選項**(原本只有眼睛偵測)
- UI 需要 Lucy 配合設計
- 測試可以先進行,UI 之後再追

**對外影響**:
- ⚠️ MiAI Roadmap 對外版列「Basic tier 已有 Yawning」**直接矛盾** — 對任何客戶 / sales 不能再講「已有 Yawning」,改成「Roadmap planned, 內部測試中」

**會後 Action**:
- [ ] Kenny:更新 memory 把 Yawning 狀態校正成「Roadmap 對外版 / 內部測試中」
- [ ] Lucy:UI 開關設計
- [ ] Jieli:RD 內部測試 + user TR 賬號驗證

---

### A2. #162 Fleet Portal Events Page Optimization(VMX-6754)

**狀態**:In Process → **Resolved**(Q1 deploy 出去)

**會議紀錄**:
- 「這應該已經結束了」
- Q1 已 deploy

**Sheet ↔ Jira 同步缺口已修復** ✅(這是 Kenny 會前抓出的 4 件之一)

---

### A3. #165 SD Card encryption(VMX-7029)

**狀態**:In Process → **Resolved**

**會議紀錄**:
- 「加密的他們也出去了,也做好了」
- 現在只要設定打開就會 work
- 要再確認 configuration:啟用後是否會自動生效
- 目前只有 API 可控制設定

**Sheet ↔ Jira 同步缺口已修復** ✅

---

### A4. #187 / #188 Mori 兩件(VMX-7161 / VMX-7162)

**狀態**:In Process → **Resolved**

**會議紀錄**:
- 「這條可以先關」
- 「先過 OTA function 再做下面」

**Sheet ↔ Jira 同步缺口已修復** ✅(Kenny 會前點出,Mori 兩件都已交付)

---

### A5. #11 Brian 自己的 Fleet Portal VMX OTA(2024/11/28,17 個月)

**狀態**:依然 In Process(沒收)

**會議揭露真因**:
- **不是 RD 做不到 — 是 Akamai CDN 設定問題**
- JSON 設定檔放在 AWS / Akamai 上,**CDN PG(purge)失效或未更新**,設備一直拿到舊 JSON
- Tony 在跟 Akamai 之間轉述需求,可能 Akamai 設定錯
- Brian:「這是小事,影響只是大家晚一點收到新檔,不會下載錯東西」
- Brian:「他們每年花 200 萬買的 support 就處理吧」
- Brian 計劃:今天找 Tony 下來把這件事搞定,有 ticket 就轉給他

**PM 觀察**:
- ✅ Kenny 會前判斷正確 — **Brian 自己不在意**,因為他知道根因在 vendor
- ⚠️ memory 該記:**Brian #11 不是內部 stale,是外部 vendor 卡住**,別在他面前主動提

---

### A6. #178 MySQL upgrade before End of July, 2026

**狀態**:In Process(維持)

**會議紀錄**:
- AWS EOL 7 月底
- Spencer plan 5月底 / 6月提供給 BMS
- 寫文件講升級路徑

**會後 Action**:
- [ ] Spencer:5月底完成 image,apply 到 VisionMax 環境
- [ ] 6月 提供給 BMS + 升級文件

---

### A7. #154 Server AI lane departure model(VMX-6722)

**狀態**:Q2 → **Q1**(往前拉,因為 Q1 已 merge)

**重大發現 — Process Gap**:
- VMX-6722 Q1(3/31)已合併
- 4/7 第二次 APP release
- **但 API 沒被 pick 進去** = label 沒設好
- Brian 自評:「label 沒被 pick 到,我在 filter 的時候漏掉它」
- 「對 AI 來講,如果 G 掛在你那邊,你很晚更新或者沒下 label,我最後 filter 時可能就會漏掉」

**Brian 戰略翻案 — VMX/BMS 同步**(整場會議最戰略級的議題):
- 過去:VisionMax 不給 fleet 改 AI 參數(怕客戶改壞),BMS 給改
- 結果:兩套 codebase / API 文件 / 維護
- **Brian 想要翻案**:「**過去的決定就過去的決定。未來我想要走向兩邊同步實作**」
- 「客人改壞了就他改的啊,他自己關起來就好」
- 配套:API 加保護避免亂改參數
- 沒人反對 → Brian 要往這方向努力

**Resource 影響**:
- 其實 Q1 出去就已經有(Q1 Cabinet APP merge 進去了)
- 預設打開,客戶不能改(沒有 API)
- BMS 現在這版也沒 API 可控制
- 文件 / Codebase 保護需後續更新

**會後 Action**:
- [ ] Brian:後面要做的事 — VMS 可改的扣弄進來 + 文件更新
- [ ] **PM 切入點**:幫 Brian 做 Q2 merge label sweep,建立 sync checklist 防止再漏 pick

---

### A8. #164 Modify Safety Reports(VMX-7083)

**狀態**:Discussion(維持)

**會議紀錄**:
- Bug 是 PDF 報表內容沒對齊網頁顯示
- 5/6 Luke 已埋 GA(上週)
- 上週開始確實沒什麼人用,但時間太短,再等
- **延長觀察期至一個月**,如果真的沒人用 export 功能 → 直接拿掉這個 task,不修
- Server 開啟時間長,先用 GA 觀察使用需求

**重要釐清 — Report 雙重定義**:
- 一個是真的轉成 Excel(讓客戶下載)
- 一個是 Table list(直接在網頁上看的)
- 雙方對 "Report" 定義有落差,要釐清

**PM 觀察**:
- GA 不只看 page view,要看 visitor / device / browser
- Lucy 用同一個 GA 帳號(Sacer 也有提供)
- 報表難看,進去會迷路一陣子

**會後 Action**:
- [ ] Brian / Kenny:跟客戶釐清要的是 Excel export 還是 Table list
- [ ] Luke:再觀察一個月

---

### A9. #168 Add box around event(VMX-5909)+ 模糊功能架構

**狀態**:In Process(維持)/ 5/6 確認完成後測試

**會議紀錄 — 模糊功能架構討論**:
- 模糊在 Server 端做(後製)
- 客戶(BMS / 自家)強烈要求模糊功能(隱私)
- **demand request 模式**(不是每個影片都做,Q2 只做 FCWS)

**三版本影片可能共存**:
1. 原始 video
2. 模糊 video
3. Debug view(AI 視角)

**UI 設計缺口**:
- API 端可以支援
- **Master/MAU 加 API 開關**(讓 fleet manager 控制誰可以用)
- 模糊不在 fleet portal 上顯示(維持 API 操作)
- **缺一個「任務完成主動通知」UI 機制** — UI user 不知道做完了,API user 沒問題

**會後 Action**:
- [ ] Lucy:模糊功能 UI 設計 + 任務完成通知機制
- [ ] Adonis / Spencer:API + Master 端開關設計

---

### A10. #174 Remote Playback supports audio(VMX-7014)

**狀態**:Feasibility → **Pending**

**會議紀錄**:
- 5/6 等 Simon 實際需求再執行
- 等 BMS Simon 進來

---

### A11. #176 Fleet Mobile APP - Push notification(VMX-7030)

**狀態**:Pending(維持)

**Q2 計劃**:
- 5月底 image 完成
- apply 到 VisionMax 環境
- 6月 提供給 BMS + 升級文件

---

### A12. #182 Manually request timestamp from playback(VMX-7132)+ 舊 Playback Sunset Plan

**狀態**:In Process(UI Spec 4/10 已釋出)

**重大決策 — 舊 Playback 頁面 Sunset Plan**(經典變更管理案例):
- 系統有 **#135 舊 Playback 頁面**預計關閉
- **預計 Q3 9月底正式移除**
- **Q2 動作**:
  - 在舊頁面上壓**紅色終止文字**(具體日期)
  - 加入紅色驚嘆號預告
  - 持續用 GA 追蹤還有多少人在使用
- 4 個月 grace period(現在 → 9月底)
- 之後正式跳 alert

**對 Hub 第三 tab「承諾層次框架」直接命中**:
- 重大變更不是「強制日期切換」(高風險)
- 用「資訊更新頻率」(極低風險)+「里程碑」(中風險)取代
- 4 個月 BT(beta)期 = AWS / Box / Atlassian 經典做法

**會後 Action**:
- [ ] Lucy:舊 Playback 紅色預告 UI
- [ ] Kenny:把這個 sunset 流程記成 PM 框架(對應 Hub 第三 tab)

---

### A13. #185 LB Plow PTO(VMX-7149)

**狀態**:5/6 Andy testing,從 wait Simon detail 推進

**會議紀錄**:
- 今天測試,應該今天測試完成
- ✅ Kenny 會前抓的「Simon 卡 detail」推進

---

### A14. #190 Vehicle rollover detection(VMX-7194)

**狀態**:Discussion → **In Process** ⭐ Kenny 會前 brief 直接命中

**會議紀錄**:
- Mori 接手 assignee
- Reporter Elvis(NAVMAN-AU)
- CC:Cary Lo(AUS)
- 描述:「Seeing Machines 客戶要求」
- **5/6 Need to add UI**
- Sheet 加新註

**對應 Roadmap**:
- MiAI Roadmap G-Sensor 第 6 種事件
- VMX-7194 detection + VMX-7419 [API] new event type rollover + VMX-7254 cloud integration
- 三件配套推進

**會後 Action**:
- [ ] Mori:detection 實作
- [ ] Lucy:UI 任務(Kenny 跟 Lucy sync UI 時可以一起)

---

### A15. #194 IOSix dongle data(VMX-7316)

**狀態**:In Process

**會議紀錄**:
- 計劃 5/22 完成
- 需求一直在變,最近都在趕
- 規格大致定了
- 剩約 2-3 週時間
- VisionMax 跟 BMS 都要做

**5/22 Configuration 議題**:
- Simon 那邊希望事件發生時可以吐 200 Hz G-Sensor 數據
- 目前只能 50 Hz
- ATV / API 設定
- 預設打開,Smartlink 有接功能就打開 / 沒接就關

**會後 Action**:
- [ ] Mori:確認硬體能否 200 Hz
- [ ] Andy:跟 Mori 確認

---

### A16. #197 UVC + road-facing side-by-side(VMX-7224)

**狀態**:5/6 等 IOSix 完成後才開始做

⚠️ **Sheet link 中 VMX-7147 是錯的**(VMX-7147 真實是「Camera recording no longer exists」)→ 會後 Slack 確認

---

### A17. #199 BLE Beacons(VMX-6782)

**狀態**:In Process → **Resolved** + 5/6 已完成提供給客戶測試

⚠️ **Sheet 領先 Jira**:
- Sheet 寫 Resolved
- Jira 仍 **Open**(Fix Version: CameraAPP_202605)
- Owner:joe.lien(連家興 - MDT)

---

### A18. **🚨 緊急議題:Single SKU + UVC Crash**(會議中插入)

**問題**:
- 設備 single camera 設定 + 外接 UVC(用於 DMS)
- 系統不支援這組合,**直接 Crash 當機**
- 客戶 Simon 已遇到,在跳腳

**根因**:
- single camera 預設 UVC 是輸入
- UVC 不支援輸入 → 一直 No FR → 最後關掉

**決策**:
- **必須立刻在現在 branch 加判斷邏輯**(不開新 branch)
- 沒資源就退回單機處理
- 必須立刻給出 Hotfix
- 上週開了新單做這件事

**會後 Action**:
- [ ] PM(Kenny):確認 hotfix 對應 Jira ticket(否則該主動建單)
- [ ] Camera APP team:緊急 patch

---

### A19. HDFE 客戶 UI 抱怨(會議結尾)

**問題**:
- Q1 改 Events Page 後客戶 HDFE 抱怨
- 點擊次數變多 / 找特定事件變難
- 客戶要切回舊版開關
- 客戶喜歡舊版 list 切法(可分十種 score)

**Brian 評估 — 引入 Beta 模式 PM 框架**:
- 「**未來重大變更時可以考慮 BT(beta)期**」
- 參考 AWS / Box / Atlassian:「告訴你新介面試用,給你時間,再正式 deprecate」
- 不一定要滿足 HDFE,但未來重大變更時做這個

**對 Kenny Hub 第三 tab「承諾層次框架」直接呼應**:
- 重大變更 = 高風險承諾
- 解法 = beta period + transition 期 + sunset 流程

**會後 Action**:
- [ ] Kenny:把 Brian 想引入的「beta 模式」具體化成 PM proposal(對應 Hub 第三 tab)

---

### A20. 新增 4 筆 ticket

| # | Task | Jira | Status | Requester |
|---|------|------|--------|-----------|
| 205 | Add sim card ICCID to inventory | VMX-7389 | New | Elvis |
| 206 | Update UI text for New Fleet Account | VMX-7391 | New | Elvis |
| 207 | UVC RAW frame error handling | VMX-7407 | New | Simon |
| 208 | 馬賽克功能在 master 加 API 開關 | (no link) | New | (內部) |
| 209 | New Role as Viewer only | (sheet 寫 VMX-7407,**應該是 VMX-7088**) | New | (?) |

⚠️ #209 Sheet link 錯,實際應該是 VMX-7088(Viewer only role)

**#209 Viewer only 權限討論**:
- 不能 Delete / Edit / Download / Retrieve
- 不能 Configuration
- Brian 質疑:「detail 都不能看了嗎?真的嗎?」
- 從 PM 角度看 download 包含 browser 看 video,要釐清

**會後 Action**:
- [ ] Kenny:跟 Brian 確認 Viewer 角色「detail 能不能看」實際定義
- [ ] 修正 sheet #209 的 Jira link 錯誤(從 VMX-7407 → VMX-7088)

---

## Part B — 戰略級議題(會議揭露,sheet/jira 看不到)

### B1. ⭐ Brian 翻案:VMX/BMS 同步戰略

**現況**:
- VisionMax 不給 fleet manager 改 AI 參數(預設打開,沒 API)
- BMS 給 fleet manager 改
- 兩套 codebase / API 文件 / 維護成本高

**Brian 戰略**:
> 「過去的決定就過去的決定。未來我想要走向兩邊同步實作。」
> 「我們給 BMS 改,我們自己也給人家改吧。」
> 「客人改壞了就他改的啊,他自己關起來就好。」

**配套**:
- API 加保護,拒絕不該的參數送進來
- 文件 / Casebase 都要改

**時程**:6 個月內會發生的架構決策

**PM 跟進角度**:
- API 文件對齊
- Fleet portal UI 加開關
- 客戶溝通(從「不能改」變「能改」要小心訊息)

---

### B2. ⭐ Yawning Detection 真實狀態 vs 對外 Roadmap

| 角度 | 內容 |
|------|------|
| MiAI Roadmap 對外版 | Basic tier(2025 Expansion)= 已 ship |
| 會議揭露內部狀態 | 還沒給客戶,內部測試中,效果不如預期 |
| Fatigue config | 目前只有眼睛,**Yawning 開關待加** |

**對 Kenny 影響**:
- 對任何客戶 / sales **不能再講「Basic tier 已有 Yawning」**
- 改成:「Roadmap planned, 內部測試中, 上線時間請我內部確認」
- 對應 memory `feedback_internal_vs_external_truth.md` 三層真相框架

---

### B3. ⭐ #154 Label 管理 Process Gap(PM 介入空間)

**問題**:
- VMX-6722 Q1 已 merge 但 API 沒 pick 進去
- Brian 自評:「label 沒設好,我 filter 時漏掉」

**PM 介入提案**:
- 幫 RD 建立 merge label 紀律 / sync checklist
- 每兩週 sweep label 狀態
- Q2 merge 前的 PM-driven check

**這才是真正的「沒人扛 = PM 介入空間」**(取代之前我推錯的 #38/#40 隱藏 task)

---

### B4. ⭐ 200 Hz G-Sensor 戰略

**客戶 Simon must-have**:
- 事件發生時要吐 200 Hz G-Sensor 數據
- 目前只能 50 Hz

**技術風險**:
- 韌體層級
- 計算邏輯不變,但取樣率改變影響準確度
- 不知道變準還是變不準
- 要實測

**Brian 對 Sales 態度**:
> 「他們沒有投降,我們也不可能先投降。」

**Mori 在弄**

---

## Part C — 會後 Action Items 總表

### 🔥 24 小時內(P0)
- [ ] **確認 Single SKU + UVC hotfix 有對應 Jira ticket**(若無就建單)
- [ ] **Yawning 對外口徑統一**:不再講「Basic tier 已有」,改「Roadmap planned, 內部測試中」
- [ ] 找 Simon DM:「BLE Beacons 已交付給你測試,有什麼 feedback?」
- [ ] 確認 #209 Viewer only 對應 Jira(該是 VMX-7088 還是 VMX-7407?)

### 📅 本週內(P1)
- [ ] VMX-7088 Viewer only 角色「detail 能不能看」釐清
- [ ] Sheet 領先 Jira 的 3 個 mismatch 私訊 owner 同步:
  - #180 VMX-7082(Lucy)
  - #195 VMX-7233(Internal)
  - #199 VMX-6782(joe.lien)
- [ ] Sheet link 錯誤修正:#194 VMX-7316(實為 AZUGA SmartLink)/ #197 VMX-7147(實為 Camera recording bug)/ #209 link
- [ ] **Label 管理 gap 提案** — 跟 Brian 提:「Q2 merge label sweep,我來扛」
- [ ] 跟 Lucy 約 sync(模糊功能 UI 設計 + Rollover UI + 順便問 Coffee Chat 待問:軌跡顏色 / Severity)

### 🎯 本月內(P2)
- [ ] **跟 Brian 提 BMS/VMX 同步戰略 PM 參與**:API 文件對齊 / Fleet portal UI / 客戶溝通三選一
- [ ] HDFE UI 抱怨 → 把 Brian 想引入的「**beta 模式**」具體化成 PM proposal(對應 Hub 第三 tab)
- [ ] 把舊 Playback Sunset Plan 流程記成 PM 框架(可 reuse)
- [ ] 200 Hz G-Sensor 進度跟 Mori sync

---

## Part D — 待釐清(Coffee Chat / Slack 確認)

### 找 Brian
- BMS/VMX 同步戰略時程具體
- VMX-7088 Viewer only detail 能不能看
- HDFE beta 模式想要什麼形式

### 找 Mori
- 200 Hz G-Sensor 韌體可行性
- K-series ↔ Chip mapping
- Harsh Acceleration / Rollover G 值門檻

### 找 Jimmy
- Yawning 內部測試效果指標
- Smoking 真實狀態(Roadmap 列 Basic / sheet 隱藏)
- Burning ADAS / Burning DMS 定義

### 找 Lucy
- 模糊功能 UI 設計時程
- Rollover UI 設計
- 任務完成主動通知機制
- 軌跡顏色 / Severity 等級(原 Coffee Chat 待問)

### 找 Spencer
- Server-side AI Stage 2/3 進度
- Master/MAU 模糊 API 開關設計
- VMX-6722 文件 / Casebase 同步

### 找 Tony
- Akamai CDN PG 失效進度(Brian 已派工)

---

## Part E — 對 Memory 系統的更新

### 已更新
1. `feedback_vmx_facts.md` Yawning 狀態校正
2. `project_meeting_2026-05-06_q2_review.md` 新建戰略洞察記憶
3. `MEMORY.md` 索引第 13 條
4. `reference_ai_tasks_sheet_2026-05-05.md` 加上 Sheet 雙向 sync 缺口註

### 待更新(會後)
- [ ] `project_vmx.md`:加入「Brian 的 BMS/VMX 同步戰略」目標
- [ ] `reference_kenny_pm_frameworks.md`:加上「Sunset Plan + Beta 模式」具體案例(舊 Playback 案)

---

## 🔄 後續校正(2026-05-07 補)

本紀錄保留 5/6 當下會議字面內容(包含 Brian 自評的「label 漏 pick」narrative)。但 2026-05-07 讀 VMX-6722 comments + sub-tasks 後發現:

- **VMX-6722 本身有 label `vmx_2026Q2`** + sub-tasks 全 closed/resolved + jimmy 3/11 留「Server AI 已完成並 deploy 到 prod」+ parent ticket 仍 NEW
- **真實 process gap 不是 label 漏 pick,是 transition discipline** — RD 寫 comment 但沒按 Open→Resolved button

對 Brian 提 process improvement 應從「transition 紀律」切入,不是「label 紀律」。詳見 [knowledge/06_calibration-log/ai-tab-jira-alignment-2026-05-07.md](../knowledge/06_calibration-log/ai-tab-jira-alignment-2026-05-07.md) H 段 + [meetings/2026-05-07_ai-weekly_meeting-record.md](2026-05-07_ai-weekly_meeting-record.md)。

5/7 AI Weekly 同時揭露:
- **LDWS 完整真相**:Server-side(VMX-6722)Q1 確實 deploy。但 device 端 YOLO Lane Detection 改善是 5/7 決議 Pending 暫緩(資源緊繃)
- **Yawning UI toggle 真實對應 ticket = VMX-7432**(Lucy 5/6 開的單),不是 VMX-7309
- **Lens Cover 雙軌維護**:Azuga 標準版 = 解除車速 / BMS 版 = 車速 > 0
- **Eating/Drinking 客訴 17 倍量級危機**(客訴 ID 6652),6/15 前 7000+ Edge case 緊急重訓
