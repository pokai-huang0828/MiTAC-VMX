# Sales-Level FAQ — 對外口徑(KB 已 deep read)

> 來源:KB General > FAQ + Master Portal,2026-05-06 Kenny + Claude 完整深讀
> 用法:對客戶 RFP / Deep Dive / Demo 直接拿這層用,**KB 已驗證**

## ⭐ KB 確定的對外答案(8 題核心)

### Q1. What ADAS and DMS features do you support?
**KB 答案**:
- **ADAS**:LDWS, FCWS, Tailgating, **Rolling Stop**, Stop & Go, **Speed Sign (in development)**
- **DMS**:Distraction, Fatigue, Phone Usage, Unfastened Seatbelt, Lens Covered, **Smoking (in development)**

⚠️ 校正以前 memory:
- ADAS 完整清單比 memory 多 1 個(Rolling Stop 已 ship)
- Speed Sign 是 **(in development)**,不是 Premium tier 2027
- Smoking 是 **(in development)**,memory 之前說「KB 沒寫」是錯的

### Q2. How mature is your AI model?
**KB 答案**(直接背):
- **Device-Side (Local) AI: 75% to 80% accuracy**
- **Server-Side (Cloud) AI: 90% to 95% accuracy** for Unfastened Seatbelt and Phone Use Detection

⚠️ Sensitivity dial 估計值(Low 0.85 / Med 0.70 / High 0.55)是 confidence threshold per event,跟 overall accuracy 不同。

### Q3. How long are videos and data stored?
**KB 答案**:**180 days standard retention** for all videos and associated data.

### Q4. How often do you update your AI model?
**KB 答案**:
- **Dataset refreshed monthly** in cloud
- **Models updated quarterly**
- New features added as available

⚠️ MiAI Roadmap Slide 6 講「月節奏 collect→filter→label→train→validate→deploy」是內部 cycle,**對外用 KB 的 quarterly model update**。

### Q5. Are AI models processed locally or in the cloud?
**KB 答案**:
- 「Local + secondary cloud analysis」hybrid 架構
- Cloud secondary 用於 Unfastened Seatbelt + Phone Use,**> 90% accuracy**
- 對應 Roadmap Slide 5 Stage 1+2(Edge AI + Server AI)

### Q6. Can thresholds and alerts be customized?
**KB 答案**:
- ✅ Voice alerts can be customized
- ❌ AI thresholds **NOT currently open for customers to modify**

⚠️ Brian 同步戰略翻案目標就是改這個,但 **KB 對外目前還是 NOT open**。

### Q7. Can we white label the platform?
**KB 答案**:✅ Yes - fully functional White Label solution
- **Brand Integration**: Replace VisionMax logo with partner brand
- **Domain & URL**: Custom domain (visionmaxfleet.com → partnerfleet.com)
- 強調:no lengthy dev cycle, instant access

### Q8. What's the difference between Device Portal and Fleet Portal?
**KB 答案**:
- **Device Management (Master Portal)**:Hardware-focused — Inventory / Health monitoring / Storage / OTA push
- **Unified Fleet Intelligence (Fleet Portal)**:Fleet data — Live View / Event Reports / Safety Analytics / Driver Coaching
- 一句話:「One manages hardware, the other analyzes fleet performance」

## ⭐ Master Portal 完整能力(KB:What can I do in Master portal?)

Administrative operations:
1. Create / edit / remove fleets
2. Add devices manually or batch import + assign to fleets / Edit / remove
3. Modify plan types
4. View health status report — devices connected ≥1 + uploaded health
5. View specific device health status
6. Manage fleet manager's accounts
7. Trend chart — fleet size + plan types over time
8. **Push OTA updates**: camera app / base + region images / MiDM client / MiDM system app / map data
9. **Access**: camera app SDK doc / MiAI SDK API doc / **web API doc** ⭐ 對技術型客戶必殺

### Batch OTA SOP(KB)
Management → Inventory → 全選 fleet 設備或多選 → 點 "Update" 推 OTA

## ⭐ Vehicle Classification(KB:How are passenger / medium / heavy defined)

| Class | 類型 | 重量(lbs) | 例子 |
|-------|------|-----------|------|
| 1-3 | Passenger / Light Duty | 6,000 - 14,000 | Pickup trucks |
| 4-6 | Medium Duty | 14,001 - 26,000 | Delivery vans |
| 7-8 | Heavy Duty | > 26,001 | Long-haul, construction |

- 不同 class 有 specific height + AI parameters
- VisionMax 開發了 3 種 height + AI param settings
- 技術人員需測量實際安裝高度(對應 HAWK-501 Camera height 不穩定 ticket)

## ⭐ Privacy Mode(KB:Behaviour of Privacy Mode in VisionMax)

- **進入**:Press and hold **Panic Button** > 2 秒
- **進入後**:
  - 停止上傳 health / GPS / photo / video
  - AI + sensor event detection 暫停
  - SD 錄影暫停
  - ⚠️ Manual Event Button 按下時 camera **仍會錄**
- **退出**:Panic Button hold > 2 秒
- **Restart**:Privacy Mode 維持(不會自動退出)

⚠️ **與 memory 衝突**:memory 校正過「紅色按鍵沒有 panic event」,但 KB 講 Panic Button 用於 Privacy Mode。可能是兩個不同按鈕(Manual Event vs Panic) — Coffee Chat 必問 Mori。

## ⭐ Manual Event Button(KB:Manual Event Button Behaviors)

| 場景 | 動作 | 行為 | 語音 |
|------|------|------|------|
| ACC ON / 來電 | 短按 | 接電話 | — |
| ACC ON / 來電 | hold > 2s | 拒接 | — |
| ACC ON / 無來電 | 短按 | Manual event recording | "Manual Event Recording" |
| ACC ON / 無來電 | hold 2-6s | Call out to server | — |
| ACC ON / 無來電 | long press +3s | Back to base call | — |
| ACC OFF / Clean install | 短按 / hold > 1s | 開機 | "Device Ready" |
| ACC OFF / ACC mode | 短按 | Manual event recording | "Manual Event Recording" |
| ACC OFF | hold 10-30s | **格式化 SD card** | "SD Card formatting, please wait" |

⚠️ Private mode 中,接電話 + Manual event 不執行(其他仍可)

## ⭐ K-series 機種差異(KB:Driver Identification Setup,**第一個 KB 確認的機種 mapping**)

| 機種 | RFID 卡 | QR Code |
|------|---------|---------|
| K245 | ✅ | ✅ |
| K245C | ✅ | ✅ |
| K265 | ✅ | ✅ |
| K220 | ❌ | ✅(QR only) |
| K145 / K145c (with i25) | ❌ | ❌ |

→ K220 不支援 RFID,K145 / K145c 連 QR 都不行(有 i25 才行)

## 客戶答題 SOP(KB-first)

1. 客戶問 → 翻 KB(這層)
2. KB 沒答案 → 不要編,改:「Roadmap planned, 我內部確認後 24h 內回覆」
3. KB vs Roadmap 衝突 → 用 Roadmap 對外 + 標「上線時間請我內部確認」
4. 內部數字(threshold / fps / 容量)→ 用 KB,不要從 NotebookLM 推測

## 仍要 Coffee Chat 釐清

- Mori:**紅色按鍵 = Manual Event Button or Panic Button?各機種幾個 button?**(KB 兩篇有衝突)
- Mori:K-series 各 chip 對應 tier
- Mori:各車種 threshold 具體值
- Brian:VMX/BMS 同步戰略時程 + 對 Q6「threshold not customizable」何時翻案
- Brian:white label 客戶誰用過(Suvio 案?)
