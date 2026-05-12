# Sheet × Jira Sync Sweeper SOP

> Kenny PM 角色升級:每兩週做 Sheet × Jira 雙向 sync。
> 起源:2026-05-05 抓出 Sheet stale → 2026-05-06 會議直接落地 4 件同步 → 但又生出 3 個新 mismatch。

## 為什麼要做這件事

業務端的不滿通常是資訊不對稱:
- **方向 1:Sheet 落後 Jira**(Jira 已 close,Sheet 沒改)→ 業務以為「PM/RD 拖延」
- **方向 2:Sheet 領先 Jira**(口頭說完成,Jira 沒 close)→ 看 Jira 以為「沒做完」

PM 是商業翻譯,要消除這層不對稱。

## 雙週 Sweeper SOP(每兩週執行一次)

### Step 1:撈 Sheet 真實 visible rows
- 開 https://docs.google.com/spreadsheets/d/1DXCf8vU7ZrtzVdMEPSxHgmDb7cPKJFDK/edit
- **用截圖,不要用 CSV export**(CSV 會把 hidden row 一起拉)
- 看右下角「已顯示 X 列(共 Y 列)」確認 visible 數
- Status 欄 filter 顯示 In Process / Discussion / Pending / Feasibility

### Step 2:抓出每筆 visible row 的 Jira link

### Step 3:批量驗證 Jira 真實狀態
- 用 Chrome MCP 或手動點開
- 重點看:**Status**(Open / In Progress / Resolved / Closed)+ **Resolution**(Unresolved / Fixed)

### Step 4:整理兩個方向的 mismatch

| Sheet | Jira | 方向 | 動作 |
|-------|------|-----|------|
| In Process | Resolved | Sheet 落後 | 私訊 owner 確認後改 sheet status |
| Resolved | Open | Sheet 領先 | 私訊 owner 提醒 transition Jira |
| Discussion | In Progress | Sheet 慢一拍 | 同步 sheet |

### Step 5:私訊 owner(分人,別丟群組)

Template:
> 「Hi [Owner],我在做雙週 sheet sync 發現 [#XXX, VMX-XXXX]:
> - Sheet 顯示:[status]
> - Jira 顯示:[status]
>
> 是不是 [推測:已交付但 ticket 沒 transition / 還在做但 sheet 改太快]?要不要一起對齊一下?」

### Step 6:更新 sheet + 在 sheet 加 sweep 紀錄
在 Discussion Note 欄加註:`5/X PM sync - Jira status: [X]`

## 已知歷史 mismatch 紀錄

### 2026-05-05 抓出(會議前)— Sheet 落後
| # | Jira | Sheet | Jira | 結果 |
|---|------|-------|------|------|
| 162 | [VMX-6754](https://jira.navman.co.nz/jira/browse/VMX-6754) | In Process | Resolved | 5/6 同步 ✅ |
| 165 | [VMX-7029](https://jira.navman.co.nz/jira/browse/VMX-7029) | In Process | Resolved | 5/6 同步 ✅ |
| 187 | [VMX-7161](https://jira.navman.co.nz/jira/browse/VMX-7161) | In Process | Resolved | 5/6 同步 ✅ |
| 188 | [VMX-7162](https://jira.navman.co.nz/jira/browse/VMX-7162) | In Process | Resolved | 5/6 同步 ✅ |

### 2026-05-06 抓出(會議後)— Sheet 領先
| # | Jira | Sheet | Jira | 結果 |
|---|------|-------|------|------|
| 180 | [VMX-7082](https://jira.navman.co.nz/jira/browse/VMX-7082) | Resolved | New | ⏳ 待私訊 Lucy |
| 195 | [VMX-7233](https://jira.navman.co.nz/jira/browse/VMX-7233) | Resolved | New | ⏳ 待私訊 Internal |
| 199 | [VMX-6782](https://jira.navman.co.nz/jira/browse/VMX-6782) | Resolved | Open | ⏳ 待私訊 joe.lien |

### 2026-05-06 Sheet link 錯誤
| # | Sheet 寫 | 真實應該是 |
|---|---------|----------|
| 194 IOSix dongle | [VMX-7316](https://jira.navman.co.nz/jira/browse/VMX-7316)(實為 AZUGA SmartLink) | (待釐清) |
| 197 UVC integration | [VMX-7224](https://jira.navman.co.nz/jira/browse/VMX-7224) + [VMX-7147](https://jira.navman.co.nz/jira/browse/VMX-7147)(實為 Camera recording bug) | 移除 [VMX-7147](https://jira.navman.co.nz/jira/browse/VMX-7147) |
| 209 Viewer only | [VMX-7407](https://jira.navman.co.nz/jira/browse/VMX-7407)(重複) | 應為 [VMX-7088](https://jira.navman.co.nz/jira/browse/VMX-7088) |

## 工具命令

### 用 Python + Chrome MCP 批量驗證(已驗證可用)

```python
# 從 sheet visible rows 抓出 jira list,批量檢查
tickets = ['[VMX-6754](https://jira.navman.co.nz/jira/browse/VMX-6754)', '[VMX-7029](https://jira.navman.co.nz/jira/browse/VMX-7029)', ...]
for t in tickets:
    # navigate to https://jira.navman.co.nz/jira/browse/{t}
    # find Status field
    # log result
```

→ 可批量自動化,我用過 22 票一次過。

## 何時做 Off-cycle sweep

- 大會議前 1 天(會議當天才動會被打臉)
- 客戶 demo 前
- 跟 Brian 1on1 前
