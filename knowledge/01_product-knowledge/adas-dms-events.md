# ADAS / DMS / G-Sensor / Map / OBD-II 完整事件

來源:KB 已讀 + MiAI Roadmap 2026-04-24 + 2026-05-06 Q2 Review 會議

## ADAS 事件(rd-facing camera)

### KB FAQ 確定(已 ship,可對客戶承諾)
官方 KB(https://service.visionmaxfleet.com/portal/en/kb/articles/what-adas-and-dms-features-do-you-support):
- **FCWS**(語音 = `"Keep distance"`)
- **LDWS**
- **Tailgating**
- **Rolling Stop** ⭐ (memory 之前漏)
- **Stop & Go**

### KB 標(in development)— 對客戶可講「開發中」
- **Speed Sign**(in development) — Roadmap 列 Advanced 2027,KB 對外目前是 dev。**5/7 AI weekly 補**:模型對 18/25/40 數字易混淆,根因是訓練 Flip 參數開啟,Jay 已立即關閉 + 擴增降至 10 倍重訓。新單 VMX-7430 / VMX-7431(woody.lee 5/6 開)+ VMX-7320 / VMX-7321(speed sign violation)

### Roadmap 列但 KB 沒寫(對客戶要小心)
| 功能 | Roadmap Tier | 狀態 |
|------|--------------|------|
| FCWS | Basic(2025) | ✅ 已 ship(2026-05-07 校正,memory 之前寫 PCWS 是錯的) |
| Rolling Stop Sign | Basic | ✅ 已 ship(2026-05-07 校正) |
| Blind Spot Monitoring (Side Camera) | Basic | 對應 S_F_R Single SKU 進行中 |
| Speeding Sign | Advanced(2027) | ⚠️ Roadmap planned |
| BCWS (Rear Camera) | Advanced | ⚠️ Roadmap planned |
| Rash Driving | Premium(2027) | ⚠️ Roadmap planned |
| Traffic Light | Premium | ⚠️ Roadmap planned |
| ANPR (License Plate Recognition) | Premium | ⚠️ Roadmap planned |
| Blurring function (ADAS) | (Roadmap Slide 2 寫 Burning ADAS,實為 Blurring)  | 對應 server-side 影像模糊化(2026-05-07 校正) |

## DMS 事件(cabin-facing camera)

### KB FAQ 確定(已 ship)
- **Distraction**
- **Fatigue**(細分 Yawning / Nodding off / Sleepy 三個子事件)
- **Phone Usage**
- **Unfastened Seatbelt**(Server-side AI 90-95% accuracy)
- **Lens Covered**(觸發 backoff:2→4→8→16 分鐘)

### KB 標(in development)
- **Smoking**(in development)⭐ memory 之前說「KB 沒寫」是錯的 — KB 有寫,標 in development

### Roadmap 列但 KB 沒寫
| 功能 | Roadmap Tier | 真實狀態(2026-05-06 會議揭露) |
|------|--------------|-----------------------------|
| **Yawning(Fatigue 子)** | Basic(2025) | ⚠️ 還沒給客戶 / 內部測試中 / 效果不如預期 / Fatigue config 下要加獨立開關。**5/7 補:夜間嘴部辨識效果不佳,加入「灰階(Grayscale)」模型重訓 + 考慮 Server 端從辨識嘴巴改為「辨識整張臉」**。Yawning UI toggle 對應 **VMX-7432**(Lucy 5/6 開) |
| **Smoking** | Basic(2025) | ⚠️ KB 標 (in development)/ Sheet 隱藏 / 4 個 Jira ticket open(VMX-6670 / 7324 / 6380 / 6920) |
| **Obstructed Camera** | Basic | 對應 Quantatec 案 VMX-6983 / VMX-7427 / HAWK-582。**5/7 揭露 Lens Cover 規格雙軌**:Azuga 標準版 = 解除車速;BMS 版 = 車速 > 0 才啟動 |
| Eating | Advanced(2027) | HAWK-562 已開 ticket(Jimmy + Vincent 5/7 加入)— **比 Roadmap 提早動工**。**🚨 5/7 揭露:BMS 客訴量是過去 17 倍(客訴 ID 6652),6/15 前 7000+ Edge case 一次性緊急重訓** |
| Drinking | Advanced | (同 Eating,共用 6/15 重訓) |
| Blurring function (DMS) | (Roadmap Slide 2 寫 Burning DMS,實為 Blurring) | 對應 cabin 影像模糊化(2026-05-07 校正) |
| VLM-based Behavior Understanding | Premium(2027) | sheet 標 2026 Q3 — 內部比 Roadmap 提早 |

## G-Sensor 事件(共 6 種,Roadmap 列)

| 事件 | 速度條件 | Low | Medium(預設) | High |
|------|---------|-----|---------------|------|
| **Harsh Braking** | > 11 km/h | > 0.55 G | > 0.45 G | > 0.35 G |
| **Harsh Cornering** | > 30 km/h | 同 Harsh Braking | 同 | 同 |
| **Driving Impact**(行駛中) | 無 | > 1.2 G | > 0.9 G | > 0.7 G |
| **Parking Impact**(停車中) | 無 | > 0.8 G | > 0.5 G | > 0.2 G |
| **Harsh Acceleration** | ? | ⚠️ 待 Mori | ⚠️ | ⚠️ |
| **Rollover** | 無 | ⚠️ 待 Mori | ⚠️ | ⚠️ |

**Reference scale**:普通煞車 ≈ 0.3-0.4 G / 急煞 (Med) = 0.45 G / 真實碰撞 (Med) = 0.9 G / 嚴重碰撞 = 1.2 G+

⚠️ **200 Hz G-Sensor 戰略議題**(2026-05-06 會議):客戶 Simon must-have 事件發生時吐 200 Hz,目前 50 Hz。Mori 在弄。

## Map-based 事件(GPS + Map,4 種)

- Mobility Map Function(MMF)— ⚠️ **還沒上線,不要對客戶承諾**
- Speed Camera Violation
- Railroad Crossing Alert
- School Zone Alert

## OBD-II 事件(6 種)

- Low Fuel
- Increase Fuel
- Decrease Fuel
- Battery Voltage
- VIN Change Event
- Diagnostic Trouble Codes

## Sensitivity Dial 估計值(⚠️ 估計,真實要問 Jimmy)

| Sensitivity | Confidence | Debounce | Cooldown | 行為 |
|-------------|-----------|----------|----------|------|
| Low | ~0.85 | 5 秒 | 長 | FP 少、FN 多 |
| Medium | ~0.70 | 3 秒 | 中 | 平衡 |
| High | ~0.55 | 1.5 秒 | 短 | FP 多、FN 少 |

對應 Jira:**HAWK-419 / VMX-6837** Independent Sensitivity Thresholds for Distractions(Jieli)

## AI Inference Pipeline(任何 AI 客訴用此框架定位)

```
1. Capture(感測)         鏡頭 + IMU + GPS,**對外 only 10 fps**(機體可達 15-30,因運算資源限制)
2. Preprocess(預處理)    resize / normalize / ROI 切割
3. Detection(偵測「是什麼」)  bounding box + confidence
4. Classification(分類「在做什麼」)  ⭐ 誤判主戰場
5. Decision(決策)        ⭐ Sensitivity dial 在這層
                          threshold + debounce + cooldown
6. Fire(觸發 + 上傳)     event packaging + 4G upload
```
