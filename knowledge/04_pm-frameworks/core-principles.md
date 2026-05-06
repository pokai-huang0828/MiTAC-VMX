# 4 條核心 PM 原則

> Kenny 自萃取自 Platform Science / CONNECTSOURCE 兩案

## 🔍 1. 讀懂需求背後的動機

- Wendy 說「功能何時出」→ 真正在意「我在客戶面前的可信度」
- Vinicius 說「需要 SDK 文件」→ 真正在測「MiTAC 值不值得深度合作」

**回應動機,不只回應表面問題**。

## 🔄 2. 你的工作是「讓事情不卡住」

具體空白地帶(全部該 PM 主動介入):

### 真實的 PM 介入空間(2026-05-06 後校正)

| 空白地帶 | 為什麼是真機會 | 切入點 |
|---------|--------------|-------|
| **#154 Label 管理 process gap** | Brian 自評 filter 漏 pick | 提 Q2 merge label sweep |
| **Sheet ↔ Jira 雙向同步缺口** | 兩個方向都有 mismatch | 每兩週 sweep |
| **K265 白名單沒 owner** | Vinicius 案卡點 | 推 owner |
| **Passenger Blurring 可行性沒結論** | CONNECTSOURCE 案 | 推結論 + Roadmap 對齊 |
| **路線圖會議沒人約** | Wendy 案 | 主動發起季度 roadmap sync |
| **「任務完成主動通知」UI 機制缺** | 模糊功能 / Demand request | 跟 Lucy 提 |

⚠️ **不要扛 AI sheet hidden row**(那是團隊已決定不做,2026-05-05 校正)。

## 💬 3. PM 是「商業翻譯」

- 技術成本 → 業務語言
  - 例:**$700/月 AWS 成本** 對工程師是基礎設施,對業務是定價變數,對 PM 是要翻譯清楚的橋樑
  - 例:200 Hz G-Sensor 韌體可行性 → 對 Sales 可講「客戶 must-have, 工程在做韌體 study」
- 業務機會 → 產品優先順序的依據
  - 例:HDFE UI 抱怨 → 不只是「個別客戶問題」, 是「未來重大變更要做 beta 模式」的機會

## 📅 4. 每次互動要有明確的 Next Step + Owner + Timeline

不能停在「我們再看看」或「到時候再說」。

### Template
> 「下一步:[行動] / 由 [人] / 在 [時間前] 完成。我會在 [check-in 時間點] 跟你 sync 進度。」

### 例
- ❌「Yawning 的事情我們再討論」
- ✅「Yawning user TR 開放 / Jieli + Lucy 協作 UI / 兩週內。我下週四 sync 你 user TR 結果。」
