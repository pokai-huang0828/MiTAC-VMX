# Archive · 已被取代的時序 snapshot

> **這個資料夾收的是**:過去某天為了 1-on-1 / 會議 / 信件 quick reference 而做的 **point-in-time snapshot**,後續被更新的 weekly summary 或 truth table 取代後搬進來保存,**不再每週 maintain**。

## 為什麼保留而不刪除

- 仍有歷史價值(可以查「Kenny 5/7 跟 Brian 講了什麼」)
- 內含當時的 reasoning 過程,不只結論
- 重要結論已遷移到永久檔(`06_truth-tables/critical-facts.md` / `weekly-summary/`)

## 命名 convention

```
YYYY-MM-DD_<topic>.md     ← 帶日期 = 時序 snapshot,只反映那天的狀態
```

## 已歸檔清單

| 檔案 | 原位置 | 取代它的永久檔 |
|------|------|--------------|
| `2026-05-07_ai-tab-jira-alignment.md` | `06_calibration-log/` | `06_truth-tables/sheet-jira-mismatches.md` H 段 + `weekly-summary/2026-05-11_*.md` |
| `2026-05-07_ai-team-row-by-row-status.md` | `06_calibration-log/` | 每週 weekly summary 取代(改成週更新) |
| `2026-05-07_cary-passenger-blurring.md` | `06_calibration-log/` | `06_truth-tables/critical-facts.md`(Lens Cover 6 月 release 結論)+ `case-learning/connectsource-passenger-blurring.md`(主案) |

## 何時搬東西進來

當以下任一條件成立時,把 `06_truth-tables/` 或其他活躍區的 dated snapshot 移到這裡:
1. 內容已被新 weekly summary 完整取代
2. 內容已被永久檔(critical-facts / roadmap-vs-internal)摘錄結論
3. 距今超過 30 天且沒被引用
