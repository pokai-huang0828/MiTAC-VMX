# AI 工作計畫 Tab × Jira Filter 36457 對齊分析

> 日期:2026-05-07
> 來源:Sheet AI 工作計畫 tab(16 visible rows)× Jira Filter 36457 "VMX opened"(257 件) + JQL 補抓 21 件 AI 相關 VMX open 票
> 工具:Chrome MCP 直連 Jira List View + Sheet 截圖驗證

## TL;DR

**深讀 10 張票 comments 後的真實結論在 H 段**(Comment 深掘後校正)。本文件結構:A/B = reference data(sheet × Jira status 對照表)、D = sheet 沒列的 active AI 票、H = 真實判斷。中間 C/E 段是原始表面分析,已被 H 段推翻,留作 calibration history。

**3 個關鍵 takeaway**(看 H 段):
1. Sheet active 不一定錯 — Jira RESOLVED 可能誤導(HAWK-527 加 VisionMax_20260602 第二輪 fix 證明)
2. VMX-6722 不是 label gap,是 transition discipline gap(jimmy 寫 deploy prod 沒按 button)
3. VMX-7309 sheet #3 Yawning + #4 Eyes 共用對應錯位 — 7309 只是 Eye threshold,Yawning 真實對應 VMX-7432

## A. AI 工作計畫 5/7 visible rows(16 行,vs 5/5 多 1 行)

| Row | # | Task | Sheet Status | PIC | Jira |
|-----|---|------|------|-----|------|
| 4 | 3 | Yawning Detection | Improving | Jieli | VMX-7309 |
| 6 | 4 | Eyes Detection | Improving | Jieli | VMX-7309 |
| 9 | 7 | Blurring Footage | P1 Improving Process Speed | Vincent | HAWK-331 / VMX-6391 / HAWK-527 |
| 10 | 8 | LDWS Server AI Model | Feasibility | Eric | VMX-6722 / VMX-7101 |
| 30 | 27 | VLM | (pending pending pending) | — | (none, 2026 Q3) |
| 31 | 28 | 鏡頭遮擋 (Quantatec & BMS) | — | Jieli | VMX-6983 / **HAWK-582 (5/6 新加)** |
| 35 | 32 | Face Not Found Issue | — | Jimmy | (none) |
| 44 | 41 | Add box around event | — | Jay, Adonis | VMX-5909 |
| 45 | 42 | Server AI 統計資料釐清 | — | Vincent, Jimmy | (none) |
| 46 | 43 | Camera height 不穩定 | — | Jay, Vincent | HAWK-501 |
| 48 | 45 | Pedestrian Detect | — | Vincent | HAWK-570 |
| 49 | 46 | Eating & Drinking | — | Jimmy | HAWK-562 |
| 50 | 47 | Rastrac False Speed | — | Jonathan | VMX-7317 |
| 51 | 48 | Request event blurry not updating | — | Adonis | HAWK-573 |
| 52 | 49 | Blurring on-demand fails | — | Adonis | HAWK-577 |
| **53** | **50** | **VisionMax PROD deployment is not blurring videos**(5/5 後新增) | — | Adonis | **HAWK-517 / HAWK-578** |

## B. Jira 17 票實際狀態(JQL List View)

| Jira | Summary | Assignee | Status | Resolved | Fix Version |
|------|---------|----------|--------|----------|-------------|
| VMX-7317 | Rastrac – False Speed Event Review | vincent.ho | **NEW** | - | - |
| VMX-7309 | Provide config of EyeStableRate threshold | joe.lien | **OPEN** | - | CameraAPP_202605 |
| VMX-7101 | LDWS Improving (Server) | jimmy.jy.huang | **NEW** | - | - |
| VMX-6983 | Quantatec - 新增鏡頭遮擋及移除遮擋事件 | james.cw.chou | **OPEN** | - | - |
| VMX-6722 | Server AI server-side lane departure | jimmy.jy.huang | **NEW** | - | (label vmx_2026Q2) |
| VMX-6391 | AI New Feature: Blurring | josh.ch.tseng (Inactive) | **RESOLVED** | 10/Dec/25 | 2025Q4 |
| VMX-5909 | Add box around event #11 | eric.h | **NEW** | - | - |
| HAWK-582 | Improve Lens cover detection | eric.h | **NEW** | - | (label AI) |
| HAWK-578 | VisionMax PROD not blurring | Luís Miguel Couto | **RESOLVED** | 04/May/26 | - |
| HAWK-577 | Blurring on-demand fails | chiehli.wang | **OPEN** | - | - |
| HAWK-573 | Request event blurry not updating | chiehli.wang | **NEW** | - | VisionMax_20260602 |
| HAWK-570 | PCWS Spec Confirmation | eric.h | **NEW** | - | (label AI) |
| HAWK-562 | Eating & Drinking detection | brian.chienlee | **NEW** | - | (label AI) |
| HAWK-527 | Blurring not reliable | vincent.ho | **RESOLVED** | 01/Apr/26 | VisionMax_20260331 + 20260602 |
| HAWK-517 | Blurring not working on STAGING | Luís Miguel Couto | **CLOSED** | 06/Feb/26 | - |
| HAWK-501 | ADAS Self-calibration wrong height | eric.h | **NEW** | - | (label AI) |
| HAWK-331 | Blurring (face/background/license plate) | Luís Miguel Couto | **CLOSED** | 05/Feb/26 | VisionMax_20260203 |

## C. Mismatch 三方向(原始表面分析,看 H 段才是真相)

> ⚠️ **此段保留作 calibration history**。光看 Jira status mismatch 推「sheet 該 hide」的判斷被 H 段推翻 — 真實要進票看 comment。

C1 原寫的「Row 9 #7 / Row 53 #50 應從 visible row 移除」→ **錯誤**,看 H1/H2。
C2 HAWK-573 等 release / HAWK-577 對應正確 → **看 H 段確認**。
C3 VMX-6722「label 漏 pick」narrative → **錯**,看 H 段(transition discipline)。
C4 VMX-7309 對應錯位 → **正確**,看 H 段確認。

## D. Sheet 沒列但 Jira 有 active AI 票(JQL: project=VMX AND status≠Done AND summary AI 關鍵字)

> 21 件 AI 相關 VMX open 票中,**18 件 Sheet 沒列**(扣除 sheet 已有的 VMX-6722 / VMX-7101 / VMX-5909)

### 高優先 — 5/6 Q2 Review 之後新開,Sheet 完全沒收

| Jira | Summary | Assignee | Created | 為何重要 |
|------|---------|----------|---------|---------|
| **VMX-7432** ⭐ | Add 'Detect Yawning' toggle under Fatigue Configuration | **lucy.sw.yen** | 5/6 | **就是 Q2 會議要 Lucy 做的 Yawning UI** |
| **VMX-7431** ⭐ | Speed sign recognition triggering incorrect speed from LED sign | woody.lee | 5/6 | LED sign 誤判 |
| **VMX-7430** ⭐ | Improve speed sign recognition to not detect exit ramp speed | woody.lee | 5/6 | exit ramp 誤判 |

### 中優先 — 4 月新開的 AI 票

| Jira | Summary | Assignee | Status | Updated |
|------|---------|----------|--------|---------|
| VMX-7335 | [AZUGA SmartLink] ACCIDENT_DETECTION 撞擊事件 | allen.yc.chung | NEW | 5/4 |
| VMX-7194 | Vehicle rollover event detection | mori.jhang | NEW | 4/30(5/6 會議推進) |
| VMX-7324 | Improve smoking event accuracy | Elvis.Tran(NAVMAN-AU) | **OPEN** | 4/14 |
| VMX-7320 | Speed sign violation at/below sign limit | vincent.ho | NEW | 4/14 |
| VMX-7321 | School zone speed sign violation outside school times | brian.chienlee | NEW | 4/14 |
| VMX-7239 | Add handboject classification model for phone use | vincent.ho | **OPEN** | 3/24 |

### 老票 stale — 應檢查是否還活著

| Jira | Summary | Assignee | Status | Updated |
|------|---------|----------|--------|---------|
| VMX-6378 | Speed sign violation | spencer.su | **IN PROGRESS** | 3/19(label vmx_2026Q1) |
| VMX-6380 | Distracted Driving - Smoking | jimmy.jy.huang | NEW | 12/10/25 |
| VMX-6761 | Stop sign detection with traffic lights | jieli.liu | OPEN | 11/13/25 |
| VMX-6221 | Survey AI Model Self-Training | jay.qiu | NEW | 9/15/25 |
| VMX-6453 | Server Model Research - Phone Use | jieli.liu | OPEN | 9/12/25 |
| VMX-6703 | Support Configurable Server AI Response Time | eric.h | NEW | 9/5/25 |
| VMX-6382 | Allow AI detection parameters configurable | vincent.ho | NEW | 7/18/25 |
| VMX-5915 | TT AU Speed cam Stop signs at traffic lights | eric.h | NEW | 5/4 |

## E. Action Items(已被 H + 5/7 AI weekly 取代)

> ⚠️ 原 E 段 P0 三項判斷錯誤(看 H 段)。**Action items 看 [`ai-team-row-by-row-status-2026-05-07.md`](ai-team-row-by-row-status-2026-05-07.md) Brian 1on1 talking points + [`../../meetings/2026-05-07_AI-Weekly_meeting-record.md`](../../meetings/2026-05-07_AI-Weekly_meeting-record.md) Action Items**。

仍有效的:
- VMX-7432 / 7430 / 7431(5/6 新開)+ VMX-7194 Rollover + VMX-7324 Smoking — sheet 沒收 — 跟 Brian 提加進 sheet
- VMX-7309 對應錯位 Sheet #3 Yawning + #4 Eyes 共用 → Yawning 真實對應 VMX-7432
- 18 件 AI 老票 stale 清查(D 段列表)

## F. Sheet status 欄(E 欄 Priority/Status)— 觀察

只有前 4 row 看到清楚的 Priority/Status 顏色標記:
- 藍色 Improving = 改善中
- 紅色 P1 Improving Process Speed = 高優先效能改善
- 綠色 Feasibility = 可行性評估

**中後段(rows 30+)Priority/Status 欄全空白** — 這些 task 的緊急度 sheet 沒標,只能從 5/4 / 5/7 update 欄字推估狀態。

→ **Sheet 結構建議**:Priority/Status 欄該全列補完,否則新人(包含 Kenny)看不出輕重。

## G. 跟 Filter 36457 "VMX opened" 的關係

Filter 36457 是「VMX 全部 open 票 257 件」的大池,**不是 AI-only**。對齊 AI 工作計畫 tab 不能直接用整個 filter 去比,要再篩 AI-related 才有意義。

實際 query 路徑:
```
project = VMX
AND statusCategory != Done
AND (summary ~ "AI" OR summary ~ "detection" OR summary ~ "model"
     OR summary ~ "Yawning" OR summary ~ "Smoking" OR summary ~ "LDWS"
     OR summary ~ "Pedestrian" OR summary ~ "Blurring"
     OR summary ~ "Rolling Stop" OR summary ~ "Speed Sign" OR summary ~ "Eating")
ORDER BY updated DESC
```
→ 21 件,可定期跑這個 query 比對 sheet。

---

## H. Comment 深掘後校正(2026-05-07 補)

只看 Jira status 欄會誤判。10 張票各自進去讀 comment + linked issues + resolution 後的真實 closure 故事:

### Tier A 5 張(Sheet active 但 Jira 已關)

| 票 | 真實 closure 故事 | Sheet 為何還在? |
|---|------|-----|
| **HAWK-331** | 2/5 spencer.su 關掉,留「另開單追 follow-up」 | Luís 2/11 直接接力新單 **HAWK-527**;sheet 上 link 已加括號標 (HAWK-527),但 row status 沒同步改 |
| **VMX-6391** | 12/10/25 由 **righter.song**(MIC)關掉 — 不是原 assignee josh(已 Inactive 離職);最後一則 comment 是 10/13/25 | VMX-6391 是「VMX 端 Blurring 初版開發」歷史單,sheet 沿用 link 是「歷史共識」不是 active |
| **HAWK-527** | eric.h 4/1 關掉(VisionMax_20260331 ship)。但 4/22 客戶 Susana V18 測試又找新問題,vincent.ho 5/6 加 **VisionMax_20260602** 第二輪 fix | **sheet active 是對的** — Jira RESOLVED 反而誤導,實際 6/2 還有第二輪 |
| **HAWK-517** | 純 ops incident — STAGING 上 ECS scaling 導致 service down,chiehli.wang 2/6 手動 restart 解決 | 演化成 HAWK-578 + 自我健康檢查機制(sheet #50) |
| **HAWK-578** | chiehli.wang 5/4 同天修 PROD 並部屬「自我健康檢查 + ECS 自動恢復」機制 | sheet 真正在追的是 follow-up 3 件:SQS retention 4→14 天(5/6 ping spencer.su)/ 客戶手動補 4/21–5/4 漏掉的 blurring / PROD 穩定觀察 |

### Tier B 2 張(Sheet 領先 Jira)

| 票 | 真實狀態 | Sheet vs Jira |
|---|------|-----|
| **HAWK-573** | chiehli.wang 4/30 留:CDN cache 為根因,each rerun 產生 unique URL,**will ship in next release**。已有 2 commits + git branch | Sheet 寫「Completed Awaiting Release」**正確**,Jira NEW 是 transition 沒走的 process gap |
| **HAWK-577** | Type 是 **New Feature**(不是 Bug),NO Fix Version。chiehli.wang 5/4 留新 API 行為設計(`pending_resources` field 等),「to be included in next release」 | Sheet 5/7 寫「測試中,預計下週 MR 於 6/2 release」與 Jira 一致(我前面誤判 sheet 寫錯欄,**實際對應正確**) |

### Tier C+D 3 張(label gap / 對應錯位)

| 票 | 真實狀態 | 校正點 |
|---|------|-----|
| **VMX-6722** | sub-tasks 全 CLOSED/RESOLVED + jimmy 3/11 留「Server AI 已完成並 deploy 到 prod」+ Brian 5/6 講 Q1 已 merge,**parent ticket 仍 NEW** | **不是 label 漏 pick(label `vmx_2026Q2` 有設)**,是 **transition 動作沒走** — jimmy 寫 comment 但沒按 Open→Resolved button |
| **VMX-7101** | 跟 6722 sibling,只有 1 則 comment(3/24 chiehli),之後沒人動。可能跟 6722 一起 ship 但同樣 transition 沒走 | 跟 VMX-6722 同 process gap |
| **VMX-7309** | scope 只是「EyeStableRate threshold API」(eyeOpenRatioCheckThreshold,fatigue eye 用)。Parent 是 HAWK-551(Bridgestone 客戶)。CDR 端 4/22 已實作完,等 server 端 joe.lien 串接,5/26 CameraAPP_202605 release | **🚨 Sheet #3 Yawning + #4 Eyes 共用 VMX-7309 是錯對應**:VMX-7309 完全沒有 Yawning 內容。Yawning UI toggle 是 5/6 新開的 VMX-7432(Lucy assignee),不是 VMX-7309 |

### 「為什麼 sheet 還掛 active」7 種模式(從 10 張票歸納)

1. **接力新單後沒 hide 舊 row**(HAWK-331 → HAWK-527)
2. **議題 ≠ ticket**(HAWK-578 後續 SQS / 手動補,sheet 在追議題級工作)
3. **Resolved 後又出新問題,加新 Fix Version 但不 reopen**(HAWK-527 加 20260602)
4. **修完等 release,Jira transition 沒走**(HAWK-573)
5. **Sheet update 寫錯 row**(原誤判;HAWK-577 / HAWK-578 實際對應正確,我看錯)
6. **Comment 留「已完成」但 transition 沒走**(VMX-6722 / VMX-7101)
7. **Sheet 用單一 ticket 兜起來涵蓋多個議題,但 ticket scope 比 sheet 列的小很多**(VMX-7309 ↔ Sheet #3+#4)

### 對 Brian 5/6 講「label 漏 pick」narrative 的修正

Brian 自評「label 沒設好 / 我 filter 漏 pick」— 但 VMX-6722 **本身有 label `vmx_2026Q2`**。真實 process gap 是 **RD 寫 comment 後不按 transition button**,不是 label 紀律。

→ 跟 Brian 提改善要從「**transition discipline**」切入,不是「label 紀律」。
