# 2026-05-11 下午 14:00 · Cary / Elvis / Brian Teams sync · Blurring API 拍板

> **時間**:2026-05-11 14:00 起(~30 分鐘)
> **形式**:Teams call · 同 group meeting link
> **參與**:Kenny / Cary Lo (MAU) / Elvis Tran (MAU PM) / Brian Chienlee(中途加入 take over)
> **轉錄**:Teams 自動 transcript(中英混合)
> **性質**:5/8 sync up + 5/11 早上 thread 的延續 · API-level 路徑最終拍板 · Q2 scope 鎖定

---

## TL;DR

| 結論 | 內容 |
|------|------|
| ✅ **Q2 scope 鎖定** | (1) BMS Blurring 整合進 VisionMax cloud · (2) Release API doc 給 Connect Source |
| ✅ **Connect Source 走 API only** | 不需要 UI portal toggle · API 自己可控任何 video / fleet / contract fleet |
| 🕐 **Auto Sense UI 是另一個 story** | 用 web UI 的客戶要等 GUI design · **Q2 不做**(long term)|
| 🕐 **Monthly subscription report** | Brian「not the target for now, future planning」· **暫不開 ticket**(post-Q2 production deploy 後有真實 usage 再開新單)|
| 📅 **時程** | End of June staging · End of July production · End of June Q2 release notes 給 Cary |
| 🚨 **Elvis push 的訊號** | 「Don't want to be surprised again」· 未來 deployment 前要 notify · Q1 release note 還沒給客戶就要先安排 |
| ⚠️ **Kenny 自評** | Execution gap — 準備的 ammunition(HTML 圖 / sound-bites)沒在現場 deploy · Brian 進來 take over · 主導權失分 |

---

## A. 會議動線(逐段紀錄)

### A1. Kenny 開場 reframe(0:04 – 1:32)

Kenny:
> "last Friday I think there was something I think is misunderstand about like the request. So I was starting too fast to talk about the UI for the front end. But based on that, I've been checking back for our previous emails information that you've been mentioned about, like the API level, so let's get back to the API level to talk about the blurring function."

Cary:「Yep.」 → 接受 reframe。

⚠️ **Kenny 自評失分點**:
- "I think... I think... I think" 訊號 = 自己也不確定
- "starting too fast" 把責任全攬,觸發 DON'T SAY 警示
- 沒在這時 share screen 帶 Cary 看 inheritance 圖
- 之後 1:19 句「pass to develop teams... different ways to manage」語言碎裂,沒給 mental model

### A2. Cary 戳關鍵:Master Portal 沒有 function

Cary 第一個 push:
> "I thought we've given the information that they want all events to be applied to blur the passenger only for a particular fleet."

→ Cary 認為早上需求已經給清楚。

Kenny 試圖解釋 master 開總開關 + API 控:
> "we can switch on the master master proto and then the because the master proto will have the all the like the powers to enable the blurring systems."

Cary:
> "but right now the master portal doesn't have that function. So can it be enabled in the API?"

Kenny:「Yes. Now or API.」 → ⚠️ **訊號模糊,Cary 開始懷疑 Kenny 不熟悉 product。**

### A3. Elvis 自己講出 inheritance + override model(主導權第二次旁落)

Elvis:
> "contract fleets are treated as if their own fleet. So there may be instances where a customer or acquire different settings for contract fleets not necessarily have to follow the master fleet. So in saying that to give the more flexibility and customization then I would suggest that we go with option A but only admins or master account can change the configuration."

→ **這本來是 Kenny 該講的東西**(Kenny HTML 圖 Contract Fleet B override 那段邏輯)。Elvis 自己口頭重建後 conclude reframe 成 Option A。

Kenny 反應:
> "I mean like option A and B actually under the system how the flows the it is the same thing how it goes."

→ ✅ **這個洞察是對的**(Spencer 早上的 A/B 在 API 層是同一條 flow),但講出來:
- 太晚(在被糾正後才講)
- 太含糊(沒解釋為什麼「same thing」)
- 沒先指 inheritance 圖再講

### A4. Cary screen share 走 Fleet Portal(主導權第三次旁落)

Cary 直接 share screen,走「MAT New South Wales 主 fleet → Sydney contract fleet」流程,自己解釋 5/8 提的「需要 per-contract-fleet 粒度」。

Cary 重申 Option B 拍板理由:
> "this feature potentially will cost extra money. ... I don't want them to turn on and on blurring. It needs to be controlled on the master level."

Cary 再提 monthly report:
> "we can also track the blurring feature on the monthly report whether what fleet has it applied from when or like some sort of usage tracking"

Kenny 回應:
> "I think the monthly report it's not the target for now... but yeah, we can think about in the future."

⚠️ **Kenny 自評嚴重失分**:這是 Cary 早上提的核心商業需求,**直接 dismiss = 否定 her input**。違反 Kenny 自己 Cary 版 HTML 寫的 "Built-in Support for Monthly Subscription Reporting" 整個 section。

### A5. Brian 進場 take over

Brian 接手釐清:

#### Brian 拆分 case
> "The only difference is so connect source has their own master account and auto sense has their own master account. The different. So that means that currently the connect source is has already integrated with the our API. Correct?"

#### Brian 拍板 API 層不分 fleet / contract fleet
> "Because if they use the API they could use the API to blurring any video they want. ... So we don't need to consider is the customer is under the free or subly."

#### Brian 確認 Q2 scope
> "So first is I think we should integrate the BMS blurring feature into our vision max. And second we need to release our API document for connection source to implement their API and then we can start this integrate with the connectors."

#### Brian 把 Auto Sense 切出 Q2
> "the autosense is another another story and scope because the for autosense their customer are use currently the m vision max web UI. So we have to use implement the UI before they can have this feature."

⚠️ **Kenny 自評**:Brian 5 分鐘把所有事情講完。對 Cary / Elvis 來說「Brian 一講就清楚 → Kenny 講半天還是糊的」,直接傷 Kenny「主對接 PM」定位。

### A6. 時程確認

| 階段 | 時程 |
|------|------|
| Staging deploy | End of June 2026 |
| Production deploy(post-DQE) | End of July 2026 |
| Q2 release notes 給 Cary | End of June 2026(對外發給客戶之前)|
| API doc share | 本週(等 Brian QPR 後 sign-off)|

### A7. Elvis 的 push back(關鍵保護動作)

Elvis:
> "Do you have any other major changes planned for Q2 as well? Because we don't want to be surprised again and have customers text us up for changes we weren't aware of."

Kenny 接住:「we will notify before our deployment next time.」

Cary 補:
> "We need the release note first... before you can push it out, that will be ideal."

Kenny commit:「we can summary the Q2 feature change to you by the end of June」

✅ **Kenny 自評做得好的部分**:結尾這段把信任挽回,給具體時間。Cary 跟 Elvis 同意。

### A8. 結尾互動

- Kenny 主動 offer 後續答疑:「if you have a questions then you can ask me」
- Cary:「that's great, thank you」
- Elvis:「Clear as mud」(意思 = clearly understood)
- 互道感謝結束

---

## B. 拍板的事實(SSOT 該去哪更新)

| 新事實 | SSOT 主檔 |
|--------|---------|
| Q2 scope = BMS Blurring 整合進 VMX cloud + 釋出 API doc | `06_calibration-log/critical-facts-log.md` 新增條 |
| Connect Source = API only · 不需要 UI portal toggle · API 控 any video / fleet | `critical-facts-log.md` Master Portal Blurring path 段加 v4 |
| Auto Sense = 用 VMX web UI · 要 GUI design · **Q2 不做** | `critical-facts-log.md` 新增條 + `case-learning/connectsource-passenger-blurring.md` § 8 |
| Monthly subscription report = post-Q2 future planning · **暫不開 Ticket**(等 production deploy 後有真實 usage 資料再開新單)| `case-learning/connectsource-passenger-blurring.md` § 8 |
| 時程:Staging end of June / Production end of July / Q2 release notes end of June | `critical-facts-log.md` + case file |

---

## C. Jira tickets(已開 · 2026-05-11 下午)

| Ticket | Summary | Type | Priority | Assignee | Due / Timeline |
|--------|---------|------|----------|---------|---------------|
| [**VMX-7457**](https://jira.navman.co.nz/jira/browse/VMX-7457) | [API] Integrate BMS Blurring functionality into VisionMax cloud(含 API doc share to MAU) | Task | 2 - Medium | **Spencer** | **Due 30/Jun/2026** staging · End of July production |
| [**VMX-7458**](https://jira.navman.co.nz/jira/browse/VMX-7458) | [VisionMax] [GUI] Blurring control UI on Master/Fleet Portal for non-API customers | Task | 2 - Medium | **Kenny** | Q2 feasibility · 實作 long-term |
| _(暫不開)_ | Monthly subscription report — Blurring tracking | — | — | — | Post-production · 等真實 usage 資料再開新單 |

### 為什麼 #4 暫不開:
- 舊單 [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427) "Improve reporting function #107"(Elvis 2025/06/05 開)是更大的 events reporting infra 工作 — Brian 4/20 acknowledge 但目前 DB performance 不足,要 Time Series DB migration
- Blurring monthly report 跟 [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427) overlap 但不是同一件事
- **2026-05-11 決策**:等 Production deploy 後有真實 usage 資料再開新單

### Kenny 開單時的 sharp 處理(repo 已 propagate):
1. **#1+#2 合併在 [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457)**:cloud integration + API doc share 寫成 2 個 deliverable 進同一票,doc share 成為 AC
2. **[VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) pattern reference 改精準**:從「Live User」改成「**Driver-Facing Camera Live View**」(GUI/Lucy team 更明確)
3. **[VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) Priority 2-Medium**(比一般 spike 高,訊號這雖然 long-term 但要動)

---

## D. Action Items

### 🔥 P0 · 今天剩下時間
- [ ] **Cary follow-up email**(把今天會議丟掉的球撿回來)— Brian / Spencer / Wendy / Elvis cc
  - 確認 Q2 scope(Ticket #1 + #2)
  - 補 monthly report 救球(Ticket #4 tracked for future)
  - 3 個 confirmation 寫進 email,讓 Cary 在文字裡答
- [ ] **Brian / Spencer 1-on-1 ping**:今天會議過程 review · 把 Kenny 的「execution gap 不是 product gap」框架講清楚

### 📅 P1 · 本週
- [ ] 開 4 張 Jira ticket(see § C)
- [ ] 跟 Spencer 拿 endpoint open production 的 concrete ETA
- [ ] Q1 release notes 還沒給 MAU 客戶之前先安排(Cary 5/11 提的 surprise prevention)
- [ ] 更新 case file + critical-facts-log + changelog(Claude 已執行)

### 🎯 P2 · 下個 sync 前(End of June)
- [ ] Q2 release notes summary 給 Cary(end of June)
- [ ] 跟 GUI team kick-off Ticket #3(Auto Sense UI 可行性)
- [ ] API doc 對 Connect Source SI 端 integration 進度追蹤

---

## E. Kenny 自我 review · Execution gap diagnosis

### 真實問題不是 prep gap,是 execution gap

| 準備層(做得好)| 執行層(沒 deploy)|
|--------------|-----------------|
| ✅ Kenny 版 HTML 完整(timeline / sound-bites / DON'T SAY / push back)| ❌ 會議現場沒打開 HTML / 沒 share screen 給 Cary 看 inheritance 圖 |
| ✅ Cary 版 HTML 圖完整 + 3 個 confirmation question 預備 | ❌ 沒主動帶 Cary 走圖 · Elvis 跟 Cary 自己 reframe · Kenny 變回答者不是領導者 |
| ✅ Don't say warning(別講 "I think" / "starting too fast")| ❌ 開場 30 秒就違反 |
| ✅ Monthly report 在 Cary 版 HTML 寫整段 "richer than UI" | ❌ 會議裡 "not the target for now" 直接 dismiss |
| ✅ Sound-bite verbatim 寫好 | ❌ 沒練習,進場 freestyle 失序 |

### 下次 protocol(會議室場景適配)

```
T-30min  獨自地方(廁所 / 工位)念 opening sound-bite × 5 次
         指圖練習 · 念 DON'T SAY × 3 遍
T-5min   關 Kenny 版 · 只留 Cary 版
         手機 Kenny 版開好(備用)
T-0      進會議室 · share Cary 版 · 開場 verbatim
         被 push 反射 = "Let me point at the diagram"
緊急     "Let me grab water" → 廁所看手機 30 秒 → 回會議
```

⚠️ **Kenny 版 HTML 不帶進會議室**(有 INTERNAL banner + DON'T SAY 字眼,被旁邊 Brian / Spencer 看到觀感差)

---

## F. 跨檔案連結

- 5/11 早上 Teams thread:[`2026-05-11_morning_cary-elvis-teams-thread.md`](2026-05-11_morning_cary-elvis-teams-thread.md)
- 5/8 Sync up source meeting:[`2026-05-08_syncup-cary-elvis_meeting-record.md`](2026-05-08_syncup-cary-elvis_meeting-record.md)
- CONNECTSOURCE case 主檔:[`../case-learning/connectsource-passenger-blurring.md`](../case-learning/connectsource-passenger-blurring.md)
- Critical Facts log:[`../knowledge/06_calibration-log/critical-facts-log.md`](../knowledge/06_calibration-log/critical-facts-log.md)
- Cary 版 HTML 圖(2pm screen share 用):[`../weekly-summary/2026-05-11_blurring-model_cary.html`](../weekly-summary/2026-05-11_blurring-model_cary.html)
- Kenny 版 HTML(會議前 drill 用,**不帶進會議室**):[`../weekly-summary/2026-05-11_blurring-model_kenny.html`](../weekly-summary/2026-05-11_blurring-model_kenny.html)

---

_Created 2026-05-11 下午,2pm sync 結束後 30 分鐘內。記錄人:Kenny / Claude。_
