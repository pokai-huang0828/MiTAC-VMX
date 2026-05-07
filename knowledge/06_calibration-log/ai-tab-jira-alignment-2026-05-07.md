# AI 工作計畫 Tab × Jira Filter 36457 對齊分析

> 日期:2026-05-07
> 來源:Sheet AI 工作計畫 tab(16 visible rows)× Jira Filter 36457 "VMX opened"(257 件) + JQL 補抓 21 件 AI 相關 VMX open 票
> 工具:Chrome MCP 直連 Jira List View + Sheet 截圖驗證

## TL;DR — 4 個重大發現

1. 🚨 **Row 9 #7 Blurring Footage 三票全已關**(HAWK-331/VMX-6391/HAWK-527 全 CLOSED/RESOLVED),sheet 還掛 P1 Improving Process Speed → **應從 visible row 移除**
2. 🚨 **Row 53 #50 VisionMax PROD not blurring 兩票全已關**(HAWK-517 CLOSED 02/06、HAWK-578 RESOLVED 05/04)— sheet 為什麼新增這列待釐清
3. 🚨 **VMX-6722 Sheet 寫 Feasibility,Jira 還 NEW** — 跟 5/6 Brian 自評「label 漏 pick」直接呼應,本身沒進 In Progress
4. ⚠️ **5/6 Q2 review 後新開 4 張票 Sheet 全部沒收錄**:VMX-7432(Yawning UI toggle)/ VMX-7431(LED sign)/ VMX-7430(exit ramp)/ HAWK-582 已收

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

## C. Mismatch 三方向

### C1. 🚨 Sheet 還掛 active,Jira 已關(P0 - 應從 visible row 移除)

| Sheet Row | # | Task | 已關 ticket | 結論 |
|-----------|---|------|-----------|------|
| **9** | **7** | **Blurring Footage** | HAWK-331 CLOSED(2/5)/ VMX-6391 RESOLVED(12/10)/ HAWK-527 RESOLVED(4/1) | **3 票全關 → row 應 hide 或標 Done** |
| **53** | **50** | **VisionMax PROD not blurring** | HAWK-517 CLOSED(2/6)/ HAWK-578 RESOLVED(5/4) | **2 票全關 → 為何新增?待釐清 Adonis** |

### C2. ⚠️ Sheet 領先 Jira(口頭完成 / Jira 沒 close)

| Sheet | Jira | Sheet 5/7 update | Jira 狀態 | 動作 |
|-------|------|-----------------|----------|------|
| #48 Request event blurry | HAWK-573 | "Completed Awaiting Release" | NEW(Fix VisionMax_20260602) | 等 release 才 transition,正常 |
| #49 Blurring on-demand | HAWK-577 | "已於 v1.1.28 部屬至 Webfleet 正式環境" | OPEN(updated 5/7) | 私訊 chiehli.wang transition Jira |

### C3. ⚠️ Sheet 寫 Feasibility / Improving,Jira 還 NEW

| Sheet | Jira | Sheet Status | Jira Status | 解讀 |
|-------|------|--------------|-------------|------|
| #8 LDWS Server AI | VMX-6722 | Feasibility | NEW | **跟 5/6 Brian「label 漏 pick」案直接呼應 — Q1 已 merge 但 Jira 還 NEW** |
| #8 LDWS | VMX-7101 | Feasibility | NEW(Updated 3/24,8 週沒動) | 真的 stale |
| #7 Blurring Footage | (3 票皆關) | P1 Improving | RESOLVED/CLOSED | Sheet status 完全沒對齊 |

### C4. ⚠️ Sheet Jira 對應錯誤

| 觀察 | 細節 |
|------|------|
| **VMX-7309 是 Eyes 不是 Yawning** | Jira 標題:"Provide the configuration of the EyeStableRate threshold" — sheet #3 Yawning + #4 Eyes 都掛同一票,Yawning 應該另有對應(會議錄音提 HAWK-332)|
| HAWK-527 5/6 已 RESOLVED | sheet #7 還列在 Jira link 但備註寫「(HAWK-527)」加括號 — 已標但 row 整體狀態未改 |

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

## E. Action Items(優先序)

### 🔥 24 小時內(P0)
- [ ] **Row 9 #7 Blurring Footage** 跟 Vincent 確認:3 票全關後這列要 hide 還是改 #50 那個 PROD bug
- [ ] **Row 53 #50** 跟 Adonis 確認:HAWK-517/578 全關了為什麼還新加這列?是「PROD 又出新 bug 但還沒開 ticket」?
- [ ] **VMX-6722 ↔ Sheet #8 LDWS Feasibility** 跟 jimmy.jy.huang DM:Q1 已 merge,Jira 為什麼還 NEW?直接命中 Brian 5/6 講的 label 紀律 gap
- [ ] **Yawning 對應修正**:#3 Yawning 改對應 HAWK-332,VMX-7309 留給 #4 Eyes(會議錄音提的)

### 📅 本週內(P1)
- [ ] **VMX-7432 Yawning UI toggle 加進 sheet**(Lucy 5/6 開的票,目前 Lucy 的工作 sheet 完全沒記)
- [ ] **VMX-7430/7431 Speed sign 兩件 woody.lee** 加進 sheet(或確認該歸到「歐盟認證 image」/Speed sign 大主題)
- [ ] HAWK-577 Blurring on-demand 私訊 chiehli.wang transition Jira(sheet 寫已部屬 v1.1.28)
- [ ] VMX-7194 Vehicle rollover detection 加進 sheet(5/6 已 In Process,sheet 沒列)
- [ ] VMX-7324 Improve smoking event accuracy(Elvis 開的)— 歸 Smoking 大主題

### 🎯 本月內(P2)— Sheet 結構性修正
- [ ] **Sheet 結構問題:同一張 ticket 對應兩個 task row**(VMX-7309 = Yawning + Eyes 都掛)— 跟 Brian 提
- [ ] **Smoking 主題大缺口**:Roadmap 列 Basic tier,Jira 有 VMX-7324 OPEN / VMX-6380 NEW,但 sheet 全部 hide
- [ ] **18 件 AI 老票 stale 清查**:跟 Brian 確認 vmx_2026Q1 label 的票哪些還在做,哪些可以 close

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
