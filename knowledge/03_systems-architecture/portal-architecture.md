# Portal 雙層架構

> 完整客戶簡報:`../../websiteview/portal-briefing.html`

## 雙層架構

| 層 | URL | 視角 | 使用者 |
|---|-----|------|-------|
| **Master Portal** | `portal.visionmaxfleet.com` | 跨 fleet 設備池總管 | Dealer / 經銷商 / MAU |
| **Fleet Portal** | `www.visionmaxfleet.com` | 單一 fleet 內運營 | Fleet Manager / 客戶 / 內部 PM |

→ 設備 flow:Master Portal 把 CDR **分配 / 開通**給 Fleet → Fleet Portal 運營

## Fleet Portal 19 頁(Kenny 名下測試帳號可登入)

```
2026Q1_user_try (fleet 選擇器)            ← PDF 漏
─────────────
Fleet Operation                            ← PDF 漏(整段)
├─ Map Overview                            ← PDF 漏
├─ Dashboard                               ✅
├─ Trips: List / Detail / Report
├─ Safety: Events / Detail / File Retrieval / Safety Reports / Coaching   ← Coaching PDF 漏
├─ Management: Devices / Drivers / Vehicles / Geofences   ← Drivers/Vehicles PDF 漏
└─ Configurations(5 tabs:Device Settings / Sensor / AI / Road Safety / Safety Score)

Administration                             ← PDF 漏(整段)
├─ Accounts & Permissions
├─ Fleets(2 tabs:Fleets / Contract Fleets)
├─ Device Usage
└─ User Activity Logs
```

## Master Portal 7 頁

```
Master Portal
├─ Dashboard(4 panel:Total Devices / Healthy-Unhealthy / Activated / Total Fleets)
├─ Analysis(Plan Types 折線圖,2 tabs:Assigned Device / Fleets)
├─ Management
│  ├─ Inventory(IMEI / Recalls / 待分配設備)
│  ├─ Diagnostics                          ← PDF 漏
│  ├─ Fleets                               ← PDF 漏(跨 fleet 列表 + New Fleet)
│  └─ User Account                         ← PDF 漏(Admin / Viewer roles)
└─ User Activity Logs                      ← PDF 漏
```

## 3-Tier User Model

| L | 在哪管 | 對象 | 權限範圍 |
|---|--------|------|---------|
| L1 | Master > User Account(14 人) | 經銷商員工 | 跨 fleet |
| L2 | Fleet > A&P(8 人) | 單 fleet portal 用戶 | 單一 fleet |
| L3 | Fleet > Drivers(1 人 = Kenny) | 駕駛員(被 RFID 識別) | 不上 portal |

⚠️ **新 Viewer Only 角色**(VMX-7088,2026-05-06 會議討論):不能 Delete / Edit / Download / Retrieve / Configuration — **「detail 能不能看」待釐清**。

## Fleet Portal 三大 Entity

```
Device(車機)── K-series 硬體 / App Version / ADAS+DMS Health
   │
   ├─ via Vehicle Profile binding
   ▼
Vehicle(車輛)── VIN / Year/Make/Model / Vehicle Type
   │
Driver(駕駛)── Employee ID / IC Card S/N / Email
```

## Contract Fleet 真相(PDF 沒寫)

PDF 只承認 2 種商業身分:`Dealer` + `Customer`。

但 **Fleet Portal Admin > Fleets 上有 `Contract Fleets` tab**,且按鈕是 `+ New Account`(不是 + New Contract Fleet)→ 三種解釋:
1. UI 超前 PDF
2. UI 殘留
3. **最可能**:Account-based 模擬(account 跨 fleet 共用,不是真 sub-fleet)

→ ⚠️ **PM 風險**:Sales 用這個灰色地帶銷售,可能簽約後 RD 交不出。

## PDF 漏掉率

- Fleet Portal nav:50% 漏(19 頁中 PDF 列 9)
- Master Portal nav:57% 漏(7 頁中 PDF 列 3)
- 頁面深度(按鍵 / 欄位):>80% 漏
- 整體系統理解:**~70% 沒覆蓋**

→ 「PDF 補強 Wiki ticket」的論據(待跟 Brian 推)。
