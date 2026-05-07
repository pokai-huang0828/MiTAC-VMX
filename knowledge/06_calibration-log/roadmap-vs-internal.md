# Roadmap vs 內部現實 不一致紀錄

> 對外 Roadmap 講的 ≠ 內部 Sheet / Jira / 會議揭露的。
> 這份的目的:**對客戶講話前先 cross-check**,別重蹈覆轍。

## 已知不一致(2026-05-07 更新)

### Yawning Detection
| 角度 | 內容 |
|------|------|
| Roadmap 對外版 | Basic tier(2025 Expansion)= 已 ship |
| 會議揭露(2026-05-06) | 還沒給客戶,內部測試中,**效果不如預期** |
| 5/7 AI weekly 補 | 夜間嘴部辨識效果不佳,加入「灰階(Grayscale)」模型重訓,並考慮 Server 端從辨識嘴巴改為「辨識整張臉」|
| Fatigue config | 目前只有眼睛偵測,**Yawning 開關待加 → 對應 VMX-7432**(Lucy 5/6 開)|
| Jira tickets | **VMX-7432**(Yawning UI toggle, Lucy assignee)⚠️ VMX-7309 是 Eye threshold 不是 Yawning |
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
| 5/6 會議 | 提早 feasibility(or 早於 Roadmap)|
| **5/7 AI weekly 揭露** | 🚨 **客訴重災區 — BMS 端誤判量是過去 17 倍**(客訴 ID 6652)。團隊 6/15 前一次性 7000+ Edge case 重訓。Jimmy + Vincent 共扛 |
| **對客戶口徑** | ✅ 「2027 Roadmap 規劃」對外不變,內部 6/15 前緊急重訓 |

### Burning ADAS / Burning DMS → 實為 Blurring function(2026-05-07 校正)
| 角度 | 內容 |
|------|------|
| Roadmap Slide 2 | 寫成 Burning ADAS / Burning DMS(typo) |
| KB | 沒寫 |
| 真實意義 | ✅ **Blurring function** — 影像 / 隱私模糊化 |
| **對客戶口徑** | 「對應 server-side 影像模糊化(隱私 / 合規場景)」|

### Server AI Stages 進度(5/7 修正)
| 階段 | Roadmap | 內部進度 | 對客戶口徑 |
|------|---------|-------------------|-----------|
| Stage 1 Edge AI | 已上 | ✅ 已上 | 可講 |
| Stage 2 Edge + Server AI | 已上 | ✅ **Server-side LDWS(VMX-6722)Q1 已 deploy prod**(jimmy 3/11 確認)。⚠️ Device-side YOLO Lane Detection 改善 5/7 決議 Pending 暫緩(資源緊繃,新 ticket 編號待釐清)| 「Server-side LDWS 已部屬,device 端持續改善中」 |
| Stage 3 Edge + Server VLM | 對外規劃 | 沒人扛(VLM sheet #27 = pending pending pending)| 講「Roadmap 中」(對外 2027) |
| Stage 4 Edge VLM | 終局 | 沒動工 | 講「終局視野」 |

## 規則

跟客戶 / 主管講之前:
1. 對 product spec 詢問 → 看 [01_product-knowledge/kb-cheatsheet.md](../01_product-knowledge/kb-cheatsheet.md) + 本檔
2. 對時程詢問 → 對外用 Roadmap(本檔最後一欄「對客戶口徑」)
3. 對技術細節 → 用 KB + 標 ⚠️ 估計

## 更新頻率

每月做一次跨 KB / Sheet / Jira / Roadmap cross-check,把新出現的不一致記到本檔。
