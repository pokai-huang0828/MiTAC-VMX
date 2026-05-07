# 內部利害關係人地圖

## MiTAC 端

| 領域 | 人 | 職責 / 關鍵議題 |
|------|---|----------------|
| **Software Head** | **Brian** | VisionMax / Cloud / Camera App / AI 整體;團隊 ~20 人;Jira dashboard 主導者 |
| Camera App | Hsinyi, Jack, Leo | 設備端錄影 / UI / 紅色按鍵 |
| AI Inference | **Jimmy**, Vincent, Eric | ADAS / DMS 模型、訓練、validation。**5/7:Vincent 角色擴大,加入飲食誤判 7000+ Edge case 重訓主導** |
| AI Inference 補 | Jieli, Andy, **Jay** | Yawning / Quantatec / Lens Cover / DMS Golden Case / Speed Sign 重訓(Jay 5/7) |
| **Cloud / API team lead** | **Spencer** | **校正(5/7):Spencer 是 Cloud / API team lead,扛睜眼率 API 全鏈路驗證 6/2**(原 memory 誤把 Adonis 當 Cloud lead)|
| Cloud Backend 一般 | Neil | Event API / DB / portal serving |
| MiDM / OTA | RD 主管 | 韌體推送 / config(**最高風險區**:Custom ID 派錯設備變磚) |
| 硬體規格 | **Mori** | K-series / G-Sensor / 200Hz / 紅色按鍵 / Rollover detection(VMX-7194)|
| 測試車隊 | **Elvis** | NAVMAN-AU,新功能驗證 / 開 Smoking accuracy 單(VMX-7324)|
| **Server AI 應用層** | **Adonis** | Server AI confidence threshold / blurring on-demand / pre_event_message / Add box around event(VMX-5909)— **不是 Cloud lead** |
| **Webservice / Blurring API** | **chiehli.wang(王傑立)**| HAWK-573 / HAWK-577 / HAWK-578 / SQS retention 改 14 天(5/6 ping spencer.su)/ Health check 機制 |
| Front-end | **Lucy** | UI 設計 / 軌跡顏色 / Severity 等級 / **Yawning UI toggle = VMX-7432(5/6 開)** / Rollover UI |
| Speed Sign 模型 | **woody.lee** | VMX-7430(exit ramp)/ VMX-7431(LED sign)5/6 新開 |
| 業務端 | **Wendy** ⚠️ | 在 Hub 第三 tab 出現,身份 / 部門 待補 — Wendy 案是「資訊不對稱」框架原型 |
| GA 分析 | Luke / Sacer | 5/6 起 Lucy 用同一 GA 帳號 |
| 韌體 / Akamai 中介 | Tony | OTA #11 真因 — 跟 Akamai 之間轉述 |

## 海外客戶

| 客戶 | 整合方式 | 對接人 | 重點 |
|------|---------|--------|------|
| **Azuga** | Custom SDK | (待補) | 21 個新 API 排隊 / SmartLink 系列 ticket |
| **Bridgeron** | API integration | (待補) | 整合會議每週 |
| **Mainfreight** | Web Platform 測試 | (待補) | 測試中 |
| **BMS** | API + 客製 | (待補) | 雙版本同步戰略對象 / 200Hz / Smoking config / VMX-6920 |
| **Platform Science (Vinicius)** | 評估中 | Vinicius / John Smith Jr / Peter | US,K265 portal 問題 / SDK 文件需求 |
| **CONNECTSOURCE** | 評估中 | (詳 case-learning) | Passenger blurring 需求 |
| **Quantatec** | 客製 | (待補) | Camera obstruction 系列(VMX-6983 / 7427) |
| **HDFE** | (待補) | (S 那邊) | 2026-05-06 抱怨 Q1 Events Page UI 變動 |
| **LB Technology** | (待補) | (待補) | Plow PTO / Posted Speed Alert |
| **Rastrac** | (待補) | (待補) | False Speed Event(VMX-7317)|
| **Seeing Machines** | (待補) | (待補) | Rollover detection 需求(VMX-7194) |
| **Suvio** | 評估中 | (待補) | 影像 + 客製語音 |
| **DSNY** | (待補) | (待補) | Camera Pilot Project / RTR+Camera |

## 每週固定會議

- Azuga AI weekly(5/6 — 5/6 Lens Cover 標準版規格 / 飲食誤判少數提及)
- **內部 AI weekly(每週三 / 5/7 最近一場揭露 4 條 action items + Lens Cover 雙軌 / 飲食 17x 客訴 / Yawning 灰階 / LDWS YOLO Pending)**
- Field-side requirements sync
- Bridgeron 整合
- Q2 Tracker review(Brian 主持,5/6)
