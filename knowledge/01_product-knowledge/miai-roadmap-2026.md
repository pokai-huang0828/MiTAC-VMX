# MiAI Roadmap 2026-04-24

> 來源:`../../MiAI Roadmap Introduce 2026024.pptx`(7 張)
> ⚠️ 這是**對外版本**(三層真相中的「對外故事」層)

## Tier × Year × Chip × TOPs ⭐(關鍵 timeline)

| Tier | Year | Theme | Chip | AI Compute |
|------|------|-------|------|-----------|
| **Entry** | 2023 | Foundation | Snapdragon 450 | < 1 TOPs |
| **Basic** | 2025 | Expansion | QCS 6125 / QCS 610 | 1 TOPs |
| **Advanced** | 1H'2027 | Advanced | QCS 5430 | 6 TOPs |
| **Premium** | 2H'2027 | Intelligence | QCS 6490 | 12 TOPs |

⚠️ **2026 是過渡期** — Advanced / Premium 都是 2027 計畫,目前 production 是 Basic tier。Sales 講 6 TOPs / 12 TOPs 功能要小心。

## AI Model 細節

| Tier | Detector | Classifier | Pose Est. | Total |
|------|----------|-----------|-----------|-------|
| Entry | YOLOv5n (~1.9M) | CustomCNNv1 (~1M) | PFLDNet (~2-3M) | ~5M |
| Basic | YOLOv8s (~11M) | CustomCNNv2 (~2M) | WHENetPose (~8M) | ~21M |
| Advanced | YOLOv11m (~20M) | CustomCNNv3 (~10M) | HRNetPose (~35M) | ~65M |
| Premium | YOLOv26l (~50M) | Transformer (~25M) | + Lightweight VLM (~125M) | ~200M |

PM lens:跟客戶講「為什麼某機種做不到 X」直接用 model size + TOPs 解釋。

## AI Architecture Evolution(Server AI 階段)

| 階段 | 架構 | Strengths |
|------|------|-----------|
| 1 | **Edge AI**(目前主流) | Real-time / Low latency / Offline / Privacy |
| 2 | **Edge AI + Server AI** | 二次驗證,降 FP / 借 server 算力 |
| 3 | **Edge AI + Server VLM** | 全影片語意理解 / 處理複雜混合行為 |
| 4 | **Edge VLM**(終局) | Real-time semantic on-device / 不依賴網路 |

→ **Expected Overall Accuracy Improvement: 20% ~ 40%**(視場景)

## ⚠️ Roadmap vs Sheet 衝突(對外 vs 內部)

| 主題 | Roadmap(對外) | Sheet(內部) | 對客戶口徑 |
|------|---------------|-------------|----------|
| VLM | 2H'2027 | 2026 Q3 | **講 2027** |
| Eating & Drinking | 1H'2027 | [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562) / 🚨 **5/7 揭露 BMS 客訴 17x 量級(ID 6652),6/15 前 7000+ Edge case 一次性重訓**(Jimmy + Vincent)| 對外維持 2027,**對 BMS 講 6/15 內部緊急重訓** |
| Yawning | Basic 2025 已 ship | 還沒給客戶 / 測試中 / 5/7 加灰階模型 → **5/11 校正**:用 **Model 11P**(嘴部→全臉)+ 統一到 **Model 26** 架構 / UI toggle = [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(Lucy)/ **掛 6/2 Fix Version** | **改:Roadmap planned, 內部測試中,Model 11P 改全臉打哈欠** |
| Smoking | Basic 2025 已 ship | **KB 標 (in development)** / Sheet 隱藏 / 4 ticket open | **改:Roadmap planned, KB 列開發中** |
| MMF | (列在 overview) | 還沒上線 | **不對客戶承諾** |
| Server-side LDWS(Stage 2) | 已上 | ✅ Q1 Cabinet APP merged,3/11 deploy prod(jimmy 確認)/ **5/11 校正**:LDWS API 從 5/7 Pending 暫緩 → **5/11 重新掛 6/2 Fix Version**([VMX-7101](https://jira.navman.co.nz/jira/browse/VMX-7101) "LDWS Improving (Server)" 待 Jira transition · 2026-05-14 校正:原誤寫 VMX-7375)| 「Server-side 已部屬,device 端 6/2 release 含 LDWS API」 |
| Speed Sign | Advanced 2027 | KB 標 in development / **5/7 揭露 18/25/40 易混淆,Flip 參數關閉 + 擴增降至 10x 重訓**(Jay)| 對外保持 2027 Roadmap |
| Lens Cover(BMS / Azuga ~~雙軌~~ → **5/11 校正單軌**)| Basic | 5/7 雙軌實作 → ⚠️ **5/11 校正**:[HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) 規格改為單軌即可滿足三客戶(Webfleet / Bridgestone / Azuga),取消 speed ≥ 20 + DMS calibration 兩個 dependency / Eric H 5/8 confirmed **6 月 release**(6/2 Fix Version)| 對三客戶講「6/2 release 統一單軌規格」 |

## AI Model 版本對應(2026-05-12 從 5/11 AI Weekly NotebookLM 錄音校正)

> SSOT 詳細在 [`06_calibration-log/critical-facts-log.md` § AI Model 版本對應 + 6/2 Fix Version 死線](../06_calibration-log/critical-facts-log.md)。

| Model | 用途 | 狀態 | 對應 ticket / 客戶 |
|-------|------|------|------------------|
| **11P** | 原:嘴部 (Mouth) 分類 → **改為:全臉 (Full Face) 打哈欠 (Yawning) 辨識** | 修改中,掛 6/2 Fix Version | Yawning UI toggle = [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432) (Lucy) |
| **11L** | 舊版 DMS(含安全帶)分類 | **將被 Model 26 取代** | — |
| **26** | 新導入 DMS 分類 + Detect 模型架構,**準確度優於 11L** | 預計掛 **6/2 Fix Version** 上線 | Yawning + 安全帶 + Distraction 統一架構 |
| **V14** | 影像模糊化 (Blurring) 舊模型版本 | 對外維持「2026-05-06 已 fix」口徑 | [HAWK-527](https://jira.navman.co.nz/jira/browse/HAWK-527) / [HAWK-578](https://jira.navman.co.nz/jira/browse/HAWK-578) Blurring 修問題 |

### 🚨 6/2 Fix Version(2026-06-02)五大必上 deliverable
> 2026-05-14 校正(從 [5/13 Azuga AI Weekly](../../meetings/2026-05-13_azuga-ai-weekly.md) 揭露):從原本三大擴大為五大。
1. **LDWS API** [VMX-7101](https://jira.navman.co.nz/jira/browse/VMX-7101)(5/7 暫緩,5/11 AI Weekly 重新掛 6/2)— Jira fixVersion 仍空
2. **Lens Cover 解耦** [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) + [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585)(5/13 新)— 移除車速 + 獨立 DMS 校正 + 修 debounce + Lens Uncovered event
3. **新版 DMS 模型(Model 26)**
4. **Eye Stable Rate threshold 開放** [VMX-7309](https://jira.navman.co.nz/jira/browse/VMX-7309) + [HAWK-551](https://jira.navman.co.nz/jira/browse/HAWK-551)(5/13 補)
5. **Camera Auto-Height 新演算法** [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501)(5/13 補,Webfleet 拒絕改手動)

### 5/15 Beta 測試前置:外部 API / 模組必須 ready

## Data Auto-Optimization Pipeline(月節奏)

```
Collect → Filter → Label → Train → Validate → Deploy → ...
```

每月一輪。PM lens:跟客戶講「持續優化」有具體 cadence 可提。

⚠️ AI Sheet 上 row 41「Monthly Model Optimization & Release Workflow」**已隱藏 = 不在使用**(2026-05-05 確認)。Roadmap 講有,實際內部沒人扛這個 process — **PM 可推進的真空白地帶之一**。
