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
| Eating & Drinking | 1H'2027 | HAWK-562 已動 | 講 2027 |
| Yawning | Basic 2025 已 ship | 還沒給客戶 / 測試中 | **改:Roadmap planned, 內部測試中** |
| Smoking | Basic 2025 已 ship | KB 沒寫 / Sheet 隱藏 / 4 ticket open | **改:Roadmap planned, 內部開發中** |
| MMF | (列在 overview) | 還沒上線 | **不對客戶承諾** |

## Data Auto-Optimization Pipeline(月節奏)

```
Collect → Filter → Label → Train → Validate → Deploy → ...
```

每月一輪。PM lens:跟客戶講「持續優化」有具體 cadence 可提。

⚠️ AI Sheet 上 row 41「Monthly Model Optimization & Release Workflow」**已隱藏 = 不在使用**(2026-05-05 確認)。Roadmap 講有,實際內部沒人扛這個 process — **PM 可推進的真空白地帶之一**。
