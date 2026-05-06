# Coffee Chat 待問清單

依人分類,問完就劃掉。

## ☕ Brian(Software Head)

### 戰略級
- [ ] **VMX/BMS 同步戰略時程**(6 個月內?具體 milestone?)
- [ ] BMS/VMX 同步我可以扛哪一塊(API 文件 / Fleet portal UI / 客戶溝通)
- [ ] **Roadmap vs Sheet 同步缺口**(Smoking / VLM 等不一致)是否有正式機制
- [ ] HDFE beta 模式想要什麼形式(toggle 切舊版?transition 期?)

### 戰術級
- [ ] Pro / Suspend 完整定價
- [ ] 「13 cams / 47 cams」含義
- [ ] Contract Fleet 真實定義(Portal 上有 tab 但 PDF 未列)
- [ ] PDF 補強 Wiki ticket 推不推
- [ ] MMF 是已 ship 還是 roadmap planned
- [ ] Jira dashboard 4 個 filter 的 JQL
- [ ] **Q2 merge label sweep PM 來扛**(對應 #154 process gap)

## ☕ Mori(硬體)

### 機種對應
- [ ] **K145c / K220 / K245 / K245c / K265 各跑哪顆 Qualcomm chip**
- [ ] Kenny 自己的 K245 屬 Entry / Basic / Advanced 哪個 tier
- [ ] 各機種 frame rate(15 / 30 fps?)

### G-Sensor
- [ ] **Harsh Acceleration / Rollover G 值門檻**(只 lock 4 種,缺這 2)
- [ ] **200 Hz G-Sensor 韌體可行性**(Simon must-have)

### 細節
- [ ] 紅色按鍵語音不一致 — 是哪幾台
- [ ] Private Mode 切換按法
- [ ] K-series spec 對照表(鏡頭 / 算力 / SD 容量)現成文件?

## ☕ Jimmy(AI Inference)

### 對外 vs 內部不一致
- [ ] **Smoking 真實狀態**:KB 沒寫 / Sheet 隱藏 / Roadmap 列 / 4 ticket open — production 到底有沒有?
- [ ] **Yawning 內部測試效果指標**(2026-05-06 會議揭露效果不如預期)
- [ ] VMX-7324 客訴 Smoking 怎麼解
- [ ] **「Burning ADAS / Burning DMS」是什麼意思**(鏡頭過曝?burn-in?typo?)

### 技術深度
- [ ] 各 event 真實 Confidence threshold(memory 是估計值)
- [ ] Sensitivity dial Low / Med / High 真實 debounce / cooldown
- [ ] Yawning validation 卡點
- [ ] **Eating / Drinking** Roadmap 標 2027,HAWK-562 已開,實際進度?
- [ ] Server-side AI 進度(Stage 2/3 何時上)
- [ ] **Face Not Found Issue**(VMX-7404 同根因?)

### 甜頭(送 Jimmy)
- [ ] VMX-7404 ADAS Failure evidence 提交(8/10 設備 / Trip 7028714 vs 7079470)

## ☕ Lucy(UI)

### 模糊 / Rollover
- [ ] 模糊功能 UI 設計時程
- [ ] Rollover UI 設計(VMX-7194 5/6 加 UI)
- [ ] 任務完成主動通知機制

### Portal 視覺
- [ ] **軌跡顏色含義**(藍 / 橘 / 紅)
- [ ] **Severity 等級**(Minor / 推測還有 Major / Critical)
- [ ] 舊 Playback 紅色預告 UI 設計

### 5/6 後續
- [ ] Yawning Fatigue config 開關 UI
- [ ] HDFE「切回舊版」開關設計

## ☕ Spencer(Cloud)

- [ ] **Server-side AI Stage 2/3 進度**(Edge+Server / Server VLM)
- [ ] Master/MAU 模糊 API 開關設計
- [ ] **VMX-6722 文件 / Casebase 同步**(對應 Brian 的雙版本同步戰略)
- [ ] Contract Fleet RBAC spec
- [ ] ADAS Failure 跟 VMX-7404 關聯
- [ ] AI debug overlay 是否該對客戶關閉

## ☕ Tony(韌體 / Akamai 中介)

- [ ] **Akamai CDN PG 失效進度**(Brian 已派工)
- [ ] OTA JSON purge 機制可不可靠

## ☕ Sales 主管

- [ ] 合約中對 Contract Fleet / Sub-fleet 的措辭

## ☕ Wendy ⚠️(身份不明,Hub 第三 tab 提到)

- [ ] **基本身份**:她是哪個部門?跟進什麼客戶?
- [ ] 她對 roadmap 資訊不對稱的具體痛點

→ 找 Brian 確認 Wendy 是誰再去約。
