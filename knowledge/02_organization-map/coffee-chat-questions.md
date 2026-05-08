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
- [ ] **#154 真實 process gap = transition discipline,不是 label**(5/7 校正:VMX-6722 本身有 label `vmx_2026Q2`,jimmy 留 deploy comment 但沒按 transition button)— PM 提改善從「transition 紀律」切入
- [ ] **5/7 揭露 LDWS device-side YOLO Pending 暫緩** — 新 ticket 編號?何時重啟?
- [ ] **5/7 Lens Cover 雙軌維護 RD 成本評估** — Azuga 標準版 vs BMS「車速 > 0」長期維護成本

## ☕ Mori(硬體)

### 機種對應
- [ ] **K145c / K220 / K245 / K245c / K265 各跑哪顆 Qualcomm chip**
- [ ] Kenny 自己的 K245 屬 Entry / Basic / Advanced 哪個 tier
- ✅ 各機種 frame rate — 機體可達 15-30 fps,**對外 only 10 fps**(2026-05-07 已釐清,運算資源限制)

### G-Sensor
- [ ] **Harsh Acceleration / Rollover G 值門檻**(只 lock 4 種,缺這 2)
- [ ] **200 Hz G-Sensor 韌體可行性**(Simon must-have)

### 細節
- [ ] 紅色按鍵語音不一致 — 是哪幾台
- [ ] Private Mode 切換按法
- [ ] K-series spec 對照表(鏡頭 / 算力 / SD 容量)現成文件?

## ☕ Jimmy(AI Inference)

### 對外 vs 內部不一致
- ✅ **Smoking 真實狀態**:KB 標 (in development) / Sheet 隱藏 / Roadmap 列 / 4 ticket open — 對外可講「KB 列開發中」(2026-05-06 校正)
- ✅ **Yawning 內部測試效果指標**(5/6 揭露效果不如預期 / 5/7 補:夜間嘴部辨識不佳,加灰階模型,考慮改辨識整張臉)
- [ ] VMX-7324 客訴 Smoking 怎麼解
- ✅ **「Burning ADAS / Burning DMS」是什麼意思** — typo,實為 **Blurring function**(2026-05-07 已釐清)

### 技術深度
- [ ] 各 event 真實 Confidence threshold(memory 是估計值)
- [ ] Sensitivity dial Low / Med / High 真實 debounce / cooldown
- [ ] Yawning 灰階模型訓練結果 / 「辨識整張臉」server 端切換時程
- [ ] **Eating / Drinking 6/15 重訓進度**(7000+ Edge case,客訴 ID 6652 17 倍量級)— Vincent 加入後 Jimmy 角色變化
- [ ] Server-side AI 進度(Server-side LDWS Q1 deploy / Device-side YOLO 5/7 Pending)
- [ ] **Face Not Found Issue**(VMX-7404 同根因?)5/7 揭露要導入 Head 邏輯

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

## ☕ Wendy Hammond(MiTAC AU 業務端,5/8 已解密)

- ✅ **基本身份**:wendy.hammond@mitac.com.au · MiTAC AU(澳洲)· 跟 Cary Lo 同部門
- ✅ **跟進案件**:PASSENGER BLURRING / 跨 reseller feature reuse / Roadmap sync
- ✅ **資訊不對稱痛點**(5/5 信揭露):「希望 conception stage 早期介入,save work 給 regional teams」— 不要事後告知
- ✅ **跟 Brian 4/30→5/4→5/5 thread 已建立**:Brian 給她 Sheet + AI Roadmap doc 同步入口

→ 不需要再「找 Brian 確認 Wendy 是誰」,身份已知。詳見 [reference_wendy_hammond_identity memory] 跟 stakeholders.md。下次跟她直接對話可問:
- [ ] AU 端 Sheet 同步她實際進去看了沒?頻率?
- [ ] AI feature Roadmap doc Brian 給的版本 vs 我自己整理的 5/7 版有沒有差?
