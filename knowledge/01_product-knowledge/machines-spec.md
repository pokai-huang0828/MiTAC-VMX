# K-series 機種規格

> ⚠️ K-series ↔ Chip ↔ Tier 的具體 mapping **memory 還沒齊** — 必問 Mori。
>
> 📄 **客戶介紹會議的完整機種規格紀錄** → [Google Doc](https://docs.google.com/document/d/1QJj6EOnZz4HFV-wG_SAlFywEw0M01FMjriRc8hwSH7M/edit?tab=t.opseshkr4x94)

## 機種列表(2026-05-08 再校正)

**K145c / K165 / K220 / K245 / K245c / K265** — 共 6 個機種(+ K246 Orion 為下一代,接班 K245c)

✅ **K165 真的存在**:Vinicius (Platform Science) 5/7 testing plan 確認 K165 是 EVO 系列 single lens dashcam,**有實機可測**(某些客戶 single lens 是 requirement)。前一版 memory 寫「沒有 K165」是錯的(2026-04 早期校正),5/8 已修正。

Kenny 自己的測試機:**K245**(L3024290010)

## Connected Dash Camera Lineup 2025(對客戶介紹用)

| 規格 | Sprint (K220) | Gemini SE (K245c) | EVO (K265) |
|------|---------------|-------------------|------------|
| 適用車型 | LCV | Medium Truck | Heavy Truck |
| Platform | Qualcomm SDM450 | Qualcomm SDM450 | Qualcomm QCS610 |
| RAM / Flash | 2GB / 16GB | 2GB / 16GB | 3GB / 32GB |
| OS | Android 10 | Android 9 | Android 10 / Linux |
| Video Channels | 最多 3(+Video Hub 可達 6) | 最多 3(+Video Hub 可達 6) | 最多 7 |
| Storage | 1× SD(最高 1TB) | 1× SD(最高 1TB) | 2× SD(最高 2TB,1TB×2) |
| WiFi / BT | 11ac 2.4/5GHz、BLE 4.2 | 11ac 2.4/5GHz、BLE 4.2 | 11ac 2.4/5GHz、BLE 5.0 |
| NFC | – | 支援 | 支援 |
| OBD / CAN | OBD Cable、MiTAC SmartGO、IOSix | 同左 | 同左 |
| Certification | CE/FCC/IC/RCM/PTCRB;AT&T、T-Mobile | CE/FCC/IC/RCM/PTCRB;AT&T、Verizon、T-Mobile、Telstra | CE/FCC/IC/RCM/PTCRB;AT&T、Verizon、T-Mobile |

→ 來源:客戶介紹會議簡報(Google Doc 同上)。

## CDR(Connected Dash Recorder) Roadmap

| 區隔 | 機種 | 平台 | 主要規格 |
|------|------|------|---------|
| Heavy Truck (up to 7CH) | **EVO (K265, K165)** | QCS610 | 最高 3 TOPS AI、最多 5 路擴充 (1×USB + 4×TVI)、LTE Cat4、WiFi 11ac、BLE 5.0、GPS/QZSS/GLONASS/Galileo、NFC、雙 SD 槽(各 512GB) |
| Heavy Truck | EVO 5G RedCap | QCS610 | 5G NR SA、NA/EU/GL SKU、5G 223 / 123 Mbps、LTE 195 / 105 Mbps |
| Medium Truck (up to 3CH) | **Gemini SE (K245c, K145c)** | SDM450 | 1× USB 擴充、LTE Cat6、WiFi 11ac、BLE 4.2、NFC |
| Medium Truck | Orion – K246 series | QCM6125 | 接班 K245c、4K、強化安全、分級 AI |
| Van / Light Truck (up to 3CH) | **Sprint (K220)** | SDM450 | 1× USB 擴充、LTE Cat6、WiFi 11ac、BLE 4.2、NFC |

✅ **K165 確認有實機**(2026-05-08 Vinicius / Platform Science 5/7 testing plan 揭露):是 EVO 系列 single lens dashcam。前面 memory 寫「沒有 K165」已校正。K165 跟 K265 一起在 Heavy Truck (up to 7CH) tier。待 Mori 確認:K165 specific chip / 算力 / SD 容量。

⚠️ **Orion / K246 系列** 是接班 K245c 的下一代(4K + 分級 AI),memory 沒提過 — 新加進來。

## 待補對應(問 Mori)

| 機種 | Chip(待確認) | Tier(待確認) | TOPs(待確認) | RFID(KB) | QR(KB) |
|------|--------------|--------------|---------------|---------|--------|
| K145c | ? | ? | ? | ❌ | ❌ |
| K165 | ? | EVO single lens | ? | ❌ | ❌ |
| K145 (with i25) | ? | ? | ? | ❌ | ❌ |
| K220 | ? | ? | ? | ❌ | ✅ |
| K245 | ? | ? | ? | ✅ | ✅ |
| K245c | ? | ? | ? | ✅ | ✅ |
| K265 | ? | ? | ? | ✅ | ✅ |

⭐ **第一個 KB 確認的機種 mapping**(2026-05-06):K220 只支援 QR Code(沒 RFID)/ K145(c) 連 QR 都不行(需 i25)。
KB 來源:https://service.visionmaxfleet.com/portal/en/kb/articles/driver-identification-setup-and-usage-for-models-k245-k245c-k265-and-k220

## LED Behaviors(KB 確認的機種差異)

| 機種 | LED 數量 | 差異 |
|------|---------|------|
| **K220 / K245** | 1 個(紅) | Manual Event Button 紅燈;沒 SD 每 15 秒閃 |
| **K265** | **2 個** | 紅(Manual Event Button)+ **橘左**(沒網路常亮)+ **藍/綠右** |
| **K145c / K245c** | (KB 待補,沒抓全) | (待 deep read) |

KB 來源:https://service.visionmaxfleet.com/portal/en/kb/articles/led-behaviors

## Reset Button(KB 確認的機種差異)

| 機種 | Reset Button 位置 |
|------|-----------------|
| **K245 / K145c / K245c** | **在 tamper proof cover 後**(要先拆) |
| **K220 / K265** | (KB 沒明說,可能是露出的) |

→ Reset = paper clip 戳。對應 troubleshooting Q10。

## 從 MiAI Roadmap 對應的 Chip 候選

| Tier | Year | Chip | TOPs |
|------|------|------|------|
| Entry | 2023 Foundation | Snapdragon 450 | < 1 |
| Basic | 2025 Expansion | QCS 6125 / QCS 610 | 1 |
| Advanced | 1H'2027 | QCS 5430 | 6 |
| Premium | 2H'2027 | QCS 6490 | 12 |

→ 推測:K245(Kenny 的)很可能是 Basic tier(2025 主力 ship 機種),但**沒確認**。

## 硬體技術棧

- 4G LTE 連網
- **雙鏡頭**:road-facing ADAS + cabin-facing DMS
- Android SoC 平台
- Cloud:`visionmaxfleet.com`
- 三層客戶整合深度:Web Platform / API / Custom SDK

## 影像規格(KB 已抓 2026-05-06)

| Video Type | Resolution | FPS | Bitrate | Size/3min |
|-----------|-----------|-----|---------|-----------|
| Side by Side(雙鏡頭並列) | 2560 × 720 | **10** | 2,764,800 | 58.8 MB |
| Separated Video(雙鏡頭分離) | 1280 × 720 | **10** | 1,382,400 | 29.4 MB |
| AUX UVC Cam(外接 UVC) | 1280 × 720 | **10** | 5,000,000 | 106.8 MB |
| AUX USB Cam(外接 USB) | 2560 × 1440 | **10** | 5,529,600 | 118.8 MB |
| Live View | 854 × 480 | — | 800,000 | 0.1 MB/s |

⚠️ **memory 之前說 15-30 fps 是錯的**(2026-05-06 KB 校正)— 全部 10 fps。
KB 來源:https://service.visionmaxfleet.com/portal/en/kb/articles/what-is-the-resolution-fps-bitrate-and-video-size-for-mitac-s-cameras

⚠️ KB 上沒按 K145c / K165 / K220 / K245 / K245c / K265 拆分 — 是按 video type(Side by Side / Separated / AUX UVC / AUX USB)拆。各 K 機種能跑哪些 video type **要 Mori 確認**。

## K265 SD update 架構限制(2026-05-07 Righter 揭露,Platform Science 案)

> 來源:Righter Song 2026-05-07 給 Vinicius 信件

- **K265 SD 卡更新不能 overwrite all partitions**(架構限制)
- 設備如果是 **LM (Lightmetrics) 版本,不能用 SD update 升到 VisionMax 版**
- 升 SD 後設備會 malfunction
- 對應策略:**直接給 VisionMax 版 sample**,不要先給 LM 版再升

→ **影響 Honeywell ME CDR 案**:5/11 起 6K 出貨的 K265 必須出廠就是 VMX 版 firmware,不能晚期切換。對應 [case-learning/honeywell-me-cdr-opportunity.md](../../case-learning/honeywell-me-cdr-opportunity.md) 風險點。

---

## 待 Coffee Chat 問 Mori

1. K145c / **K165** / K220 / K245 / K245c / K265 各跑哪顆 Qualcomm chip(K165 5/8 新加,Vinicius 5/7 確認有實機)
2. K245(Kenny 自己的)屬 Entry / Basic / Advanced 哪個 tier
3. ~~各機種 frame rate~~ ✅ 已釐清:機體可達 15-30 fps,**對外 only 10 fps**(運算資源限制,2026-05-07)
4. 紅色按鍵各機種語音不一致 — 是哪幾台?
5. Private Mode 切換按法(KB 沒寫清楚)
6. **Harsh Acceleration / Rollover G 值門檻**(只 lock 4 種,缺這 2 種)
7. 200 Hz G-Sensor 韌體可行性(2026-05-06 會議 Simon 客戶要求)
