# 事件記錄：CONNECTSOURCE × Passenger Blurring 需求

> 信件主旨：`RE: VMX Roadmap Update and Explanation <PASSENGER BLURRING>`
> 記錄範圍：2026/04 – 2026/05/04
> 記錄人：Pokai Huang (pokai.huang@mitacmdt.com)

---

## 1. 事件背景

澳洲 MiTAC 經銷商（產品品牌名：**CONNECTSOURCE**）接獲一個馬來西亞車隊業者的合作需求。該客戶因當地隱私法規及工會規定，要求在行車記錄器影像中自動模糊乘客臉部，此即 **Passenger Blurring（乘客模糊化）** AI 功能。

Wendy（澳洲業務窗口）向 MiTAC VisionMax 產品端（Brian）反映此需求，並詢問功能上線時程，引發內部關於路線圖透明度、功能開發優先順序與成本分攤的討論。

---

## 2. 主要關係人

| 姓名 | 角色 |
|---|---|
| Wendy | 澳洲 CONNECTSOURCE 業務窗口（MiTAC 經銷商端） |
| Brian Chienlee（李健） | VisionMax 解決方案負責人（MiTAC 產品端） |
| Cary Lo | MiTAC 內部財務/商務分析 |
| Pokai Huang（黃柏凱） | （本人，信件 Cc 串內） |

---

## 3. 商業規模

| 項目 | 數字 |
|---|---|
| 馬來西亞客戶硬體台數 | 1,165 台裝置 |
| 預估連線數 | 1,000 個連線 |
| 合約期限 | 36 個月 |
| 潛在收益（Wendy 估算） | ~$216,000 USD（約 $6/月/連線） |
| Passenger Blurring AWS 額外成本 | $700 USD/月 |
| AWS 成本（36 個月合計） | ~$25,200 USD |
| 淨收益估算（扣除 AWS 成本） | ~$190,800 USD |

> 財務上具備可行性，前提是 $6/月/連線的定價模型已涵蓋 AWS 成本分攤。

---

## 4. 時間軸

### 早期需求提出（2026/04 初）
- Wendy 向 Brian 提出馬來西亞客戶的 Passenger Blurring 需求
- 說明合約規模（1,165 台、1,000 連線、36 個月）以及功能背景（隱私法規與工會要求）

### 2026/04/24 — 財務與功能可行性討論
- **Cary Lo** 提出財務問題：
  - 1,165 台 HW 每月產生約 $1,165 USD 的基礎收益
  - Passenger Blurring AWS 成本 $700/月 是否已計入定價模型？
  - 車隊規模是否符合 Passenger Blurring 功能的適用條件？
- **Brian** 回覆：
  - 確認 AWS 額外成本為 $700/月
  - 說明此功能原為 **BMS 客戶** 開發的原型，整合至 CONNECTSOURCE 環境需要**額外開發工作**，不能直接套用
  - 預計目標時程：**Q2 2026（七月）**

### 2026/05/04 — 路線圖透明度衝突浮上檯面
- **Wendy** 表達對 MiTAC 路線圖缺乏透明度的不滿：
  - 長期沒有召開路線圖同步會議
  - 業務端無法對客戶做出有效承諾
  - 要求 Brian 提供更明確的時程資訊
- **Brian** 回覆：
  - 分享 **AI Feature Roadmap 簡報**：https://docs.google.com/presentation/d/1FIkUrx_-f1ouI3j0Tne7HdjuW1nTgnBST7GvNwcPuo/edit?usp=sharing
  - 分享 **需求管理追蹤表（Google Sheets）**：https://docs.google.com/spreadsheets/d/1DXCf8yU7ZrtzVdMEPSxHgmDb7cPKIFDK/edit?gid=639348744
  - 說明 Passenger Blurring 功能已排入 Q2 2026 路線圖，七月為目標

---

## 5. 衝突核心分析

### 5.1 業務端 vs 產品端的期望落差

| 面向 | Wendy（業務端）的期望 | Brian（產品端）的現實 |
|---|---|---|
| 功能時程 | 盡快上線，可對客戶承諾 | 需額外開發，Q2 2026 / 七月 |
| 功能範圍 | CONNECTSOURCE 可直接使用 | 需針對 CONNECTSOURCE 重新整合 |
| 資訊頻率 | 定期路線圖同步 | 被動回應，沒有主動推播機制 |
| 承諾精度 | 具體日期 | 「Q2 / 七月」（粗粒度） |

### 5.2 根本問題診斷

1. **資訊不對稱是主因**：業務端不知道路線圖，只能被動等待。Wendy 的情緒反應背後是系統性的溝通斷裂，不是個人關係問題。

2. **功能原型 ≠ 可交付功能**：Passenger Blurring 對 BMS 可用，但對 CONNECTSOURCE 需要重新整合。這個差異沒有在早期被清楚傳達，導致業務端誤判功能的就緒程度。

3. **承諾時程粒度不足**：「Q2 2026 / 七月」對業務端太粗，客戶端無法據此規劃。更有效的說法應是：「六月確認可行性、七月開始整合測試、Q3 正式上線」。

4. **成本歸屬未釐清**：$700/月的 AWS 成本是否計入 $6/月/連線的定價？若未涵蓋，CONNECTSOURCE 的報價結構需要重新評估。

---

## 6. 待辦事項（Action Items）

### Brian / VisionMax 產品端
- [ ] 提供 Passenger Blurring 的具體里程碑節點（不只說「七月」），讓業務端可以管理客戶預期
- [ ] 確認 $6/月/連線的定價模型是否已包含 $700/月 AWS 成本分攤
- [ ] 建立定期 roadmap sync 機制（建議每季一次），確保澳洲業務端有常態資訊流

### Wendy / CONNECTSOURCE 業務端
- [ ] 向馬來西亞客戶溝通功能時程：Q2 2026 / 七月為目標，但需等 Brian 提供更細的里程碑確認

### Cary Lo / 商務端
- [ ] 確認 1,165 台裝置是否符合 Passenger Blurring 功能的最小部署規模條件
- [ ] 釐清 AWS 成本分攤是否已反映在 CONNECTSOURCE 現行定價結構中

---

## 7. 參考資料

- AI Feature Roadmap 簡報：https://docs.google.com/presentation/d/1FIkUrx_-f1ouI3j0Tne7HdjuW1nTgnBST7GvNwcPuo/edit?usp=sharing
- 需求管理追蹤表（Google Sheets）：https://docs.google.com/spreadsheets/d/1DXCf8yU7ZrtzVdMEPSxHgmDb7cPKIFDK/edit?gid=639348744

---

## 8. PM 觀察與建議

### 短期（立即可做）
Brian 應在下次回信中把「七月」轉化為可驗證的里程碑：
> 「預計六月底確認整合方案可行性，七月啟動開發，Q3 結束前提供 CONNECTSOURCE 測試版本。任何變動我會提前通知。」

這句話的關鍵不在日期，而在「任何變動我會提前通知」——這才是 Wendy 真正需要的承諾。

### 中期（流程改善）
建立 **VisionMax Roadmap Sync** 定期會議（每季一次），澳洲、台灣業務端與產品端共同參與，輸出一頁簡報說明：
- 已上線功能
- 進行中的功能（含預計里程碑）
- 規劃中但未承諾的功能

### 長期（定價結構）
若 Passenger Blurring 成為標準功能，需在 CONNECTSOURCE 的定價模型中明確將 AWS 成本納入，避免每次都需要個案討論。

---

_Last updated: 2026/05/05 — 初版建立，記錄 2026/04–05 信件串內容。_
