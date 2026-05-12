# VisionMax Diagnostics

> 來源:KB「VisionMax Diagnostics Information」(2026-05-06 deep read)
> 對應:Master Portal > Diagnostics 頁面 / 客戶報修 / [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure 議題

## 監控範圍

VMX 系統持續監控:
- GPS tracking
- Sensor detection
- Camera operation
- AI features
- Data storage

## Diagnostic Q&A(KB 已抓)

### Q1: "Location Function" issues
- **意思**:device GPS 位置最近 10 分鐘沒被偵測到
- **影響**:不能建 trip / 不能偵測 ADAS / DMS / 不能記錄 video 位置
- **Solution**:確保車輛在開放環境,GPS 能收訊號

### Q2: "Sensor Events Detection" 失敗
- **意思**:device 不能偵測 harsh acc / harsh dec / harsh cornering
- **Solution**:檢查 device 是否裝好

⚠️ 完整 Q&A list KB 文章還有更多內容(Q3+),沒抓完。

## 對 PM 議題的對應

### [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure
- KB 確認:**Location Function 問題會導致 ADAS / DMS 都不能偵測**
- 對應你 K245(L3024290010)的 ADAS Failure → 可能是 GPS + 30 km/h × 3min 雙重原因
- ⚠️ 必確認:Trip 7028714 是 GPS 失效?還是純粹速度條件不滿足?

### Master Portal Diagnostics 頁面
- 對應 portal-architecture.md 中 Master > Diagnostics
- 顯示「Has Issue」/ Issue Type(MiAI Issue, GPS Issue 等)
- Kenny portal 走訪時看到 5 台 Has Issue / 1 台 MiAI Issue

## 客戶用法

- 客戶 fleet manager → Master Portal Diagnostics 看自己 fleet 設備健康
- Has Issue 設備 → 點進去看 Issue Type → 對照 KB Q&A 自助 troubleshoot
