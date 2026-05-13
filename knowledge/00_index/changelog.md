# Knowledge Changelog · 近 30 天變動紀錄

> 每次 Claude 改 knowledge / case-learning / weekly-summary 順手加一行。**新的在上面**。
> 格式:`YYYY-MM-DD · 動作 · 檔案 · 一句話 why`

## 2026-05-13 · PS Vinicius 撞 VMX-7404(跨客戶第三例)

- 2026-05-13 · **APPEND Phase 7** · `case-learning/vinicius-platform-science.md` + `.html` — Vinicius 5/13 06:2X mail 反映 K265 L1225380005 OTA + SDK ✅ 但 ADAS Failure 持續 + reboot 無效 / Righter 5/13 11:41 reply install + 30 km/h drive on lane-markings + 綠框 horizon alignment 附圖 / Kenny PM 判斷不另回 thread(避免 PM 補刀 RD),內部 cross-link 到 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)
- 2026-05-13 · **UPDATE** · `knowledge/06_calibration-log/vmx-7404-tracking.md` + `.html` — 現況段加「PS 撞線」/ Evidence 表拆雙層(Trip-level + 跨客戶 3 行)/ 待動作加 PS follow-up monitor + Brian 1on1 戰略點 · meta 從 2026-05-06 → 2026-05-13
- 2026-05-13 · **STRATEGIC INSIGHT** · **[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 跨客戶證據鏈擴大為三家**:Kenny 自測(MiTAC 內部 K245)+ Webfleet([HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) / 574 / 401)+ Platform Science(K265)— 都撞同根因(30 km/h × 3 mins 行駛條件 + install angle)· 對評估期 Brian / Steve 報告 = 重大 PM 籌碼

## 2026-05-13 · Elvis Teams thread + cost model 三輪校正

- 2026-05-13 · **APPEND § 9** · `case-learning/connectsource-passenger-blurring.md` + `.html` — 5/13 早上 Kenny 推 4-step flow → Elvis 09:18 pushback(Step 3 質疑必要性 + Step 4 bandwidth)→ Spencer rationale(Step 3 = cost / storage 控制點)→ cost model 三輪修訂(v1 誤引 Rekognition / v2 校正自家 AI / v3 storage 重算 1.8× 不是 10×)→ profitability sensitivity(break-even 在 ~8×)→ Kenny v3 訊息送出 → 等客戶回 cost mode + download UX
- 2026-05-13 · **CALIBRATION** · Storage 倍數真相:**~1.8×(不是 10×)**因為原始檔本來就會存,只有 blurred copy 隨 trigger 倍增。AI 處理量 10× 是物理事實但 cost scaling 黑盒(MiTAC 自家 AI infra)
- 2026-05-13 · **FRAMING 防身術** · 整理 6 條外部訊息 wording 規則(Mechanism / hypothetical / scales meaningfully higher / subject to Spencer / separate commercial arrangement / BMS 不可見轉設計理由) — § 9.7 可重用

## 2026-05-12 下午 Δ · Jira 重抓 + Outlook + NotebookLM 三線對齊

- 2026-05-12 · **NEW SNAPSHOT** · `jira_data/jira_tickets_snapshot_2026-05-12T15.json`(164 票 = 137 舊 + 27 新)— 透過 Chrome MCP + Jira REST API `key in (...)` JQL + `updated >= 2026-05-12 AND project in (VMX, HAWK)` 二次抓取,Diff 結果:**1 票狀態變動 + 27 票同日新建**
- 2026-05-12 · **DIFF** · [VMX-7407](https://jira.navman.co.nz/jira/browse/VMX-7407) New → Resolved 5/12 13:25(@righter.song)— UVC RAW Frame 不支援 error handling 已 fix
- 2026-05-12 · **NEW DOC** · `weekly-summary/2026-05-12_afternoon-delta.md` — Jira / Outlook / NotebookLM 三線 delta,含 5/12 新建的 [VMX-7459](https://jira.navman.co.nz/jira/browse/VMX-7459)(Lens Cover toggle)/ [VMX-7462](https://jira.navman.co.nz/jira/browse/VMX-7462)(Rollover UI)/ [VMX-7441](https://jira.navman.co.nz/jira/browse/VMX-7441) 7458(Blurring Master/Fleet 雙層)等 27 票
- 2026-05-12 · **CALIBRATION** · `06_calibration-log/critical-facts-log.md` 加 **AI Model 版本對應 + 6/2 Fix Version 死線**(從 5/11 AI Weekly 錄音 NotebookLM 揭露:Model 11P 嘴部→全臉打哈欠 / 11L 舊 DMS / 26 新 DMS 取代 11L / V14 舊 Blurring · 6/2 死線含 LDWS API + Lens Cover + Model 26)
- 2026-05-12 · **UPDATE** · `01_product-knowledge/miai-roadmap-2026.md` 加 4 個 Model 版本對應表(11P / 11L / 26 / V14)+ 6/2 Fix Version 死線標註
- 2026-05-12 · **OUTLOOK** · 確認 5 個訊號:Lucy VMX-7441 設計稿 cc Kenny review / Jimmy 5/12 11:00-13:00 AI Weekly @ A0512 / Vinicius 5/11 22:03 收到 JS lib V1.0.4 開始測試 / Simon Wu 對 Brian Fleet Portal R02 draft 給 page-by-page feedback / Honeywell ME CDR 5/11 內部會待補
- 2026-05-12 · **NOTEBOOKLM** · 揭露 repo 缺的 3 個錄音:**5-10 Syncup with MAU for API questions** / **5-11 ai weekly meeting.m4a** / **5-8 Chat for API with MAU**(meeting note 待做)
- 2026-05-12 · **JIRA-SNAPSHOT HTML** · `websiteview/docs/00_index/jira-snapshot.html` 加 5/12 下午 Δ 段(1 狀態變動 + 27 新票快取 + 4 個 AI Model 死線標)

## 2026-05-12 晚 · 視覺 UIUX 13 頁 audit + 7 個 polish + session handoff

- 2026-05-12 · **AUDIT** · Chrome MCP screenshot 主動審 13 頁(index / knowledge / case-hub 4 tab / styleguide / 2 portal slide / 6 docs)
- 2026-05-12 · **VISUAL FIX** · 7 個 polish:nested anchor / Zone 0 4+1 / NOW card 空白 / table column squeeze / .html→.md / Sticky TOC overlap / TOC §N prefix
- 2026-05-12 · **NEW DOC** · `weekly-summary/2026-05-12_session-handoff.md` — 完整 session 收尾與下一個 Claude 入口
- 2026-05-12 · **STAKEHOLDERS** · 「每週固定會議」list → 表格(會議 / 時段 / 性質 / 重點),Q2 Tracker review 標 ❌ 已過期

## 2026-05-12 後續 · 全 hub 自動加 Jira 連結 + comment-level ingest

- 2026-05-12 · **AUTO-LINK** · 全 hub `.md` + `.html` 內 **549 個 unlinked VMX-* / HAWK-* mention** 自動加上 Jira hyperlink(MD 用 `[KEY](url)` · HTML 用 `<a class="ext-link jira-link">`),跨 **50 個檔案**
- 2026-05-12 · **COMMENT INGEST** · 透過 Chrome MCP + Jira REST API 抓取所有 137 ticket 的 **last 3 comments**(總 ~84 KB)。從 comment 內容揭露 5 個額外 docs 沒反映的 Resolved/Closed 狀態:VMX-6925 / VMX-7346 / HAWK-578 / HAWK-527 / HAWK-331
- 2026-05-12 · **CALIBRATION** · `06_calibration-log/critical-facts-log.md` 「Jira 本週新 Resolved」段重組為 4 子段(已 ship / 已 Closed / 設計完未 ship / 進行中)共記錄 **12 個 ticket 進度變動**

## 2026-05-12 · Jira 全量 snapshot ingest + cross-ref audit

- 2026-05-12 · **NEW DOC** · `websiteview/docs/00_index/jira-snapshot.html`:透過 Chrome MCP + Jira REST API 一次抓取**全 hub 提及的 137 個 VMX/HAWK ticket** 即時狀態,加進 Knowledge Hub hero 「Meta links」第三個入口
- 2026-05-12 · **NEW CSS/JS** · `css/jira-snapshot.css` + `js/jira-snapshot.js`:status 過濾 + age-based 顏色強化 + 連 Jira ticket 的外部連結
- 2026-05-12 · **CALIBRATION** · `06_calibration-log/critical-facts-log.md`:加 2 段
  - 「Jira 本週新 Resolved/Closed」5 個 ticket([VMX-7239](https://jira.navman.co.nz/jira/browse/VMX-7239) / 7419 / 7381 / 6353 / 6920)docs 之前未反映
  - 「Jira `New` status 含意」段 — 全 hub 137 票 93 個 (68%) 是 New,實際多數已完成只是 RD transition 漏按
- 2026-05-12 · **UPDATE** · `02_organization-map/stakeholders.md` BMS 列:[`VMX-6920`](https://jira.navman.co.nz/jira/browse/VMX-6920) 加 ✅ Closed 2026-03-09 (Jimmy)
- 2026-05-12 · **SNAPSHOT** · `jira_data/jira_tickets_snapshot_2026-05-12.json`(repo root, 25 KB)— 137 ticket 完整狀態 raw data,以後可拿來 diff 比對

## 2026-05-11 晚 · Repo 整併 + UI / CSS / JS 完全分離

- 2026-05-11 · **MOVE** · `VMX_images/` → `websiteview/VMX_images/`(29 PNG · 7 檔路徑同步)· Web 資產統一進 `websiteview/`
- 2026-05-11 · **MOVE** · `meetings/*.md.html` × 2 + `weekly-summary/*.html` × 3 → `websiteview/docs/{meetings,weekly-summary}--*.html`(加前綴避免撞名)
- 2026-05-11 · **CONVERT** · 7 個未轉的 `.md` 補產 HTML view · `case-learning/` × 3 + `meetings/` × 4(舊版自帶 inline style 的 2 個也重做進 doc-standalone.css 框架)
- 2026-05-11 · **DELETE** · `knowledge/archive/`(3 個 md 已搬進 calibration-log 主檔,本來就重複)
- 2026-05-11 · **RENAME** · `portal_reference/` → `presentations/`(Kenny 後續會放其他 pptx 進來)
- 2026-05-11 · **REFACTOR** · `websiteview/case-hub.html` inline `<script>` 抽到 `js/case-hub.js` · 42 處 `style="..."` 抽到 `css/case-hub.css`(新增 5 個 card status 變體 + 12 個 utility class)· 結果:**0 個 inline style / script**
- 2026-05-11 · **UI** · `css/knowledge.css` 內 `.doc-content` 排版優化 · 行高 1.7→1.75 · 段落 14px margin · 內文 72ch max-width · h1 30px / h2 padding+ / h3 `▸` marker / blockquote 強化 / hr 改 gradient / 首段 lede / inline code 顏色 brand-blue
- 2026-05-11 · **README** · 重寫資料夾結構表 + HTML 結構段(反映 .md = source、.html = view 分層)

## 2026-05-11 收工 audit(本日最終對齊檢查)

- 2026-05-11 · **AUDIT** · 跑完整天 SSOT consistency check · grep [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457)/7458/6427 + Option A/B + Brian Jira=SSOT + 5/8 P0 標記 · 找出 5 個 drift / 漏洞並修正:
  - **F1**:changelog 寫的 `2026-05-11_blurring-inheritance-model.html` v0 draft 已不存在,描述改成 SUPERSEDED
  - **F2**:`00_index/ssot-map.md` CONNECTSOURCE 狀態從「🟡 5/8 校正中」更新為「🟢 ACTIVE · Q2 scope 已鎖定」· 加 Jira tickets 對應主檔分類 · 加 Calibration rules 4 條
  - **F3**:`memory/project_week_summary_2026-05-11.md` 補完整 5/11 timeline(早上→下午→傍晚四段)+ Kenny 失分/補分 ledger · `MEMORY.md` 加「Brian Jira=SSOT rule」⭐⭐ entry
  - **F4**:`meetings/2026-05-08_syncup-cary-elvis_meeting-record.md` P1 + P2 Action Items 全標已執行(5/11 下午 sync 完成 + 5/8 (A)/(B) UI 框架 superseded)
  - **F5**:`websiteview/case-hub.html` CS page 卡片重新排序(5/8 superseded 灰卡從中間移到底部 · Q2 拍板→Jira queue→Brian SSOT 三張綠卡連續 · monthly report wording 修正「仍開 #4」→「Ticket #4 暫不開」)
- 2026-05-11 · **NEW ENTRY** · `00_index/ssot-map.md` 加「📋 Jira tickets 對應主檔」+「🎯 Calibration rules」兩個新分類 · 對應 4 張 Jira([VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457)/7458/7404/6427) + 4 條 calibration rule(Jira=SSOT / doc≠endpoint / Option A vs B / Connect Source API only)

## 2026-05-11 傍晚 v4(本日 · Brian 二次回應 + calibration 校正)

- 2026-05-11 · **CALIBRATION** · Kenny ping Brian 確認後 · **Brian 二次回應「不用那麼麻煩, 他看我 Jira 寫清楚了」** · 校正之前「不留書面 trail」推測 → **真實立場 = Jira ticket 就是 SSOT, external email 重複 Jira 內容 redundant**
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · 「Brian 攔下」條重寫成「Jira = SSOT, email follow-up redundant」· 加適用/不適用情境 + 客戶 chase 時口頭答覆規則
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` § 8.8 · 加 v2 校正紀錄 + 6 個 chase 時口頭答覆模板(Q1/Q2/doc/endpoint/monthly report/Option A/B)
- 2026-05-11 · **UPDATE** · `websiteview/case-hub.html` · 橘卡(攔下)改成綠卡(認可)· 修正解讀為 Brian 對 Kenny 開單質量肯定
- 2026-05-11 · **INSIGHT** · MDT 文化:**書面工作 > 口頭工作** · 把 Jira / case file / changelog 寫精細 = 對 Brian 等同「Kenny 有 own」訊號 · 補回今天 2pm execution gap 一半失分

## 2026-05-11 傍晚 v3(本日 · Brian 攔下 follow-up email + calibration)

- 2026-05-11 · **DECISION** · Cary follow-up email 起草後 Brian 說「不要發」· 暫停 · 推測 Brian 不想在 spec/timeline 鎖死前留書面 commitment trail
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` § 8.8 · 完整紀錄事件 + 推測原因 + Kenny 後續動作 + email draft 存底 + implication
- 2026-05-11 · **NEW CALIBRATION** · `06_calibration-log/critical-facts-log.md` · 加「Brian 攔下對 Cary 書面 follow-up」校正條 · **規則:未來對外發 commitment 文件前先 Brian sign-off**
- 2026-05-11 · **TODO** · Kenny Teams 短訊 ping Brian 確認:(1) Brian 自己發還是 hold?(2) 若 hold,什麼 trigger 後再 communicate

## 2026-05-11 傍晚 v2(本日 · [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) deliverable 拆分 + repo 對齊)

- 2026-05-11 · **JIRA COMMENT** · [`VMX-7457`](https://jira.navman.co.nz/jira/browse/VMX-7457) 加 comment 釐清 2 個 deliverable 不同 timeline · A(doc share 本週)/ B(cloud integration staging 30/Jun · prod end-Jul)· 對 Cary 兩條 commitment traceable
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` § 8.4 · 加「[VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) 內 2 個 deliverable 不同 timeline」table
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · Jira tickets reference 段加 deliverable A/B 拆分說明 + 對 Cary 兩條 commitment
- 2026-05-11 · **UPDATE** · `websiteview/case-hub.html` CS page · [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) row 加 2 deliverable bullet 表 + timeline 拆分

## 2026-05-11 傍晚(本日 · Jira tickets 開好 + repo 對齊)

- 2026-05-11 · **NEW JIRA** · [`VMX-7457`](https://jira.navman.co.nz/jira/browse/VMX-7457) "[API] Integrate BMS Blurring functionality into VisionMax cloud" · Task · 2-Med · Spencer assignee · Due 30/Jun/26(staging)· #1+#2 合併 · API doc share 寫進 AC
- 2026-05-11 · **NEW JIRA** · [`VMX-7458`](https://jira.navman.co.nz/jira/browse/VMX-7458) "[GUI] Blurring control UI on Master/Fleet Portal for non-API customers" · Task · 2-Med · Kenny assignee · Q2 feasibility · pattern 改 "Driver-Facing Camera Live View"
- 2026-05-11 · **DECISION** · #4 monthly subscription report 暫不開 ticket · 舊單 [VMX-6427](https://jira.navman.co.nz/jira/browse/VMX-6427) 是更大 events reporting infra 不對等 · Production deploy 後再開新單
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` § 8.4 · placeholder #1/#2/#3/#4 換成真實 [VMX-7457](https://jira.navman.co.nz/jira/browse/VMX-7457) / [VMX-7458](https://jira.navman.co.nz/jira/browse/VMX-7458) + 加 sharp 處理說明
- 2026-05-11 · **UPDATE** · `meetings/2026-05-11_afternoon_cary-elvis-sync.md` § C · 同步 Jira queue + Kenny 開單 sharp 處理
- 2026-05-11 · **UPDATE** · `websiteview/case-hub.html` CS page · Jira queue table 改成真實票號 + 加 #4 不開原因註腳
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · ticket reference 加進對應段落

## 2026-05-11 下午晚段(本日 · 2pm Cary/Elvis/Brian sync 後)

- 2026-05-11 · **NEW**    · `meetings/2026-05-11_afternoon_cary-elvis-sync.md` · 2pm sync 完整紀錄 — Brian take over 拍板 Q2 scope + Jira queue + Kenny execution gap 自評
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` · 加 § 8 2pm sync 結論 + § 8.4 Jira ticket queue(4 張)+ § 8.7 Kenny execution gap 自評
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · 加 2 條校正:(1) Connect Source = API only / Auto Sense = UI(Q2 不做)(2) Option A vs B 在 API 層同一條 flow(superseded UI 視角框架)
- 2026-05-11 · **NEW(2 prep assets)** · `weekly-summary/2026-05-11_blurring-model_kenny.html` + `_cary.html` · 給 Cary 2pm sync 用的 HTML 圖(Kenny 內部練習用 + Cary 對外 client-facing 兩版)
- 2026-05-11 · **SUPERSEDED** · `weekly-summary/2026-05-11_blurring-inheritance-model.html` v0 draft · 已被 `_kenny.html` + `_cary.html` 雙版本取代並移除 · weekly-summary/ 內僅留 _kenny / _cary 兩版
- 2026-05-11 · **NOTE**   · Jira tickets #1-#4 由 Kenny 自己手動開 · ticket draft 完整內容見 `meetings/2026-05-11_afternoon_cary-elvis-sync.md` § C

## 2026-05-11 下午(本日 · CONNECTSOURCE morning thread 後續)

- 2026-05-11 · **NEW**    · `meetings/2026-05-11_morning_cary-elvis-teams-thread.md` · 早上 Teams thread 紀錄 — Cary 拍板 Option B(Centralised at Master) + endpoint 未 open 限制 + monthly report 新需求 + 2pm Q1 API sync 安排
- 2026-05-11 · **UPDATE** · `case-learning/connectsource-passenger-blurring.md` · 加 § 6 5/11 morning thread + § 7 更新後 Action Items · 5/8 P0 標已執行
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · Master Portal Blurring path 段加 v3 Cary 拍板 Option B · 新增「API doc share ≠ endpoint open」校正條
- 2026-05-11 · **UPDATE** · `meetings/2026-05-08_syncup-cary-elvis_meeting-record.md` · Action Items § C 標 P0 5/11 早上已執行 + 4 條 5/11 新訊號

## 2026-05-11(本日)

- 2026-05-11 · **STRUCT** · `knowledge/00_index/` · 建索引層 + changelog + ssot-map(取代散落的「最近改了什麼」資訊)
- 2026-05-11 · **STRUCT** · `knowledge/archive/` · 建 archive · 收 3 個 2026-05-07 dated snapshot
- 2026-05-11 · **MOVE**   · `06_calibration-log/{ai-tab-jira-alignment,ai-team-row-by-row-status,cary-passenger-blurring}-2026-05-07.md` → `archive/2026-05-07_*.md`(被 weekly-summary + critical-facts 取代)
- 2026-05-11 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · 加 KPI 100K(差 15K)+ Lens Cover 6 月 release 單軌兩條
- 2026-05-11 · **UPDATE** · `06_calibration-log/vmx-7404-tracking.md` · 加 § H HAWK 側平行案([HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) / 574 / 401)
- 2026-05-11 · **UPDATE** · `01_product-knowledge/adas-dms-events.md` · Lens Cover 6 月 release 校正
- 2026-05-11 · **UPDATE** · `01_product-knowledge/machines-spec.md` · 加 K265 LM 版 SD update 架構限制段
- 2026-05-11 · **UPDATE** · `02_organization-map/stakeholders.md` · 加 Steve KPI / Stark Honeywell / Phil Soung / Vinicius / Webfleet+Bridgestone+Azuga / Honeywell ME
- 2026-05-11 · **UPDATE** · `03_systems-architecture/plan-types.md` · 加 Plan Type ↔ ADAS/DMS 啟用 / Contract Fleet / Honeywell 驗證三段
- 2026-05-11 · **NEW**    · `case-learning/honeywell-me-cdr-opportunity.md` · Honeywell ME CDR 新案
- 2026-05-11 · **UPDATE** · `case-learning/vinicius-platform-science.md` · 加 § 11 Live View P2P / JS lib / camera-side video without download
- 2026-05-11 · **NEW**    · `weekly-summary/2026-05-11_week-of-may-8.md` · 第一份 weekly summary template v1 → v2

## 2026-05-08

- 2026-05-08 · **NEW**    · `meetings/2026-05-08_syncup-cary-elvis_meeting-record.md` · 5/8 Sync up Kenny / Cary / Elvis(21 min)
- 2026-05-08 · **UPDATE** · `06_calibration-log/critical-facts-log.md` · 加 K165 真實存在校正 + Master Portal Blurring path v1/v2 雙校正

## 2026-05-07

- 2026-05-07 · **NEW**    · `meetings/ai-weekly-internal-roundup.md` · 5/7 AI Weekly 重大訊號(17x 客訴 / LDWS Pending / Lens Cover / Yawning 灰階)
- 2026-05-07 · **NEW**    · `06_calibration-log/cary-passenger-blurring-2026-05-07.md` → 2026-05-11 已 archive
- 2026-05-07 · **NEW**    · `06_calibration-log/ai-team-row-by-row-status-2026-05-07.md` → 2026-05-11 已 archive
- 2026-05-07 · **NEW**    · `06_calibration-log/ai-tab-jira-alignment-2026-05-07.md` → 2026-05-11 已 archive

## 2026-05-06

- 2026-05-06 · **NEW**    · `meetings/2026-05-06_q2-request-review_meeting-record.md` · Brian Q2 review 戰略翻案
- 2026-05-06 · **UPDATE** · `06_calibration-log/roadmap-vs-internal.md` · Yawning / Smoking / VLM / Eating drift table
- 2026-05-06 · **UPDATE** · `06_calibration-log/sheet-jira-mismatches.md` · 5/5 + 5/6 sweep 結果

## 2026-05-05

- 2026-05-05 · **INIT**   · 初版 knowledge 結構建立(6 大分類 43 docs)

---

## Action / 約定

| Action | 何時用 |
|--------|--------|
| **NEW**    | 新增檔案 |
| **UPDATE** | 既有檔加內容 |
| **MOVE**   | 移動位置(含 archive) |
| **DELETE** | 刪除檔案(罕用,通常 archive) |
| **STRUCT** | 結構性改動(資料夾、命名 convention) |
| **MERGE**  | 合併 2 個檔成 1 個 |

> 規則:**每次 Claude / Kenny 編輯 knowledge / case-learning / weekly-summary 任何檔,在本檔最上面加一行**。
