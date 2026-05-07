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

### 2026-05-07 AI 工作計畫 tab 深掘(讀 10 張票 comments)

**只看 Jira status 欄會誤判**。深讀 comment 後新增 7 種 mismatch 模式,推翻一些表面判斷。

| 模式 | 案例 | 教訓 |
|------|------|------|
| 1. 接力新單後沒 hide 舊 row | HAWK-331 → HAWK-527 | sheet link 加括號標新單,但 row status 沒同步 |
| 2. 議題 ≠ ticket | HAWK-578 + SQS retention follow-up | sheet 在追議題級工作,Jira 票只是事件單據 |
| 3. Resolved 後又出新問題,加 Fix Version 不 reopen | HAWK-527 加 20260602 | Jira RESOLVED 反而誤導,sheet active 是對的 |
| 4. 修完等 release,Jira transition 沒走 | HAWK-573 | sheet 寫「Awaiting Release」是正確訊號 |
| 5. Sheet update 寫錯 row | (誤判) | HAWK-577/578 對應實際正確,我曾誤判 |
| 6. Comment 留「已完成」但 transition 沒走 | VMX-6722 / VMX-7101 | jimmy 寫 deploy prod 但沒按 Open→Resolved button |
| 7. 單一 ticket 對應多 sheet rows,scope mismatch | VMX-7309 ↔ Sheet #3 Yawning + #4 Eyes | VMX-7309 只是 Eye threshold API,沒 Yawning 內容 |

**重要校正**:Brian 5/6 自評「label 漏 pick」narrative 不準確 — VMX-6722 本身有 label `vmx_2026Q2`,真實 process gap 是 **transition discipline**(RD 寫完 comment 沒按 button)。

## 規律 / 啟示

1. **Resolved → 沒人回頭關** 是常態。Sheet 上看到 In Process 不一定真的 active
2. **「我做完了」≠ Jira closed**。產品端認為交付給客戶測試 = sheet 動;但 Jira ticket 要等 QA / verification 才 close
3. **Sheet link 寫錯**多發生在新增 row 時複製貼上沒改 link
4. **Sheet 隱藏 row** 跟 mismatch 不同 — hidden = 不在使用,mismatch = 還在用但狀態不對齊
5. **🆕 Sheet active 不一定錯**:Jira RESOLVED 可能誤導,要看 comment 才知道有沒有第二輪 fix 或議題級 follow-up
6. **🆕 議題 vs ticket 心智模型**:sheet row = 議題;Jira ticket = 事件單據。一議題可能 N 張票或 0 張票
7. **🆕 Transition discipline gap > Label discipline gap**:RD 不按 button 比沒下 label 更常見

## 防呆建議(對 Brian / Sheet owner)

- 每兩週 sweep(PM 來扛)
- 新增 row 時驗證 link
- Resolved 後在 sheet 加 verification 階段(client testing / staging / production)
- Sheet 加「Last verified」欄
- **🆕 不要光看 Jira status 推 sheet 改動,要進去看 comment 跟 linked issues 再決定**
- **🆕 對 Brian 提改善:從「transition 紀律」切入,不是「label 紀律」**
