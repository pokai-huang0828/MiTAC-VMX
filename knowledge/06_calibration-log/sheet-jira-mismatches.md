# Sheet ↔ Jira Mismatch 紀錄

> 雙向同步缺口。Sheet 跟 Jira 不一致是常態,需 PM 每兩週 sweep。

## 兩個方向

### 方向 1:Sheet 落後 Jira(Jira 已關 / Sheet 沒改)
業務端看 Sheet 以為「PM/RD 拖延」,實際 RD 已交付。

### 方向 2:Sheet 領先 Jira(口頭說完成 / Jira 沒 close)
看 Jira 以為「沒做完」,實際產品端認為已交付。

## 歷史紀錄

### 2026-05-05 sweep(會議前抓)— Sheet 落後 4 件

| Sheet # | Jira | Sheet 寫 | Jira 真實 | 結果 |
|---------|------|---------|----------|------|
| 162 | VMX-6754 | In Process(7 個月)| Resolved | 5/6 會議同步 ✅ |
| 165 | VMX-7029 | In Process(5 個月)| Resolved | 5/6 會議同步 ✅ |
| 187 | VMX-7161 | In Process | Resolved | 5/6 會議同步 ✅ |
| 188 | VMX-7162 | In Process | Resolved | 5/6 會議同步 ✅ |

### 2026-05-06 sweep(會議後新增)— Sheet 領先 3 件

| Sheet # | Jira | Sheet 寫 | Jira 真實 | 結果 |
|---------|------|---------|----------|------|
| 180 | VMX-7082(Lucy GA tracking)| Resolved | **New** | ⏳ 待私訊 Lucy |
| 195 | VMX-7233(VisionAgent GA Code)| Resolved | **New** | ⏳ 待私訊 Internal |
| 199 | VMX-6782(BLE Beacons)| Resolved | **Open** | ⏳ 待私訊 joe.lien |

→ 5/6 動作 owner 在 sheet 加註「5/6 已完成 提供給客戶測試」但沒 close Jira。

### Sheet link 錯誤(2026-05-06)

| Sheet # | Sheet 寫 link | Jira 實際是 | 應該是 |
|---------|------------|-----------|--------|
| 194 | VMX-7316 | [AZUGA SmartLink] 新增事件支援 | 該找 IOSix 對應 ticket |
| 197 | VMX-7147(第二個 link)| Camera recording no longer exists | 移除 VMX-7147,只留 VMX-7224 |
| 209 | VMX-7407(重複)| UVC RAW frame error handling | 應為 **VMX-7088 Viewer only** |

## 規律 / 啟示

1. **Resolved → 沒人回頭關** 是常態。Sheet 上看到 In Process 不一定真的 active
2. **「我做完了」≠ Jira closed**。產品端認為交付給客戶測試 = sheet 動;但 Jira ticket 要等 QA / verification 才 close
3. **Sheet link 寫錯**多發生在新增 row 時複製貼上沒改 link
4. **Sheet 隱藏 row** 跟 mismatch 不同 — hidden = 不在使用,mismatch = 還在用但狀態不對齊

## 防呆建議(對 Brian / Sheet owner)

- 每兩週 sweep(PM 來扛)
- 新增 row 時驗證 link
- Resolved 後在 sheet 加 verification 階段(client testing / staging / production)
- Sheet 加「Last verified」欄
