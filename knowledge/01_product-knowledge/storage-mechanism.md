# Storage Overwrite Mechanism(SD Card + Internal Flash)

> 來源:KB「SD Card Overwriting Mechanism」+「Internal Flash Overwrite Mechanism」(2026-05-06 deep read)
> 對客戶解釋「老影片去哪了 / 為什麼 event 找不到」必備

## SD Card(主要儲存)

3 種文件類型 + storage limit:

| 類型 | 何時錄 | Storage Limit | 觸發刪除條件 | 每次刪量 |
|------|-------|--------------|------------|---------|
| **Video** | Normal recording | (空間優先)| 剩餘 < 1.5 GB | 2 GB |
| **Event** | ACC on 觸發 | 9% 總容量 | 用滿 9% | 100 MB |
| **Parking Event** | ACC off 觸發 | 9% 總容量 | 用滿 9% | 100 MB |

- **檢查頻率:每 50 秒**
- 例:128 GB SD → Event 限 11.52 GB(128 × 9%)→ 滿了刪 100 MB

## Internal Flash(內部儲存)

4 種文件類型:

| 類型 | 內容 | Storage Limit | 觸發 | 每次刪量 |
|------|------|--------------|------|---------|
| **Event** | ACC on 觸發 | 10% | 用滿 10% | 100 MB |
| **Parking Event** | ACC off 觸發 | 10% | 用滿 10% | 100 MB |
| **Snapshot** | Timeline / Face ID / Headshot | 5% | 用滿 5% | 100 MB |
| **Photo** | 事件觸發拍照 | **100 張** | 超過 100 張 | 1 張(最舊) |

- **檢查頻率:每 50 秒**(item 1-3)/ 每張照片觸發時(item 4)
- 例:8 GB internal flash → Event 限 819 MB(8 × 1024 × 10%)

## Cloud Retention(KB FAQ)
- 所有 video + 相關資料:**180 days**(對外標準保留期)

## 對 PM 議題

### 客戶問「我上個月的 event 影片不見了」
- 先看是 SD 或 Cloud
- SD:9% Event 限制可能滿了(每 100 MB 刪)
- Cloud:超過 180 days 自動刪

### #128 What if I need video from last month
- KB 對應有專文(待 deep read)
- 如果是 Video folder(連續錄)→ 大概率被覆蓋
- 如果是 Event(已上傳 cloud)→ 180 days 內可拿

### sheet #199 BLE Beacons / Storage Calculator
- KB 提供 Jotform 計算機:https://form.jotform.com/243577498838479
- 客戶可估 SD 容量 vs 錄影時數
