# 已校正的關鍵 VMX 事實

> 過去 Claude / 對話中答錯後修正的事實。**對 RD / 客戶 / 內部講話前先看這份**。

## BMS 客戶端 API 有 driver/passenger 獨立 blurring 能力(2026-05-08 校正)
- ❌ 之前以為:redocly v2026-Q1 沒 blurring endpoint = blurring 沒 driver/passenger 區分
- ✅ **正確**:**BMS 客戶端內部 API 已支援 driver/passenger 獨立 blurring control,只是沒對外公開**
- 校正日:2026-05-08
- 校正人:Kenny(回覆 Cary 5/7 thread 後內部確認)
- 應用:對 Cary / Wendy 講「現有 API 已支援」有依據,但**邊界**是「能力存在」≠「公開可用」(要 Q2 2026 update 才能 ship 給 CONNECTSOURCE)
- 跟 Brian 5/4 給 Wendy 的「Q2 2026 update / 7 月最早 ship」commitment 一致

## Master Portal Blurring config UI 路徑(2026-05-08 兩次校正)
- ⚠️ **v1 早上 Brian/Spencer 確認可實作**:`Master Portal > Management > Fleets > (select Fleet) > Fleet Detail > Configurations > (new) Blurring`
- 🚨 **v2 同日下午 5/8 Sync-up Meeting Elvis 螢幕分享現場糾正**:這條路徑**只能控制整個 main fleet 級**,一動 = 影響 main + 所有 contract fleets,**沒 per-contract-fleet 粒度**
- 客戶實況:Australia 1 fleet + 各 reseller 客戶當 contract fleets,**必須 pinpoint 特定 contract fleet**
- ✅ **修正後兩條實作路徑**(待 Brian / Spencer 拍):
  - **(A)** Master Portal 補 contract fleet 視圖 + 加 Blurring config — ⚠️ 隱私問題(contract fleet 不見得想讓上層看到)
  - **(B)** Fleet Portal 加 per-contract-fleet Blurring config UI(沿用 Live User pattern)
- 應用:**Kenny 5/7 14:41 回信對外承諾的 portal path 不夠精細**,要回 thread 校正
- 詳見:`meetings/2026-05-08_syncup-cary-elvis_meeting-record.md` + `cary-passenger-blurring-2026-05-07.md` H 段

## 機種列表(2026-05-08 再校正)
- ❌ v1 之前答:K245 / K265 / K165
- ⚠️ v2 校正(2026-04):K145c / K220 / K245 / K245c / K265(認為沒有 K165)
- ✅ **v3 真相(2026-05-08 Outlook Vinicius 5/7 信件揭露)**:**K165 真的存在** — Vinicius 在 5/7 11:02 AM 給 Paul Lee 的 testing plan 中明確要求測 K165(single lens dashcam,某些客戶 single lens 是 requirement)。
  - 所以 K-series 完整應為:**K145c / K165 / K220 / K245 / K245c / K265**(可能還有 K246 Orion 未來機種,Vinicius 也提到)
- 校正人:Vinicius Francisquinho (Platform Science) 5/7 testing plan
- 重要:**對 Vinicius / Platform Science 不要再說「沒有 K165」**;K165 = 單鏡頭 dashcam 版本
- 待動作:跟 Mori 確認 K165 完整 spec(chip / 鏡頭 / 算力)+ 為什麼之前 memory 說沒有

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

## ADAS 範圍 vs DMS(初版校正)
- ❌ 之前答:ADAS 含 yawning / phone / smoking
- ✅ **正確**:DMS 是另一回事;ADAS 範圍詳細看下方 5/6 KB 校正

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

## Yawning 真實狀態(2026-05-06 / 5/7 兩次校正)
- ❌ 之前答:Roadmap Basic tier 已有
- ✅ **5/6 會議揭露**:還沒給客戶用,內部測試中,效果不如預期。Fatigue config 下要加獨立 enable/disable 子選項
- ✅ **5/7 AI weekly 補**:夜間嘴部辨識效果不佳,加入「灰階(Grayscale)」影像重新訓練,並考慮 Server 端從「辨識嘴巴」改為「辨識整張臉」
- 對外口徑:「Roadmap planned, 內部測試中」**不能說「已有」**
- Yawning UI toggle 真實對應 ticket:**VMX-7432**(Lucy 5/6 開,assignee)

## Brian #11 OTA 17 個月 ticket 性質
- ❌ 之前答:stale(Brian 拖延)
- ✅ **正確**:**不是內部 stale,是 Akamai CDN 設定問題**
- 校正日:2026-05-06
- 校正人:會議錄音(Brian 自己說)
- 重要:**別在 Brian 面前主動提這個 ticket**

## #154 Server AI lane departure 為什麼 API 沒釋出(2026-05-07 再校正)
- ❌ v1 之前答:RD 沒做完
- ⚠️ v2(5/6 會議錄音 Brian 自評):「Q1 已 merge 但 label 沒設好,Brian filter 時漏 pick」
- ✅ **v3 真相(2026-05-07 讀 VMX-6722 comments + sub-tasks)**:VMX-6722 **本身有 label `vmx_2026Q2`**,sub-tasks 全 closed/resolved + jimmy 3/11 留「Server AI 已完成並 deploy 到 prod」+ parent ticket 仍 NEW。**不是 label 漏 pick,是 transition discipline gap** — RD 寫 comment 沒按 Open→Resolved button
- 校正日:2026-05-07(Comment 深掘後)
- 重要:**對 Brian 提 process improvement 從「transition 紀律」切入,不是「label 紀律」**
- 補充:**LDWS 5/7 完整故事**:Server-side(VMX-6722)Q1 確實 deploy。但 device 端 YOLO Lane Detection 改善是 5/7 AI weekly 決議 Pending 暫緩 + 開新 ticket(編號待釐清)— 這是另一條工作

## ADAS 範圍(2026-05-06 KB 校正)
- ❌ 之前答:只含 FCW / LDW / Stop and Go / Tailgating
- ✅ **正確**:**FCWS / LDWS / Tailgating / Rolling Stop / Stop & Go(已 ship)+ Speed Sign(in development)**
- 校正人:KB 2026-05-06
- 註:詳細 5/7 補充 Speed Sign Flip 重訓在 [feedback_vmx_facts.md] memory

## Smoking 在 KB 真實狀態(2026-05-06 校正)
- ❌ 之前答:狀態待釐清
- ✅ **正確**:**KB 上 Smoking 標 (in development)**。對外可講「開發中」有官方依據
- 校正日:2026-05-06
- 註:Sheet row 隱藏 / Jira 多單 open 是內部狀態,不影響對外口徑
