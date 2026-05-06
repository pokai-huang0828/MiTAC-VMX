# K-series 機種規格

> ⚠️ K-series ↔ Chip ↔ Tier 的具體 mapping **memory 還沒齊** — 必問 Mori。

## 機種列表(校正過)

**K145c / K220 / K245 / K245c / K265** — 共 5 個機種

⚠️ **沒有 K165**(之前 Claude 答錯過)

Kenny 自己的測試機:**K245**(L3024290010)

## 待補對應(問 Mori)

| 機種 | Chip(待確認) | Tier(待確認) | TOPs(待確認) | RFID(KB) | QR(KB) |
|------|--------------|--------------|---------------|---------|--------|
| K145c | ? | ? | ? | ❌ | ❌ |
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

⚠️ KB 上沒按 K145c / K220 / K245 / K245c / K265 拆分 — 是按 video type(Side by Side / Separated / AUX UVC / AUX USB)拆。各 K 機種能跑哪些 video type **要 Mori 確認**。

## 待 Coffee Chat 問 Mori

1. K145c / K220 / K245 / K245c / K265 各跑哪顆 Qualcomm chip
2. K245(Kenny 自己的)屬 Entry / Basic / Advanced 哪個 tier
3. 各機種 frame rate(15 / 30 fps?)
4. 紅色按鍵各機種語音不一致 — 是哪幾台?
5. Private Mode 切換按法(KB 沒寫清楚)
6. **Harsh Acceleration / Rollover G 值門檻**(只 lock 4 種,缺這 2 種)
7. 200 Hz G-Sensor 韌體可行性(2026-05-06 會議 Simon 客戶要求)
