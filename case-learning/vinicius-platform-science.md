# Handover: Platform Science × MiTAC — Vision Max APIs 專案

> 本文件彙整黃柏凱 (pokai.huang@mitacmdt.com) Outlook 收件匣中所有與 **Vinicius Francisquinho** (Platform Science) 相關之信件,時間範圍 **2026/04/16 – 2026/05/04**,主旨皆為 `Re: Vision Max APIs`,標籤 `Working` / `Important!!!`。

---

## 1. 專案背景

Platform Science 為一家位於美國 Minnetonka, MN 的車隊軟體服務商,旗下 Video Safety 解決方案正在評估與 MiTAC AIoTBC (車載/視訊) 攝影機產品線整合。本案以 **VisionMax** 平台 (MiTAC 雲端管理 portal) 與 **MiTAC CDR 系列攝影機** (K220 / K245 / K265 / K425 等) 為核心,目標是讓 Platform Science 透過 SDK / API 取得攝影機資料並做 cloud-to-cloud 整合,亦不排除 OEM image 客製化。

---

## 2. 主要關係人

### Platform Science (客戶端)
| 姓名 | 角色 | Email |
|---|---|---|
| Vinicius Francisquinho | Engineering Director, Video Safety (今年初新任) | vinicius.francisquinho@platformscience.com |
| Vikram Jayaraman | (前期窗口) | vikram.jayaraman@platformscience.com |

地址: 4400 Baker Road, Minnetonka, MN 55343 / M: +1 (612) 250-2664

### MiTAC (供應端)
| 姓名 | 中文 | 角色 |
|---|---|---|
| Stark Yang | 楊永吉 | Director,Video Telematics 團隊負責人 |
| Brian Chienlee | 李健 | VisionMax 解決方案負責人 |
| Conant Ho | 何肇峯 | 技術 PM,主要對外窗口 |
| Paul SP Lee | 李世博 | PS Account Sales |
| Righter Song | 宋祐全 | RD Engineer (AIoTBC RD SW1),韌體/inventory 操作 |
| Pokai Huang | 黃柏凱 | (本人,Cc 串內) |

---

## 3. 時間軸 (Timeline)

### Phase 1 — 初次需求接洽 (4/16 – 4/17)
- **4/16 18:20** Stark 將 Brian 加入串列,並請 Vikram 分享 Platform Science 的 camera project plan & milestone,以提供對應 roadmap。
- **4/17 10:19** Vikram 回覆: 目前主力是對 **K265** 進行 additional validation,希望了解 MiTAC 今年至明年初的 camera roadmap。
- **4/17 11:46** Vikram 補充: 期望項目包含 **multi-channel 支援**、**CAN decoding**、**non-China manufacturing**。
- Stark 回覆: MiTAC 新平台特色為 **AI 算力提升**、**清晰前車車牌擷取**、**5G**、**non-Chinese modem**,符合 PS 期待,並可後續安排 briefing。

### Phase 2 — VisionMax 帳號與設備設定 (4/20 – 4/21)
- **4/20 14:42** Brian 完成設定:
  - 為 Vinicius 建立 VisionMax production 帳號,verification 信已寄至 vinicius.francisquinho@platformscience.com
  - **Master Portal**: https://portal.visionmaxfleet.com/
  - **Fleet Portal**: https://www.visionmaxfleet.com/
  - **API 文件**: https://visionmax.redocly.app/
  - **API KEY**: `tH5YIgS5TjM8pvFIxrIU0WkP-eUZe6YtBO4JQ8MA2dg`
  - 規則: VisionMax 註冊需以裝置 SN,且 SN 必須先加到 backend whitelist 才能加入 master portal inventory。
  - K425 (Lightmetrics version) 刷成 MiTAC 版本: Righter 將提供 SD 卡刷 image 文件;最新版為 **2025 Q4**,**2026 Q1** 測試中,完成後可提供更新。
- **4/21 01:25** Righter 寄附件給 Vikram,說明 device update 方式。
- **4/21 06:31** Vinicius 回覆出差至週四,將於下週五至下週一執行流程。

### Phase 3 — 安排首次正式會議 (4/21 – 4/22)
- **4/22 02:45** Vinicius 主動提案下週開會,自我介紹為今年初新任 Engineering Director,有許多問題想請教 MiTAC。
- **4/22 04:16** Stark 在英國出差,授權 Conant + Brian 找時段對接;Paul 將遠端加入。
- **4/21 23:44** Conant 提議 4/27 ~ 4/30,Taiwan 20:00 (CDT 07:00) 之時段。
- **4/22 09:54** Vinicius 確定 **4/29**。

### Phase 4 — Inventory 加入問題 (4/28)
- **4/28 08:59** Vinicius 回報無法將 K265 加入 VisionMax portal,出現錯誤。
  - K265: IMEI `353995720096134` / SN `L1225380005`
- **4/28 10:31** Vinicius 補上需加入 whitelist 的兩台裝置:
  - K265: IMEI `353995720096134` / SN `L1225380005`
  - K245: IMEI `357216578001266` / SN `F4723090088`
- **4/29 01:58** Righter 確認:兩台裝置皆已加入 inventory。

### Phase 5 — 4/29 會議與後續行動 (4/29)
- **4/29 07:53** Vinicius 「Thanks Righter, I will test these today!」
- **4/29 08:59 (會後)** Vinicius 致謝 Conant、Brian,並提出下一步:
  1. 分享簡報檔
  2. 分享 SDK 文件 (建立自有 camera app 評估用,API 文件已有)
  3. 提供設備報價
  4. 提供下單流程
  - 「There are multiple things I want to try out now and get installed in our test truck.」
- **4/29 08:19** Conant 回覆:附上 CDR roadmap 與 SDK 連結
  - SDK: https://drive.google.com/file/d/121XoPoTtx7R1QBXXzkdovsKMzMm1auN5/view?usp=sharing
- **4/29 09:38** Vinicius 詢問: SDK 是否 K265 / K245 / **Orion K246** 共用?
- **5/3 19:15** Conant 回覆: SDK 對所有 CDR 機型 (K220 Sprint / K245c Gemini SE / K265 EVO) 通用,僅有少數 model-specific API 變異,文件中明示。

### Phase 6 — 週末密集測試 (5/4,最新狀態)
- **5/4 09:30** Vinicius 最新進度回報:
  - 整體測試良好,SDK 完整。
  - **問題: K265 dashcam 仍無法在 VisionMax portal 運作**,推測 K265 image 也有問題,需要 Righter 為 K265 提供 **與 K245 相同的處理流程**。
  - 已用 K245 成功:修改 OEM image、替換錄影 app 為自家 app、傳輸至自有 server。
  - 但初期實作仍希望透過 VisionMax 進行 **cloud-to-cloud 整合**,而非走 OEM image 路線。
  - 再次催促 **設備報價**,以利完整方案驗證。

### Phase 7 — JS Live View lib 交付 + ADAS Failure 撞線(5/11 – 5/14)
- **5/11 02:31** Kenny 交付 **JS Live View lib V1.0.4**(`https://www.visionmaxfleet.com/lib/vmRTC/1.0.4/...`)
- **5/11 22:03** Vinicius 回覆「Thanks, I will start running some tests with it」 — ✅ V1.0.4 testing loop close
- **5/12 10:08** Righter 通知 Vinicius:K265 OTA profile 已設好(配 [VMX-7287](https://jira.navman.co.nz/jira/browse/VMX-7287) K265 2026Q1 region build Resolved)
- **5/13 06:2X** Vinicius 回報:
  - ✅ OTA + SDK Live Stream 都正常運作
  - 🚨 **新問題:ADAS Failure**(portal 訊息「ADAS could not be calibrated. Please inspect camera lens's mounting status...」)
  - 嘗試 reboot device 無效
  - 推測的 SN:**K265 L1225380005**(從 portal screenshot 判斷,待確認)
- **5/13 11:41** Righter reply:
  - 解釋 ADAS 必須等 calibration 完成才會啟動
  - 給安裝指引(附綠框 horizon alignment 圖)
  - 行駛條件:**≥ 30 km/h on roads with clear lane markings**
- **5/13 下午** Kenny PM 判斷:
  - Righter 已答核心問題,Kenny **不另回 thread**,避免 PM 補刀 RD
  - CC 持續監看 Vinicius follow-up
  - 內部 cross-link 此事件到 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 同根因 thread(評估期 cross-customer 證據)

- **5/14 12:17** Vinicius reply Righter:**「Thanks Righter. I will do that!」** — ✅ 接受 install + 30 km/h SOP,實測 loop 開啟
  - CC: alicia / conant / stark + 3 個 PS 內部
  - PM 處理:Kenny 仍不介入 thread,等 Vinicius 實測完回報

**🎯 評估期 PM 重點**:Platform Science 撞 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 根因 = **跨客戶證據鏈**現第四條(Kenny 自測 + Webfleet [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) + PS + **🆕 MiTAC 自測 [VMX-7470](https://jira.navman.co.nz/jira/browse/VMX-7470)**)。jay.qiu 5/15 confirm [VMX-7470](https://jira.navman.co.nz/jira/browse/VMX-7470) ANR crash root cause = HAWK-574 同(Race Condition + Dangling Pointer + Memory Corruption),fix 在 MiAIServiceApp 1.4.43.3 + SdkMiAIService 1.4.44。詳見 [vmx-7404-tracking.md](../knowledge/06_calibration-log/vmx-7404-tracking.md)。
- **待動作**:等 Vinicius 5/18-22 實測完 install + drive 後是否仍有 ADAS Failure。若仍 fail,**升級成 Jira ticket Kenny 領 root cause** — 評估期重大 PM 表現機會

---

## 4. 技術資訊速查

### 相關產品線 (MiTAC CDR)
- **K220** (Sprint)
- **K245 / K245c** (Gemini SE) — 已成功修改 OEM image 與錄影 app
- **K246** (Orion) — Vinicius 詢問是否同 SDK
- **K265** (EVO) — Platform Science 主驗證對象,目前 portal 註冊與 image 仍卡關
- **K425** (Lightmetrics → MiTAC 版本可刷),最新 2025 Q4,2026 Q1 測試中

### 服務與工具
- Master Portal: https://portal.visionmaxfleet.com/
- Fleet Portal: https://www.visionmaxfleet.com/
- API Docs: https://visionmax.redocly.app/
- SDK (Google Drive): 連結同上 Phase 5

### 已加入 inventory 的測試裝置
| 機種 | IMEI | SN |
|---|---|---|
| K265 | 353995720096134 | L1225380005 |
| K245 | 357216578001266 | F4723090088 |

> 註:這些是客戶端裝置識別碼,屬商業敏感資訊,共用時請留意。

---

## 5. 待辦事項 (Action Items)

### MiTAC 端 (急迫)
1. **[Righter]** 為 **K265** 提供 image 修正流程 (對齊先前提供 K245 的版本) — Vinicius 認為 K265 image 有誤,導致 dashcam 在 VisionMax portal 無法運作。
2. **[Conant / Sales]** 提供 Vinicius 先前要求的 **設備報價** 與 **下單流程**;具體機種待確認 (推測涵蓋 K265 / K245 / K246 及測試卡車所需配件)。
3. **[Brian / RD]** 後續 **2026 Q1** K425 image 完成後,主動提供 PS 更新。

### 待客戶端釐清
- Vinicius 雖然提到 cloud-to-cloud 整合為「初期實作」首選,但同時也嘗試 OEM image 路線。需釐清最終商業模式 (純 API 整合 vs. 客製 OEM)。
- K246 Orion 是否在採購清單中。

---

## 6. 商機與風險判讀

### 機會點
- 客戶端對 SDK 整體評價正面 (`SDK is very comprehensive`、`worked nicely`)。
- Vinicius 已實際完成 K245 的 OEM image 修改與錄影 app 替換,代表整合能力強、推進迅速。
- 雙方在 1 個月內已完成:首次接洽 → 帳號 / 設備建立 → Kickoff 會議 → SDK 測試 → 提出採購意向。
- Platform Science 規劃在 **test truck** 安裝多項設備,屬於可量化的試點階段,後續具備擴大採購潛力。

### 風險點
- **K265 image / portal 註冊問題重複出現**,若無法在短期內解決,恐影響客戶信任。
- 報價遲未提供,Vinicius 已二次催促 (4/29 與 5/4),拖延將影響 PO 時程。
- Platform Science 強調 **non-China manufacturing** 與 **non-Chinese modem**,需確認所提報機種完全符合。
- 客戶內部對 cloud-to-cloud vs OEM 雙路線並行,存在後續整合範圍變動風險。

---

## 7. 信件清單索引

| # | 日期時間 | 寄件者 | 摘要 |
|---|---|---|---|
| 1 | 2026/05/04 09:30 | Vinicius | 週末測試回報,K265 image 仍有問題,催報價 |
| 2 | 2026/05/03 19:15 | Conant | SDK 通用於所有 CDR 機型 |
| 3 | 2026/04/30 | Vinicius | (Working / Important) |
| 4 | 2026/04/29 09:38 | Vinicius | 詢問 K265/K245/K246 SDK 是否共用 |
| 5 | 2026/04/29 08:59 | Vinicius | 會後行動清單:簡報、SDK、報價、下單流程 |
| 6 | 2026/04/29 08:19 | Conant | 提供 CDR roadmap 與 SDK 連結 |
| 7 | 2026/04/29 07:53 | Vinicius | 將測試 Righter 提供之 inventory 設定 |
| 8 | 2026/04/29 01:58 | Righter | 兩台裝置已加入 inventory |
| 9 | 2026/04/28 10:31 | Vinicius | 補充 whitelist 需加入清單 (K265/K245) |
| 10 | 2026/04/28 08:59 | Vinicius | 回報 K265 加入 portal 失敗 |
| 11 | 2026/04/22 09:54 | Vinicius | 確認 4/29 開會 |
| 12 | 2026/04/22 04:16 | Stark | 授權 Conant + Brian 安排會議 |
| 13 | 2026/04/22 02:45 | Vinicius | 自我介紹,提案下週會議 |
| 14 | 2026/04/21 23:44 | Conant | 建議 4/27–4/30 之時段 |
| 15 | 2026/04/21 06:31 | Vinicius | 出差中,下週執行流程 |
| 16 | 2026/04/21 01:25 | Righter | 提供裝置更新附件 |
| 17 | 2026/04/20 14:42 | Brian | 建立 VisionMax 帳號與所有資源連結 |
| 18 | 2026/04/17 11:46 | Vikram | 需求補充:multi-channel、CAN、non-China |
| 19 | 2026/04/17 10:19 | Vikram | K265 validation,需 roadmap |
| 20 | 2026/04/16 18:20 | Stark | 將 Brian 加入,詢問 PS camera 計畫 |

---

## 8. PM 分析與策略洞察

### 8.1 Platform Science (Vinicius) — 客戶關係解讀

**客戶動機層次**

| 表面需求 | 背後真正在意的事 |
|---|---|
| 需要 SDK 文件 | 在內部評估 MiTAC 是否值得深度投入 |
| 詢問報價 | 想確認 MiTAC 有意願正式做生意，不只是做 POC |
| K265 portal 問題 | 在測試 MiTAC 的技術支援反應速度 |
| 提到 cloud-to-cloud | 希望與 MiTAC 是平台對平台的夥伴關係，而非純硬體採購 |

**Vinicius 的行為特徵**
- 技術型決策者，週末自己動手測試 SDK，代表他同時是評估者也是執行者
- 已成功完成 K245 OEM image 修改與 app 替換，整合能力強
- 兩度催促報價（4/29 與 5/4），說明他內部已有採購壓力，主動性高
- 用「初期實作」描述 cloud-to-cloud，暗示後續還有更深合作規劃

**風險信號**
- K265 問題若持續未解，會讓 Vinicius 認為 K265 不成熟，轉向只用 K245
- 報價遲未回應，在技術評估期可能導致決策停擺
- Platform Science 對 non-China manufacturing 的要求，是潛在否決條件，需提前確認所提機種是否完全符合

---

### 8.2 PM 策略啟示（Platform Science 視角）

**承諾的層次應與確定性對應**

研發 PM 無法保證固定上線日期，但可以承諾透明度：

| 可承諾的事 | 說法 |
|---|---|
| 評估時程 | 「兩週內告訴你這個功能可不可以做」|
| 里程碑節點 | 「六月底前給你 MVP 評估結果」|
| 資訊更新頻率 | 「每月底給你一次進度更新，任何變化你會第一個知道」|

客戶失去信任，往往不是因為「日期延了」，而是因為「延了才通知」。

**技術型客戶的溝通策略**

Vinicius 這類客戶不需要你說功能多強，他需要：精準的技術文件、清楚的限制說明、以及你能跟上他測試節奏的反應速度。對技術型決策者，要用技術語言溝通，不只講商業故事。

---

## 9. 給 Claude Code 的後續任務建議

如將此 handover 帶入 Claude Code,可考慮下列開發或文件任務:

1. **整理一份英文版回信草稿給 Vinicius**,內容包含:
   - K265 image 修正流程預計提供時程
   - 設備報價與下單流程的初步回覆 (待業務確認)
   - 重申 SDK / API 支援
2. **建立內部 tracking checklist** (Markdown / GitHub Issue 模板),追蹤 Action Items #1~3。
3. **建立 K245 vs K265 image flashing SOP 文件骨架**,讓 Righter 補充細節。
4. **針對 VisionMax API 文件 (https://visionmax.redocly.app/) 進行整合範例程式撰寫**,協助 Platform Science cloud-to-cloud 串接驗證。
5. **建立 Platform Science 測試裝置 Inventory 表 (CSV / JSON)**,後續若有更多裝置加入便於管理。

---

---

_Last updated: 2026/05/05 — 新增 PM 分析與策略洞察（Section 8）。CONNECTSOURCE Passenger Blurring 事件已獨立記錄於 `connectsource-passenger-blurring.md`。_
---

## 10. 2026-05-07 / 5-8 重大更新(從 Outlook thread 補)

### 5/7 11:02 AM Vinicius 給 Paul Lee + Conant Ho 的 testing plan(cc Vikram, Righter, Stark, Brian, Kenny)

**Test truck setup**(in Platform Science office):
- Install **Evo K265** in test truck
- 2 side cameras connected to Evo
- 1 rear camera connected to Evo(先 truck 內測,後續要連 trailer)
- InCab Display 連 Evo

**後續變化**:
- 換 **K165** 測 single lens dashcam(某些客戶 single lens 是 requirement)
- 用 K245 + Video Hub 測,評估這條方案可行性(K246 Orion 是未來機種,目前 K245 先頂)

→ **🚨 K165 重要**:之前 memory 寫「沒有 K165」是錯的(2026-04 早期校正)。Vinicius 5/7 信件確認 K165 真的存在,是 EVO 系列 single lens dashcam 版本。已校正 critical-facts-log + machines-spec。

### 5/7 8:44 PM Vinicius 給 Righter 的進度

✅ **VisionMax 已成功連線** — 原本以為 cable 問題,實際是 **camera APN 問題**,已解決。

⏳ 等 cable 資訊 → 訂 sample equipment → truck 物理連接測試。

### 5/7 3:26 AM Righter Song 給 Vinicius 的關鍵限制

- 設備 F4723090033(K245 IMEI 357216578000516)已加進 inventory ✓
- ⚠️ **K265 SD card 限制**:不能 overwrite all partitions(架構限制)
- ⚠️ **LM(Lightmetrics)版本不能用 SD update** 升到 VisionMax → 必須**直接給 VisionMax 版 sample**,不要先給 LM 再升
- 需要新 VisionMax sample 給 Vinicius 後續測試

### 對 Action Items 的影響

- **Action Item #1 K265 image 修正流程** → 已經由 Righter 5/7 直接回應限制(不能 SD upgrade);後續策略改成「直接給 VisionMax sample」
- **Action Item #2 設備報價下單** → 5/7 11:02 Vinicius 把 testing plan + cable 需求轉給 Conant Ho,Conant 在處理
- **Action Item #3 SDK/API 支援** → 已連線成功,等下一輪測試發現再說

### 對 stakeholders 的更新

| 角色 | 5/7 揭露 |
|---|---|
| Conant Ho(何肇睪 - MDT)| 接 Vinicius testing plan + cable 規劃,sample equipment 訂單對接窗口 |
| Righter Song(宋祐全 - MIC)| 設備 inventory + image flashing 限制專家 |
| Paul Lee(李世博 - MDT)| Account Sales Manager,Vinicius 主對接 sales |
| Stark Yang(楊永吉 - MDT)| Director, Video Telematics — thread 內監督 |

_Last updated: 2026-05-08 — 補 5/7 testing plan + APN 解決 + K165 校正 + K265 SD update 限制。_

---

## 11. 2026-05-08 / 5-9 weekend 進度(Live View API 議題浮現)

### 5/8 13:22 Paul → Brian/Conant(VisonMax Account Device Listing thread)
- Vinicius 手上 3 台清單:K245 × 2(F4723090088 / F4723090033)+ K265 × 1(L1225380005)
- 客戶反映 **EVO (K265) ADAS 和 DMS 沒啟動**
- 請 Brian / Conant 確認 device 在 VMX platform 上設定正確

### 5/8 15:35 → 15:56 Brian / Righter / Brian 連動
- Brian 對 Righter:**確認 3 台 SN 是否在 PS Master account 下,application version 是否要 update,plan type 是否正確**
- Righter:K245 × 2 在 inventory,K265 已分配給 **"Platform Science" fleet**,K265 (L1225380005) AI function 看起來 OK
- Brian:舊樣機 app version 不一定 2026 Q1,可能要 update + 告知客戶網路用量

→ **校正**:Righter 說 K265 AI 沒問題,但 Vinicius 反映 ADAS/DMS 沒啟動 → 推測差在 **plan type 沒對到 ADAS/DMS 啟用層級** 或 **DMS calibration 沒完成**(需 20 km/h × 15 sec)

### 5/9 01:57 Vinicius 新問題:Live View 怎麼接到 PS portal
- VMX docs 沒寫 live view streaming 怎麼接到客戶 portal
- 客戶端要做 cloud-to-cloud 整合,但 Live View 部分卡住

### 5/9 10:27 Brian 回應 Live View 機制
> "Since Live View works as a P2P connection (directly from browser or app to device), it does not use cloud API calls. If you decide to adopt a Server-to-Server API integration approach, we will provide the JavaScript library or the necessary technical assistance."

**重大事實**:
- **Live View = P2P 直連**(browser/app → device),**不走 cloud API**
- 要做 Server-to-Server 整合,MiTAC 提供 **JS library + 技術協助**

### 5/9 13:11 Vinicius 最新狀態(2 個 open question)
1. **JS library 供 testing**:做完了 PS portal 的 clone,要對接 VMX API 驗證,要 JS lib
2. **Camera-side video 直接看不下載**:VMX 支不支援?

### 對 Action Items 的更新

| Action | 狀態 |
|---|---|
| K265 image 修正流程 | 等新 VisionMax sample 採購(LM 版不能 SD upgrade)|
| 設備報價下單 | Conant / Paul 對接中,5/11 週一上午 tier pricing 會議 |
| ADAS/DMS 啟動 | **新議題** — 推測 plan type / calibration,需 Brian / Conant 確認 |
| Live View JS lib | **新承諾** — Brian 5/9 承諾提供,等 Conant 出件 |
| Camera-side video without download | **新開放問題** — KB 沒列,要查 |

### Kenny 動作(本週)
- 開新檔 / 加段同步 Live View JS lib 議題到 case-learning
- 跟 Brian / Conant 對齊 plan type 對應 ADAS/DMS 啟用的具體條件
- 把「Camera-side video without download」開個 question 給 KB / Spencer 答

_Last updated: 2026-05-11 — 補 5/8–5/9 Device Listing thread + Live View P2P/JS lib + camera-side video without download 兩個 open question。_
