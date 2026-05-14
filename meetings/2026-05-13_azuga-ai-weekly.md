# 2026-05-13 Azuga AI Weekly — 會議完整紀錄

- **日期**:2026-05-13(Tue)下午
- **性質**:Azuga AI Weekly(Mitac × Azuga + Webfleet/BMS 聯合 weekly)
- **整理視角**:Kenny PM 角度 · 議題 + Jira comment 交叉驗證 + 對 6/2 release scope 影響
- **來源**:會議錄音 → NotebookLM 兩份摘要(短版 + PM 版)+ 5/14 重抓 Jira filter 36457/36458 cross-check
- **整理人**:Kenny Huang(黃柏凱)
- **修訂史**:2026-05-14 初版整理(會議隔天)

---

## 一頁總覽

| 項目 | 內容 |
|------|------|
| 議題數 | **8 個**(2 份 NotebookLM 摘要合併去重) |
| Action items | **11 個**(對 Mitac 內部 + 客戶端) |
| 客戶出席 | Sebastian / Martin / Jakob / Sirphim / Sophin / Jacob / Sabine(Webfleet + Azuga 聯合) |
| Mitac 出席 | Brian / Eric / Allen / Jay / Vincent / Jieli |
| **對 6/2 release 影響** | **三大 deliverable → 五大 deliverable**(+ Eye Stable Rate threshold + Camera Auto-Height 新演算法) |
| 新發現 bug | VMX-7471 dmsCamera null bug(由 mori.jhang 5/13 揭露)|
| 客戶切換等待模式 | **HAWK-501** Auto-Height: Sebastian 5/13「等下版本」 |
| 待開新單 | (1) Camera Auto-Height 後續單(Sebastian 開)(2) Eating/Drinking 訓練資料(評估後)(3) PECWS(規格 review 後)|

> **重要校正**:此會議原以為是「BMS AI Alignment」獨立場,5/14 確認**就是 5/13 Azuga AI Weekly 同一場**,Webfleet/BMS 議題在同一場討論。

---

## 8 議題逐項

### 1. HAWK-401 — DMS 不同安裝角度模型訓練(舊案,12 月以來無進展)

**討論**:
- Webfleet 希望模型支援 DMS 鏡頭不同安裝位置(尤其低位)
- Mitac 在收集不同角度的影像準備訓練,**但尚未獲核准推進**
- 需耗費龐大工程資源收集各種角度照片

**Jira 證據**:
- [HAWK-401](https://jira.navman.co.nz/jira/browse/HAWK-401) status=New, assignee=allen.yc.chung, priority=Gating, updated 5/12
- 5/12 sebastian「@allen.yc.chung what is the current state of this ticket? Are you actively working on this topic?」**Allen 未回**
- 12/3 sebastian 接受條件 + 額外開 HAWK-471 處理 load factor

**決策**:Allen 與客戶(Jacob/Sirphi/Sophin)重新對焦優先級,再決定研發投入

---

### 2. Lens Cover Detection — 6/2 修(獨立邏輯 + debounce + 移除車速限制)

**討論**:
- **痛點**:Webfleet 最新韌體 Lens Cover 偵測不穩定 — Martin/Jakob **無法成功偵測**,debounce 失效
- **根因**:現行架構下若 DMS 臉部校正未完成,Lens Cover 偵測**不會觸發**
- **6/2 新規格**:
  1. 移除車速限制
  2. 獨立於 DMS 校正狀態之外進行判定
  3. 修 debounce time 問題
  4. **首次觸發後不再發,直到 obstruction 移除達 configured period → 觸發 Lens Uncovered event**(eric.h 5/13 對 Webfleet 確認)

**Jira 證據**:
- [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) Improve Lens cover detection design · Open · jieli.liu · fv=VisionMax_20260602
  - 5/13 19:20 **eric.h** 對 Sirphim / Jakob / Sebastian 發新規格 update
  - 5/8 13:38 eric.h「planned for next release in June」
- [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) 'Lens cover' detection not properly working · New · leo.tsai · fv=VisionMax_20260602(**5/13 新開**)
  - 5/11 brian.chienlee「@leo.tsai please check the provided app log」
- [HAWK-573](https://jira.navman.co.nz/jira/browse/HAWK-573) Request event blurry not updating · fv=VisionMax_20260602(同期)

**決策**:Vincent 6/2 修 debounce + Jira 補 root cause 在 ticket 上;Sebastian/Jakob 提供 failed 影片與 log

---

### 3. PECWS — Pedestrian Collision Warning System(規格確認階段)

**討論**:
- Eric 已回覆所有前期問題
- **目前設計為舊有設計**,僅在 Azuga 和 Webfleet 端討論過
- Mitac 正式啟動前**必須先完成規格確認**

**Jira 證據**:無對應 ticket(尚未開單)

**決策**:Eric / Jacob / Sirphi 共同 review 並確認規格,確認後 Mitac 才開發

---

### 4. Camera Auto-Height Detection 誤差議題(關鍵)

**討論**:
- **客戶反對「改手動」**:
  - Martin 與 Sebastian:已在線上運行的數千台設備,逐台關閉自動校正不可行(遷移成本龐大)
  - 安裝人員無法精準測量卡車內實際高度
  - **Jakob**:自動校準是產品的一大賣點,期望修復精準度,不是依賴車輛類型或手動輸入
- **Mitac 回應(Brian)**:RD 正在開發新演算法彌補誤差;請客戶**暫緩手動設定討論**,等 6/2 新版本實測驗證

**Jira 證據**:
- [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) ADAS Self-calibration resolves wrong height · **status: New → Open(5/13 跨客戶觸發)** · eric.h · priority 1-High · fv=VisionMax_20260602
  - 5/13 15:57 **sebastian**「According to brian.chienlee the Mitac team is working on some improvements to make the auto height detection more reliable. **Let's wait for the next version and check again.**」← **客戶切換到等待模式**
  - 4/29 13:56 eric.h 詳列 `device.system_camera_height_auto_detect` 參數設計(預設 true = MiAI 自動估計;false = 用 server 值)

**決策**:
- Jay 持續改善 auto height 演算法 + ADAS 影響評估,6/2 確認結果
- Martin 內部討論固定高度後果
- **Sebastian 關 HAWK-501,開新單追蹤 Auto-Height fix**(等票號)

---

### 5. HAWK-482 — AI 模型跨版本測試 + Log 路徑對齊

**討論**:
- 客戶希望有工具評估 AI 版本表現(v19 比 v18)
- **Mitac 立場**:開發成本極大(huge effort),**Not feasible for now**;現階段依賴內部用新舊版本針對客戶提供影像回放
- **Log 路徑對齊**:客戶口中的「Application Log」= Mitac 的「R logs」
- **對「非物件事件」(疲勞 / 分心)**:無 debug 畫面時,Mitac 必須依賴 app log 才能 root cause(找不到臉孔 / 眼球穩定率異常)
- **內部路徑**:`/rlogs` + `/log` 資料夾(內部記憶體根目錄)

**Jira 證據**:
- [HAWK-482](https://jira.navman.co.nz/jira/browse/HAWK-482) Provide a event detection replay functionality · New · 5 comments
  - 3/20 sebastian 要 ServerAI 自動 re-evaluate Webfleet/Azuga 提供的 snapshot 比版本差異 — **2 個月沒回**
  - 1/22 allen「For current evaluation from Mitac side, It's hard to generate this function or tool due to technically issue」

**決策**:
- 雙方確認「不開發外部 tool,Mitac 內部用 log 回放」
- Martin / 客戶端 engineering 更新內部文件:**未來 false negative 報告必須含影片 + /rlogs + /log**

---

### 6. Eye Stable Rate Threshold 開放(6/2 release 新範圍)

**討論**:
- 6/2 更新將**開放讓客戶透過參數設定睜眼率閾值**
- 用於微調疲勞(Fatigue)偵測敏感度

**Jira 證據**:
- [VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309) Provide the configuration of the EyeStableRate threshold · Open · joe.lien · fv=CameraAPP_202605
- [HAWK-551](https://jira.navman.co.nz/jira/browse/HAWK-551) [CAM Lite] Inaccurate fatique detection → new config to lower EyeStableRate threshold · New · brian.chienlee · fv=VisionMax_20260602(對應 ticket)

**決策**:Jieli + APP team 把 threshold 設定包入 6/2 firmware

---

### 7. Eating & Drinking 訓練資料 — Azuga 主動提供去識別化影片

**討論**:
- 近期飲食誤判(對應 Roadmap-vs-internal.md L46 客訴 17×)
- **Azuga 主動提議**:從龐大事件庫提供「去識別化(Anonymized,看不到人臉)」的行車影片給 Mitac 訓練
- **Mitac 回應**:下個月評估**「看不到臉時,僅有水杯或食物的影像對 root cause 是否有實質幫助」**

**Jira 證據**:無對應 ticket(尚未開單)

**決策**:Eric / Vincent 內部評估;若可行則於 ticket 上回覆客戶索取

---

### 8. ADAS 校正完成語音提示延遲(對應 HAWK-587 新票)

**討論**:
- **Alpha 測試車隊回報**:ADAS 校正完成的語音提示,要等到第一次違規(如車道偏移)時才會播報
- **Mitac 澄清**:這是**系統設計使然** — 當設備 Debug Overlay 關閉時語音延遲;Debug Overlay 開啟時校正完成當下會立刻通知

**Jira 證據**:
- [HAWK-587](https://jira.navman.co.nz/jira/browse/HAWK-587) CALIBRATION COMPLETED notification (if active) delayed until first ADAS violation · New · brian.chienlee · 5/13 開 · **0 comments**

**決策**:**非 bug,規格使然** — 文件化(Brian 紀錄在 HAWK-587 上)

---

## Action Items 整合(11 個 · 對人 + 期限)

| # | 對象 | Task | Due | Jira |
|---|---|---|---|---|
| 1 | **Allen**(Mitac) | HAWK-401 priority 與 Jacob/Sirphi 對焦,Sebastian 將 HAWK-401 重新指派給 Allen | 下次 weekly | [HAWK-401](https://jira.navman.co.nz/jira/browse/HAWK-401) |
| 2 | **Allen + Brian**(Mitac) | HAWK-482 + PECWS priority 與 Azuga 對焦,規格 / 商業價值未明前攔截 RD | 下次 weekly | [HAWK-482](https://jira.navman.co.nz/jira/browse/HAWK-482) |
| 3 | **Vincent**(Mitac) | 修 Lens Cover debounce + Jira 補 root cause | **6/2** | [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) / [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) |
| 4 | **Jieli + APP team**(Mitac) | Lens Cover 解耦邏輯 + Eye Stable Rate threshold 包入 6/2 firmware | **6/2** | [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) / [VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309) |
| 5 | **Jay**(Mitac) | Camera Auto-Height 新演算法 + ADAS 事件影響評估 | **6/2** | (待 Sebastian 開新單) |
| 6 | **Eric + Vincent**(Mitac) | Camera Height 演算法加速 + Eating/Drinking 去識別化影片可行性評估 | 1 個月 | (新 ticket TBD) |
| 7 | **Eric + Jacob/Sirphi**(共同) | PECWS 規格 review + 確認 | 啟動前 | (新 ticket TBD) |
| 8 | **Sebastian**(Webfleet) | 關 HAWK-501 + 開新單追蹤 Auto-Height fix | 本週 | [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) |
| 9 | **Sebastian / Jakob**(Webfleet) | 提供 Lens Cover failed 影片 + log 給 Mitac | 盡快 | [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) |
| 10 | **Martin**(Webfleet 內部) | 評估若需固定攝影機高度參數可能影響與後果 | — | — |
| 11 | **Martin + 客戶端 engineering** | 更新內部文件 / 提報流程 — 未來 false negative 報告必須同時提供**影片 + /rlogs + /log** | — | — |

---

## 對 6/2 Fix Version 的修訂(**重要**:三大 → 五大 deliverable)

**舊敘述**(5/11 AI Weekly 內部 roundup 記的):
1. LDWS API([VMX-7101](https://jira.navman.co.nz/jira/browse/VMX-7101) "LDWS Improving (Server)")
2. BMS 鏡頭遮蔽拆分([HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) + [VMX-6983](https://jira.navman.co.nz/jira/browse/VMX-6983))
3. 新版 DMS 模型(Model 26)

**新敘述**(5/13 Azuga AI Weekly 確認):
1. LDWS API([VMX-7101](https://jira.navman.co.nz/jira/browse/VMX-7101))
2. **Lens Cover 解耦**([HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) 規格 + [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) 實作 bug):移除車速 + 獨立於 DMS 校正 + 修 debounce
3. 新版 DMS 模型(Model 26)
4. **Eye Stable Rate threshold 開放**([VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309) + [HAWK-551](https://jira.navman.co.nz/jira/browse/HAWK-551))
5. **Camera Auto-Height 新演算法**([HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) 後續單,Sebastian 開)

---

## 對 Kenny Pending 追蹤的影響

對應 [pending-confirmations-2026-05-14.xlsx](../pending-confirmations-2026-05-14.xlsx):

| Excel ID | 變動 |
|---|---|
| **ID 1 LDWS API VMX-7101** | Jira 上 fixVersion 仍空,沒「6/2 重掛」comment — **chase Jimmy 在 Jira 補 fixVersion=VisionMax_20260602** |
| **ID 7 Blurring API VMX-7457** | 加 VMX-7471 dmsCamera null bug 子線(mori.jhang 5/13 揭露)|
| **ID 20 6/2 Fix Version 全名單** | 從「三大」改「**五大**」(+Eye Stable Rate threshold + Camera Auto-Height) |
| **ID 26 Brian Coffee Chat** | 加問項:PECWS spec timeline + HAWK-482 priority |
| **新項目候選** | (a)Sebastian 開 Camera Height 新單 等票號 (b)Azuga Eating/Drinking 去識別化影片 評估 1 個月 (c)VMX-7471 dmsCamera bug |

---

## 隱藏細節(NotebookLM 摘要 1 漏記,摘要 2 才有)

對未來看 transcript 校正時的提醒:
- 摘要 1(短版)只有 5 議題 + 7 action items;**漏記**了 #6 Eye Stable Rate threshold、#7 Eating/Drinking、#8 ADAS Voice 三個議題
- 摘要 2(PM 版)是 8 議題完整版,結構是「核心 AI 功能 / 硬體校正 / API & 排障」三層,加 3 個 PM Task 分派
- 兩份對 HAWK-482 結論用詞看似衝突(「需要 dataset」vs「Not feasible」),實際**一致** — Mitac 內部用 log 自己回放,不開發外部 tool

---

## 後續同步

寫進 repo:
- 本檔 `meetings/2026-05-13_azuga-ai-weekly.md` + HTML mirror
- [critical-facts-log.md § 6/2 Fix Version 死線](../knowledge/06_calibration-log/critical-facts-log.md) — 三大 → 五大 deliverable
- [pending-confirmations-2026-05-14.xlsx](../pending-confirmations-2026-05-14.xlsx) — 改 ID 20,加 3 個新項目
- [ai-weekly-internal-roundup.md](ai-weekly-internal-roundup.md) — 加 cross-ref 到本檔
- [knowledge/00_index/changelog.md](../knowledge/00_index/changelog.md) — 本日變動紀錄
