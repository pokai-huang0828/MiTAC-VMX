# 已校正的關鍵 VMX 事實

> 過去 Claude / 對話中答錯後修正的事實。**對 RD / 客戶 / 內部講話前先看這份**。

## 機種列表
- ❌ 之前答:K245 / K265 / K165
- ✅ **正確:K145c / K220 / K245 / K245c / K265**(沒有 K165)
- 校正日:2026-04 早期
- 校正人:Kenny

## 紅色按鍵功能
- ❌ 之前答:Panic + 雙擊取消 + 長按重啟 + factory reset
- ✅ **正確**:接聽電話 + Manual event + Server callback + 格化 SD(**沒 panic event**)
- 校正人:Kenny

## FCW 語音
- ❌ 之前答:"Frontal Collision Warning"
- ✅ **正確**:`"Keep distance"`
- 校正人:Kenny

## 疲勞分類
- ❌ 之前答:單一 Fatigue event
- ✅ **正確**:細分 Yawning / Nodding off / Sleepy 三個子事件
- 註:Yawning 真實狀態 → 看 [roadmap-vs-internal.md](roadmap-vs-internal.md)

## ADAS 範圍
- ❌ 之前答:含 yawning / phone / smoking
- ✅ **正確**:**只含 FCW / LDW / Stop and Go / Tailgating**;DMS 是另一回事
- 校正人:Kenny

## Smoking 在不在官方 list
- ❌ 之前答:在
- ✅ **正確**:**不在 KB list**(Sheet row 隱藏 / Roadmap 列 Basic / 4 個 Jira open)— **狀態待釐清**
- 註:VMX-7324 客訴根源就是這個
- 待動作:Coffee chat 找 Jimmy 釐清

## ADAS 觸發時間 / Calibration 條件
- ❌ 之前答:60 km/h × 3 分鐘
- ✅ **正確**:**30 km/h × 3 分鐘 + 平坦少彎**
- 校正日:2026-05-05
- 校正人:Kenny
- 重要:**沒滿足就觸發 ADAS Failure**,語音 `"Can't detect the road level, ADAS off"`
- 應用:**VMX-7404 根因**,市區走停會反覆觸發

## G-Sensor 事件數
- ❌ 之前答:4 種(Harsh Braking / Cornering / Driving Impact / Parking Impact)
- ✅ **正確**:**6 種**(+ Harsh Acceleration + Rollover)
- 校正日:2026-05-05(MiAI Roadmap 揭露)
- 註:Harsh Acc / Rollover G 值門檻 ⚠️ 待 Mori 確認

## VLM Roadmap 時程
- ❌ 之前答:2H'2027(對內)
- ✅ **正確**:對內 Sheet 寫 2026 Q3,**對外用 Roadmap 2027**(Kenny 裁示)
- 校正日:2026-05-05

## AI sheet 隱藏 row 是「PM 介入空間」
- ❌ 之前答:hidden row + No PIC = PM 該扛
- ✅ **正確**:**hidden row = 團隊已決定不做**,別扛
- 校正日:2026-05-05
- 校正人:Kenny

## Yawning 真實狀態(2026-05-06 會議揭露)
- ❌ 之前答:Roadmap Basic tier 已有
- ✅ **正確**:**還沒給客戶用,內部測試中,效果不如預期**
- 校正日:2026-05-06
- 校正人:會議錄音
- 對外口徑:「Roadmap planned, 內部測試中」**不能說「已有」**

## Brian #11 OTA 17 個月 ticket 性質
- ❌ 之前答:stale(Brian 拖延)
- ✅ **正確**:**不是內部 stale,是 Akamai CDN 設定問題**
- 校正日:2026-05-06
- 校正人:會議錄音(Brian 自己說)
- 重要:**別在 Brian 面前主動提這個 ticket**

## #154 Server AI lane departure 為什麼 API 沒釋出
- ❌ 之前答:RD 沒做完
- ✅ **正確**:**Q1 已 merge 但 label 沒設好,Brian filter 時漏 pick**
- 校正日:2026-05-06
- 校正人:會議錄音
- 重要:**這是 PM process 介入空間**(merge label sweep)
