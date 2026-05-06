# 內部利害關係人地圖

## MiTAC 端

| 領域 | 人 | 職責 / 關鍵議題 |
|------|---|----------------|
| **Software Head** | **Brian** | VisionMax / Cloud / Camera App / AI 整體;團隊 ~20 人;Jira dashboard 主導者 |
| Camera App | Hsinyi, Jack, Leo | 設備端錄影 / UI / 紅色按鍵 |
| AI Inference | **Jimmy**, Vincent, Eric | ADAS / DMS 模型、訓練、validation |
| AI Inference 補 | Jieli, Andy | Yawning / Quantatec / DMS Golden Case |
| Cloud Backend | **Spencer**, Neil | Event API / DB / portal serving |
| MiDM / OTA | RD 主管 | 韌體推送 / config(**最高風險區**:Custom ID 派錯設備變磚) |
| 硬體規格 | **Mori** | K-series / G-Sensor / 200Hz / 紅色按鍵 |
| 測試車隊 | **Elvis** | NAVMAN-AU,新功能驗證 |
| Cloud Server / Server AI | **Adonis** | Server AI confidence threshold / blurring on-demand / pre_event_message |
| Front-end | **Lucy** | UI 設計 / 軌跡顏色 / Severity 等級 / Yawning UI 開關 / Rollover UI |
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
| **CONNECTSOURCE** | 評估中 | (詳 Case_learning) | Passenger blurring 需求 |
| **Quantatec** | 客製 | (待補) | Camera obstruction 系列(VMX-6983 / 7427) |
| **HDFE** | (待補) | (S 那邊) | 2026-05-06 抱怨 Q1 Events Page UI 變動 |
| **LB Technology** | (待補) | (待補) | Plow PTO / Posted Speed Alert |
| **Rastrac** | (待補) | (待補) | False Speed Event(VMX-7317)|
| **Seeing Machines** | (待補) | (待補) | Rollover detection 需求(VMX-7194) |
| **Suvio** | 評估中 | (待補) | 影像 + 客製語音 |
| **DSNY** | (待補) | (待補) | Camera Pilot Project / RTR+Camera |

## 每週固定會議

- Azuga AI weekly
- 內部 AI weekly
- Field-side requirements sync
- Bridgeron 整合
- Q2 Tracker review(Brian 主持)
