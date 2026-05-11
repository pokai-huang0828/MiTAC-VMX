# 2026-05-11 早上 · Cary / Elvis Teams thread + 2pm 計畫

> **時間**:2026-05-11 上午(QPR 會議期間,Brian 不在場)
> **形式**:Teams chat thread(同 5/8 sync 的 group)
> **參與**:Kenny / Cary Lo (MiTAC AU) / Elvis Tran (MiTAC AU PM)
> **性質**:5/8 Sync up 的 P0 Action Items 實際執行 + Q2 portal path 經 Spencer alignment 後**拍板 Option B**
> **後續**:今天 2pm(台灣)Kenny + Elvis(可能 Cary)另開 Teams 講 Q1 API

---

## 一頁總覽

| 項目 | 結論 |
|------|------|
| **Q2 portal path** | ✅ **Cary 拍板 Option B(Master Centralised)** — Master 直接控所有 Blurring permission(含 Contract Fleet level),Fleet 不 manage |
| **拍板理由** | 1. Feature 可能 incur extra fee → SI 要 full control which fleet 推<br>2. **新需求**:monthly subscription report 加上「每 master account 下有多少 device 啟用此 feature」(billing tracking)|
| **Q1 API doc share** | ⏳ 等 Brian sign-off(QPR 後)|
| **重大限制揭露** | 🚨 **即使 doc 分享,客戶不能 call API** — endpoint 還沒在現 VMX 環境 open,要 internal validation 完成才開 |
| **暫時對外口徑** | 「Blurring function is on our roadmap」(等 Brian 同意才講)|
| **2pm 安排** | Kenny + Elvis 今天 2pm 再 sync 講 Q1 API · 同 group meeting link · Stark 也有 call shortly |

---

## A. Thread 動線(逐則摘要)

### A1. Kenny 開頭(QPR 進行中暫不能拍 Brian)
> "Brian and Spencer are currently in a meeting, I'll follow up with them once they're available and get back to you with the results via email."

### A2. Kenny + Spencer aligned 後出 preliminary update

#### Q1 · Sharing the Blurring API documentation
- **狀態**:API spec sharing 仍需 Brian sign-off
- **🚨 重要限制(新揭露)**:
  > "even once the document is shared, the customer will not be able to call the API yet, **because the endpoint has not been opened on our current VisionMax environment**. It will only be enabled after our internal validation is completed."
- 暫時可告知客戶「Blurring on roadmap」(等 Brian agree)

#### Q2 · Fleet / Contract Fleet level control(Spencer 提兩個 model)

| Option | 說明 | 5/8 sync 對應 |
|--------|------|--------------|
| **Option A — Two-tier delegated** | Master 持 overall blurring entitlement,delegate 給 Fleet · Fleet 自己決定 Contract Fleet 上 enable 與否 | ≈ 5/8 sync 的 **(B)** Fleet Portal 加 UI |
| **Option B — Centralised at Master** | Master 直接控所有 Blurring permission(含 Contract Fleet 層級)· Fleet 不 manage | ≈ 5/8 sync 的 **(A)** Master Portal 補視圖 |

> 兩個都 technically feasible · 差別在「客戶要給 Fleet 多少 autonomy」

### A3. Cary 回應:選 **Option B**

> "We both select OPTION B
> reason being this will potentially incur an extra fee, thus the SI need to be able to have full control which fleet they would like to push this feature out to.
> Meanwhile, It will also be great, if we can have this appear on the **monthly subscription report**.
> So we know how many devices under each master account has this feature implemented."

**重大轉折**:5/8 Cary 還警告 Master Portal 視圖會有「隱私 alarming」顧慮,**今天反而選 Centralised**。

**原因解讀**:
- billing 控制 > 隱私顧慮(extra fee 對 SI 商業模式更重要)
- Master 視角 = SI / dealer 視角,SI 要直接管 fee 流向
- 新需求 monthly subscription report 也只能由 Master 統一產出

### A4. 2pm 後續 sync(Q1 API)
- Kenny 邀請 Cary + Elvis 下午 sync 講 Q1 API
- Cary:14:00 our time(台灣)OK
- Elvis: 「I am available」
- Stark 那邊另外有 call shortly(不在本 group)
- 同 group meeting link

---

## B. 新事實摘要(SSOT 該去哪改)

| 新事實 | SSOT 主檔 | 更新動作 |
|--------|---------|---------|
| Q2 portal path 拍板 Option B Centralised at Master | `06_calibration-log/critical-facts-log.md`「Master Portal Blurring config UI」段 | 加結論:Cary 5/11 確認走 Centralised at Master |
| **Endpoint 未在現 VMX 環境 open** — 即使 doc 分享客戶也不能 call | `06_calibration-log/critical-facts-log.md` | 加新校正條 |
| Monthly subscription report 加「Blurring 啟用裝置數」新需求 | `case-learning/connectsource-passenger-blurring.md` | 加新需求段 |
| CONNECTSOURCE Action Items 進度更新 | `case-learning/connectsource-passenger-blurring.md` § Action Items | P0 第一條已執行 5/11 早上 |

---

## C. 對 5/8 Sync up 的 P0 Action Items 進度

從 5/8 meeting record:

| P0 | 5/8 寫的 | 5/11 早上實況 |
|----|---------|--------------|
| 回 thread 校正 Q2 portal path | 草稿待寄 | ✅ 已 reach out(經 Spencer alignment),提 Option A/B 兩個 model,**Cary 已拍板 Option B** |
| 跟 Spencer 確認 Blurring API doc 能否 share | 待動作 | 🟡 進行中:Spencer aligned · 仍等 Brian sign-off |
| 跟 Brian + Spencer 對齊 (A)/(B) 走哪條 | 待動作 | 🟡 進行中:Spencer 端已給兩個 model · 等 Brian QPR 後拍板 |

---

## D. Action Items(從本次 thread 掉出來)

### 🔥 P0(今天)
- [ ] **2pm Q1 API sync 跟 Elvis(可能 Cary)** — 同 Teams group
- [ ] **Brian QPR 結束後** 回頭 confirm:
  - API doc share 是否 OK
  - Option B 拍板是否符合 RD 端能力評估
  - Endpoint open 時程(internal validation 何時完成)
- [ ] 寫正式 email reply 給 Cary thread,確認 Brian 最終 position(Spencer preliminary already aligned)

### 📅 P1(本週)
- [ ] 跟 Spencer 細談 monthly subscription report 加新欄位的可行性
  - 對應 Jira 哪張 ticket?(VMX-5908 webhook?VMX-6586 group?或新單?)
- [ ] 把 Option B 拍板訊息寫進 `case-learning/connectsource-passenger-blurring.md`
- [ ] 更新 `06_calibration-log/critical-facts-log.md` Master Portal Blurring path 段

### 🎯 P2
- [ ] 若 Brian 同意 share API doc,準備一份「能 share 但不能 call」的 wording 給 Cary 對外用
- [ ] Monthly subscription report 加 Blurring 欄位若進 sprint,排優先級

---

## E. 戰略觀察

### Cary 的決策邏輯
- 5/8 vs 5/11 立場翻轉:從「擔心隱私(反對 Master 視圖)」→ 變成「billing 優先(選 Master centralised)」
- 推測:5/8 後內部討論發現「extra fee 由誰收 / 誰決定推」才是核心商業問題,隱私是次要顧慮可後續用 BMS 既有「Master 預設 on,Fleet 端不顯示開關」的設計 mitigate

### Spencer 的 Option 重新框架(語意上比 5/8 (A)/(B) 更精準)
- Spencer 用「**delegated** vs **centralised**」當主軸,比 5/8 sync 的「視圖層級」更貼近實作意圖
- Two-tier delegated 更貼近現有 Live User pattern;Centralised at Master 更貼近 SI billing 角度
- → 未來再有類似議題,用「delegation model」框架對外講會比「portal path」清晰

### Monthly subscription report 新需求 = 商業模式深化訊號
- 5/8 還在問「能不能做」,5/11 直接要求「能不能算錢」
- → 客戶已經把這當成下一輪 monetization,SI 要 billing visibility
- 對 MiTAC HQ 意義:Blurring 不只 feature,**是新一輪 subscription tier 上升的依據**

### Kenny 在 thread 中的定位繼續鞏固
- Brian 不在的時候 Kenny 直接代為 align Spencer,不是 Brian backup 而是**前線 PM**
- Cary 沒有等 Brian,直接跟 Kenny 拍板 Option B + 開新 2pm meeting
- → 5/8 sync 之後 Cary 線真的把 Kenny 當 entry point

---

## F. 跨檔案連結

- 5/8 Sync up source meeting:[`2026-05-08_syncup-cary-elvis_meeting-record.md`](2026-05-08_syncup-cary-elvis_meeting-record.md)
- CONNECTSOURCE case 主檔:[`../case-learning/connectsource-passenger-blurring.md`](../case-learning/connectsource-passenger-blurring.md)
- Critical Facts(Master Portal Blurring path 校正):[`../knowledge/06_calibration-log/critical-facts-log.md`](../knowledge/06_calibration-log/critical-facts-log.md)
- Plan Type 議題(可能跟 Blurring 並列為新 plan tier):[`../knowledge/03_systems-architecture/plan-types.md`](../knowledge/03_systems-architecture/plan-types.md)
