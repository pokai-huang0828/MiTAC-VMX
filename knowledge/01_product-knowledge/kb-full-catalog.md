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

## 待擴充 knowledge 文件

| 優先級 | KB 文章 | 該擴進 knowledge 的哪 |
|-------|---------|---------------------|
| P0 | What ADAS and DMS features do you support | 加 `01_product-knowledge/sales-faq.md`(新檔) |
| P0 | How mature is your AI model | 同上 |
| P0 | How long are videos and data stored | 同上 |
| P0 | Can thresholds and alerts be customized | 同上 |
| P0 | Are AI models processed locally or in the cloud | 同上 |
| P1 | Master Portal 8 篇 | `03_systems-architecture/master-portal-operations.md`(新檔) |
| P1 | Driver Identification K245/K245C/K265/K220 | 補進 `01_product-knowledge/machines-spec.md` |
| P1 | Behaviour of Privacy Mode | 補進 `01_product-knowledge/voice-alerts.md` |
| P2 | API Reference | `01_product-knowledge/api-reference.md`(新檔) |
| P2 | VisionAgent 3 篇 | `01_product-knowledge/visionagent-app.md`(新檔) |
