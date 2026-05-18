# 2026-05-13 · BMS AI Weekly Meeting — Brian email summary(NotebookLM 生成)

> **來源**:brian.chienlee 5/13 18:08 寄出 Outlook 信件(主旨 "20260513 BMS AI Weekly Meeting", 標 Meeting Summary + Working + Important)
> **生成**:By NotebookLM(Brian 自註)
> **收件者**:eric.h / vincent.ho / jay.qiu + 6 個
> **CC**:pokai.huang / mori.jhang / spencer.su + 2 個
> **抓取**:2026-05-18 morning sweep(Outlook 上週信件)

---

## 5 議題

### 1. 不同位置 AUX DMS Cam 安裝位置模型訓練 — [HAWK-401](https://jira.navman.co.nz/jira/browse/HAWK-401)

關於針對特定 AUX DMS Cam 安裝角度加強 AI 模型訓練的 Ticket **自 12 月以來未有進展**。MiTAC 目前正在收集不同角度的影像作為訓練準備,但**尚未獲得繼續推進該功能的核准**。

### 2. 鏡頭遮蔽偵測 (Lens Cover Detection)

在 **Webfleet 端的最新韌體**中,鏡頭遮蔽偵測運作不穩定,包含 debounce 失效,**Martin 與 Jacob 無法成功偵測**。

這與先前討論將鏡頭遮蔽與 DMS 未校準邏輯分開的項目有關。MiTAC 確認這與 debounce 時間的問題有關,**預計在 6 月 2 日的新版本中進行修復**。

> 對應 [HAWK-585](https://jira.navman.co.nz/jira/browse/HAWK-585) 'Lens cover' detection not properly working — 5/13 開單,本週 leo.tsai → **vincent.ho** 接手
> 對應 [HAWK-582](https://jira.navman.co.nz/jira/browse/HAWK-582) Improve Lens cover detection — 規格層(jieli.liu / fv=VisionMax_20260602)

### 3. 行人碰撞警示系統 (Pedestrian Collision Warning System)

關於行人碰撞警示系統,Eric 已回覆了所有前期問題,但**在 MiTAC 正式啟動專案前,必須先完成規格確認**。目前的設計為**舊有設計,僅在 Azuga 和 Webfleet 端進行過討論**。

### 4. 攝影機自動高度偵測 (Auto Camera Height Detection Problem) — [HAWK-482](https://jira.navman.co.nz/jira/browse/HAWK-482) / [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501)

- **Eric 曾提議**關閉自動偵測並改用手動設定攝影機高度
- 但 **Martin 與 Sebastian 認為此方案不切實際**:
  - 現有車隊已有數千台設備運行中,改回手動設定會造成龐大的遷移成本
  - 安裝人員無法精準測量卡車內的實際高度
- **Jacob 認為自動校準是產品的一大賣點**,期望能修復自動校準的精準度,而不是依賴車輛類型或手動輸入
- **MiTAC 目前正在開發新演算法以減少誤差**

> 校正:5/14 Azuga AI Weekly 提出「5 大 deliverable」第五項 = Camera Auto-Height 新演算法(Jay 領)。本週 [HAWK-587](https://jira.navman.co.nz/jira/browse/HAWK-587) CALIBRATION COMPLETED notification 從 brian.chienlee → **jay.qiu**,與 HAWK-501 同步推進。

### 5. AI 模型跨版本測試流程與日誌擷取 — [HAWK-482](https://jira.navman.co.nz/jira/browse/HAWK-482)(日誌擷取部分)

為了在未來的 AI 版本(如 v19 比較 v18)中評估改善情況,需要建立資料集。

| 事件類型 | MiTAC 所需資料 |
|---------|--------------|
| **物件偵測**(如手機 / 香菸 / 安全帶) | MiTAC 僅需影片即可用不同模型重播測試 |
| **非物件事件**(如疲勞 / 分心) | 若影片中沒有 debug 畫面,**MiTAC 必須依賴應用程式日誌**(例如:找不到臉孔、眼球穩定率異常)才能進行模型對比 |

**日誌路徑**:雙方確認所需的應用程式日誌指的是內部記憶體根目錄中的 **`/rlogs`** 與 **`/log`** 資料夾。

---

## 待辦事項 (Action Items)

| 負責 | 動作 | 目標 / 時程 |
|------|------|------------|
| **Allen (MiTAC)** | 確認 AI 安裝位置模型訓練需求的優先級 | 需與 Jacob 和 Sirphi 確認優先順序,Sebastian 把工單指派給 Allen |
| **Vincent (MiTAC)** | 修復鏡頭遮蔽偵測的 debounce 時間問題 | 預計 **6/2 下一個版本發布**,並在會後於 ticket 補充原因 (root cause) |
| **Sebastian / Jacob (Webfleet)** | 針對鏡頭遮蔽偵測失效問題,提供相關影片範例與日誌 | 供 MiTAC 分析 |
| **Eric / Jacob / Sirphi** | 針對行人碰撞警示系統,共同 review 並確認規格 | 確認後 MiTAC 才開始開發 |
| **Jay (MiTAC)** | 持續改善自動高度偵測的演算法,以及高度誤差對 ADAS 事件偵測的影響 | 預計在下一個版本中確認結果 |
| **Martin (Webfleet)** | 在 webfleet 內部討論,評估若需固定攝影機高度參數可能帶來的影響與後果 | — |
| **Sebastian (Webfleet)** | 關閉目前關於高度偵測的工單,並建立一個新的後續工單追蹤修復自動校準功能的需求 | — |
| **Martin / 客戶端工程團隊** | 更新內部文件與提報流程:未來在回報「非物件偵測事件(如疲勞)」的 False Negative 時,**必須同時提供影片以及內部記憶體中的 /rlogs 與 /logs 資料夾** | 以便 MiTAC 找出根本原因並建立 AI 對比資料集 |

---

## PM 觀察(Claude 補)

1. **HAWK-401 backlog 已 5 個月** — 影像收集中但未獲核准。要不要在下次 Brian 1on1 提:「這 ticket 從 12 月卡到現在,要不要正式 Defer 而不是持續 New 狀態」
2. **Eric 想關閉自動高度偵測 = 已被 Webfleet 否決** — 後續 Kenny 對外溝通 Camera Height 不能再含混講「考慮改回手動」。**標準口徑 = MiTAC 開發新演算法減少誤差**(對應 5/14 三大 → 五大 deliverable 校正)
3. **AI 跨版本測試的「非物件事件」依賴日誌** — 這是個結構性 friction point。Webfleet 客戶端工程團隊未來回報疲勞 False Negative **強制要求附 /rlogs + /logs**。Kenny 如果遇到 Azuga / PS 客戶報疲勞問題,**第一句話該說「請同時提供 /rlogs 與 /logs 資料夾」**而不是只要 video
4. **行人碰撞警示「規格未鎖」** — Eric / Jacob / Sirphi 三方等規格確認才能開發,**對外溝通不能承諾 timeline**。可以講「設計 review 中,規格確認後 MiTAC 才會開始開發」

---

## 引用對齊

- [`weekly-summary/2026-05-18_week-of-may-18.md`](../weekly-summary/2026-05-18_week-of-may-18.md) — 本週 sync,本檔是 5/13 BMS meeting source
- [`meetings/2026-05-13_azuga-ai-weekly.md`](2026-05-13_azuga-ai-weekly.md) — 同日 Azuga AI Weekly,5 大 deliverable 校正源頭
- [`meetings/ai-weekly-internal-roundup.md`](ai-weekly-internal-roundup.md) — 5/14 內部 AI Weekly,3 大反差(Lens Cover 重構 / Yawning 2000 假圖 / Eating-Drinking 飲水)
- [`knowledge/06_calibration-log/critical-facts-log.md`](../knowledge/06_calibration-log/critical-facts-log.md) § 6/2 五大 deliverable

---

_Last sync: 2026-05-18 · 來源:Brian 5/13 18:08 寄出 Outlook 信(NotebookLM 生成)· 完整逐字稿保留,PM 觀察為 Claude 補_
