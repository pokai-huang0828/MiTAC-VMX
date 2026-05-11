# Data Ingestion Workflow · 給 Kenny 資料 → Claude 整理進 .md → 更新 HTML

> 2026-05-11 起 Kenny 與 Claude 的核心工作流。
>
> **核心邏輯**:User 給 raw data → Claude 分類進對的 .md → 順手刪舊版本 → 更新對應 HTML doc card。
> 全 static · 無 build script · 直接編輯 HTML 反映變動。

---

## A. 工作流總圖

```
┌─────────────────────────────────────────────────────────────┐
│  Kenny 提供 raw data                                         │
│  (Outlook / Teams 截圖 / Jira ticket / 會議筆記 / KB 截圖)  │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 1 · Claude 分類:這是 L1 / L2 / L3?                   │
└─────────────────────────────────────────────────────────────┘
                            ↓
                ┌───────────┴───────────┐
                ↓                       ↓
       ┌──────────────┐        ┌──────────────┐
       │ L1 時序層    │        │ L2 校正層    │
       │ weekly /     │        │ truth-tables │
       │ archive /    │        │ critical-    │
       │ meetings     │        │ facts 等     │
       └──────┬───────┘        └──────┬───────┘
              │                       ↓
              │              ┌──────────────┐
              │              │ L3 知識層    │
              │              │ 01 ~ 05      │
              │              │ (有對應就改) │
              │              └──────┬───────┘
              ↓                     ↓
       ┌─────────────────────────────────────┐
       │  Step 2 · 刪 / archive 舊版本       │
       │  - 同事實的舊 dated snapshot 搬     │
       │    knowledge/archive/               │
       │  - 同事實的舊段落直接刪除           │
       └─────────────────────────────────────┘
                            ↓
       ┌─────────────────────────────────────┐
       │  Step 3 · 更新 SSOT 鏈              │
       │  - SSOT master 加新事實             │
       │  - 引用處只改 link / 一句話摘要     │
       └─────────────────────────────────────┘
                            ↓
       ┌─────────────────────────────────────┐
       │  Step 4 · 更新 HTML 入口            │
       │  - websiteview/knowledge.html       │
       │  - websiteview/case-hub.html        │
       │  - websiteview/index.html(若是 P0) │
       └─────────────────────────────────────┘
                            ↓
       ┌─────────────────────────────────────┐
       │  Step 5 · changelog.md 加一行       │
       └─────────────────────────────────────┘
```

---

## B. 分類決策樹

「Kenny 給了我這份 data,該放哪裡?」

### B1. 客戶 / 案件相關?
- 有具體客戶 / 公司名 / 案件背景 → **`case-learning/<case-name>.md`**
  - 新案 = 新建檔 / 既有案 = 對應檔加段
  - 命名 convention:`<lowercase-case-name>.md`(例:`honeywell-me-cdr-opportunity.md`)
- 同時影響多家客戶 / pattern 性質 → 抽出框架進 `04_pm-frameworks/`

### B2. 會議 / 即時事件?
- 1-on-1 / 週會 / 客戶 Teams call → **`meetings/YYYY-MM-DD_<topic>.md`**
- 已校正的結論若是「以後也適用」→ **同時** 抽進 `06_calibration-log/critical-facts-log.md`

### B3. 對外口徑變動?
- 「對客戶這樣講」vs「內部真相」之間有差距 → **`06_calibration-log/roadmap-vs-internal.md`** 加 row
- 對客戶口徑 / 規格細節 → **`01_product/sales-faq.md`** 或對應 spec 檔

### B4. 產品事實 / KB 更新?
- KB 上看到新東西 → 對應 `01_product/` 下檔加段
- 機種 spec / 限制 → `01_product/machines-spec.md`
- 事件 / config 行為 → `01_product/adas-dms-events.md`

### B5. 組織 / 人事變動?
- 新對接人 / 新角色 → **`02_organization-map/stakeholders.md`**
- 想問特定人的問題 → **`02_organization-map/coffee-chat-questions.md`**

### B6. Sheet × Jira mismatch?
- 出現新一輪不一致 → **`06_calibration-log/sheet-jira-mismatches.md`** 加 table row

### B7. 流程 / SOP?
- 「以後重複做 X 用這個流程」→ **`05_workflows/` 新檔或對應檔加段**

### B8. 校正歷史(別再答錯)?
- 「Claude 之前答錯 X,正確是 Y」→ **`06_calibration-log/critical-facts-log.md`**

### B9. 本週狀態總攬?
- 上週發生的事件 + Jira pending + Δ 對齊 → **`weekly-summary/YYYY-MM-DD_week-of-XXX.md`**

---

## C. SSOT 規則(關鍵)

### C1. 識別 SSOT
- 改一個事實前先查 [`00_index/ssot-map.md`](../00_index/ssot-map.md) 確認主檔位置
- 例如「Lens Cover 6 月 release」master 在 `critical-facts-log.md`,**不是** `adas-dms-events.md`

### C2. 改 SSOT 後怎麼處理引用處
| 引用處的內容 | 該怎麼做 |
|------------|---------|
| 完整描述 | ❌ 不要 — 改成一句話摘要 + link 回 SSOT |
| 一句話摘要 | ✅ 保留,確認摘要還對得起 SSOT 最新版 |
| 早已不正確的內容 | 刪掉 |

### C3. 建新 SSOT 時
1. 在 `00_index/ssot-map.md` 對應分類加一行(概念 / 主檔 / 引用處)
2. 在 changelog.md 加 `STRUCT · ssot-map · 加 <X> SSOT` 一行

---

## D. 舊資料清理 SOP(保持資料潔淨)

### D1. 何時把檔搬 `knowledge/archive/`
- 檔名帶日期(`YYYY-MM-DD`)的 snapshot,內容**已被新檔取代** → 搬
- 同主題有新檔/週報出現後,舊檔超過 30 天 → 搬
- 命名:`YYYY-MM-DD_<topic>.md`(把日期前綴標準化)

### D2. 何時直接刪某段
- SSOT 主檔重寫某個事實時,舊版本直接砍(別留「v1 過時, v2 是新的」這種疊版本)
- 若需要保留 history,改用 `~~strike-through~~` 或 commit history

### D3. 何時刪整個檔
- 內容已完全併入別檔且沒人引用 → 確認沒 link 後刪
- 在 changelog.md 加 `DELETE` 紀錄

### D4. 防呆 checklist
改完事實後檢查:
- [ ] SSOT 主檔有改
- [ ] 其他引用處的摘要還對嗎?(grep 一下事實關鍵字)
- [ ] 舊版本砍掉了嗎?
- [ ] changelog 加了嗎?
- [ ] HTML doc card 還對嗎?(`knowledge.html` / `case-hub.html`)

---

## E. HTML 更新 SOP

### E1. 新增一份 .md 文件
**動 `websiteview/knowledge.html`**:在對應 `<section class="cat">` 內加 doc card:
```html
<a class="doc-card" href="../knowledge/<cat>/<file>.md"
   data-title="標題" data-file="<file>.md" data-tags="關鍵字">
  <div class="doc-title">中文 / 英文標題</div>
  <div class="doc-file"><file>.md</div>
  <div class="doc-foot"><span class="stars">★★★★☆</span></div>
</a>
```
分類 doc 數記得改頂上 `<span class="num">X</span>`。

### E2. 新增一份 case-learning
**動 `websiteview/case-hub.html`**:加 tab + 對應 sidebar + page section(參考 honeywell page 結構)。

### E3. 新增一份 weekly-summary
**動 `websiteview/index.html`** 的 NOW zone — 把 featured card 換成最新 weekly summary。

### E4. 主要事實大變動(critical-facts 加新校正)
**動 `websiteview/index.html`** 的 Critical Facts mini card 的描述。

---

## F. Claude 工作的標準回應模板

當 user 給 raw data,Claude 應該:

1. **辨識 Step 1**:回 user「這份資料 = L1/L2/L3 X 類型,應該放 <檔>」
2. **執行 Step 2-4**:寫進 .md / 刪舊 / 更新 HTML doc card / changelog
3. **回報結構性變動**:列出所有改動的檔(透明 diff)

範例 prompt(user):
> 「我剛開完跟 Brian 的 1-on-1,他說 K265 的 LM 版要 6 月才有 VMX 版可賣」

範例 Claude 回應:
> 這是「產品事實 + 校正」雙重性質。
> 1. `01_product-knowledge/machines-spec.md` § K265 SD update 段加「6 月才有 VMX 版」
> 2. `06_calibration-log/critical-facts-log.md` 加新校正條
> 3. `case-learning/honeywell-me-cdr-opportunity.md` 風險點段 update(影響 5 月 6K 出貨)
> 4. `case-learning/vinicius-platform-science.md` § 11 update sample 採購策略
> 5. changelog.md 加 4 行
> 6. `websiteview/knowledge.html` machines-spec card 的 doc-foot 不動(內容變但不影響卡片元素)

---

## G. 常見錯誤(避免)

| ❌ 錯誤 | ✅ 正確 |
|--------|-------|
| 同事實寫進 3 個檔當保險 | SSOT 寫一次,其他地方 link |
| 舊版本留著「以防萬一」 | 直接刪,git history 已備份 |
| 改完不更 HTML card | 一定要同步 doc card 文字 |
| 改完不更 changelog | 每次必加 |
| 帶日期的 snapshot 一直留在主層 | 30 天後搬 archive |

---

_Last updated: 2026-05-11 — 初版。配合 00_index/ + archive/ 的新 IA。_
