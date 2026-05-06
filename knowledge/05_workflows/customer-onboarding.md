# Customer Onboarding SOP(裝相機 → 配置 → 上線)

> 來源:KB Quick Start Guide / Camera Install Position / APN Setting / How to Add Device + Account
> 用途:海外客戶 / 新 fleet 客戶 onboarding

## 整體流程

```
1. Master Portal 註冊 master account
   ↓
2. Master Portal 加 device 到 inventory
   ↓
3. Master Portal 創 fleet + 把 device 分到 fleet
   ↓
4. Master Portal 創 fleet manager account(+ Viewer Only Role 待釐清)
   ↓
5. 技術人員到車上裝相機(VisionAgent app)
   ↓
6. APN 設定(if SIM 不通)
   ↓
7. Camera Install Position 確認(VisionAgent live view)
   ↓
8. ignition on → 等 calibration → "Calibration Completed"
   ↓
9. Driver Profile 創 + RFID/QR 卡發放
   ↓
10. Driver tap 卡 → trip 開始 → 上線
```

## Step-by-step

### 1. Master 加 Device(KB:How do I add a new device)
- Login Master Portal
- Management → Inventory
- + New Device(individual 或 import CSV)
- ⚠️ Only master admin 可加 — fleet admin 不行

### 2. Assign Device to Fleet
- Inventory 選 device → assign 到 fleet
- 設備 power on + 連網後開始 reporting

### 3. 加 Fleet Manager Account(KB:How to Add New Account)
- Master Portal → Management → User Account
- 新增

### 4. 裝相機 — VisionAgent(KB:How to Check Camera Install Position)

**前置**:VisionAgent app(iOS / Android)+ smartphone WiFi 連 device hotspot

**Outward Camera 設定**:
- 車輛停 level ground
- 相機 view parallel to ground
- **Ground:Sky = 50:50**
- 矩形框內是 ADAS engine 處理區 → 確保 unobstructed view

**Inward Camera 設定**:
- 設 Driver Location:**Right (RHD)** / **Left (LHD)**
- Camera Location:選 A / B(具體選法看 KB 圖)
- DMS 需 clear view of driver's face

### 5. APN 設定(KB:How do I set APN through VisionAgent)
**何時要做**:Telecom APN setting 導致網路失敗時

SOP:
1. VisionAgent → Search Dashcam → 確認 CDR # match
2. Save + Yes(連 device WiFi)
3. Home → SIM → setting screen
4. Enter APN info → Save Changes
5. Verify → OK
6. Diagnostics → 看 APN saved + online 狀態
7. Disconnect

### 6. Driver Identification 設定
**機種能力**:
- K245 / K245C / K265:RFID + QR
- K220:QR only
- K145(c) with i25:都不行

**SOP**(KB:Driver Identification Setup):
- VisionMax → Management → Driver → + New Driver
- 輸入 IC Card S/N(RFID 號)+ name + photo + employee ID
- 完成後,trip 開始時相機說「Please tap your ID card」/「Please scan your ID QR code」
- Driver tap NFC 或 scan QR(in-cabin camera 前 3 秒內)

### 7. 第一次 Calibration
- 開車到開放路段
- ADAS:**30 km/h × 3 分鐘 + 平坦少彎**
- DMS:20 km/h × 15 秒 + 司機臉穩定
- 完成語音:"Calibration Completed"

### 8. 健康檢查
**Master Portal**:Management → Diagnostics
- 看 device 「Has Issue」狀態
- Issue Type:Location Function / Sensor Events Detection / 等
- KB Diagnostics 文章有詳細 Q&A

## 常見 Onboarding 卡點

| 問題 | KB 對應文章 | 解法 |
|------|-----------|------|
| Camera 不開 | Troubleshooting > 沒開機 | 檢查電源 / fuse / 手動 ignition switch |
| Network 不通 | VisionAgent > APN | 設 APN |
| Calibration 失敗 | (vehicle classification / camera height) | 確認 vehicle class + height settings |
| Driver 卡讀不到 | Using camera > NFC | 對齊 NFC symbol / 換 supported card 格式 |
| ADAS Failure | Diagnostics + 30km/h × 3min | 看 GPS / 速度條件 / camera 高度 |

## 對應 PM 議題

- **Vinicius (Platform Science)** 案的 K265 white-list 卡點 — 可能是 onboarding step 2 (assign to fleet)沒推 owner
- **Connect Source** Passenger Blurring 跟 onboarding 無關,是 feature
- **Quantatec obstruction**:VisionAgent 可看 inward camera blocked 警示
