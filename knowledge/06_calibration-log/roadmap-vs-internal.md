# Roadmap vs 內部現實 不一致紀錄

> 對外 Roadmap 講的 ≠ 內部 Sheet / Jira / 會議揭露的。
> 這份的目的:**對客戶講話前先 cross-check**,別重蹈覆轍。

## 已知不一致(2026-05-06 截止)

### Yawning Detection
| 角度 | 內容 |
|------|------|
| Roadmap 對外版 | Basic tier(2025 Expansion)= 已 ship |
| 會議揭露(2026-05-06) | 還沒給客戶,內部測試中,**效果不如預期** |
| Fatigue config | 目前只有眼睛偵測,**Yawning 開關待加** |
| Jira tickets | VMX-7309 / HAWK-332(In Process)|
| **對客戶口徑** | ✅ 「Roadmap planned, 內部測試中」<br>❌ 「已支援 Yawning」 |

### Smoking
| 角度 | 內容 |
|------|------|
| Roadmap 對外版 | Basic tier 2025 = 已 ship |
| KB | 沒寫 |
| AI Sheet | row 隱藏(2026-05-05 確認) |
| Jira | 4 個 open ticket(VMX-6670 / 7324 / 6380 / 6920) |
| 會議 Note(4/2) | 「Edge 70% 準確,正在跟 server YOLO11-L 整合」 |
| **對客戶口徑** | ⚠️ 必問 Jimmy 真實狀態。預設「Roadmap planned, 內部開發中」 |

### MMF (Mobility Map Function)
| 角度 | 內容 |
|------|------|
| Roadmap | Slide 2 列在 overview |
| memory | 還沒上線、測試中 |
| Jira | VMX-6353 / VMX-6925(open) |
| **對客戶口徑** | ❌ **不對任何客戶承諾** |

### VLM(Vision-Language Models)
| 角度 | 內容 |
|------|------|
| Roadmap 對外版 | 2H'2027(Premium tier) |
| AI Sheet 內部 | **2026 Q3** |
| Jira | (No PIC, sheet 標 2026 Q3)|
| Kenny 裁示 | sheet 是內部真相,roadmap 對外 |
| **對客戶口徑** | ✅ 「2H'2027 Roadmap 規劃」 |

### Eating / Drinking
| 角度 | 內容 |
|------|------|
| Roadmap | Advanced tier 1H'2027 |
| AI Sheet | HAWK-562 已開,Jimmy 在動 |
| 會議揭露 | 提早 feasibility(or 早於 Roadmap)|
| **對客戶口徑** | ✅ 「2027 Roadmap 規劃」 |

### Burning ADAS / Burning DMS → 實為 Blurring function(2026-05-07 校正)
| 角度 | 內容 |
|------|------|
| Roadmap Slide 2 | 寫成 Burning ADAS / Burning DMS(typo) |
| KB | 沒寫 |
| 真實意義 | ✅ **Blurring function** — 影像 / 隱私模糊化 |
| **對客戶口徑** | 「對應 server-side 影像模糊化(隱私 / 合規場景)」|

### Server AI Stages 進度
| 階段 | Roadmap | 內部進度(2026-05-06) | 對客戶口徑 |
|------|---------|-------------------|-----------|
| Stage 1 Edge AI | 已上 | ✅ 已上 | 可講 |
| Stage 2 Edge + Server AI | 已上 | 部分 ticket 進行(VMX-6722 LDWS Eric Feasibility / VMX-6703 / 7346) | 有限度講「已開發 server-side validation」 |
| Stage 3 Edge + Server VLM | 對外規劃 | 沒人扛 | 講「Roadmap 中」 |
| Stage 4 Edge VLM | 終局 | 沒動工 | 講「終局視野」 |

## 規則

跟客戶 / 主管講之前:
1. 對 product spec 詢問 → 看 [01_product-knowledge/kb-cheatsheet.md](../01_product-knowledge/kb-cheatsheet.md) + 本檔
2. 對時程詢問 → 對外用 Roadmap(本檔最後一欄「對客戶口徑」)
3. 對技術細節 → 用 KB + 標 ⚠️ 估計

## 更新頻率

每月做一次跨 KB / Sheet / Jira / Roadmap cross-check,把新出現的不一致記到本檔。
