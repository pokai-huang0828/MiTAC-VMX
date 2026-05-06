# 重大 UI 變更管理框架

> 源自 2026-05-06 Q2 Review 會議:HDFE 抱怨 + 舊 Playback Sunset Plan

## Brian 引入的 Beta 模式

> 「未來重大變更時可以考慮 BT(beta)期 — 像 AWS、Box、Atlassian 都是先告訴你新介面試用,給你時間,再正式 deprecate。」 — Brian 2026-05-06

## 對應 Kenny 承諾層次框架

| 變更類型 | 承諾風險 | 解法 |
|---------|--------|------|
| 強制日期切換 | 高風險 | 不建議 |
| beta period + 切換按鈕 | 中風險 | ✅ Brian 想引入 |
| 紅色預告 + GA 追蹤 + 漸進式 sunset | 低風險 | ✅ 已在做(舊 Playback) |
| 純資訊更新 | 極低風險 | 任何時期都可 |

## 4 階段標準 Sunset SOP(從舊 Playback 案萃取)

### Stage 1:GA 追蹤期(觀察)
- 埋 GA 看誰在用
- **觀察至少一個月**(時間太短沒意義)
- 不只看 page view,要看 visitor / device / browser

### Stage 2:預告期(資訊更新層)
- 在頁面上加紅色預告 / 驚嘆號
- 寫具體日期(不是「即將不再維護」)
- 範例:「此功能將於 2026-09-30 終止支援」

### Stage 3:Beta period(中風險承諾層)
- 提供「新版 / 舊版切換」按鈕
- 4 個月 grace period(現在 → 9月底)
- 用戶有選擇權

### Stage 4:正式 deprecate(高風險承諾層)
- 跳 alert
- 引導到新介面
- 舊頁面下線

## 已在跑的 Sunset 案例(VMX 內)

| 功能 | 預告日 | 正式下線 | Stage |
|------|-------|---------|-------|
| 舊 Playback 頁面(#135 / #147 / #182 / VMX-7132) | Q2 2026-05 | Q3 2026-09-30 | Stage 2-3 之間 |

## 客戶溝通 template

對抱怨「不習慣」的客戶(像 HDFE):

> ❌ 「新介面比較好,習慣就好了」
>
> ✅ 「我聽到你的 feedback。**這個變更我們確實該提供 transition 期**,我會跟產品確認能否給你切換按鈕。同時你能告訴我哪些操作具體變難嗎?(滑鼠次數 / 找事件 / 篩選)我整理後給 owner」

→ 對應 4 條核心原則:
1. 讀懂動機(他要可信度,不只是 UI)
2. 讓事情不卡住(主動推 toggle 提案)
3. 商業翻譯(把 UX 痛點翻成產品 task)
4. Next Step + Owner + Timeline
