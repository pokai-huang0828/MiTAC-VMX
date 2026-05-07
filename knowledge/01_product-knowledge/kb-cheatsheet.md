# VMX KB Cheatsheet

> **官方 KB**:https://service.visionmaxfleet.com/portal/en/kb/vm
> ⚠️ KB 實際 **60+ 篇**(完整 catalog 見 [kb-full-catalog.md](kb-full-catalog.md)),這頁只摘核心 9 篇。
> 其他重要 KB 內容:[sales-faq.md](sales-faq.md)(對客戶 RFP)/ [../03_systems-architecture/master-portal-operations.md](../03_systems-architecture/master-portal-operations.md)(Master Portal 8 篇)

## 已讀核心 9 篇

| # | 主題 | 重點 |
|---|------|------|
| 1 | Manual Event Button Behaviors | 紅色按鍵:接電話 / Manual event / Server callback / 格化 SD(**沒 panic event**) |
| 2 | LED Behaviors(分機種) | LED 號燈分機種,要查 KB 文章對應 |
| 3 | Parking Mode Behavior | 停車模式行為定義 |
| 4 | Camera stay-on after ignition off | **3 分鐘 suspend 窗口**(熄火後續傳 + 等 ACC 重啟) |
| 5 | Supported ADAS events | **FCW / LDW / Stop and Go / Tailgating**(只這 4 個) |
| 6 | Supported DMS events | Distraction / Fatigue / Lens Cover / Phone / Seatbelt(**KB 沒列 Smoking**) |
| 7 | In-cabin alerts | 完整語音指令地圖,見 [voice-alerts.md](voice-alerts.md) |
| 8 | Sensor events | G-Sensor 4 種 + 數值 threshold,見 [adas-dms-events.md](adas-dms-events.md) |
| 9 | Traffic Sign features | **TW 客戶只能承諾 Speed Limit**;Stop / School / Railway 沒支援 |

## KB 待補的區塊(問 Mori / Jimmy)

- 各 KB 文章內「圖片表格」具體數字(FCW TTC / Tailgating distance / Stop and Go configured distance)
- 「Why are thresholds different for Passenger / Medium Vehicle / Heavy Duty?」(車種差異)
- 機種 spec 對照表(K145c / K220 / K245 / K245c / K265 各自鏡頭 / 算力 / SD 容量)
- Master Portal / Fleet Portal / VisionAgent 三大類 KB 文章

## 結構性事實(對所有客戶適用)

- **20 km/h 是 DMS 全域門檻** — 速度沒到 DMS 不會觸發
- **30 km/h × 3 分鐘 + 平坦少彎** = ADAS 基礎計算 / calibration 條件 ⚠️ **2026-05-05 校正過,不是 60 km/h**
- **DMS calibration**:20 km/h × 15 秒,只要司機臉穩定即可
- **Lens Cover exponential backoff**:觸發間隔 2→4→8→16 分鐘
- **熄火後 3 分鐘窗口**:設備不立即關機,先續傳 + 等 ACC 重啟
- **Traffic Sign 分區域支援**:**TW 客戶只能承諾 Speed Limit**
- **MMF (Mobility Map Function)**:**還沒上線、測試中**,不要對任何客戶承諾
- **DMS IR 補光**:夜間反而比白天好(但深色隔熱紙會擋 IR)
- **ADAS 沒 IR**:夜間 recall 必然較差 — 結構性事實

## 不在 KB 但常被問

| 主題 | 真實狀態 | 對客戶口徑 |
|------|---------|-----------|
| Smoking | **KB 標 (in development)**(memory 之前說「KB 沒寫」是錯的)/ Sheet 隱藏 / Roadmap 列 Basic / 4 個 Jira open | ⚠️ 「KB 列開發中」可講有官方依據,**不能保證上線時間** |
| Yawning | KB 沒寫 / Sheet #3 顯示但 still in dev / 2026-05-06 會議:效果不如預期 / **5/7 AI weekly:夜間嘴部辨識不佳,加灰階模型,考慮改辨識整張臉** / Yawning UI toggle 對應 **VMX-7432**(Lucy 5/6 開) | ⚠️ Roadmap planned, 內部測試中 |
| Eating/Drinking | Roadmap Advanced 2027 / HAWK-562 已開 / **5/7:BMS 客訴量是過去 17 倍(ID 6652),6/15 前 7000+ 案例緊急重訓** | ⚠️ 對外維持 2027 Roadmap,內部 6/15 重訓 |
| MMF | KB 沒寫 / Roadmap 列 / 沒上線 | ⚠️ 不對客戶承諾 |
