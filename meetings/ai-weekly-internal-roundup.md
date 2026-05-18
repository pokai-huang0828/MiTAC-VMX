# AI Weekly (Internal) Meeting Roundup · Series

> **會議系列**:內部 AI Weekly · 每週二、四 10:00 – 12:00 · 內部 RD + PM(主持 Jimmy)
> **檔案規則**(2026-05-12 Kenny 校正後 series 化):**每場新會議在這個檔頂部加 H2 section,時間倒序**,不再每場開新 dated 檔
> **對應 stakeholders.md 表 row**:[`02_organization-map/stakeholders.md` § 每週固定會議 → 內部 AI weekly](../knowledge/02_organization-map/stakeholders.md#每週固定會議)
> **NotebookLM source**:`5-7 ai weekly.m4a` / `5-11 ai weekly meeting.m4a` / `5-14 ai weekly meeting I.m4a` + `5-14 ai weekly meeting II.m4a` / **`5-18 ai weekly meeting I.m4a` + `5-18 ai weekly meeting II.m4a`** (notebook 名「神達VMX」 — 5/18 後共 49 sources)
> **AI 團隊任務追蹤 Sheet**:[Google Sheets — AI team tasks list](https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit?gid=339075798#gid=339075798)(每場 weekly 看這份對齊 PIC 進度)

---

## 2026-05-18 AI Weekly(via NotebookLM `5-18 ai weekly meeting I.m4a` + `II.m4a` · Kenny PM 角度交叉 5/14 + 5/13)

> **抓取背景**:Kenny 5/18 同步從 NotebookLM 神達VMX notebook 抓 5-18 兩段錄音的 PM 視角整理。**本場最大訊號 = Lens Cover 決策從 5/14「大改底層」收斂為「只加參數」**,風險大幅降低但對外口徑要重整。Kenny 自己整理的逐字稿摘要 + raw transcript 一起入庫。

### 🎯 本場 4 大核心議題(對齊 5/14 看新訊號)

| # | 議題 | 5/14 立場 → 5/18 現況 | 對 6/2 deliverable 衝擊 |
|---|---|---|---|
| 1 | **Lens Cover 邏輯重構決策大轉彎** | 5/14「**大改底層狀態機 + 解除校正綁定**」→ 5/18 **退回**:底層維持現有邏輯,**僅新增 2 個參數**(是否連續觸發 / 時間間隔)| 🟢 **風險大幅降低** · Jieli「明後天」(~5/19-20)即可完成參數修改供測試,**非完美重構而是最安全 workaround** |
| 2 | **打哈欠 (Yawning) 全臉模型進入實彈實測** | 5/14「2000 張假圖,信心極低」→ 5/18 **直接動手測**:Vincent 用 5-6 個自我模擬(說話誤報)+ 客訴影片,共 10+ 筆,跑 Edge 端 vs Server 全臉模型對比 | ⏳ 「今天上、晚一點確認」— Server 全臉模型能否擋住 Edge 端誤報 = 本週決定 |
| 3 | **Speed Sign 誤判分析 + OCR 第三方套件導入** | 5/14 純加資料重訓 → 5/18 **發現新舊資料特徵相反**(新資料看數字 / 舊資料看背景 → 衝突),引入 **PPOCRV5 (PaddleOCR V5)** 第三方 OCR 後處理過濾 | 🆕 AI 團隊**首次掛載第三方文字辨識套件補 CNN 極限** · 下週四(5/22)決定是否加進 Server |
| 4 | **客訴影片 AES256 解密成功 + Camera Height 確認 125 cm** | 5/14 卡在 Base64 解密 → 5/18 **James 成功解出**,提供 150-170 筆測試片段,客戶實測車高 **125 cm 真的很矮** | 🟡 新算法在窄路把估計值壓到 ~167 cm,**比原算法 200+ cm 好但仍偏高(差 40%)** — 客戶可能過於期待 |

### 📊 各 PIC 工作進度報告(5/18 揭露版)

| PIC | 5/18 報告 | vs 5/14 進度 |
|---|---|---|
| **Vincent** | 全臉打哈欠 Server 模型驗證:5-6 個自我模擬影片(含「說話」動作)+ 客訴影片共 ~10+ 筆。流程:Edge 端跑得結果 → Server 端跑去比模型 → 看 Server 能否擋住 Edge 誤報 | 5/14「PoC 在 PC 跑現有資料」→ 5/18「直接拿 server 跑全臉模型實彈測試」(放棄等資料擴充) |
| **Jieli** | Lens Cover 邏輯**捨棄底層大改**,改用 2 個參數控制觸發模式(預設 0 不重複)。明後天(5/19-20)完成參數修改供測試 | 5/14「5/19 Beta 死線壓力大」→ 5/18「明後天就能完成,風險大幅降低」 |
| **Jimmy** | (與團隊共同處理)飲食誤判 (Eating/Drinking) 資料標註與重訓,剩餘 ~13,000 筆。**新增 6 個物件**:背管 / 大瓶子 / 小罐子 / 便當盒 / 持物 / 餐具 → 物件已 9-10 個,擔心模型負擔。**設計大轉彎**:從「物件 + 嘴巴重疊」改為「物件 + 臉/頭重疊 + 雙手在方向盤」邏輯(類似 Smoking) | 5/14 階段性收斂飲水 → 5/18 物件大量擴充 + 邏輯重新框架 |
| **Jay** | Speed Sign 誤判:產出 4000+ 張訓練測試結果圖表。發現新舊資料特徵依賴相反(數字 vs 背景)。準備:(a) 關閉 Flip + 擴增倍率 20 → 10 重訓 (b) 測 PPOCRV5 套件後處理 | 5/14 純關閉翻轉 → 5/18 證實單純加資料不可解,改第三方 OCR 補強 |
| **Eric** | 參與速限標誌分析 / 全臉模型驗證方式 / Lens Cover 底層邏輯討論(無特定個人單項開發進度) | — |
| **Jonathan / Adonis** | 會議中**未提及進度** | 連續兩週未報,可能需要 Jimmy 單獨追蹤 |
| **API / Cloud 團隊** | Blurring 非同步架構已準備好,可透過 API 打單測試驗證 | 5/14「設計完成」→ 5/18「**ready 給 Jimmy 等人實打**」 |
| **James / 測試團隊** | 成功將客訴影片 Key 從 Base64 轉 AES256 並解密,提供 150-170 筆測試片段 | 5/14「協助解密」→ 5/18「完成 + 已交付」 |

### ✅ Action Items(本場 5 件)

| # | 任務描述 | Owner | Deadline | 關聯 Ticket / 物件 |
|---|---|---|---|---|
| 1 | 使用真實 + 模擬影片(~10+ 筆)驗證 Server 端全臉打哈欠模型過濾效果 | **Vincent** | 本週內 / 盡快 | [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432) Yawning UI toggle |
| 2 | 完成 Lens Cover **參數化控制邏輯**開發(支援不重複 / 指定間隔兩種模式)+ 把 Sense/CCH 跟 BMS 兩組參數列出來給 Kenny 確認規格 | **Jieli** | 5/19-20(明後天)| [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) + [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) |
| 3 | 用 PPOCRV5 套件測現有 Speed Sign 誤報照片,評估過濾效果 → Server 端是否加 | **AI 團隊** | **5/22 下週四前** | (未指明 Jira) |
| 4 | 關閉 Flip 參數 + 擴增倍率降為 10 倍重新訓練速限標誌模型 | **Jay** | 近期 | (未指明 Jira) |
| 5 | 將剩餘 ~13,000 筆含「瓶子」等飲食特徵資料集結重訓 | **AI 團隊**(Jimmy + Vincent) | 盡快(配合 Beta) | [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562) |

### 🔄 新訊號與差異分析(5/18 vs 5/14)

#### 1. 策略大轉彎:Lens Cover 開發風險收斂
- **5/14 立場**:RD 企圖解開 Lens Cover 與 DMS 校正深度綁定,大改底層狀態機滿足客戶
- **5/18 現況**:**「真正要實作時又有不同想法」→ 決議退回不動底層**。改以「增加參數」讓 App 自己決定是否連發或設定冷卻時間
- **意義**:6/2 死線前選擇**最安全 workaround**而非完美重構。debounce time 還是維持在 CDR 那邊去做
- **規格對比**:
  - **Sense/CCH**:Lens Cover + Lens Uncover 兩個 event,**前一狀態改變才觸發下一次**(遮住觸發 → 不重複,除非障礙物移掉觸發 Uncover 後才能再觸發 Cover)
  - **BMS**:**連續觸發**(用 timeout 參數控制間隔)
  - debounce time:CCH alertTime=10s / BMS alertTime=60s
  - workSpeedMin:**CCH=0 km/h / BMS=5 km/h**(這個 leo.tsai 5/14 也在 VMX-6983 提醒過)
- **PM 動作**:Jieli 會列出兩組參數 → Kenny 確認規格符合客戶要求

#### 2. CNN/YOLO 辨識極限浮現,轉向 OCR 輔助 (Speed Sign)
- **5/14 立場**:單純關閉翻轉參數重訓
- **5/18 現況**:資料證實單純餵資料會出現「看數字 vs 看背景」特徵衝突 → **首次決定掛載第三方文字辨識套件作為後處理**修正 CNN 模型極限
- **PPOCRV5 = PaddleOCR V5(PaddlePaddle 開源 OCR framework 3.0 最新版本)**
- 已測試:4 種影像增強方式都能抓到數字 / 速限文字
- **Class 111** = 美國 + 加拿大共用速限類別代碼,**不管模型怎麼換一定要保留**(美國有 1,100 之類沒做字,加拿大也走這類)
- **意義**:AI 團隊首次承認「純 CNN/YOLO 對細小數字辨識有極限」,改採混合架構

#### 3. 打哈欠驗證進入「實彈射擊」階段
- **5/14 立場**:只有 2000 張假資料,對全臉模型準確度毫無信心
- **5/18 現況**:**放棄等資料擴充**,直接錄製「說話」影片丟給 Server AI 實測,以最快速度驗證全臉模型是否具備商業過濾價值
- 流程:Edge 端跑一次得結果 → 同時 Server 端跑去比模型 → 結論在「禮拜四(5/22)」討論

#### 4. Eating/Drinking 邏輯架構重新框架(重大設計變動)
- **5/14 立場**:階段性收斂,先過濾「飲水」特徵
- **5/18 現況**:**從「物件 + 嘴巴重疊」改為「物件 + 臉/頭重疊 + 雙手在方向盤」邏輯**
  - 不再要求「進到嘴的動作」(BMS 早期討論過,這邏輯不符合實際吃東西時間)
  - 類似 Smoking 邏輯:只要拿在手上 + 接近臉/頭就算違規
  - 安全邏輯:「確保雙手在方向盤,不要拿別的東西」
- **物件擴充**:從原本「飲水」擴大到 9-10 個物件 → 擔心模型負擔
- **驗證方式**:用 YOLO 88 類最大 server 版直接測,看能不能抓到「杯子」「水瓶」— **如果連杯子都抓不到,方向錯了,後面別浪費時間**
- **客訴單 6252** 提到司機夜間反光誤報現象

#### 5. 6/2 釋出範圍校正:Sense + CCH + BMS 三家一起上,Webfleet 7 月才給
- **錄音原話**:「Sense 跟 CCH 跟 BMS 三個一起上,在 6 月 2 號那一天」/「T(Webfleet)... 一樣是六月底就是六月這個版本,六月這個版本**七月才給他**」
- **意義**:重大校正之前 weekly summary 寫的「6/2 五大 deliverable 對所有客戶一起上」籠統口徑 — 實際是**先給 Sense / CCH / BMS,Webfleet 晚一個月**
- 對 Kenny 對 Webfleet (Sebastian / Jacob / Martin) 溝通要說「6/2 是 Sense/CCH/BMS 先上,Webfleet 排在 7 月版本」

### 🛠 開發 / 技術資訊追蹤

#### Model 版本號
- **Model 26**:新分類模型,**MVP 已測 86% 準確率**(跟 V14 / 11P 差不多)
- 還在訓練:海景房(高機器)92-96% / 服務器訓練中,需要更好機器(5090 級別,市面上 12-16 萬可以買到專門卡)
- Vincent「另外一台還沒完,但 9 幾 %」「另外一台是 ver 盤」「海景房的 92-96% 很高」

#### 第三方套件
- **PPOCRV5 (PaddleOCR V5 / framework 3.0 最新版)**:支援中文 + 英文 + 日文,本場決議用來補 Speed Sign 後處理。Jay 已測現有誤報照片有效

#### 客戶資料解密
- **AES256 + Base64 → binary 轉換流程已通**(James 負責)
- 客訴影片實測高度確認 **125 cm**(很矮 — 屬於小道路 / 大車內視野角度問題)
- 新算法在這段路測到 ~167 cm(舊算法 ~200+ cm,改善 40% 但仍偏高 — 環境受限)

#### 6/2 對齊死線
- 對齊 release 包:Lens Cover 參數化 + 睜眼率 + Blurring 非同步 API + Model 26 + 速限標誌(若 PPOCRV5 加進去)
- **三家對齊**:Sense + CCH + BMS 6/2 同步上 → Webfleet 7 月

### 📌 PM 觀察 / 對外口徑校正(Claude 補)

1. **5/14 寫進 critical-facts-log 的「Lens Cover 必須開發參數化計時迴圈機制重構底層狀態機」需要校正之校正** — 實際 5/18 退回「底層不動,只加參數」,Jieli 5/19 Beta 死線壓力反而下降。**對外口徑要改為「底層架構維持,新增 2 個參數讓 App 控制觸發模式」**
2. **6/2 三大 / 五大 deliverable 必須區分客戶範圍** — 之前 weekly summary 籠統講「對所有客戶」,實際 5/18 揭露「Sense + CCH + BMS 同步 6/2,Webfleet 排 7 月」。Kenny 對 Sebastian / Martin / Jacob 溝通要明確說「Webfleet 7 月版」
3. **Camera Auto-Height 125 cm 實測 = 環境受限警訊** — 對 Brian / 客戶溝通新算法 release 時要管理期望:「窄路 / 大車情境改善但無法完美 — 客戶過於期待要小心」
4. **PPOCRV5 第三方套件導入 = 對外可講「AI 團隊持續優化精準度」** — 但不要承諾 timeline,因為下週四才決定是否進 Server
5. **Eating/Drinking 邏輯改成「雙手在方向盤」框架 = 對 Azuga 溝通校正** — 之前 5/13 Azuga AI Weekly 答應「漸進處理飲水」現在進化為「雙手安全邏輯」,屬於正向強化但需要明確說「不是只看飲水,是整體手部安全行為偵測」

### 🔗 引用對齊

- 上一場:[2026-05-14 AI Weekly](#2026-05-14-ai-weekly)(本檔下方 ↓)
- 上一場對齊的 calibration:[`06_calibration-log/critical-facts-log.md` § 2026-05-14 AI Weekly Internal 3 大反差](../knowledge/06_calibration-log/critical-facts-log.md)— 本場 Lens Cover 條目已被 5/18 推翻,critical-facts-log 已加 strikethrough
- AI 團隊任務追蹤:[Google Sheets — AI team tasks list](https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit?gid=339075798#gid=339075798)
- 本週 weekly summary:[`weekly-summary/2026-05-18_week-of-may-18.md`](../weekly-summary/2026-05-18_week-of-may-18.md) — 5/18 AI Weekly section
- 對應 Jira:[VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(Yawning toggle)/ [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) + [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585)(Lens Cover)/ [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562)(Eating/Drinking)/ [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) + [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458)(Blurring API)

---

## 2026-05-14 AI Weekly(via NotebookLM `5-14 ai weekly meeting I.m4a` + `II.m4a` · Kenny PM 角度交叉 5/11 + 5/13)

> **抓取背景**:2026-05-15 由 Kenny 點名「5/14 內部 AI weekly 缺校正」後,從 NotebookLM 神達VMX notebook 反查 5-14 兩段錄音的 PM 視角整理。本場會議**沒有 cross-customer commitment**,所以議題多在內部 RD 對自家承諾的 reality check,**3 大議題都從「對外輕鬆承諾」翻成「內部底層必須重做」**。

### 1. 本次會議 4 大核心議題

| # | 議題 | 底層真相 | 對 6/2 deliverable 的衝擊 |
|---|---|---|---|
| 1 | **Yawning 全臉模型面臨資料匱乏** | 團隊確認用於全臉打哈欠辨識的訓練資料極少,**僅約 2000 多張 AI 生成影像**(不是真實採集)。決議先在 PC 端以現有影像跑可行性 PoC | 🚨 **6/2 上線高準確度打哈欠 = 機率極低**。Kenny 必須提早對 Azuga / Webfleet 做期望值管理 |
| 2 | **Lens Cover 底層邏輯重構 + 參數化** | 為兌現 5/13 對 Azuga「解除車速 + 解除 Calibration 依賴」承諾,RD 發現舊狀態機把兩者綁太深 → 廢除「需等 Recalibrate 才能再觸發」限制,改採 Configurable Parameter(預設 0 = 不重複觸發)→ 底層大改 | ⏳ Jieli **下週一 5/19 要交 Beta** · 對應 [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582)(設計)+ [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585)(實作 bug) |
| 3 | **Eating/Drinking 採階段性收斂優化** | 內部討論發現「食物」種類過於發散(三明治 / 零食袋 / 各種包裝),**實務上無法完美定義所有食物 + 無法區分「拿杯子貼臉」vs「實際喝水」**。決議先集中資源處理「飲水(瓶子/杯子)」特徵,加入負向資料庫重訓 | ⚠️ 對外口徑要從「完美解決」改為「**階段性優化 — 先過濾最常發生的特徵**」· 不能再答應客戶 100% 解 |
| 4 | **Blurring 非同步架構定案** | 確認採用**無 GPU 的一般 CPU Instance** 跑 Python 影像處理。規劃 SQS (Message Queue) 接收資料 + Callback API 回傳結果的非同步處理流程 | ✓ 對齊 CONNECTSOURCE Q2 scope · Spencer 5/11 拍板的 API-only path · 預計 6/2 釋出 |

---

### 2. 各 PIC 工作進度報告(5/14 揭露版)

| PIC | 5/14 會議報告 | vs 5/11 進度 |
|---|---|---|
| **Vincent** | 將全臉打哈欠模型轉為 **DLC + TF 格式**。資料量過少,先在 PC 端針對現有影片做初步準確度驗證 | 5/11 還在準備 2 萬至 10 幾萬筆訓練資料 → 5/14 揭露真實可用只有 2000 張(資料規模差異極大,要釐清) |
| **Jieli (竭力)** | 負責 Lens Cover 邏輯重構 + 廢除 Calibration 依賴,改成參數化計時迴圈機制。**下週一 5/19 Beta 死線** | 5/11「正釐清標準版 vs BMS 參數常數」→ 5/14 升級為「底層架構大改」(時間壓力極大) |
| **Jonathan / Jay / Adonis / Eric** | 本次會議**未具體提及進度**(可能在 Part I 講過或不在這場 agenda) | 需在後續會議單獨追蹤 — 特別是 Eric(指導 Server AI Yawning 訓練) |
| **API / Cloud Team** | 已完成 Blurring Python 處理程式,準備 **SQS + Callback API** 串接設計;需提供操作流程給 UI 端 (Lucy) 以利前端介面設計 | 5/12 揭露的 VMX-7441 / 7458(Blurring Master/Fleet 雙層)實作正在推進 |
| **James** | 提供 **AES256 加密格式**,協助團隊解密客戶客訴影片進行分析 | 新訊號 — 5/11 沒提及 James 角色 |

---

### 3. Action Items(5 件)

| # | 任務描述 | Owner | Deadline | 關聯 Ticket |
|---|---|---|---|---|
| 1 | 使用現有 2000 張生成資料,於 PC 端初步驗證全臉打哈欠模型可行性 | **Vincent** | 本週內(5/16 前) | [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432) Yawning UI toggle (Lucy)— 設計卡 PoC 結果 |
| 2 | 實作 Lens Cover 重複觸發參數,解除依賴 DMS 校正之限制 | **Jieli** | **5/19 下週一(Beta)** | [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) + [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) |
| 3 | 開發 Blurring 服務的 SQS 接收 + Callback API 串接流程 | API / Cloud 團隊 | 6/2 版本 | [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) + [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) |
| 4 | 解密客戶客訴影片(AES256)並進行特定路段算法驗證 | 測試員 / **James** | N/A | 未指名(口頭提「J 有傳一個 G 給我...卡住」客訴單,未指名單號) |
| 5 | 將「飲水(瓶子/杯子)」等特徵加入負向資料庫進行重訓 | AI 團隊 | N/A · 集中資源優先處理 | [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562) Eating & Drinking · Jimmy + Vincent |

---

### 4. 5/14 vs 5/11 + 5/13 重大新訊號(差異分析)

#### 🚨 訊號 A:「輕易承諾」轉為「技術負債引爆」 (Lens Cover)
- **5/6 + 5/13 對外**:輕鬆答應 Azuga 要把 Lens Cover 與車速、Calibration 脫鉤
- **5/14 內部**:RD 盤點發現舊狀態機把兩者綁定極深 → **必須緊急捨棄舊架構,開發全新的「參數化計時迴圈機制」** + 5/19 Beta 死線壓力極大
- **PM 啟示**:對客戶的承諾要 cross-check RD 底層架構成本,不要再讓「對外輕鬆 yes / 內部緊急救火」的 pattern 重演 — 對應 [communication-frameworks.md 承諾層次](../knowledge/04_pm-frameworks/communication-frameworks.md)

#### 🚨 訊號 B:Yawning 模型資料荒,準確率極限浮現
- **5/11 決議**:打哈欠轉向 Server AI + 全臉 (Full Face) 模型
- **5/14 揭露**:手上竟**只有 2000 多張 AI 生成假資料**,團隊對其準確度「沒有期待」
- **對外 PM 動作**:6/2 釋出高準確度打哈欠功能 = 機率極低 → Kenny 必須對 Azuga (Sebastian) / Webfleet 提早做**期望值管理**(Expectation Management)。對應 Azuga 5/13 場「Yawning 仍在優化,對 6/2 釋出無信心」口徑要再加強

#### 🚨 訊號 C:Eating/Drinking 從「完美解決」退為「階段性收斂」
- **5/13 Azuga 場**:客戶提議提供去識別化(Anonymized)影像,以全面解決誤報
- **5/14 內部**:認知無法完美定義所有「食物」(三明治 / 零食袋 / 包裝)+ 無法區分「拿杯子貼臉」vs「實際喝水」
- **PM 決議**:不糾結完美定義,改採收斂策略 — **先從佔最大宗的「飲水」特徵過濾起**。對 Azuga 回覆要說「我們先處理飲水這類最常發生的誤報特徵,不承諾一次解決所有食物」

#### ✓ 訊號 D:Blurring 架構定案(無 GPU + SQS + Callback)
- **5/11 + 5/13 對外口徑**:Spencer 5/11 拍板 API only · Server-to-Server JS lib
- **5/14 內部具體化**:技術選型確認 **CPU Instance + SQS Message Queue + Callback API**(非同步)
- **對 CONNECTSOURCE 線啟示**:對 Elvis / Cary cost model 對話可加上「我方 Blurring 跑在 CPU,不是 GPU 高成本架構」這個物理事實 — 加強 § 9.7 cost framing 信心

---

### 5. 會議提及 / 對應的 Jira Ticket
- 5/14 內部會議**口頭討論為主**,未直接點名具體 VMX-XXXX 票號
- 提到「**J 有傳一個 G 給我...卡住**」客訴單但未指名(Action Item 4 對應)
- 會議當天(5/14)Jira 新建 **147 票**(VMX-7411~7482 區間)— 對齊 [`jira_data/jira_tickets_snapshot_2026-05-14.json`](../jira_data/jira_tickets_snapshot_2026-05-14.json) snapshot。5/15 又新增 [VMX-7482](https://jira.navman.co.nz/jira/browse/VMX-7482)「[EdgeTensor] Add SDK API to config airplane mode」(jack.fl.chen / 5/15 早上創)
- 跨參考主檔:Yawning → [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432) · Lens Cover → [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) / [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) · Eating/Drinking → [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562) · Blurring → [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) / [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458)

---

## 2026-05-11 AI Weekly(via NotebookLM `5-11 ai weekly meeting.m4a`)

### 1. AI Model 版本對應(4 個)
- **Model 11P**:原本用於「嘴部 (Mouth)」辨識的分類模型 → 現正被修改為「全臉 (Full Face) 打哈欠 (Yawning)」辨識 — 對應 [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432) Yawning UI toggle (Lucy)
- **Model 11L**:舊版 DMS(含安全帶)分類模型 — **將被 Model 26 取代**
- **Model 26**:新導入 DMS 分類 + Detect 模型架構,**準確度優於 11L**,Yawning + 安全帶 + Distraction 統一架構
- **V14**:影像模糊化 (Blurring) 舊模型版本 — 對應 [HAWK-527](https://jira.navman.co.nz/jira/browse/HAWK-527) / [HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578) Blurring 修問題

### 2. 6/2 Fix Version(2026-06-02)— 五大必上 deliverable
> **2026-05-14 校正**:從 [2026-05-13 Azuga AI Weekly](2026-05-13_azuga-ai-weekly.md) 揭露,實際是**五大**不是三大。原 5/11 內部會議只記到三大,漏了 Eye Stable Rate threshold 和 Camera Auto-Height(這兩個是 5/13 跟 Azuga/Webfleet 對齊時補上)。

| # | Item | Owner | 對應 ticket / row |
|---|---|---|---|
| 1 | **LDWS API**(5/7 暫緩,5/11 **重新掛 6/2**)| AI / Jimmy | [VMX-7101](https://jira.navman.co.nz/jira/browse/VMX-7101) "LDWS Improving (Server)" 待從 Jira 確認 transition · 2026-05-14 校正:原誤寫 VMX-7375 (leo.tsai 的 Add Manual End Button) · **Jira fixVersion 仍空** |
| 2 | **Lens Cover 解耦** | Vincent / Jieli | [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582)(Open,fv=VisionMax_20260602)+ [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585)(5/13 新開 leo.tsai)+ [VMX-6983](https://jira.navman.co.nz/jira/browse/VMX-6983)。**新規格**:移除車速 + 獨立 DMS 校正 + 修 debounce + Lens Uncovered event |
| 3 | **新版 DMS 模型(Model 26)**| AI 團隊 | 統一架構,Yawning + 安全帶 + Distraction |
| 4 | **Eye Stable Rate threshold 開放**(5/13 補)| APP team (joe.lien) | [VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309)(Open,fv=CameraAPP_202605)+ [HAWK-551](https://jira.navman.co.nz/jira/browse/HAWK-551) 對應 CAM Lite fatique 客訴 |
| 5 | **Camera Auto-Height 新演算法**(5/13 補)| Jay | [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) New→Open 5/13。Webfleet 拒絕改手動,Brian 承諾 6/2 演算法實測。Sebastian 後續會關 HAWK-501 + 開新單,Mitac 端待票號 |

### 3. 5/15 Beta 測試前置死線
- **要求外部 API / 模組需在此之前 ready** — 等於 Kenny 對 Cary / Elvis / Wendy / MiTAC AU 的 commitment 都要在 5/15 前確認 API 規格凍結

### 4. Regression Risk(NotebookLM 自動 PM 建議)
- 6/2 同時上 Model 26(DMS 底層替換)+ 11P(嘴部→全臉)+ V14 → vNext(Blurring)— **三個 model 同時動,Regression Bug 高風險**
- 動作建議:跟 QA 團隊(Righter / Richard)擬 Regression Test Plan 鎖「Head 邏輯」+「Model 26」雙重路徑;UI 團隊敲「打哈欠開關」Figma 設計

### 5. 跟 5/7 比的變化
- 5/7 「飲食 17x 客訴重訓 6/15」**未在 5/11 重提**(待 Vincent + Jimmy 6/15 deliverable 自走)
- 5/7 「LDWS YOLO Pending 暫緩」→ 5/11 **LDWS API 重新掛 6/2 Fix Version**(變動)
- 5/7 「Lens Cover 雙軌」→ **HAWK-582 已校正單軌**(critical-facts-log 已記),5/11 重申 6/2 上

---

## 2026-05-07 AI Weekly(via NotebookLM `5-7 ai weekly.m4a`,38 sources 全庫查詢)

> **整理視角**:Kenny PM 角度,逐 PIC + action item + 跟 5/6 Azuga AI weekly 落差
> **目的**:跟 sheet AI 工作計畫 row-by-row 5/7 snapshot 對齊,找出 sheet 沒寫到 / 寫得不準的訊號

### 1. 各 PIC 工作進度報告(5/7 會議揭露版)

| PIC | 5/7 會議報告內容 | Sheet 對應 row | Sheet 寫的 vs 會議揭露 |
|-----|---|---|---|
| **Vincent** | 將 7000 多筆吃東西、喝水、手持物品的誤判照片(Edge cases)加入負向資料庫,集中資源於 6/15 前完成模型 Retrain。同時協助評估將「Head 邏輯」導入原有 Face 演算法 | #45 Pedestrian / #7 Blurring / #43 Camera height | 🚨 Sheet 沒這條,飲食重訓不在他名下 row(#46 Eating Jimmy 才有)— Vincent 角色擴大 |
| **Jieli (竭力)** | 處理 BMS 專案 Lens Cover 獨立邏輯(車速 > 0 才啟動),必須趕上 6/2 交付 | #28 鏡頭遮蔽([VMX-6983](https://jira.navman.co.nz/jira/browse/VMX-6983) + [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582)) | ✓ 對齊。Sheet 5/7 「BMS 正在確認規格」跟會議「車速 > 0」一致 |
| **Jimmy (居明)** | 收集與統整客訴的誤判資料,目前手上已收集 307 張邊緣情境照片,持續擴充 Data pool | #32 Face Not Found / #46 Eating | 部分對齊。#32 sheet 寫 13975 張未 review,跟會議 307 張對不上(可能不同資料集)|
| **Jay (傑)** | 處理 Speed Sign 模型辨識混淆問題,已將訓練參數中「Flip(翻轉)」關閉並重新訓練 | sheet 沒對應 row! | 🚨 **Speed Sign 不在 AI 工作計畫 visible rows**。可能是新增工作或被 hide。會議講「立即執行」 |
| **Eric** | 已完成 ECS 伺服器實例的 Health Checking 機制,解決模型突然消失導致服務掛點問題,已部署生產環境 | #50 VisionMax PROD not blurring([HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578)) | ✓ 對齊。Sheet 5/7 寫的「自我健康檢查機制」就是這個 |
| **Spencer** | 負責睜眼率 (Eye opening rate) API 開發,須從 Camera App 到 Server 端完成全鏈路驗證,趕上 6/2 時程 | #4 Eyes Detection([VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309)) | 🚨 **Sheet 寫 done done 太樂觀**。會議揭露 Server 端串接還沒完成,要趕 6/2 |
| **Jonathan** | 5/7 會議未具體提及進度 | #47 Rastrac False Speed | Sheet 自己進度推進(Train 99%/Test 98%/100%),但會議沒列為討論點 |
| **Adonis** | 5/7 會議未具體提及進度 | #41 / #48 / #49 / #50 | Sheet 5/7 有 update,但會議沒提 |

---

### 2. 會議決定的 Action Items(4 件 High Priority)

| # | Action | Owner | Deadline | 對應 Sheet row |
|---|---|---|---|---|
| 1 | 飲食與手持物品誤判大重訓(7000+ 筆 Edge case 重訓) | AI 團隊(**Vincent + Jimmy**) | **6/15** | #46 Eating & Drinking([HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562), Jimmy)+ Vincent 加入 |
| 2 | 實作 BMS 專屬 Lens Cover 邏輯拆分(車速 > 0)| Camera App + Jieli | **6/2** | #28 鏡頭遮蔽([VMX-6983](https://jira.navman.co.nz/jira/browse/VMX-6983) + [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582))|
| 3 | 睜眼率 (Eye opening rate) API 全鏈路驗證 | Cloud / **Spencer** | **6/2** | #4 Eyes Detection([VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309))|
| 4 | Speed Sign 模型修正與重訓(關閉 Flip 參數)| AI 團隊 (Jay) | **立即** | 🚨 **無對應 sheet row** |

---

### 3. 5/7 vs 5/6 Azuga AI Weekly 重大新訊號(落差與警訊)

#### 🚨 訊號 A:誤判規模與急迫性暴增 17 倍
- **5/6**:Azuga 會議僅提到少數抽菸/飲食的誤判
- **5/7**:BMS 等客戶端回報的飲食誤判案件量**高達先前的 17 倍**。團隊被迫將原先分批訓練的計畫,改為在 6/15 前「一次性」將萬筆資料集中重訓
- **影響**:#46 Eating & Drinking 從 sheet「預計 6/10 Feasibility results」升級為 6/15 前緊急重訓。Vincent 加入扛
- **客訴 ID**:6652(過去也曾被指為精準度較低的特定帳號 ID)

#### 🚨 訊號 B:Lens Cover 規格出現嚴重分歧 → 雙軌維護
- **5/6**:剛與 Azuga 敲定「標準版 Lens Cover」要「解除車速限制」並獨立於 DMS 校正之外
- **5/7**:BMS 卻基於司機休息隱私,強烈要求 Lens Cover 必須「車速 > 0」才能啟動
- **影響**:RD 必須**緊急將標準版與 BMS 版的邏輯拆分雙軌維護**
- **對 PM 啟示**:多客戶 customization 衝突,跨客戶協調成本暴增

#### 🚨 訊號 C:夜間與死角防禦機制升級
- **5/7 深入探討 5/6 未觸及的底層優化**:
  - **Yawning 夜間打哈欠**:導入「灰階(Grayscale)模型」,並考慮 Server 端從「辨識嘴巴」改為「辨識整張臉」
  - **Face Not Found 死角**:當夜晚或角度偏斜找不到臉(Face)時,將導入「Head 邏輯(找頭)」作為輔助判定
- **對應 sheet**:#3 Yawning(Jieli)目前 sheet 5/7 空白,但會議揭露其實有「灰階模型重新訓練」這條進度 — sheet 沒寫

#### 🚨 訊號 D:LDWS Pending 暫緩 + 開新 ticket
- **5/7 揭露**:「關於 YOLO Lane Detection 導入,因團隊目前資源緊繃,**決議先 Pending 暫緩,並開立新 Ticket 追蹤**」
- **對 5/6 Brian「Q1 已 merge」narrative 的修正**:
  - [VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722) Server-side LDWS 確實 Q1 已 deploy(jimmy 3/11 留言確認)
  - 但 5/7 講的是 **device 端 YOLO Lane Detection 的進階改善**,這條是**新工作 + 暫緩**,不是 6722
- **對應 sheet** row 10 #8 LDWS:5/7 寫「pending」**是真實狀態**,但要追的是「新 ticket 在哪 / 何時開」

### 訊號 E:Camera Height 期望值管理(PM 介入點)
- 5/7 揭露:「PM 將提供 20% 的誤差範圍數值以進行期望值管理」
- 對應 #43 Camera height([HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501), Jay+Vincent)
- **Kenny 的 PM 角色任務**:準備 20% 誤差數值給 BMS

---

### 4. 會議提及的 Jira Ticket / 模型版本號 / Fix Version

| 項目 | 詳情 |
|------|------|
| **Fix Version 1.18** | ECS 實例異常的修復機制,5/4 已部署生產環境 |
| **Fix Version 1.1.28** | 同上 — 自我健康檢查機制 |
| **客訴 6652** | 飲食誤判量是過去 17 倍的特定帳號;在先前對話中 6652 也曾被指為精準度較低的特定帳號 ID |

⚠️ 會議沒明確提到 VMX-XXX 票號 — Jira ticket 對應靠 sheet/comment 推

---

### 5. 5/7 各功能盤點(會議揭露版,跟 sheet 對齊)

| 功能 | 5/7 會議講的 | sheet row 對齊度 |
|------|--------------|--------|
| Yawning 打哈欠 | 夜間嘴部辨識效果不佳,加入灰階模型重新訓練,考慮改為辨識整張臉 | 🚨 sheet #3 5/7 空白 — 漏寫 |
| Eating/Drinking | 客訴重災區,正將水杯/吃東西等加入負向資料庫,6/15 前重訓 | 🚨 sheet #46 5/7 寫「處理 face not found 尚未評估」— 嚴重 understatement |
| Lens Cover | BMS 提車輛靜止隱私需求,實作「車速 > 0 才啟用」BMS 獨立邏輯 | ✓ 對齊 #28 |
| LDWS 車道偏移 | YOLO Lane Detection 導入因資源緊繃決議 Pending,開新 ticket | ✓ 對齊 #8(但要追新 ticket 編號)|
| Blurring 影片模糊化 | 連續追蹤補充機制解決車牌閃爍;非同步處理,部分檔案上傳即可啟動 | ✓ 對齊 #7 / #48 / #49 |
| Speed Sign 速限標誌 | 18/25/40 等數字易混淆,根因是 Flip 參數開啟,要求關閉 + 擴增降至 10 倍重訓 | 🚨 **sheet 沒對應 row** |
| Face Not Found | 將導入 Head 邏輯,當臉部遺失以頭部框線輔助判定,Log 印出信心度 | 部分對齊 #32(但 5/7 sheet 沒寫 Head 邏輯導入)|
| Camera Height | 依賴長期統計與天際線對齊推算高度。PM 提供 20% 誤差範圍給 BMS | ✓ 對齊 #43 |
| Pedestrian | **5/7 會議未提及**(5/6 報告中列為下半年 Roadmap)| sheet #45 5/7 寫「整理回覆資訊」— 對應 5/6 工作,5/7 已不是焦點 |
| Rastrac / VLM | **5/7 會議錄音皆未提及** | sheet #47 Rastrac 自己有重大進度(Train 99%/Test 98%/100%),但會議沒拿出來分享 |

---

### 6. Action Items(Kenny PM 角度)

### 🔥 24h 內(P0)
- [ ] **Speed Sign 模型修正**沒對應 sheet row — 跟 Brian 確認要不要新增 row 追蹤
- [ ] **Eating/Drinking 17x 量級的客訴危機** — sheet #46 5/7 update 嚴重 understatement,PM 私訊 Jimmy 確認真實緊急度 + 把 Vincent 加進 PIC
- [ ] **Camera Height 20% 誤差範圍數值準備** — 我自己要做的 PM 任務,要找 Jay/Vincent 拿真實數據

### 📅 本週內(P1)
- [ ] **LDWS device 端 YOLO Lane Detection 新 ticket 編號追蹤** — 私訊 jimmy.jy.huang 或 Brian
- [ ] **Lens Cover 雙軌維護**對 RD 成本影響評估 — 跟 Brian 提多客戶 customization 衝突的長期問題
- [ ] **Spencer 睜眼率 API 6/2 進度** — sheet #4 Eyes 寫 done done 但會議講還沒完成,要校正

### 🎯 本月內(P2)
- [ ] **Yawning 灰階模型 + 整張臉辨識**新方向加進 sheet #3
- [ ] **Face Not Found 引入 Head 邏輯** sheet #32 寫上去
- [ ] **VLM / Rastrac 沒在會議討論**問 Brian 是不是被 deprioritize / 換 owner

---

### 7. 對 sheet AI 工作計畫的修正建議

| Sheet row | 5/7 sheet 寫的 | 5/7 會議揭露 | 該怎麼校正 |
|-----------|---|---|---|
| #3 Yawning | 空白 | 灰階模型重訓 + 考慮辨識整張臉 | 補上「灰階模型訓練中,考慮辨識整張臉」|
| #4 Eyes | done | Spencer 睜眼率 API 還在做,趕 6/2 | 改成「CDR 端 done / Server 端進行中,6/2 交付」|
| #46 Eating | 處理 face not found 尚未評估 | 客訴重災區 17 倍量,6/15 前緊急重訓 | 大改:加入 Vincent + 註明 6/15 deadline + 17 倍量級 |
| #43 Camera height | 拿到小 Brian 影片待測 + 80% CI 調整 | 同上 + PM 提供 20% 誤差範圍給 BMS | 加上 PM 任務 |
| #45 Pedestrian | 整理回覆資訊 | 5/7 未提,5/6 列下半年 Roadmap | 確認是否該移到「下半年 Roadmap」標 |
| (新)Speed Sign | (無) | Jay 立即關閉 Flip 重訓 | 需新增 row |
| (新)LDWS YOLO Lane Detection | 包在 #8 | 5/7 Pending 暫緩,新 ticket | 釐清新 ticket 編號 |
