# AI 工作計畫 16 行 5/7 逐行狀態 snapshot

> 日期:2026-05-07
> 來源:Sheet AI 工作計畫 tab BR(4/30)/ BS(5/4)/ BT(5/7)三欄截圖實況
> 用途:Brian 1on1 / Coffee chat 前 quick reference

## 群組速覽

| 群組 | 行數 | 說明 |
|------|------|------|
| 🟢 推進中(動能清楚)| 5(#47/#32/#28/#43/#41) | 都有 5/7 進度 |
| 🟡 等 release | 3(#48/#49/#50) | 6/2 那波會出去 |
| 🟠 慢但活著 | 5(#7/#4 Eyes/#3 Yawning/#45/#46) | 動能不夠,需 PM 推 |
| 🔴 沒動 / stale | 3(#8 LDWS/#27 VLM/#42 Server AI 統計) | 真 stale 或計畫性 pending |

---

## 🟢 進度推進中

### Row 50 / #47 Rastrac False Speed(VMX-7317 / Jonathan)— **本週最強進度**
- 4/30:loop sign 抓 296 張 + 類似 sign 436 張
- 5/4:訓練 device 分類器 + detection model
- **5/7:236 張 augmentation→4720,分類器 Train 99% / Test 98% / False Speed Event 100% (2/2)。預計轉 onnx→tflite/dlc**
- **狀態:模型訓練完成,等轉 device 端格式即可上線**

### Row 35 / #32 Face Not Found(no Jira / Jimmy)
- 4/30 → 5/4:停在 24699 張待 review(2 週沒動)
- **5/7:13975 張(已處理 ~10700 張,40%+ 進度)+ 加入 head 標籤**
- **狀態:本週剛 unstuck,預計 5/13 完成**

### Row 31 / #28 鏡頭遮擋 Quantatec & BMS(VMX-6983 + HAWK-582 / Jieli)
- 4/30:MiAI SDK 功能完成,交給 Leo 整合
- 5/4:BMS 也需要,當天提供規格確認,預計 6 月上
- **5/7:BMS 正在確認規格(車輛先移動,之後忽略車速,運作 lens cover)**
- **狀態:VMX 端完成 → 擴散到 BMS,規格收斂中**
- 註:HAWK-582 是 5/6 新增 ticket(eric.h assignee)

### Row 46 / #43 Camera height 不穩定(HAWK-501 / Jay+Vincent)
- 4/30:新方法 95% CI 範圍 + 每筆重算
- 5/4:還需更多人拿影片測試
- **5/7:拿到小 Brian 影片待測。改用 80% CI + 比對 TROI 天際線位置減少誤差**
- **狀態:演算法調整中,還在驗證階段**

### Row 44 / #41 Add box around event(VMX-5909 / Jay+Adonis)
- 4/30:Debug view 位置誤差最多到 999 毫秒(video 沒毫秒資訊)
- 5/4:要產影片給 Adonis 做邏輯
- **5/7:已提供可產生 Debug View 資訊的 Python 代碼給 Adonis**
- **狀態:Jay 端產出 → Adonis 接手實作中**

---

## 🟡 等 release(都是 6/2 那波)

### Row 51 / #48 Request event blurry(HAWK-573 / Adonis)
- 4/30:CDN cache 根因,backend 加 timestamp 解決
- 5/4:MR to dev,下次 release (6/2) 解決
- **5/7:Completed (Awaiting Release)**
- 狀態:✅ 修完等 6/2 release。Jira HAWK-573 NEW(transition 沒走),已有 2 commits

### Row 52 / #49 Blurring on-demand fails(HAWK-577 / Adonis)
- 5/4 ≈ 5/7:允許 partial 處理 / 影片就緒自動補送 blur task / 測試中,預計下週 MR 於 6/2 release
- 狀態:📅 設計收斂,本週要送 MR
- 註:Jira HAWK-577 是 New Feature 不是 Bug

### Row 53 / #50 VisionMax PROD not blurring(HAWK-517+578 / Adonis)
- **5/7:已於 v1.1.28 部屬至 Webfleet PROD。引入自我健康檢查機制,Model Volume 異常自動重啟 ECS,SQS 保留機制確保任務不漏**
- 狀態:✅ 已修 + 加保險絲
- ⚠️ Sheet 沒記的 follow-up:**SQS retention 從 4 天改 14 天**(chiehli.wang 5/6 已 ping spencer.su,還沒 confirm)+ 客戶手動補 4/21–5/4 漏掉的 blurring

---

## 🟠 慢但活著

### Row 9 / #7 Blurring Footage(HAWK-331/6391/527 / Vincent)
- 4/30:時序補碼減少模糊閃爍,測試中
- 5/4:回客戶說小臉部 case AI 無法 cover,要靠人工
- **5/7:補碼+模糊保留方式效果不錯。License Plate 改 yolo26l 效果好。但 DMS 窗外的車牌沒碼到,再看怎麼處理**
- **狀態:模型一直在演進(yolo26l 是新版),但客戶持續找新 edge case → 6/2 release HAWK-527 second wave**

### Row 6 / #4 Eyes Detection(VMX-7309 / Jieli)
- 5/4 / 5/7 都是 **done**
- 狀態:✅ Eyes 真的完成
- 註:Jira VMX-7309 還 OPEN 是 transition 沒走(joe.lien 在串 server 端)

### Row 4 / #3 Yawning Detection(VMX-7309 / Jieli)
- 4/30:更新驗證方式
- **5/4:目前優先處理 Lens Cover 的任務,等該任務完成後回來處理 Yawning 的後續驗證與測試**
- **5/7:空白**
- **狀態:🚨 Jieli 暫停 Yawning,先做 Lens Cover(Row 31 #28)。對外 Roadmap 還掛 Basic tier,5/6 會議揭露的「不如預期」+ 現在被 Lens Cover 壓後**
- ⚠️ Yawning UI toggle 真實對應 ticket 是 **VMX-7432**(Lucy 5/6 開的單),不是 VMX-7309

### Row 48 / #45 Pedestrian Detect(HAWK-570 / Vincent)
- 5/4:討論 Jakob 問題,回覆評估結果
- **5/7:正在整理各個問題的回覆資訊**
- **狀態:還在「整理問題」階段,沒實際進到改 model**

### Row 49 / #46 Eating & Drinking(HAWK-562 / Jimmy)
- 4/30 → 5/4:都寫「預計 6/10 Feasibility results」
- **5/7:目前處理 face not found,尚未評估**
- **狀態:🚨 Jimmy 同時扛兩件,Eating & Drinking 被 Face Not Found 排擠。6/10 Feasibility 可能延期**

---

## 🔴 沒動 / 沒人扛

### Row 10 / #8 LDWS Server AI(VMX-6722/7101 / Eric)
- 4/30:評估 device 端模型改善 (Yolo lane detect 方法)
- 5/4:讓 Jonathan 試
- **5/7:pending**
- **狀態:🚨 Brian 5/6 會議講「Q1 已 merge」對應到 VMX-6722,但 sheet 5/7 寫 pending — 兩條訊息打架**
- 真實:VMX-6722 sub-tasks 全 closed/resolved + jimmy 3/11 留 deploy prod。Sheet 5/7 寫 pending 可能在追的是 device 端的「進一步」改善,不是 server-side ship

### Row 30 / #27 VLM(no PIC, 2026 Q3)
- 4/30 / 5/4 / 5/7:**pending / pending / pending**
- 狀態:🟡 計劃 2026 Q3,目前不動正常
- ⚠️ 對外 Roadmap 寫 2H'2027 — sheet 內部跟對外差 1 年,Brian 5/5 已裁示「對客戶講 2027」

### Row 45 / #42 Server AI 統計資料釐清(no Jira / Vincent+Jimmy)
- 4/30:本週重新訓練 server 模型,目的解決 phone 誤報
- 5/4:討論決定持續優化方向
- **5/7:空白**
- **狀態:🚨 沒 Jira ticket + 5/7 沒人寫 + 「持續優化方向」這種模糊話 = 變相 stale。Jimmy 又同時扛 #32 Face Not Found 跟 #46 Eating,#42 排第幾?**

---

## Brian 1on1 talking points(只給 Kenny 看)

1. **#3 Yawning 被 #28 Lens Cover 排擠** — Jieli 一個人扛兩件,要不要排序?
2. **#46 Eating & Drinking 被 #32 Face Not Found 排擠** — Jimmy 同樣狀況
3. **#42 Server AI 統計資料釐清** — 沒 Jira、5/7 沒寫、Vincent+Jimmy 都掛名 — 這列是不是該歸 Done 或 hide?
4. **#8 LDWS 5/7 pending vs Brian 5/6 講 Q1 已 merge** — 真實狀況到底哪個?
5. **#50 PROD blurring follow-up SQS retention 14 天**(chiehli.wang ping spencer.su)— sheet 沒寫,要不要追進度?

---

## ⚠️ NotebookLM 5/7 AI Weekly 揭露的 sheet 漏記訊號(2026-05-07 補)

詳見 [2026-05-07_ai-weekly_meeting-record.md](../../meetings/2026-05-07_ai-weekly_meeting-record.md)。會議揭露 sheet 嚴重 understatement / 漏寫的點:

| Sheet row | sheet 5/7 寫的 | 會議揭露 | 嚴重度 |
|-----------|---|---|---|
| #46 Eating | 「處理 face not found 尚未評估」 | **客訴 17 倍量級重災區,6/15 前一次性緊急重訓,Vincent 加入** | 🚨🚨🚨 |
| #4 Eyes | done done | Spencer 睜眼率 API 還在做,趕 6/2 全鏈路驗證 | 🚨 |
| #3 Yawning | 空白 | 灰階模型重訓 + 考慮 Server 端從嘴巴改辨識整張臉 | 🚨 |
| (無 row)Speed Sign | — | Jay 立即關閉 Flip 重訓,擴增降至 10 倍 | 🚨 sheet 沒這條 |
| #8 LDWS | pending | YOLO Lane Detection 因資源緊繃決議 Pending,**開新 ticket** | sheet 寫對但要追新 ticket |
| #43 Camera Height | 80% CI 調整 | + **PM 提供 20% 誤差範圍給 BMS**(Kenny 的 PM 任務)| 中,我自己要做 |
| #32 Face Not Found | 13975 張 review | + **導入 Head 邏輯**,當臉部遺失以頭部框線輔助判定 | 中 |
| #28 Lens Cover | BMS 確認規格 | **標準版 / BMS 版邏輯雙軌維護**(Azuga 標準版要解除車速,BMS 要 > 0)| 中,長期成本 |

### 客訴 ID 6652
- 飲食誤判 17 倍量級主要來自此特定帳號
- 在先前對話也曾被指為精準度較低的特定帳號 ID

### 5/7 會議沒提到的 sheet rows
- #47 Rastrac False Speed(Jonathan)— sheet 自己 update Train 99%/Test 98%/False Speed 100%,會議沒分享
- #27 VLM — pending pending pending
- #41 Add box around event(Jay/Adonis)
- #48 Request event blurry / #49 Blurring on-demand / #50 PROD blurring(Adonis)— 會議沒提 Adonis 進度

### Owner 認知更新
- **Spencer 是 Cloud / API team owner**(不是 Adonis)— 會議揭露 Spencer 扛睜眼率 API 全鏈路驗證
- **Vincent 角色擴大** — 不只 #45 Pedestrian + #43 Camera height,還加入飲食誤判重訓主導
- **Jonathan / Adonis 5/7 會議都沒被點名** — 不確定是否在會中
