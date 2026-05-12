# VMX In-Cabin Voice Alerts(完整 KB 抓)

> 來源:KB「What in-cabin alerts are available?」(2026-05-06 deep read)
> 預設語言 English (US),portal 可改

## 1. Device Startup and Status

| 事件 | 語音 |
|------|------|
| Device powers on | **Device Ready** |
| Driver ID card 成功讀取 | Success |
| Driver 需要 tap ID | Please tap your ID card |
| ID card 讀取失敗 | Failed to read the ID Card |
| Camera calibration 完成 | Calibration Completed |
| OTA 完成 | Auto update complete |

## 2. SD Card

| 事件 | 語音 |
|------|------|
| 沒 SD card | No SD Card |
| SD card 滿 | SD Card Full |
| 格式化中 | SD Card Formatting, please wait |
| 格式化完成 | Format completed |
| 讀寫 / 格式化錯誤 | SD Card Error |

## 3. System Reconfiguration

| 事件 | 語音 |
|------|------|
| SD 掛 / 卸 / 第三鏡頭裝卸 | Setting up device, please wait |
| Remote / manual setting 套用 | Setting up device, please wait |

## 4. Wi-Fi Hotspot

| 事件 | 語音 |
|------|------|
| Hotspot 開 | Hotspot ON |
| Hotspot 關 | Hotspot OFF |

## 5. Driving Behaviour Events(G-Sensor)

| 事件 | 語音 |
|------|------|
| Harsh acceleration | Harsh Acceleration Detected |
| Harsh braking | Harsh Braking Detected |
| Harsh cornering | Harsh Cornering Detected |
| Impact (driving) | Impact Detected |
| Impact (parked) | Impact Detected |
| Manual emergency recording | **Emergency Recording** |
| Long-time driving | **Time for a break** ⭐ memory 沒這條 |

## 6. ADAS Events

| 事件 | 語音 |
|------|------|
| FCW(Frontal Collision Warning) | **Keep distance** |
| LDW(Lane Departure Warning) | Lane departure |
| Stop and Go | Traffic has moved, please proceed |
| Tailgating | Tailgating |
| Collision risk | Collision risk detected |
| ADAS enabled | ADAS on |
| ADAS disabled (no road level) | **Can't detect the road level, ADAS off** ⭐ [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 黃金線索 |

## 7. DMS Events

| 事件 | 語音 |
|------|------|
| Yawning | Yawning detected, stay alert |
| Nodding off | Nodding off detected, stay alert |
| Eyes closed | **Sleepy detected, stay alert** ⭐(三個 Fatigue 子事件全有獨立語音)|
| Distraction | Distraction detected, keep eyes on road |
| Cell phone usage | Cell phone usage |
| Unfastened seatbelt | **Danger! Fasten your seat belt** |
| In-cabin camera obstructed | **Alert! Inward camera is blocked, please remove the obstacle** ⭐ 對應 Quantatec / [VMX-7427](https://jira.navman.co.nz/jira/browse/VMX-7427) |
| DMS enabled | DMS on |
| DMS disabled (no face) | Can't find a face, DMS off |

## 8. Traffic Sign and Signal Events

| 事件 | 語音 |
|------|------|
| Stop sign detected | Stop sign detected |
| Stop sign violation (rolling stop) | Stop sign ahead, slow down your speed |
| Red light violation | Red Light Violation |
| Speed camera ahead | Safety camera ahead |
| Average speed camera (Autodoria) | Average speed camera ahead |
| Speed camera violation | Speed Camera Violation |
| Rolling stop | Rolling Stop |
| Railway crossing ahead | Railway crossing ahead |
| Railroad crossing violation | Railroad Crossing Violation |
| School zone ahead | School zone ahead |
| School zone speed violation | School Zone Speed Violation |
| Wrong-way driving | Turn around safely, you are going in the wrong direction |

## 9. Speed Limit Reminders

格式:**"Speed limit [value]"** — 例:Speed limit 30 / 40 / ... / 110

| 事件 | 語音 |
|------|------|
| 超過 cruise speed | Lower your speed |
| Speed limit 提醒 | Speed limit --- |

## 10. Geofencing

| 事件 | 語音 |
|------|------|
| 進入 geofence | Enter Geofence |
| 離開 geofence | Leave Geofence |

## 11. System and Privacy

| 事件 | 語音 |
|------|------|
| Device call-out | Calling |
| **Private mode enabled (panic button)** | **Private Mode On** |
| **Private mode disabled (panic button)** | **Private Mode Off** |
| Camera error auto-recovery | Camera Rebooting, Please Wait |
| Camera errors 無法 fix | (待抓全文) |

## ⚠️ 重要校正 / 區分

### Manual Event Recording vs Emergency Recording
- **Manual Event Recording**:短按按鈕(無來電時)= 錄一個 manual event
- **Emergency Recording**:**Manual emergency recording triggered**(更緊急情境的 G-Sensor 觸發)
- **不是同一個!** memory 之前以為是同一個是錯的

### Privacy Mode = Panic Button
- KB 在這份明確寫「Private mode enabled (panic button)」
- 跟 Privacy Mode 文章 + Manual Event Button 文章對應
- ⚠️ **可能 Manual Event Button 跟 Panic Button 是同一個按鈕的不同 hold pattern**(短按 = Manual / hold > 2s = Panic / hold 10-30s = format SD)
- 還是要 Coffee Chat 跟 Mori 釐清

### Reset Button ≠ Manual Event Button(KB 確認)
- **Manual Event Button = Red Indicator Light**(K220/K245/K265)— **可徒手按**
- **Reset Button = paper clip 戳**(K245/K145c/K245c 在 tamper proof cover 後)
- → 是兩個不同的 button

### [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure 黃金線索
語音 `"Can't detect the road level, ADAS off"`
- 觸發條件:速度 < 30 km/h 持續 / 車速反覆掉到 30 以下 / ADAS 計算中斷
- 市區通勤經典情境
