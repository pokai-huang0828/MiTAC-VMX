# VisionMax Driver Scorecard / Safety Score

> 來源:KB「VisionMax Driver Scorecard」(2026-05-06 deep read)
> 用途:對客戶 demo Safety Score / Coaching 必背

## 啟用條件

- Driver profile 已建
- Driver 已 log in/out 車輛
- Score 計算需累積 **> 5,000 km** 駕駛距離

## 計分機制

### 初始
- 每個 driver 起始 Safety Score = **100**

### 計分基於
1. **Sensor-detected events**(impact / harsh driving)
2. **AI-detected events**(ADAS / DMS)
3. **Speeding events**

### 規則
- 各 event type 有 specific weighting(**可調**)
- 事件越多分數越低
- 只看 **最近 5,000 km** 的事件(滾動視窗)

## 公式(KB 揭露,2026-05-07 補完整)

```
Safety Score = (1 − (∑ Trip score) / 5000) × 100

Trip score    = TRUNCATE((Event Score × 70 / 100) + (Overspeed Score × 30 / 100), 2)
Event Score   = Event Score × Weight
Overspeed Score = (Cumulative distance of Overspeed / Trip distance) × 100
```

**重點**:
- Event 與 Overspeed 是 70 / 30 加權
- Event Score 還會再乘上 per-event-type weighting(各事件可調)
- Overspeed 用「**超速距離 / 行程距離**」百分比,不是次數
- 整體分數是 **5,000 km 滾動視窗** 累積 trip score 的反向(扣越多分越低)

## 對 PM 議題的對應

- 對應 sheet **#186 Safety Score at vehicle level instead of by driver**(Simon,VMX-7151)
  - 客戶要的是「車輛層級」(not driver) — KB 明確是 driver-based
  - 可能要 fork 一套新邏輯 / 新 weighting
- 對應 #164 Modify Safety Reports(VMX-7083)— PDF 報表內容跟網頁顯示不一致
- 對應「事件 weighting 可調」 → Brian 同步戰略想開放 fleet 改

## 客戶口徑

> 「Safety Score 從 100 起算,基於 sensor / AI / speeding 三類事件加權扣分,只看最近 5,000 km 的滾動視窗。各事件 weighting 在內部維護,目前 fleet manager 不能改。」(對應 KB「Threshold not customizable」)

## 待釐清(Coffee Chat)

- 完整公式(KB 截斷)
- 各事件 weighting 具體值(不對外公開但 PM 內部要知道)
- **Vehicle level Safety Score** 跟 driver level 怎麼整合(VMX-7151 議題)
