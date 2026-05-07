# 2026-05-07 AI Weekly Meeting

> **來源**:NotebookLM `5-7 ai weekly.m4a` source(38 sources 全庫查詢結果)
> **整理視角**:Kenny PM 角度,逐 PIC + action item + 跟 5/6 Azuga AI weekly 落差
> **目的**:跟 sheet AI 工作計畫 row-by-row 5/7 snapshot 對齊,找出 sheet 沒寫到 / 寫得不準的訊號

---

## 1. 各 PIC 工作進度報告(5/7 會議揭露版)

| PIC | 5/7 會議報告內容 | Sheet 對應 row | Sheet 寫的 vs 會議揭露 |
|-----|---|---|---|
| **Vincent** | 將 7000 多筆吃東西、喝水、手持物品的誤判照片(Edge cases)加入負向資料庫,集中資源於 6/15 前完成模型 Retrain。同時協助評估將「Head 邏輯」導入原有 Face 演算法 | #45 Pedestrian / #7 Blurring / #43 Camera height | 🚨 Sheet 沒這條,飲食重訓不在他名下 row(#46 Eating Jimmy 才有)— Vincent 角色擴大 |
| **Jieli (竭力)** | 處理 BMS 專案 Lens Cover 獨立邏輯(車速 > 0 才啟動),必須趕上 6/2 交付 | #28 鏡頭遮蔽(VMX-6983 + HAWK-582) | ✓ 對齊。Sheet 5/7 「BMS 正在確認規格」跟會議「車速 > 0」一致 |
| **Jimmy (居明)** | 收集與統整客訴的誤判資料,目前手上已收集 307 張邊緣情境照片,持續擴充 Data pool | #32 Face Not Found / #46 Eating | 部分對齊。#32 sheet 寫 13975 張未 review,跟會議 307 張對不上(可能不同資料集)|
| **Jay (傑)** | 處理 Speed Sign 模型辨識混淆問題,已將訓練參數中「Flip(翻轉)」關閉並重新訓練 | sheet 沒對應 row! | 🚨 **Speed Sign 不在 AI 工作計畫 visible rows**。可能是新增工作或被 hide。會議講「立即執行」 |
| **Eric** | 已完成 ECS 伺服器實例的 Health Checking 機制,解決模型突然消失導致服務掛點問題,已部署生產環境 | #50 VisionMax PROD not blurring(HAWK-578) | ✓ 對齊。Sheet 5/7 寫的「自我健康檢查機制」就是這個 |
| **Spencer** | 負責睜眼率 (Eye opening rate) API 開發,須從 Camera App 到 Server 端完成全鏈路驗證,趕上 6/2 時程 | #4 Eyes Detection(VMX-7309) | 🚨 **Sheet 寫 done done 太樂觀**。會議揭露 Server 端串接還沒完成,要趕 6/2 |
| **Jonathan** | 5/7 會議未具體提及進度 | #47 Rastrac False Speed | Sheet 自己進度推進(Train 99%/Test 98%/100%),但會議沒列為討論點 |
| **Adonis** | 5/7 會議未具體提及進度 | #41 / #48 / #49 / #50 | Sheet 5/7 有 update,但會議沒提 |

---

## 2. 會議決定的 Action Items(4 件 High Priority)

| # | Action | Owner | Deadline | 對應 Sheet row |
|---|---|---|---|---|
| 1 | 飲食與手持物品誤判大重訓(7000+ 筆 Edge case 重訓) | AI 團隊(**Vincent + Jimmy**) | **6/15** | #46 Eating & Drinking(HAWK-562, Jimmy)+ Vincent 加入 |
| 2 | 實作 BMS 專屬 Lens Cover 邏輯拆分(車速 > 0)| Camera App + Jieli | **6/2** | #28 鏡頭遮蔽(VMX-6983 + HAWK-582)|
| 3 | 睜眼率 (Eye opening rate) API 全鏈路驗證 | Cloud / **Spencer** | **6/2** | #4 Eyes Detection(VMX-7309)|
| 4 | Speed Sign 模型修正與重訓(關閉 Flip 參數)| AI 團隊 (Jay) | **立即** | 🚨 **無對應 sheet row** |

---

## 3. 5/7 vs 5/6 Azuga AI Weekly 重大新訊號(落差與警訊)

### 🚨 訊號 A:誤判規模與急迫性暴增 17 倍
- **5/6**:Azuga 會議僅提到少數抽菸/飲食的誤判
- **5/7**:BMS 等客戶端回報的飲食誤判案件量**高達先前的 17 倍**。團隊被迫將原先分批訓練的計畫,改為在 6/15 前「一次性」將萬筆資料集中重訓
- **影響**:#46 Eating & Drinking 從 sheet「預計 6/10 Feasibility results」升級為 6/15 前緊急重訓。Vincent 加入扛
- **客訴 ID**:6652(過去也曾被指為精準度較低的特定帳號 ID)

### 🚨 訊號 B:Lens Cover 規格出現嚴重分歧 → 雙軌維護
- **5/6**:剛與 Azuga 敲定「標準版 Lens Cover」要「解除車速限制」並獨立於 DMS 校正之外
- **5/7**:BMS 卻基於司機休息隱私,強烈要求 Lens Cover 必須「車速 > 0」才能啟動
- **影響**:RD 必須**緊急將標準版與 BMS 版的邏輯拆分雙軌維護**
- **對 PM 啟示**:多客戶 customization 衝突,跨客戶協調成本暴增

### 🚨 訊號 C:夜間與死角防禦機制升級
- **5/7 深入探討 5/6 未觸及的底層優化**:
  - **Yawning 夜間打哈欠**:導入「灰階(Grayscale)模型」,並考慮 Server 端從「辨識嘴巴」改為「辨識整張臉」
  - **Face Not Found 死角**:當夜晚或角度偏斜找不到臉(Face)時,將導入「Head 邏輯(找頭)」作為輔助判定
- **對應 sheet**:#3 Yawning(Jieli)目前 sheet 5/7 空白,但會議揭露其實有「灰階模型重新訓練」這條進度 — sheet 沒寫

### 🚨 訊號 D:LDWS Pending 暫緩 + 開新 ticket
- **5/7 揭露**:「關於 YOLO Lane Detection 導入,因團隊目前資源緊繃,**決議先 Pending 暫緩,並開立新 Ticket 追蹤**」
- **對 5/6 Brian「Q1 已 merge」narrative 的修正**:
  - VMX-6722 Server-side LDWS 確實 Q1 已 deploy(jimmy 3/11 留言確認)
  - 但 5/7 講的是 **device 端 YOLO Lane Detection 的進階改善**,這條是**新工作 + 暫緩**,不是 6722
- **對應 sheet** row 10 #8 LDWS:5/7 寫「pending」**是真實狀態**,但要追的是「新 ticket 在哪 / 何時開」

### 訊號 E:Camera Height 期望值管理(PM 介入點)
- 5/7 揭露:「PM 將提供 20% 的誤差範圍數值以進行期望值管理」
- 對應 #43 Camera height(HAWK-501, Jay+Vincent)
- **Kenny 的 PM 角色任務**:準備 20% 誤差數值給 BMS

---

## 4. 會議提及的 Jira Ticket / 模型版本號 / Fix Version

| 項目 | 詳情 |
|------|------|
| **Fix Version 1.18** | ECS 實例異常的修復機制,5/4 已部署生產環境 |
| **Fix Version 1.1.28** | 同上 — 自我健康檢查機制 |
| **客訴 6652** | 飲食誤判量是過去 17 倍的特定帳號;在先前對話中 6652 也曾被指為精準度較低的特定帳號 ID |

⚠️ 會議沒明確提到 VMX-XXX 票號 — Jira ticket 對應靠 sheet/comment 推

---

## 5. 5/7 各功能盤點(會議揭露版,跟 sheet 對齊)

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

## 6. Action Items(Kenny PM 角度)

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

## 7. 對 sheet AI 工作計畫的修正建議

| Sheet row | 5/7 sheet 寫的 | 5/7 會議揭露 | 該怎麼校正 |
|-----------|---|---|---|
| #3 Yawning | 空白 | 灰階模型重訓 + 考慮辨識整張臉 | 補上「灰階模型訓練中,考慮辨識整張臉」|
| #4 Eyes | done | Spencer 睜眼率 API 還在做,趕 6/2 | 改成「CDR 端 done / Server 端進行中,6/2 交付」|
| #46 Eating | 處理 face not found 尚未評估 | 客訴重災區 17 倍量,6/15 前緊急重訓 | 大改:加入 Vincent + 註明 6/15 deadline + 17 倍量級 |
| #43 Camera height | 拿到小 Brian 影片待測 + 80% CI 調整 | 同上 + PM 提供 20% 誤差範圍給 BMS | 加上 PM 任務 |
| #45 Pedestrian | 整理回覆資訊 | 5/7 未提,5/6 列下半年 Roadmap | 確認是否該移到「下半年 Roadmap」標 |
| (新)Speed Sign | (無) | Jay 立即關閉 Flip 重訓 | 需新增 row |
| (新)LDWS YOLO Lane Detection | 包在 #8 | 5/7 Pending 暫緩,新 ticket | 釐清新 ticket 編號 |
