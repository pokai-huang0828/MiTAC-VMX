# VMX In-Cabin Voice Alerts

來源:KB 第 7 篇「In-cabin alerts」+ Coffee chat 整理

## 重要 Voice Alerts(必背)

| 語音 | 含義 | 對應事件 |
|------|------|---------|
| **"Keep distance"** | FCW(前車距離過近)| ADAS 主要 alert |
| **"Can't detect the road level, ADAS off"** | ADAS 計算中斷 | **VMX-7404 黃金線索**,30 km/h × 3min 沒滿足 |
| **"Can't find a face, DMS off"** | DMS 自動停用 | DMS 失效訊號 |
| **"Emergency Recording"** | 紅色按鍵 manual event | KB 內 "Manual Event Recording" vs "Emergency Recording" 不一致 ⚠️ |
| **"Private Mode On / Off"** | 紅色按鍵切換 | 具體按法 KB 沒寫清楚 ⚠️ |

## ⚠️ 已校正(別再答錯)

| 我之前答錯 | 正確答案 |
|-----------|---------|
| FCW = "Frontal Collision Warning" | **"Keep distance"** |

## 待釐清(Coffee Chat)

- ⚠️ **Manual Event Button vs Panic Button 衝突**(2026-05-06 KB deep read 發現):
  - KB「Manual Event Button Behaviors」講接電話 / Manual event / Server callback / 格 SD
  - KB「Behaviour of Privacy Mode」講 **Panic Button hold > 2s** 進 / 退 Privacy Mode
  - **可能是兩個不同 button**,或同一個 button 不同 hold 時間
  - **必問 Mori**:紅色按鍵 = Manual Event 還是 Panic?各機種幾個 button?
- KB 「Manual Event Recording」vs 「Emergency Recording」哪個是真的
- 紅色按鍵語音各機種不一致(問 Mori 哪幾台)

## Privacy Mode 切換(KB 已 deep read)

來源:https://service.visionmaxfleet.com/portal/en/kb/articles/visionma

- **進入**:Press and hold Panic Button > 2 秒
- **進入後行為**:
  - 停止上傳 health / GPS / photo / video
  - AI + sensor event detection 暫停
  - SD 錄影暫停
  - Manual Event Button 按下時 camera **仍會錄**(不受 Privacy 影響)
- **退出**:Panic Button hold > 2 秒
- **Restart 後維持 Privacy Mode**(不會自動退出)

## Manual Event Button 完整行為(KB 已 deep read)

來源:https://service.visionmaxfleet.com/portal/en/kb/articles/emergency-button-behaviors

| ACC | 場景 | 動作 | 行為 | 語音 |
|-----|------|------|------|------|
| ON | 來電 | 短按 | 接電話 | — |
| ON | 來電 | hold > 2s | 拒接 | — |
| ON | 無來電 | 短按 | Manual event recording | "Manual Event Recording" |
| ON | 無來電 | hold 2-6s | Call out to server | — |
| ON | 無來電 | long press +3s | Back to base call | — |
| OFF | Clean install | 短按 / hold > 1s | 開機 | "Device Ready" |
| OFF | ACC mode | 短按 | Manual event recording | "Manual Event Recording" |
| OFF | — | hold 10-30s | 格式化 SD card | "SD Card formatting, please wait" |

⚠️ Private mode 中,「接電話 + Manual event」不執行(其他仍可)
