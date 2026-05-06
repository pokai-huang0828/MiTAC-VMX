# VMX KB 完整文章 Catalog

> 來源:https://service.visionmaxfleet.com/portal/en/kb/vm
> 掃描日期:2026-05-06
> ⚠️ memory 之前說「KB 9 篇」是嚴重低估 — 實際 **60+ 篇**

## 6 個 Top-level Categories

```
VM Knowledge Base
├── General                  (子目錄 5 個,共 32 篇)
│   ├── API                  (3 篇)
│   ├── FAQ                  (15 篇)
│   ├── Installation         (2 篇)
│   ├── Troubleshooting      (2 篇)
│   └── Getting Started      (10 篇)
├── Fleet Portal             (15 篇)
├── Master Portal            (8 篇)
├── Using camera             (14 篇)
├── VisionAgent              (3 篇)
└── Declarations             (4 篇 — 法律,不重要)
```

## General > API(技術型客戶必看,3 篇)

1. VisionMax Portal Interface Updates
2. **API Reference** ⭐ 對 Vinicius 等技術型 buyer 是必殺
3. Is the portal cloud hosted (AWS, Azure, etc.)?

## General > FAQ(銷售級必背,15 篇)⭐⭐⭐

1. How does the emergency 2-way call feature work?
2. **VisionMax Driver Scorecard** ⭐
3. **VisionMax Diagnostics Information** ⭐
4. Parking Mode Behavior
5. How long does the camera stay on after I turn off my vehicle?(熄火 3min 窗口)
6. SD CARD Recording time: Connected DashCam Footage Storage Calculator
7. I'm not receiving the password reset email
8. **Can we white label the platform?** ⭐ Sales
9. **What ADAS and DMS features do you support?** ⭐⭐ RFP 標準答案
10. **How mature is your AI model?** ⭐⭐ Deep dive 必問
11. **How long are videos and data stored?** ⭐⭐ 隱私 / 合規
12. What's the difference between VisionMax Device Portal and Fleet Portal?
13. **How often do you update your AI model?** ⭐ 對應月節奏 Roadmap
14. **Are AI models processed locally or in the cloud?** ⭐ Edge vs Server
15. **Can thresholds and alerts be customized?** ⭐ 對應 Brian 同步戰略

## General > Getting Started(10 篇)

1. What are the supported ADAS events?(已 → adas-dms-events.md)
2. What are the supported DMS events?(已 → adas-dms-events.md)
3. How long does a software update take?
4. What in-cabin alerts are available?(已 → voice-alerts.md)
5. Which NFC cards are compatible with the camera?
6. How do I update the camera's software?
7. **What Are the Trigger Conditions for Each Traffic Sign and Signal Feature** ⭐ memory 標待補,實則有
8. Where Are My Videos Stored on the SD Card?
9. **What is the resolution, FPS, Bitrate and video size for MiTAC's cameras?** ⭐ memory 標待補,實則有(已抓內容)
10. **Why are thresholds different for Passenger, Medium Vehicle and Heavy Duty?** ⭐ memory 標待補,實則有(已抓)

## General > Installation(2 篇)

1. What is the Installation procedure
2. VisionMax Quick start Guide

## General > Troubleshooting(2 篇)

1. How to export the system logs from K220?
2. What if the camera is not turning on when I start the vehicle?

## Fleet Portal(15 篇)

1. How can we turn off the sound "please tap your ID card"?
2. Can I save the live view video?
3. What is the Map Overview?
4. **How to change the sensitivity of ADAS and DMS?** ⭐ 對應 sensitivity dial
5. What are the supported sensor events?(已 → adas-dms-events.md G-Sensor)
6. **How to retrieve a video file**
7. **Behaviour of Privacy Mode in VisionMax** ⭐ memory 標待釐清,實則有
8. VisionMax Update History & Release Notes
9. How do I view what version of the SW installed currently?
10. **How are passenger / medium-duty / heavy-duty vehicles defined, and how is camera height set?** ⭐ memory 標待補,實則有
11. How many geofences can be configured in the camera?
12. What is the meta data shown with the video?
13. Is the video compressed?
14. What is the codec used for live view?
15. What if I need video from last month?

## Master Portal(memory 0/8 完全沒覆蓋,8 篇)⚠️

1. How do I add a new device to my fleet?
2. **What can I do in Master portal?** ⭐⭐ 對應 portal 雙層
3. VisionMax Update History & Release Notes
4. How to Change Devices Settings to a Normal Car
5. How do I set portal language, time zone, date format?
6. **How do I update SW for all devices at one time?** ⭐ 批量 OTA
7. Portal Usage Guides
8. How to Add New Account?

## Using camera(14 篇)

1. Manual Event Button Behaviors(已校正紅色按鍵 → kb-cheatsheet.md)
2. How to care for the camera?
3. Will a software update erase my stored videos?
4. What are the various LED Behaviors(分機種,已 → kb-cheatsheet.md)
5. **Driver Identification Setup and Usage for Models K245, K245C, K265, K220** ⭐ K-series spec 線索
6. Where can I find the QR code for the Driver ID?
7. **Internal Flash Overwrite Mechanism** ⭐
8. **SD Card Overwriting Mechanism** ⭐
9. **How to reset device?** ⭐
10. How often does diagnostic refresh or runs a check of the device?
11. Precautions and notices
12. What happens if I tap my card again? Does it start a new trip?
13. What if my card always got failed when taping?
14. What are the supported NFC card formats?
15. How do I know that my card is recognized?

## VisionAgent(3 篇)

1. How to Check Camera Install Position
2. How do I set APN for the SIM in the camera through VisionAgent?
3. Can I use a smartphone to connect to the device via WiFi or BT?

## Declarations(4 篇 — 法律)

略

## ⚠️ 關鍵 KB 事實校正(memory 之前錯)

### 影像 FPS = 10(memory 寫 15-30 是錯)
| Video Type | Resolution | FPS | Bitrate | Size/3min |
|-----------|-----------|-----|---------|-----------|
| Side by Side | 2560 × 720 | 10 | 2,764,800 | 58.8 MB |
| Separated | 1280 × 720 | 10 | 1,382,400 | 29.4 MB |
| AUX UVC | 1280 × 720 | 10 | 5,000,000 | 106.8 MB |
| AUX USB | 2560 × 1440 | 10 | 5,529,600 | 118.8 MB |
| Live View | 854 × 480 | — | 800,000 | 0.1 MB/s |

### 車種 threshold 差異(KB 解釋過,但無具體數字)
- 載重影響加速 → 大車需要更多時間到同樣速度
- 因此 threshold 不同
- ⚠️ 具體數字 KB 沒給,還是要問 Mori / Jimmy

## Deep Read 進度(2026-05-06)

### ✅ Deep read 完成 18 篇
**General > FAQ(8 篇)**:
- ✅ What ADAS and DMS features do you support → `sales-faq.md`
- ✅ How mature is your AI model → `sales-faq.md`(Local 75-80% / Cloud 90-95%)
- ✅ How long are videos and data stored → `sales-faq.md`(180 days)
- ✅ How often do you update your AI model → `sales-faq.md`(Dataset monthly / Models quarterly)
- ✅ Are AI models processed locally or in the cloud → `sales-faq.md`(hybrid)
- ✅ Can thresholds and alerts be customized → `sales-faq.md`(NOT open)
- ✅ Can we white label the platform → `sales-faq.md`(✅ logo + domain)
- ✅ What's the difference between Device Portal and Fleet Portal → `sales-faq.md`

**General > FAQ 補(4 篇)**:
- ✅ VisionMax Driver Scorecard → `safety-score.md`
- ✅ VisionMax Diagnostics Information → `diagnostics.md`
- ✅ Parking Mode Behavior → 待整合
- ✅ How long does the camera stay on → 校正(3 分鐘 suspend window)

**General > Getting Started(3 篇)**:
- ✅ What is the resolution, FPS, Bitrate → `machines-spec.md`(全 10 fps / 4 video types)
- ✅ Why are thresholds different for Passenger / Medium / Heavy → `vehicle-classification.md`
- ✅ What in-cabin alerts are available → `voice-alerts.md`(完整 11 類)

**General > API(2 篇)**:
- ✅ API Reference(只是 link 到 web API doc)
- ✅ Is the portal cloud hosted (AWS, Azure, etc.) → AWS confirmed

**Master Portal(2 篇)**:
- ✅ What can I do in Master portal → `sales-faq.md` Master Portal section
- ✅ How do I update SW for all devices at one time → batch OTA SOP

**Fleet Portal(2 篇)**:
- ✅ How are passenger / medium / heavy defined → `vehicle-classification.md`
- ✅ Behaviour of Privacy Mode → `voice-alerts.md` Privacy Mode

**Using camera(2 篇)**:
- ✅ Manual Event Button Behaviors → `voice-alerts.md` 完整 8 種行為
- ✅ Driver Identification Setup K245/K245C/K265/K220 → `machines-spec.md` RFID/QR mapping

**VisionAgent(1 篇)**:
- ✅ Can I use a smartphone via WiFi or BT → `visionagent-app.md`

**General > Getting Started(1 篇)**:
- ✅ What Are the Trigger Conditions for Each Traffic Sign → 部分(全文長,只摘 Speed Limit)

### ✅ Deep read 第三批新增 8+ 篇

**Fleet Portal**:
- ✅ How to change the sensitivity of ADAS and DMS → 對應 sensitivity dial,Configurations → AI Event Detection → vehicle class → Low/Med/High
- ✅ How to retrieve a video file → SOP:Trip → Trip List → Retrieve Video → Playback SD Card

**Using camera**:
- ✅ SD Card Overwriting Mechanism → `storage-mechanism.md`
- ✅ Internal Flash Overwrite Mechanism → `storage-mechanism.md`
- ✅ How to reset device → `troubleshooting.md`(Reset button paper clip / K245/K145c/K245c 在 tamper cover 後)
- ✅ LED Behaviors → `machines-spec.md` 加機種 LED 差異(K220/K245 1 個 / K265 2 個)

**Master Portal**:
- ✅ How to Add New Account → `customer-onboarding.md`
- ✅ How do I add a new device → `customer-onboarding.md`
- ✅ VisionMax Update History → 目前是空(沒當期 update)

**VisionAgent**:
- ✅ How to Check Camera Install Position → `customer-onboarding.md`(Outward 50:50 / Inward driver location)
- ✅ How do I set APN → `customer-onboarding.md` APN SOP

**Installation / Troubleshooting**:
- ✅ VisionMax Quick start Guide → `customer-onboarding.md`
- ✅ What if camera not turning on → `troubleshooting.md` Q1
- ⏳ How to export system logs from K220(沒讀)
- ⏳ What is Installation procedure(沒讀)

**General > FAQ**:
- ✅ SD CARD Recording time(主要 link 到 Jotform calculator)
- ⏳ I'm not receiving password reset(沒讀)

**Deep Read 進度**:**~25 / 60+ 篇**(~40% coverage)

### ⏳ 仍未 read(P2-P3,實際要用時再讀)
- General > FAQ 剩 3 篇
- Fleet Portal 剩 ~9 篇(geofences / video metadata / codec / 等技術細節)
- Using camera 剩 ~8 篇(care for camera / NFC formats / precautions / 等)
- Master Portal 剩 ~3 篇(language / change to normal car / Portal Usage Guides)
- Getting Started 剩 5 篇(software update time / NFC compat / video storage / 等)
- API Reference(只是 link)/ Installation procedure
