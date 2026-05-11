# 00 · Index 索引層

> 這層的存在是為了讓 Kenny / 接手 Claude **第一眼就知道資訊在哪裡**,而不用爬 6 個資料夾找。

## 三個檔案,各管一件事

| 檔 | 用途 | 何時更新 |
|----|------|---------|
| [`changelog.md`](changelog.md) | **時序動線** — 近 30 天 knowledge / case-learning / weekly-summary 有什麼變動 | 每次 Claude 編輯文件時順手加一行 |
| [`ssot-map.md`](ssot-map.md) | **概念索引** — 「Lens Cover release 時程」這種事實的 SSOT 在哪個檔 | 新增 SSOT 概念時加 |
| `README.md`(本檔) | 索引層說明 | 結構變動時 |

## Knowledge 三層模型

```
┌─────────────────────────────────────────────────────┐
│  L1 · 時序層(weekly cadence,會 stale)            │
│      weekly-summary/  +  archive/                   │
├─────────────────────────────────────────────────────┤
│  L2 · 持續校正層(monthly cadence,事實表)         │
│      06_truth-tables/                               │
├─────────────────────────────────────────────────────┤
│  L3 · 穩定知識層(quarterly cadence,基礎事實)     │
│      01_product/ 02_org/ 03_systems/                │
│      04_pm-frameworks/ 05_workflows/                │
└─────────────────────────────────────────────────────┘
```

### Cadence 規則
- **L1(weekly)**:每週一上工前更新一份 weekly summary。stale 的 dated snapshot 搬 archive/
- **L2(monthly / event-driven)**:Critical fact / roadmap drift / sheet-jira mismatch 校正時更新
- **L3(quarterly)**:產品 spec / 組織 / 系統架構變動時更新(基本上不太動)

## 三條更新黃金規則

1. **SSOT only**:每個事實只在 master 檔詳寫,其他地方只引用 + link
2. **每次更新事實順手加 changelog 一行**(讓未來 Claude / Kenny 看得到變動)
3. **舊版本不留,直接刪 / 搬 archive**(別累積過時版本)

詳細工作流見 [`05_workflows/data-ingestion-workflow.md`](../05_workflows/data-ingestion-workflow.md)。
