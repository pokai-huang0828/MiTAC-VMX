# Vehicle Classification + Camera Height

> 來源:KB Fleet Portal「How are passenger / medium / heavy defined and how is camera height set」(2026-05-06 抓)

## Class 分類(KB)

| Class | 類型 | 重量(lbs) | 例子 |
|-------|------|-----------|------|
| 1-3 | Passenger / Light Duty | 6,000 - 14,000 | Pickup trucks |
| 4-6 | Medium Duty | 14,001 - 26,000 | Delivery vans |
| 7-8 | Heavy Duty | > 26,001 | Long-haul, construction |

## 為什麼要分(KB:Why are thresholds different)

- 載重影響加速 → 大車需要更多時間到同樣速度
- 因此各事件 threshold 必須差別設定

## Camera Height 設定

- 各 vehicle 類型有 **specific height settings + AI parameters**
- VisionMax 開發了 **3 種 vehicle types 對應的 height + AI param**
- 技術人員需測量實際安裝高度

## 對應 PM 議題

- **HAWK-501 Camera height 不穩定**(2026-05-06 Q2 sheet) → 跟車種高度設定有關
- 客戶問「為什麼相同事件 threshold 不同」→ KB 有官方答案
- ADAS calibration 30 km/h × 3min 條件 → 跟 camera height 都是 ADAS 準確度的關鍵
