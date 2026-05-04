# VMX Master Portal & Fleet Portal — 完整位層架構

> 來源:NotebookLM 鎖定《VisionMax_架構及整合方式_260123.pdf》單一來源萃取
> 萃取時間:2026-04-29
> 標註說明:[1] = PDF 內「Master - Dashboard (1/2)、(2/2)」與「Master - Management (1/2)」截圖
>          [2] = PDF 內「General Operation Settings」之 Dashboard 與 Management 截圖
> ⚠️ PDF 未列的子層,NotebookLM 標「PDF 未列」— 不要自己腦補

---

## 一、Master Portal(經銷商 / 設備管理端)

> 使用者:**Dealer(經銷商)** + 內部 MAU/MiTAC 管理者
> 商業權責:銷售車隊管理服務、將 CDR 設備分配/開通給底下各車隊

### 主選單:`Dashboard` [1]

提供 CDR 派發狀態、各 fleet 的 CDR 數量比例、Plan Type 分布

**畫面 / 面板 (Panels)**:

| Panel | 包含欄位 / 圖例 |
|-------|----------------|
| `Devices Assigned to Fleets` | `Total Devices` / `Assigned Devices` / 百分比圖表 |
| `Devices with Active Plan` | `Total Assigned Devices` / `Active Devices` / 百分比圖表 |
| `Total Fleets` | `Totals` + 圖例分類:`Devices >= 300` / `Devices >= 100` / `Devices >= 50` / `Devices < 50` |
| `Total Activated Plan Types` | `Totals` + 圖例分類:`Standard` / `Pro` |

### 主選單:`Analysis` [1]
> PDF 未列子層細節

### 主選單:`Management` [1]
- 次選單:`Inventory` [1]
  > PDF 未列細部欄位

---

## 二、Fleet Portal(車隊智慧與營運端)

> 使用者:**Fleet Manager(客戶端車隊管理者)**
> 商業權責:實際營運車隊;透過 Configuration 介面針對 Passenger / Medium Vehicle / Heavy Duty 三種車型微調參數

### 主選單:`Dashboard` [2]

**畫面 / 面板 (Panels)**:

| Panel | 包含欄位 / 標註 |
|-------|----------------|
| `Online Devices` | `Total Devices in Service` + 百分比圖表 + 標註 `Driver Status online` |
| `Trip Summary` | `Trips` / `Driving Distance (Km)` / `Driving Time (Hours)` + 標註 `Trip Status` |

**地圖區塊 (Map View)**:
- 標註功能:`GPS info (speed, longitude, latitude, heading, altitude)` [2]

**設備列表 (Device List)**:
- 搜尋與操作按鈕:`Q Search unit name` / `All Status (下拉選單)` / `Clear` / `Q (搜尋圖示)` / `C (重新整理圖示)` / 分頁切換 `< 1 >` `5 / page`
- 顯示狀態:`Results: [數字]`
- 表格欄位 (Table Headers):`Asset ID` / `Status` (如:`Offline`) / `Live View`
- 列表內連結:`Parking Photo`

### 主選單:`Trips` [2]
- 次選單:`Trip List` [2]
- 次選單:`Trip Report` [2]

### 主選單:`Safety` [2]
- 次選單:`Events` [2]
- 次選單:`Retrieved Files` [2]
- 次選單:`Safety Report` [2]

### 主選單:`Management` [2]
- 次選單:`Devices` [2]
  - 搜尋與操作按鈕:`Q Search unit name` / 下拉選單 / `More` / `Clear` / `Q (搜尋圖示)` / `+New Group` / `C (重新整理圖示)`
  - 顯示狀態:`Results: [數字]`
  - 表格欄位 (Table Headers):
    - `Asset ID`(標註 `Devices identification`)
    - `Status`
    - `Serial Number`
    - `Vehicle Type`
    - `Plan Type`(標註 `Type (STD/Adv/Pro)`)
    - `Activated Since`
    - `App Version`
  - 列表內操作圖示:
    - 視訊攝影機圖示 → `Live View`
    - 電話圖示 → `Online Call`
    - `P` 圖示 → `Parking Photo`
- 次選單:`Geofences` [2]

### 主選單:`Configurations` [2]
> PDF 未列子層細節 — 但前一輪回答有提到可控參數:
> - Device Settings(Volume / KPH / Parking Photo / RFID 音效提示)
> - Sensor Event Detection
> - AI Event Detection
> - 交通標誌與號誌偵測
> - 超速與安全評分
> 這些是針對 Passenger / Medium Vehicle / Heavy Duty 三種車型分別設定

---

## 三、Elastic Portal 模組(給選擇 VisionMax Elastic 方案的客戶套用)

> 來自前一輪 NotebookLM 萃取(同一份 PDF):
> 神達提供給「Storage 自管」客戶的現成 UI 模組

| 模組 | 用途 |
|------|------|
| `Device Info` | 設備基本資訊呈現 |
| `Configuration` | 客戶端的設定面板(對應 Fleet Portal Configurations) |
| `Health Report` | 設備健康度報表 |
| `Live` | 即時影像/狀態 |

> ⚠️ PDF 在此 Portal 沒列具體 sub-section,只列模組名稱

---

## 四、NotebookLM 提出的 PM Action Items

### Task 1 — 前端 / UI 團隊(Lucy / Ben)
請以這份 PDF 原始架構表為基準,盤點目前 Figma UI Spec,確認是否有任何未經正式決策就多出來的「幽靈按鈕」或「幽靈次選單」,確保交付規格與原始系統架構一致。

### Task 2 — 後端 / API 團隊(Spencer)
針對 Fleet Portal → Management → Devices 下所列出的:
- `Asset ID`, `Status`, `Serial Number`, `Vehicle Type`, `Plan Type`, `Activated Since`, `App Version`
- 以及 `Online Call` 功能

請確認對應的 API Endpoints 都能完整吐出這些欄位資料,避免前端缺少 Data Binding。

---

## 五、PDF 未涵蓋(需要走 Live UI 補的地方)

| 區塊 | PDF 給了什麼 | 還缺什麼 |
|------|--------------|---------|
| Master Dashboard | 4 個 Panel 的欄位 | 每個欄位點擊後跳哪裡?Filter 怎麼設? |
| Master Analysis | 只有名稱 | 完全沒寫子層 |
| Master Inventory | 只有名稱 | 表格欄位、操作按鈕都沒寫 |
| Fleet Configurations | 高層分類 | 每個參數的範圍、預設值、車型差異 |
| Fleet Trip List / Report | 只有名稱 | 表格欄位、Filter、Export 等操作都沒寫 |
| Fleet Safety > Events | 只有名稱 | 事件類型、欄位、嚴重度標示都沒寫 |
| Fleet Geofences | 只有名稱 | 圍欄類型、新增流程、Trigger 設定都沒寫 |
| Elastic Portal sub-sections | 只有 4 個模組名稱 | 每個模組的內部結構都沒寫 |

→ **Brian 要的「對客戶解釋每個按鍵」要走 Live UI 補完**,PDF 是 60% 骨架,40% 要實機驗證。

---

## NotebookLM 結尾追問

> *「請問您接下來需要我針對這份架構中的哪一個特定次選單(例如 Management > Devices 或 Dashboard),進一步去比對 Jira 上現有的 Bug 或客戶需求(Ticket)嗎?」*

---

# 第六章:Live UI Walkthrough 補完(Brian Task)

> 目的:對著實際 portal UI,補上 PDF 沒寫的按鍵 / 欄位 / 互動,直到能完整對客戶解釋。
> 走法:每個 sub-menu 一節,每個畫面元素都記 What / Why / Caveat。
> 所有「⚠️ 待驗」標籤要在後續 Coffee Chat / 點擊驗證後解除。

## 6.0 Fleet Portal 左側 Nav 完整地圖(對比 PDF)

```
2026Q1_user_try (fleet 選擇器,PDF 漏)
─────────────────
Fleet Operation                 (PDF 漏的群組標題)
├─ Map Overview                  (⚠️ PDF 漏)
├─ Dashboard                     ✅
├─ Trips ▾
│  ├─ Trip List                  ✅
│  └─ Trip Report                ✅
├─ Safety ▾
│  ├─ Events                     ✅
│  ├─ File Retrieval             (⚠️ PDF 寫 "Retrieved Files",名稱不一致)
│  ├─ Safety Reports             (⚠️ PDF 寫 "Safety Report",單複數不一致)
│  └─ Coaching                   (⚠️ PDF 完全漏)
├─ Management ▾
│  ├─ Devices                    ✅
│  └─ Geofences                  ✅
└─ Configurations                ✅

Administration                  (PDF 漏的整個群組)
├─ Accounts & Permissions        (⚠️ PDF 漏)
├─ Fleets                        (⚠️ PDF 漏)
├─ Device Usage                  (⚠️ PDF 漏)
└─ User Activity Logs            (⚠️ PDF 漏)

(底部 4 圖示:👤 / ⚙ / ❓ / 🔔  全部 PDF 漏)
```

→ **Nav 層級 PDF 漏掉率約 50%**(8 個 sub-menu / 群組標題沒寫)

---

## 6.1 Fleet Portal > Trips > Trip List

**URL**: `/trips/trip-list`
**樣本資料**: 104 筆 trips,11 頁,fleet `2026Q1_user_try`(Q1 內部試用)

### 頁首篩選列
| 元素 | What | Why | Caveat |
|------|------|-----|--------|
| `Search device name or driver name.` | 搜尋過濾 | 多設備時找特定車 | ⚠️ fuzzy or exact? |
| 日期範圍(預設 30 天) | 篩 trip 時間 | — | 跟 Events 預設(1 天)不同 |
| `All Trip` 下拉 | trip 狀態篩選 | 只看 Live 或 Finished | ⚠️ 待驗下拉選項 |
| `Clear` | 清空篩選 | — | — |
| 🔍 藍色搜尋鍵 | 套用篩選 | — | ⚠️ 自動 apply 還是必須按? |
| `Results: N` | 符合筆數 | — | — |
| `Export` | 匯出 trip 清單 | 給保險 / 主管 | ⚠️ 格式 / 範圍待驗 |
| ↻ Refresh | 重抓 | — | — |

### 表格欄位
| 欄位 | 顯示 | 備註 |
|------|------|------|
| `Trip` | ▶ `Live` 綠 / 🚩 `Finished` | Live 沒 End Date |
| `Start Date & Time` ↕ | — | 可排序 |
| `End Date & Time` ↕ | `-` (Live) | 可排序 |
| `Asset ID` | 設備 ID | — |
| `Driver` | 頭像 + 名 / `Not Recognized` | DMS / RFID 沒辨識會顯示 Not Recognized |
| `Mileage (KM)` ↕ | `-` (Live) | — |
| `Duration` ↕ | `-` (Live) | — |

### 分頁
- `<` `>` + 頁碼 + `10 / page` 下拉(⚠️ 待驗其他選項)

---

## 6.2 Fleet Portal > Trip Detail

**URL**: `/trips/trip-list/trip-detail/{tripId}`
**範例**: trip 7079470 (J0325360006) / trip 7028714 (L3024290010 自己)

### 頁首
- Breadcrumb: `Trip List > Trip Details`
- `← {Asset ID}` 返回 + 顯示設備
- 🔵 `📹 Retrieve Video` 按鈕 — **客戶最高頻動作**,⚠️ 對應 VMX-7227(調閱卡死 P1 bug)

### 中央地圖
- 軌跡線(藍 / 橘 / 紅 三色)— **顏色含義 ⚠️ 待驗**(假說:藍 = 正常 / 橘 = 警示 / 紅 = 違規)
- 群集 pin 數字(N 個事件聚一處)
- 地圖控制:⛶ 全螢幕 / `+` / `-` / ◇ 圖層

### 右側 Trip Summary
- Driver / Vehicle / Date & Time(Start + Duration + End)/ Mileage (KM)
- 若 Vehicle = `-` 表示沒設 vehicle profile,可從 Management > Devices 補

### 右側 Events Timeline
- `Results: N`(不含 Start / End)
- Export / Refresh

**Event 類型對照**(全 fleet 累積 + KB 對照):

| Event | 圖示 | 性質 | KB 對應 | 有影片? |
|-------|------|------|---------|--------|
| `Start` | 🔵 | trip 起點 | — | — |
| `End` | 🔴 + P | trip 結束(P 推測 = Parking Photo) | — | — |
| `DMS Started` | 文件✓ | 系統事件:DMS calibration 完成 | 20 km/h × 15s | ❌ |
| `ADAS Started` | 車形 | 系統事件:ADAS calibration 完成 | 60 km/h × 3 min | ❌ |
| `Speed Sign Violation` | 標誌 | 違規:超速 | KB 9 Traffic Sign(TW 唯一支援的種類) | ✅ |
| `Power Outage` | 相機+X | 設備斷電 | 對應「電源接線盲區」(B+/ACC 接錯) | ⚠️ 待驗 |
| `Harsh Braking` | 📈 | 違規:急煞 | KB 8 Sensor events(>11 km/h + >0.45G) | ✅ |
| `Stop and Go` | 🚗 | 違規:跟車過近 | KB 5 ADAS event | ✅ |

---

## 6.3 Fleet Portal > Safety > Events(列表頁)

**URL**: `/safety/events`
**樣本**: 04/29 一天 = 29 events
**預設日期**: 只今天(跟 Trip List 預設 30 天**不同**)

### 頁首
- 🔽 `Filter` 按鈕(⚠️ 待驗篩選維度)
- 日期範圍(預設今天)
- `Sort by event` 下拉(⚠️ 其他排序選項待驗)
- `Export Events` — 跟 Trip List 的 `Export` 不同名
- ⚙️ 齒輪(⚠️ 待驗)
- ↻ Refresh
- 🟦 Grid view / ☰ List view 切換

### Event Card 元素
- ☐ 左上 checkbox(批次操作)
- 影片縮圖 + ▶(系統事件 = 山形占位圖,違規事件 = 真實縮圖)
- 縮圖內嵌時戳浮水印
- 事件圖示 + `事件名稱` + 🔵 點(⚠️ 點 = 未檢視?)
- `179 Days` ← **保留剩餘天數**(已驗證,見 6.4)
- 🔖 書籤
- 🗑️ 紅垃圾桶刪除(⚠️ 與 Detail 頁的 `Discard event` 名稱不一致)
- Driver / Asset ID / 時間

### 4/29 全 fleet event 分布
| 類型 | 數量 | 性質 |
|------|------|------|
| Speed Sign Violation | 13 | 違規 ⭐ 主流 |
| DMS Started | 7 | 系統事件 |
| ADAS Started | 5 | 系統事件 |
| Stop and Go | 3 | 違規 |
| Harsh Braking | 1 | 違規 |
| **合計** | **29** | — |

→ ⭐ **客戶要解釋的**:DMS/ADAS Started 是「狀態事件」不是違規,要會講清楚

---

## 6.4 Fleet Portal > Safety > Event Detail(單筆事件深入頁)

**URL**: `/safety/events/detail/{uuid}`
**樣本**: Speed Sign Violation @ J0325360006 04/29 11:52:52

### 頁首 Action Bar
- ← 返回
- 🟢 `Minor` 嚴重度徽章(⚠️ 推測還有 Major / Critical 待驗)— **PDF 完全沒提 Severity**
- 事件名稱 + 🔖 書籤
- 🔴 `Discard event`(永久丟棄,跟 Card 的 🗑️ 不同名)
- 💬 `Comments`(留言)
- 🔵 `Download`(下載影片) — **客戶最高頻**

### 左側資訊
- Driver / Date & Time / Asset ID
- ⏰ **`Expire in 179 days`** ← ✅ **保留期 = 180 天倒數,過期影片永久刪**
- Mini-map + GPS 詳細(Lat/Long / Heading / Altitude)
- 🔗 `Trip details...` 回連到該 trip
- 🎚️ `Add to coaching material` toggle ← 連到 `Coaching` sub-menu(PDF 漏的功能在這)

### 右側雙鏡頭
**Road-Facing Camera**(ADAS):黃線車道 + 紅框前車
**Driver-Facing Camera**(DMS):7 個白框標籤即時顯示

> 👁️ DMS 偵測標籤(KB 6 完整對照):
> `CALL` / `TXT` / `DSY`(distraction) / `DRP`(drop / 打瞌睡) / `ALERT` / `BELT`(安全帶) / `SMK`(吸菸 — ⚠️ 不在官方 list,Beta)

**綠色 debug overlay**(影片內嵌技術資訊):
- Road-Facing: SDK 名 / `CamApp` 版本 / `MiAIApp` 版本 / GPS 訊號 / FPS / 相機溫度 / `Calb`(校正)/ `CalbStatus`
- Driver-Facing: GPS / FPS / Gyro / B-/R- 三軸 / `EyeStableRate`(眼睛穩定率)/ `CalbStatus`

> ⚠️ **AI debug overlay 應該不對客戶顯示,但這個 fleet 看到 = 內部測試 fleet 開了。客戶 fleet 應確認關閉**

**底部浮水印**:時間 + 速度 + GPS + **設備機型(`K220` / `K245` 等)**

### 影片控制
- ▶/⏸ / 🔇 / 拉桿 / 剩餘時間 / ⊞(⚠️ 待驗,可能單窗/雙窗切換)

### 底部圖表(forensic)
- Tab `Speed`(GPS 速度時間序列,Y 軸 0-60+ km/h)
- Tab `Acceleration`(加速度,對應 G-Sensor 門檻)
- Legend: 藍實線 = `GPS Speed` / 灰虛線 = `No GPS`

---

## 6.5 PDF 不一致 / 漏掉清單(累積至本節)

| # | 問題 | 嚴重度 |
|---|------|------|
| 1 | Sub-menu 名稱 `Retrieved Files` vs 實際 `File Retrieval` | 中 |
| 2 | Sub-menu 名稱 `Safety Report` vs 實際 `Safety Reports` | 低 |
| 3 | `Coaching` sub-menu 完全沒列 | **高** |
| 4 | `Map Overview` 主選單沒列 | 高 |
| 5 | 整個 `Administration` 群組(4 個子項)沒列 | **高** |
| 6 | 三層方案說法(Web/API/SDK)vs PDF 兩層方案(Server-to-Server / Elastic) | **高** |
| 7 | Trip Detail 頁所有元素 | **高** |
| 8 | Event Detail 頁所有元素 + Severity 概念 | **高** |
| 9 | AI debug overlay 不該對客戶顯示 | 中 |
| 10 | Card 上 `🗑️ 刪除` vs Detail 頁 `Discard event` 不一致 | 中 |
| 11 | Trip List 預設 30 天 vs Events 預設 1 天 | 低 |
| 12 | `Export` (Trip List) vs `Export Events` (Events) 命名不一致 | 低 |

→ ⭐ **可以提案做一張「PDF 補強 Wiki ticket」**,把以上 12 點交給 Lucy / Brian 排版回 PDF

---

## 6.6 客戶常見問題彙編(累積至本節)

### 關於 Trip
- Q「為什麼有些 trip 顯示 `Not Recognized`?」→ DMS 沒辨識到臉 / RFID 沒刷
- Q「為什麼 Live trip 沒 Mileage?」→ trip 結束才結算
- Q「Export 格式?」→ ⚠️ 待驗(CSV / Excel)
- Q「軌跡顏色?」→ ⚠️ 待驗(假說:藍 = 正常 / 橘 = 警示 / 紅 = 違規)
- Q「Vehicle = `-`?」→ 沒設 profile,去 Management > Devices 補
- Q「Power Outage 是設備壞了嗎?」→ 多半是安裝錯線(B+/ACC 綁一起),不是設備故障

### 關於 Event
- Q「ADAS / DMS Started 算違規嗎?」→ 不是,系統狀態事件
- Q「`179 Days` 是什麼?」→ 影片保留剩餘天數,過期永久刪
- Q「能刪除事件嗎?」→ 可以,但⚠️ 不可逆 + 影響保險,建議用 🔖 + Filter
- Q「為什麼有的事件沒影片?」→ 系統事件不存影片,只記時間
- Q「Severity 怎麼算?」→ ⚠️ 待 Coffee chat 驗(可能影像 + 速度 + 加速度演算法)
- Q「綠字 debug 訊息客戶會看到嗎?」→ ⚠️ 待驗,應該只在內部 fleet 開
- Q「Discard event vs 🗑️ 刪除?」→ ⚠️ 待驗(可能 Discard = 標記忽略,Delete = 連影片刪)
- Q「能延長保留期嗎?」→ 找 MAU / 主管,預設 180 天
- Q「Add to coaching material?」→ 加進 `Coaching` 給駕駛培訓用

---

## 6.7 走過的頁面進度表(逐項勾)

### Fleet Portal
- [x] Trip List
- [x] Trip Detail
- [x] Safety > Events(列表)
- [x] Safety > Event Detail(單筆)
- [ ] Trip Report
- [ ] Map Overview
- [ ] Dashboard
- [ ] Configurations
- [ ] Management > Devices
- [ ] Management > Geofences
- [ ] Safety > File Retrieval
- [ ] Safety > Safety Reports
- [ ] Safety > Coaching
- [ ] Administration > Accounts & Permissions
- [ ] Administration > Fleets
- [ ] Administration > Device Usage
- [ ] Administration > User Activity Logs

### Master Portal
- [ ] Dashboard
- [ ] Analysis
- [ ] Management > Inventory
- [ ] (其他可能未列入 PDF 的)

---

## 6.8 待驗清單(統一收斂,後續 Coffee Chat / 點擊解掉)

### 找 Lucy(UI / 前端)
- 軌跡線顏色含義
- Severity 等級總共幾級 / 怎麼判定
- AI debug overlay 在客戶 fleet 是否該關
- `Discard event` vs 🗑️ Delete 的差異
- Trip List `All Trip` 下拉、Sort、`10/page` 下拉的所有選項
- ⚙️ 齒輪圖示功能

### 找 Spencer(API / 後端)
- 影片保留期 180 天的儲存策略 / 是否可調
- Export 格式 / 範圍
- `Comments` 功能的存儲位置 / 通知機制

### 找 Mori(硬體)
- Camera 溫度 58.5°C 算正常嗎?多少會 throttle?
- FPS 3.3 / 0.9(從 debug overlay 看到)是不是真實 frame rate?

### 找 Brian(主管)
- 提「PDF 補強 Wiki ticket」可不可推
- Coaching 功能對主管的實際使用流程

---

# 第七章:Master Portal 7 頁完整盤點 + 系統地圖綜合

> 走完日期:2026-04-30
> 走過總數:Fleet Portal 19 頁 + Master Portal 7 頁 = **26 頁**
> URL 根:`portal.visionmaxfleet.com`(注意 `portal.` 子網域,不是 `www.`)

## 7.0 Master Portal 左側 Nav 完整地圖

```
Master Portal Nav
├─ Dashboard                       ✅ PDF 有
├─ Analysis                        ✅ PDF 有
├─ Management ▾
│  ├─ Inventory                    ✅ PDF 有
│  ├─ Diagnostics                  ⚠️ PDF 漏
│  ├─ Fleets                       ⚠️ PDF 漏
│  └─ User Account                 ⚠️ PDF 漏
└─ User Activity Logs              ⚠️ PDF 漏
```

→ Master Portal 共 7 頁,**PDF 只列了 3**(Dashboard / Analysis / Inventory)。漏掉率 **57%**。

---

## 7.1 Master Portal > Dashboard

| | |
|---|---|
| **URL** | `portal.visionmaxfleet.com/dashboard` |
| **頁面用途** | 跨 fleet 設備管理總覽(經銷商視角) |

**4 個 Panel**:

| Panel | 內容 |
|-------|------|
| Total Devices | 46(43 Assigned + 3 In Inventory)donut 圖 |
| Healthy / Unhealthy | 24 / 5 + Issue Type 5 類:**Location / Sensor / Camera / MiAI / Footage Storage** |
| Activated By Fleets | 42 Activated / 1 Not Initiated |
| Total Fleets | 8 fleets,Top 5(MDT DQE 15 設備最多) |

→ 跟 Fleet Portal Dashboard 完全不同視角:Master = 設備池總管,Fleet = 車隊運營者

---

## 7.2 Master Portal > Analysis

| | |
|---|---|
| **URL** | `/analysis` |
| **頁面用途** | 期間設備分配 / Plan Type 變化 |
| **預設範圍** | 過去 7 天 |
| **2 Tabs** | `Assigned Device`(active) / `Fleets` |
| **目前面板** | Plan Types 折線圖 |

⭐ **新發現:Plan Type 共 4 種** — `Suspend` / `Standard` / `Pro` / `Advanced`(Fleet Portal Devices 頁只看到 Pro)

---

## 7.3 Master Portal > Management > Inventory

| | |
|---|---|
| **URL** | `/management/inventory` |
| **頁面用途** | 設備池(待分配 vs 已分配) |
| **2 Tabs** | `Devices in Inventory`(active,3 台)/ `Active in Fleets` |
| **欄位** | **IMEI** / Serial Number / Model / Fleet / Last Connection / **Recalls** / MiAI Version |
| **動作** | + New Device / Export / ↗ Assign / ⬆ Upload |

⭐ 新概念:
- `IMEI` 顯示(Fleet Portal 沒露)
- `Recalls`(硬體召回次數)
- Inventory vs Active in Fleets 二元

3 inventory 設備:K245 / K145 / K220(全 fleet "MDT" 待分派)

---

## 7.4 Master Portal > Management > Diagnostics

| | |
|---|---|
| **URL** | `/management/diagnostics` |
| **頁面用途** | 跨 fleet 設備健康檢查 |
| **2 Tabs** | `Device Health Check`(active)/ `Device Activity` |
| **2 Stat Cards** | No issue: **33** / Has Issue: **5**(合計 38)|
| **欄位** | Serial Number / Model / **Current Owner**(fleet)/ Device Health Check / Report Timestamp |
| **頁面註記** | "Excluded devices that have not been activated or have never connected to VisionMax server." |

→ 對應 Master Dashboard 的 Healthy/Unhealthy 24/5(Inventory 也算)

---

## 7.5 Master Portal > Management > Fleets

| | |
|---|---|
| **URL** | `/management/fleets` |
| **頁面用途** | **跨 fleet 列表**(管理者視角)|
| **欄位** | Fleet ID / **Account(s)** / **Device(s)** / Phone / Address / Created |
| **Result: 8 fleets** | 含 2026Q1_user_try(8 帳號 / 10 設備) / AIOTBC VTD / **MDT DQE(15 設備最多)** / MDT FT / 3 個 test fleets |
| **動作** | + **New Fleet**(經銷商核心動作)/ + New fleet account |

⭐ 跟 Fleet Portal「Administration > Fleets」對比:

| 項目 | Master Portal Fleets | Fleet Portal Admin > Fleets |
|------|----------------------|---------------------------|
| 視角 | 多 fleet 列表 | 單 fleet 設定頁 |
| 動作 | 新建 fleet / 跨比較 | 編輯自己 fleet 的個資 |

---

## 7.6 Master Portal > Management > User Account

| | |
|---|---|
| **URL** | `/management/user-account` |
| **頁面用途** | Master 層級帳號管理(經銷商員工)|
| **欄位** | User Name / Account Email / **Role** / Status / Created |
| **Result: 14**(比 Fleet Portal A&P 8 多)| |
| **Roles** | Admin + **Viewer**(至少 2 種,Fleet 只看到 Admin)|
| **Status** | Active / **Deactive** |

Email domains:`mitacmdt.com` / `mic.com.tw` / `visionmaxfleet.com` / `gmail.com` — 跨組織訪問者

---

## 7.7 Master Portal > User Activity Logs

| | |
|---|---|
| **URL** | `/userActivityLogs/list` |
| **頁面用途** | Master 層級登入登出稽核 |
| **欄位** | Date & Time / User Name / Email / Type / Action / **IP Address**(完整顯示)|
| **Result: 32**(vs Fleet Portal 88,較少)| |
| **跟 Fleet 版差異** | **沒有 Fleet 欄位**(因為跨 fleet)|

---

## 7.8 完整系統地圖(綜合 26 頁)

### 兩層 Portal 結構

```
┌────────────────────────────────────────────────────────────────┐
│                   Master Portal                                 │
│                portal.visionmaxfleet.com                       │
│                                                                  │
│  使用者:Dealer / 經銷商 / MAU 管理者                            │
│  視角:跨 fleet 設備池總管(Inventory + Allocation + 健康)       │
│                                                                  │
│  ・Dashboard ─ 跨 fleet 統計                                    │
│  ・Analysis ─ Plan Type 演變                                     │
│  ・Management ─ Inventory / Diagnostics / Fleets / User Account  │
│  ・User Activity Logs ─ 跨 fleet 稽核                            │
└────────────────────────────────────────────────────────────────┘
                             │
                             │  「分配 / 開通」
                             ▼
┌────────────────────────────────────────────────────────────────┐
│                   Fleet Portal                                  │
│              www.visionmaxfleet.com                            │
│                                                                  │
│  使用者:Fleet Manager(客戶端) + 內部 PM(Kenny)               │
│  視角:單一 fleet 內運營(Trip + Event + Coaching)               │
│                                                                  │
│  ・Map Overview / Dashboard                                     │
│  ・Trips ─ List / Detail / Report                                │
│  ・Safety ─ Events / Detail / File Retrieval / Reports / Coaching│
│  ・Management ─ Devices / Drivers / Vehicles / Geofences         │
│  ・Configurations(5 tabs)                                      │
│  ・Administration ─ A&P / Fleets / Device Usage / Activity Logs   │
└────────────────────────────────────────────────────────────────┘
                             │
                             │  「裝在車上 / 駕駛開」
                             ▼
                ┌─────────────────────────────┐
                │   Edge:K-Series 車機         │
                │   K145c / K220 / K245 /     │
                │   K245C / K265              │
                └─────────────────────────────┘
```

### 3-Tier User / Account Model

| 層級 | 管理位置 | 對象 | 範例 | 權限範圍 |
|------|---------|------|------|---------|
| **L1** | Master Portal > User Account | 經銷商員工 | andrew.cheng / mio.msf | 跨 fleet |
| **L2** | Fleet Portal > A&P | 單 fleet portal 使用者 | brian / pokai.huang / Righter | 單一 fleet |
| **L3** | Fleet Portal > Drivers | 駕駛員(實際開車的人) | Kenny Huang(IC `3bbc8453`) | 不上 portal,只被識別 |

### Fleet Portal 三大 Entity 模型

```
┌─ Device(車機)── K-series 硬體 / App Version / ADAS+DMS Health
│    │
│    ├─ via Vehicle Profile binding
│    ▼
├─ Vehicle(車輛)── VIN / Year / Make / Model / Vehicle Type
│
└─ Driver(駕駛)── Employee ID / IC Card S/N(RFID)/ Email
```

每個 **Trip / Event** 都 reference 上述三者(Asset ID / Vehicle / Driver)。

### 共用概念跨 Portal 對應

| 概念 | Master 看到的 | Fleet 看到的 |
|------|--------------|-------------|
| Device 健康度 | Issue Type 5 類:**Location / Sensor / Camera / MiAI / Footage** | ADAS AI Health + DMS AI Health(只 2 欄位) |
| Plan Type | 4 種:Suspend / Standard / Pro / Advanced | 只看到 Pro |
| Fleet ID | 8 個全部 | 只看到自己選的 |
| Inventory | 有完整管理頁 | ❌ 完全看不到 |
| IMEI | ✅ 顯示 | ❌ 不顯示 |
| Recalls | ✅ 顯示 | ❌ 不顯示 |

### 資料流:設備 → Cloud → Portal

```
[Edge 車機] ─ WebSocket / HTTPS / MQTT ─→ [VisionMax Server]
                                              │
                                              ├─→ AWS S3(影片 / 照片)
                                              ├─→ MySQL(metadata / events)
                                              └─→ MiDM(韌體 / Custom ID 派送)
                                              │
                                              ▼
                                          API + Portal UI
                                     (Master + Fleet 共用 backend)
```

## 7.9 PDF 漏掉率統計

| 區域 | 漏掉率 | 備註 |
|------|--------|------|
| Fleet Portal Nav 結構 | ~50% | 19 頁中 PDF 列 9 |
| Master Portal Nav 結構 | ~57% | 7 頁中 PDF 列 3 |
| 頁面深度(按鍵 / 欄位 / Tab) | >80% | 各頁細節幾乎全沒寫 |
| 跨 Portal 概念對照(Plan Type / Issue Type 等) | ~70% | 共用概念沒對到 |
| **整體系統理解** | **~70% 沒覆蓋** | |

→ Brian Wiki 補強 ticket 有滿滿論據

## 7.10 全 26 頁進度表(總)

### Fleet Portal(19 / 19 ✓)
- [x] Map Overview / Dashboard
- [x] Trips: List / Detail / Report
- [x] Safety: Events / Event Detail / File Retrieval / Safety Reports / Coaching
- [x] Management: Devices / Drivers / Vehicles / Geofences
- [x] Configurations
- [x] Administration: Accounts & Permissions / Fleets / Device Usage / User Activity Logs

### Master Portal(7 / 7 ✓)
- [x] Dashboard / Analysis
- [x] Management: Inventory / Diagnostics / Fleets / User Account
- [x] User Activity Logs

## 7.11 走完之後最該深挖的 5 件事(收斂下一階段)

1. **ADAS Failure 真因投查**(Master Diagnostics 顯示 5 台 Has Issue,Fleet Portal Devices 看到 8/10 ADAS Failure 含 Kenny 的 L3024290010)→ 對 VMX-7404 是直球
2. **Plan Type 4 種差異**(Suspend / Standard / Pro / Advanced)→ 商業面 Coffee Chat 給 Brian
3. **Contract Fleets 概念**(Fleet Portal Admin > Fleets 第二個 tab)→ 客戶結構搞清楚
4. **MiAI Issue 那 1 台是哪台**(Master Dashboard Issue Type 顯示)→ 可能跟 Kenny 的 L3024290010 同根因
5. **Configurations 5 tabs 內容**(目前進去看到空,需要點開驗證預設值)→ NotebookLM Task 2 的「不同車型預設參數建議書」素材源

---

# 第八章:商業模型 — Plan Type 4 種 + Contract Fleet 真相

> 取得日期:2026-04-30
> 來源:NotebookLM 鎖定《VisionMax_架構及整合方式_260123.pdf》單一來源萃取 + Live UI 互補
> 為什麼重要:這章是「商業面」的權威定義,**對 Sales / 主管溝通時不能講錯**

## 8.1 Plan Type 4 種完整解析

PDF 來源:投影片「Subscription Plans (For TSP)」

| Plan | 包含功能 | 定價(per device/month) | 邊緣端(Edge)行為 |
|------|---------|------------------------|------------------|
| **Standard**(基礎階) | `Sensor Event Detection` + `VMX VT Cloud` + `GPS + Video` | **$5(13 cams) / $7(47 cams)** | **強制關閉所有 MiAI(ADAS/DMS)模型**,只留 G-Sensor 觸發錄影,以節省設備 CPU 算力與雲端儲存成本 |
| **Advanced**(中階) | Standard 全部 + **`ADAS Event Detection`**(FCW / LDW / Stop and Go / Tailgating 等車外輔助) | **$7(13 cams) / $9(47 cams)** | 釋放**前向鏡頭(Outward Camera)**AI 算力,**嚴禁開啟車內 DMS 監控** |
| **Pro**(最高階) | Standard + Advanced 全部 + **`DMS Event Detection`**(全 AI 包) | (PDF 內有定價,本次未滾到 — 待補) | 全 AI 開啟,前向 + 駕駛艙鏡頭都運算 |
| **Suspend**(停用) | PDF 未列細節 | — | 推測 = 帳號暫停,設備保留但不收費也不上傳。**待 Coffee Chat Brian 確認** |

> ⚠️ **「13 cams / 47 cams」**含義 ⚠️ 待驗。可能是:鏡頭硬體規格(K220 雙鏡頭 vs K245 多鏡頭)/ fps / 通道數。**Coffee Chat Brian 對焦**

### 升級邏輯(從 Standard → Advanced → Pro)

逐層解鎖:
- Standard:G-Sensor only(物理感測)
- Advanced:+ 前向 AI(ADAS — 路面安全)
- Pro:+ 駕駛艙 AI(DMS — 駕駛行為)

> Suspend 不在升級鏈內,是「凍結狀態」

### PM 系統聯動洞察(NotebookLM 自動分析)

1. **業務端落差(Sales Gap)**
   - **問題**:業務常希望用 Standard 的價格讓客戶「試用」Pro 的功能
   - **後果**:帳款系統(Billing)跟實際開放權限不符
   - **PM 紅線**:**升降級必須嚴格透過系統後台或 API 進行變更,不能 hack**

2. **Edge 端資源浪費**
   - **問題**:如果 Cloud 端 Plan Type 是 Standard,但車機端的 Camera App 卻沒有把 MiAI(DMS/ADAS)模型 Unload
   - **後果**:設備依然在白白消耗 CPU 算力 + 發熱
   - **客戶感知**:嚴重的硬體客訴(發熱 / 當機 / 重啟)

3. **PM 必問問題**
   - 「Standard 客戶的設備上,MiAI 真的有 Unload 嗎?」
   - 「Plan 升級時,Edge 端的 model load / unload 流程順不順?」
   - 「升降級多久生效?(立刻 vs 下次重啟)」

---

## 8.2 Contract Fleet 真相 — PDF 完全沒寫!

### NotebookLM 嚴格盤點 4 種商業情境

| 商業情境 | PDF 承認? | PDF 內證據(若有)|
|---------|-----------|-----------------|
| **1. 經銷商(Dealer / Distributor)** | ✅ 承認 | • 投影片 `Architecture (2/3)`:"This type is **Master**, belonging to the **dealer**, responsible for selling fleet management services and assigning CDRs to each fleet."<br>• 投影片 `VisionMax Elastic (2/4)` 架構圖左下角標 `Distributors Portal` 區塊 |
| **2. 合作夥伴(Partner)** | ❌ **PDF 未列** | 整份文件**未出現 Partner 術語**。針對串接 API 或自建架構的第三方,**PDF 統一用 `customer` 稱呼**(無階層區分) |
| **3. 子車隊(Sub-fleet / Contract Fleet)** | ❌ **PDF 未列** | NotebookLM 搜遍 PDF 沒找到 |
| **4. 外包服務(Outsource Service)** | ❌ **PDF 未列** | 同上 |

### ⭐⭐ 核心警訊(NotebookLM PM 結論原文)

> 「我們的官方架構文件《VisionMax_架構及整合方式_260123.pdf》在商業情境的定義上**極度侷限,僅承認「經銷商 (Dealer)」與「客戶 (Customer)」兩種身分**。
>
> 若業務單位(Sales)對外承諾系統支援『子車隊』或『合作夥伴分級』,**在架構面上將完全失去文件支撐**,RD 也無法依此開出對應的 RBAC(角色權限控制)規格。」

### Live UI vs PDF 的 Gap

**Fleet Portal Admin > Fleets** 頁面上**確實有 `Contract Fleets` tab**(Result: 0,空),且 + 按鈕命名是 `+ New Account`(不是 `+ New Contract Fleet`)。

**這個 gap 三種可能解釋**:

| 可能性 | 說法 | 對 Kenny PM 工作的意義 |
|-------|------|----------------------|
| 1️⃣ **UI 超前 PDF** | RD 已實作,文件還沒更新 | Coffee chat Spencer 確認 RBAC spec 在哪 |
| 2️⃣ **UI 是殘留** | 之前計劃中沒啟用的功能 | 可建議 RD 把 tab 隱藏 / 刪除 |
| 3️⃣ **Account-based 模擬** | `+ New Account` 暗示**用 account 跨 fleet 共用**來模擬 sub-fleet,**不是真的 sub-fleet** | 對 Sales / 客戶要解釋清楚:不是真的 sub-fleet,是 account share |

> ⭐ **可能性 3 最像真相**:從按鈕命名看,Contract Fleet 比較像「我的 fleet 邀請另一個 fleet 的 admin 進來協同管理」,不是真的 hierarchical sub-fleet

---

## 8.3 NotebookLM 自動產出的 PM Action Items

### Task 1 — 海外業務端(Sales / Account Managers)
> 強制對齊銷售話術。**在《VisionMax_架構及整合方式》文件未更新前,業務端不得向客戶承諾原生系統支援「子車隊 (Contract Fleet)」或「外包服務」等階層架構**,避免簽約後 RD 無法交付。

### Task 2 — 雲端架構負責人(Tech Lead — Spencer)
> 評估架構文件的更新需求。如果現行 VisionMax API 實際上已經需要服務 Contract Fleet 場景,則需要把它寫進 PDF + 實作 RBAC spec。

---

## 8.4 Kenny PM 視角的 3 個立即動作

| # | 動作 | 對誰 | 為什麼 |
|---|------|------|-------|
| 1 | 確認「`Contract Fleets` tab 是不是真有功能?還是 UI 殘留?RBAC spec 在哪?」 | **Coffee Chat Brian + Spencer** | 文件 vs UI 不一致,你做為 PM 不能不知道答案 |
| 2 | 點 Contract Fleets 的 `+ New Account` 看 dialog 內容,驗證 Account-based 模擬假說 | 自己 5 分鐘做 | 直接看 UI 比聽說有效 |
| 3 | 跟 Sales 對焦話術:「合約上怎麼描述 Contract Fleet?」 | 海外業務 / Sales 主管 | 客戶買單但 RD 交不出 = 你 PM 會被夾在中間 |

---

## 8.5 待解疑問清單(更新)

> 累積本章新增的 ⚠️ 待驗項目

### Plan Type 相關
- [ ] **Pro 方案完整定價**(本次回答沒滾到 — 回 NotebookLM 補問)
- [ ] **Suspend 方案的詳細定義 + 是否計費**
- [ ] **「13 cams / 47 cams」具體含義**(鏡頭硬體 / fps / 通道?)
- [ ] **Plan 升降級的生效時機**(立刻 / 下次重啟 / 下個帳期)
- [ ] **MiAI Unload 流程是否可靠**(VMX 是否有 ticket 在追)

### Contract Fleet 相關
- [ ] **`+ New Account` dialog 內容**(自己點一下就知道)
- [ ] **`Contract Fleets` tab 的 RBAC spec**(Spencer)
- [ ] **PDF 何時會更新加入 sub-fleet 概念**(Brian)
- [ ] **Sales 合約中對 Contract Fleet 的措辭**(Sales 主管)

---

## 8.6 商業模型整體理解(總結)

```
┌────────────────────────────────────────────────────────┐
│ 神達 PDF 認可的商業關係                                 │
│                                                          │
│  經銷商 (Dealer) ─────────→ 客戶 (Customer)             │
│  Master Portal              Fleet Portal                │
│  (Distributors Portal)      (含 1-N 個 fleet)            │
│                                                          │
│  ─ 銷售車隊管理服務          ─ 實際運營車隊                │
│  ─ 分配 CDR 設備             ─ 在 Configuration 改參數    │
│                              ─ 訂閱 Standard/Advanced/Pro │
└────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────┐
│ UI 上有但 PDF 沒寫的灰色地帶 ⚠️                        │
│                                                          │
│  ・Contract Fleets tab(Fleet Portal Admin > Fleets)    │
│  ・+ New Account 按鈕(暗示 account 跨 fleet 共用)      │
│  ・Partner / Sub-fleet / Outsource 概念                  │
│                                                          │
│  → PM 風險點:Sales 可能用這些灰色地帶銷售             │
│                                                          │
└────────────────────────────────────────────────────────┘
```

→ 這章可以**直接拿給 Brian / 主管當 review 材料**,證明你不只走完 26 頁,還抓到「商業模型 vs 文件」的不一致風險。
