# MiTAC × Customer (Video Safety Solution) — 會議深度分析

- 會議日期:2026-04-29
- 平台:Webex
- 整理形式:**基於會議紀錄重建的對話流 + PM 視角深度分析**
- 重要說明:對白為合理重建,非原始錄音字幕。事實內容對齊紀錄。

---

## 全場戰術概覽(讀完整份再回頭看這張表)

| 階段 | 主導者 | 真正在發生什麼 |
|---|---|---|
| 1 開場 + NDA | 雙方 | 客戶端早就準備好,MiTAC 還在內部跑 → 後手 |
| 2 MiTAC 產品總覽 | Conant | 大量資訊鋪墊,但客戶心裡早有偏好 |
| 3 EVO / Orion 技術 | Conant | 把 K265 賣點打出來,成功讓客戶選定主力機種 |
| 4 隱私 / K165 | 雙方 | 客戶「不接受駕駛艙鏡頭」的需求被 K165 接住 |
| 5 Android + App 部署 | Peter ↔ Conant | Peter 在驗證「我自家 App 能不能跑」 |
| 6 CAN / OBD | Peter ↔ Conant | Peter 摸 SDK 的邊界 |
| 7 整合架構 ⚠️ | **Vinicius** | **整場會議真正的攻防點** |
| 8 AI 模型矩陣 | Brian | 把「能 / 不能」釘死,客戶帶 AI 直接 No |
| 9 Fleet Event Sensing | Brian | 用能力清單堵客戶疑慮 |
| 10 製造 + 樣品 + 測試 | Vinicius | 把球丟回 MiTAC,Q2 倒數開始 |
| 11 Action Items 收尾 | Vinicius | 多數待辦在 MiTAC 端 |

---

# 階段 1 — 開場 + NDA 確認(§1, §2)

## 對話重建

> **Conant**:「歡迎大家。先介紹我們這邊,我是 Conant,負責產品規劃與行銷,後續單一窗口找我就好。Brian 帶軟體與雲端,團隊 20 人左右。Kenny 是我們的 Technical Support,目前在熟悉產品。」
>
> **John**:「謝謝。我是 John,負責 Video Safety Solutions 的相機產品、Web Portal、AI 模型整體。我們客戶主要在北美,LATAM 和 EU 也有覆蓋。」
>
> **Vinicius**:「我是 Vinicius,工程這邊的主管,Platform Science 一年多,從 Trimble 那邊過來,Video Safety 領域今年初接手。對了,**我們 Legal 已經確認過 NDA 沒問題,這邊是 OK 的**。」
>
> **Conant**:「了解,那我們這邊還要再確認一下,確認後再回覆。」
>
> **Peter**:「我是 Peter,Productivity Side,Mobile Lead,Android App / Android OS 背景,規劃把 Video Feed 整合進我們的平板。」

## PM 深度分析

兩個觀察點:

**第一**:Vinicius **主動拋出「我們 NDA OK」**這句話的位置。他放在自我介紹之後立刻講,代表他刻意要把球丟給 MiTAC — 「我這邊都準備好了,你們呢?」。Conant 回「再確認」是被擺在後手。

**第二**:三位客戶的角色分工已經很清楚 —
- **John**:策略決策層,但他在後續會議裡發言很少
- **Vinicius**:工程操盤手,**這場真正的提問者**
- **Peter**:Mobile 整合 owner,問題很具體很細

MiTAC 三位:
- **Conant**:商務窗口、產品鋪陳
- **Brian**:技術 / 平台 / AI(後面才上場)
- **Kenny**:旁聽

## 旁白給 Kenny

> **NDA 這條你要主動追蹤**。Conant 講「再確認」是禮貌話,但客戶端已經 OK 一個月以上的話,MiTAC 內部還沒簽會被視為**誠意問題**。下次你看到 Conant,問他一句:「NDA 內部跑到哪了?要不要我幫忙催?」 — 這是 PM 該有的主動。

---

# 階段 2 — MiTAC 產品總覽(§3, §4, §5)

## 對話重建

> **Conant**:「先給大家看我們的整套 Video Telematics Solution。我們有四個產品線:Connected DVR、Video Hub(開發中)、各式相機、配件與雲端服務。CDR 這邊分三個級距 — Sprint 走輕型車、Gemini SE 中型、EVO 重型可以到 7 路。Orion 是 Gemini SE 的接班機種,正在開發中。」
>
> **Vinicius**:「Heavy Truck 那邊的 EVO,7 路怎麼接?」
>
> **Conant**:「主機是 K265,平台 Qualcomm QCS610,擴充靠 1 個 USB + 4 個 TVI port。一條 mini USB 轉 4 顆 TVI 的線,加上 USB Type-C 可以再接一顆,前向加駕駛艙兩顆,2 + 4 + 1 = 7。」
>
> **Vinicius**:「LTE 是 Cat4 還是 Cat6?」
>
> **Conant**:「K265 是 Cat4,有 5G RedCap 版本可選。Sprint 跟 Gemini SE 是 Cat6。」

## PM 深度分析

這個階段表面是「產品介紹」,實際上 Conant 在做兩件事:

**1. 把 lineup 全部攤開,讓客戶看到「縱深」**
資訊量很大不是缺點,目的是建立「MiTAC 不是只會做一款」的印象。後續客戶談 Pricing 時,會被引導去組合採購(主機 + 配件 + 雲端)。

**2. 把 K265 自然地推到主場**
注意他怎麼描述各機種:
- Sprint:輕型車(言下之意 = 「不夠 fancy」)
- Gemini SE:中型,正在被 Orion 接班(言下之意 = 「快過時了」)
- **EVO (K265):重型、7 路、QCS610**(言下之意 = 「旗艦」)

對應客戶需求(美國商用車隊,普遍要 ≥ 2 顆 Side Camera),**K265 是唯一合理選擇**。Conant 沒有明說「你買 K265」,但鋪陳完客戶就會自己選 K265。

## 旁白給 Kenny

> 這是 product positioning 的標準操作:**不要直接推銷,讓客戶自己選**。你之後做客戶簡報,記住這個技巧 — 把 lineup 鋪開,把客戶需求對應出來,讓客戶說出「那我要 X」。
>
> 另外,**Vinicius 一進入產品環節就直接問 LTE Cat 等級**,代表他做過功課、知道哪些規格會卡點。這種客戶你不能用 marketing 話術應付。

---

# 階段 3 — EVO / Orion 技術深挖(§6, §7)

## 對話重建

> **Conant**:「K265 的 AI 是內嵌的 — QCS610 + Android / Linux,我們在上面跑 1.1 TOPS 等級的偵測。雙 SD 卡槽,各 512GB,所以本地最多 1TB 影片儲存。」
>
> **Vinicius**:「那 Orion(K246)是什麼定位?」
>
> **Conant**:「Orion 三個亮點:第一,**Li-ion SuperCAP 容量是前代 10 倍**,突發斷電還能存檔上傳。第二,**4G LTE 標配,5G RedCap 選配**,所以未來客戶要升 5G 不用換主機。第三,**AI 從 Gemini SE 那代往上跳一階**,1.1 TOPS,DMS 可以做到 4-way cabin adjustment。」
>
> **Vinicius**:「畫質呢?」
>
> **Conant**:「Outward 從 1080p 升到 **4K**,LPR(車牌辨識)和遠距物件辨識會更準。」

## PM 深度分析

Conant 在這裡做了一個**未來保證**動作:**把 Orion 描繪成「給未來」的機種**。

為什麼這對 MiTAC 重要?

- 如果客戶**現在**選 K265,Conant 馬上有單拿
- 如果客戶**未來**想升級,Orion 已經在 roadmap → MiTAC 不會被換掉

這是經典的「現在 + 未來雙軌綁定」銷售結構:
- 短期:K265 拿單
- 長期:Orion 鎖住升級路徑

但 — **Vinicius 沒有上鉤**。他後續問題都還是繞著 K265 打,Orion 只是「想試試看」(§16 紀錄)。對 Vinicius 來說,Q2 測試壓力太大,他不會為了 Orion 拖時間。

## 旁白給 Kenny

> 注意 Conant 怎麼用「容量是 10 倍」這種**相對數字**而不是絕對數字 — 因為絕對數字一講,客戶就會問「對手做到多少」。**相對數字保留比較空間**,這是話術細節,你之後簡報可以學。
>
> 另外,Orion 4K + 4-way cabin adjustment 你要去查清楚對應市場上哪些對手機種,讓自己有概念。

---

# 階段 4 — 駕駛艙鏡頭隱私 / K165(§8)

## 對話重建

> **John**:「我們有部分 fleet 客戶,他們的司機公會或客戶政策不允許駕駛艙錄影。這個你們怎麼處理?」
>
> **Conant**:「我們有 K165,K265 的單鏡頭版本 — **只有前向,沒有駕駛艙**。同樣 7 路擴充能力,只是少一顆 in-cabin。另外我們有 **Camera Cap**,橡膠材質的鏡頭蓋,如果客戶想保留 K265 但臨時遮駕駛艙,可以用這個。」
>
> **Vinicius**:「Camera Cap 是貼紙還是實體蓋?」
>
> **Conant**:「實體蓋,不是貼紙。我們會寄樣品給你們看。」

## PM 深度分析

這段表面平淡,實際很關鍵 — 北美 fleet 市場的隱私阻力比想像中大。

兩個層次:
1. **強制法規層**:某些州、某些工會合約不允許錄影司機
2. **客戶偏好層**:司機抗拒 → 工會反彈 → fleet 老闆怕麻煩

MiTAC 應對的方式很聰明:**不是「我們可以關掉」,而是「我們直接給你硬體版本不一樣的機種」**。

差別在哪?
- 「軟體關掉」= 客戶要相信你關掉了 → **信任成本**
- 「硬體沒有」= 沒有就是沒有 → **沒有信任問題**

K165 + Camera Cap 這套組合,讓 Platform Science 可以對「強制無錄影」和「臨時無錄影」客戶**都有解**。

## 旁白給 Kenny

> 這條線你要記住一個 PM 心法:**當客戶有政治 / 法規敏感問題時,給他「硬體層」的解,而不是「軟體開關」**。硬體解不可逆 → 客戶法務會更安心。
>
> Camera Cap 你要實際弄一個樣品到手上,**自己把它裝在 K265 上拍照**。下次客戶問,你發照片過去比講十句話有用。

---

# 階段 5 — Android 平台 + App 部署(§9, §10)

## 對話重建

> **Peter**:「Sprint 是 Android 9,Gemini SE 是 Android 9,EVO 是 Android 10。**這些會升嗎?**」
>
> **Conant**:「不會。為了穩定,現有機種的 Android 版本就鎖在那裡了,不會年度升級。新一代會用當下最新的 entry version — Orion 從 Android 13 起跳,下一代會 16 起跳。」
>
> **Peter**:「那這些裝置是 Play Certified 嗎?我家 App 用了 Firebase。」
>
> **Conant**:「**不是**。我們跑的是 Stock Android,自己編譯後在相機上運行。**沒有 GMS**。如果你 App 用 Google 服務,可能要改寫不依賴 Google 的版本。權限有問題,可以把 App 給我們,我們協助處理。」
>
> **Peter**:「OTA 怎麼做?」
>
> **Conant**:「我們有 **MyDN Service**(正式名稱我再確認),OS、設定、應用程式都可以遠端升級。」

## PM 深度分析

這段是 Peter 的主場,也是**整場會議裡客戶端最具體的「我能不能用」驗證**。

Peter 的真實需求是:「**我家 App 能不能不改太多就跑起來?**」

Conant 的回答其實藏了三個雷:

**雷 1:Android 版本不升**
表面是「為了穩定」,實際含意是 — 客戶 App 如果未來用了新版 Android API,這些舊機種會直接不能跑。Peter 要面對「**雙版本維護**」(舊機種一份、新機種一份)。

**雷 2:沒有 GMS**
Firebase Cloud Messaging、Google Maps SDK、Google Sign-In、Google ML Kit 全部不能用。Peter 必須改寫或找替代品。

**雷 3:MyDN 名稱還沒確定**
連 Conant 都記不住正式名稱,代表這個服務在 MiTAC 內部可能還在整理 / 命名,**文件成熟度可能不足**。Peter 要拿這個服務做 OTA 規劃,等於他要倚賴一個「還沒成形」的東西。

## 旁白給 Kenny

> 你之後一定會被 Peter 問到「OTA 流程細節」、「APK sideload 步驟」、「Firebase 替代方案」。你現在就該:
>
> 1. **找 Conant 把 MyDN 正式名稱、文件、API 拿到手**
> 2. **整理一份「車載 Android 替代方案對照表」**(Firebase → MQTT、Google Maps → Mapbox/HERE、Google Sign-In → 自家 OAuth)
> 3. **問 Brian:這些 K220/K245/K265 的 Android 版本維護到什麼時候?有 EOL 計畫嗎?**

---

# 階段 6 — CAN / OBD 資料抽取(§11)

## 對話重建

> **Peter**:「車輛資料怎麼拿?Ignition、speed、VIN 這些。」
>
> **Conant**:「兩個選擇。**第一**,純硬體 Dongle,你們自帶 CAN Decoder,自己解。**第二**,我們跟第三方合作的 Dongle,內建 Decoder,直接拿到已解碼的高階資料。透過我們的 **Standard SDK** 或 API。」
>
> **Peter**:「SDK 是 high-level 還是 low-level?」
>
> **Conant**:「High-level。直接拿 Ignition、Speed 這種具象欄位。如果有缺,可以反映給我們。」

## PM 深度分析

這段隱藏的訊息:**MiTAC 在 OBD 這條線是 reseller**,不是技術擁有者。

第二款 Dongle 是「跟第三方合作」,代表:
- 解碼能力是第三方的(可能是 Geotab、Bsm Wireless、CalAmp 之類的供應商)
- 客戶要的欄位「如果有缺」,**MiTAC 要去跟第三方反映** → 改動週期不快

對 Platform Science 而言,這代表:
- **如果他們的核心需求是 OBD 資料**,綁 MiTAC 就等於間接綁 MiTAC 的第三方
- 如果哪天他們想要更多元 / 更深的 CAN 資料(例如商用車的 J1939 私有訊號),路徑會很長

## 旁白給 Kenny

> 這是「PM 該追問」的典型題:Conant 一句「跟第三方合作」帶過 → 你要主動問清楚:
>
> 1. **第三方是誰?**(這個你可能要私下問 Conant 或 Brian)
> 2. **客戶提需求,從反映到實作的週期是多久?**
> 3. **如果第三方換了,客戶要不要重新整合?**
>
> 這些問題不會在客戶會議上問,但你內部要知道答案。

---

# 階段 7 — 整合架構爭議(§12)⚠️ 全場核心攻防

## 對話重建

> **Vinicius**:「我看你們文件裡有三種整合模式。我們**理想中量產用 Mode B** — MiTAC Camera App + 我們自家 Customer Comm App,透過你們的 **VisionMax CDR SDK** 串到我們 Cloud。測試初期我們會用 Cloud-to-Cloud,但量產目標是 Mode B。」
>
> **Brian**:(停頓一下)「這個 Mode B... 老實說,**目前沒有客戶以這種方式整合**。文件這張圖,我也不清楚它的來源。」
>
> **Vinicius**:「沒關係,我回頭跟我們內部 Vikran 確認文件出處。但 — 這個 SDK 是不是會放上 roadmap?我們需要知道方向。」
>
> **Brian**:「我們會內部評估,後續回覆你。」

## PM 深度分析

**這 30 秒是整場會議最重要的攻防**。

### Vinicius 的攻擊點

他不是在問「能不能」,他是在**設定一個前提**:「我們已經決定要走 Mode B,現在問你們會不會配合」。

這種談判技巧叫 **assumed close** — 把選擇預設成「OK」,讓對方變成必須拒絕的一方。

### Brian 的防守

Brian 沒有正面拒絕,他用了三道緩衝:
1. **「沒有客戶這樣用」** — 暗示「這條路沒走過,風險自負」
2. **「文件來源不明」** — 把球丟回客戶,反質疑你們資訊哪來的
3. **「內部評估,後續回覆」** — 標準的拖延招

但 Brian 沒有說 No。為什麼?
- 直接 No → 客戶可能撤
- 答應開放 → MiTAC 商業模式自我降級(看前面我們聊過的 SDK 商業邏輯)
- **拖時間 + 內部討論** = 唯一安全選擇

### Vinicius 的真實壓力

他剛從 Trimble 過來,Platform Science 收購 Video Safety 業務,**他扛著「把 video 整合進主平台」的 KPI**。Mode B 不是他的偏好,是他的工作目標。如果 MiTAC 不開,他要嘛換供應商,要嘛承擔失敗。

## 旁白給 Kenny

> **這條線之後三個月你要全程盯著**。判斷指標:
>
> 1. Brian 內部評估 SDK 開放的會議,你能不能旁聽?(主動爭取)
> 2. 客戶端 Vikran 確認文件來源後,會不會拿出更多舊資料?(代表他們對 MiTAC 期待可能高於現實)
> 3. MiTAC 的決策會不會走到 Conant / Brian 之上的層級?(如果走上去,代表這單規模值得「破例」)
>
> **PM 真正的價值就在這種戰略題上**。技術問題你慢慢學,但這種商業 / 戰略觀察,你現在就要練。

---

# 階段 8 — AI 模型矩陣(§13)

## 對話重建

> **Vinicius**:「AI 模型有沒有可能我們帶資料 fine-tune?或者帶我們自己的模型?」
>
> **Brian**:「兩個情境分開講。**第一**,Camera App + AI 是雙軌架構,我們透過內部機制傳 trigger / threshold,**這個 SDK 目前沒對外開放**。所以你們要把自己的 AI 塞進我們 Camera App,**不行**。**第二**,你們自己做 Camera App + 自己的 AI,在 Android 平台上自由開發,**可以**,但這樣就用不到我們的 AI。」
>
> **Vinicius**:「fine-tune 我們的資料呢?」
>
> **Brian**:「**目前不可行**。涉及資料標註流程跟合作模式。」
>
> **Vinicius**:「了解。那訓練資料區域呢?」
>
> **Brian**:「主要北美,涵蓋歐洲、澳洲、印度。模型架構同一套。」
>
> **John**:「這個 OK,對我們北美客戶不會有負面影響。」

## PM 深度分析

Brian 在這裡做了一個關鍵動作:**把可行性矩陣攤開**。

| 模式 | 可行性 | Brian 表態 |
|---|---|---|
| MiTAC Camera App + MiTAC AI | ✅ | 標準路徑 |
| MiTAC Camera App + 客戶 AI | ❌ | SDK 未開 |
| 客戶 Camera App + 客戶 AI | ✅ | 但失去 MiTAC AI 價值 |
| 客戶資料 fine-tune MiTAC AI | ❌ | 商業合作模式問題 |

這張矩陣的戰略意義:**Brian 把所有「客戶想要客製 AI」的路全部關掉**,只留「用我們的整套」或「你自己從零」兩條路。

為什麼?
- 客戶 fine-tune = MiTAC 的 AI 變成「半客製」 → 維護複雜度爆炸
- 客戶帶模型 = MiTAC AI 沒收入,變相成為 hardware 代工

注意 John 接話「OK,不會有負面影響」 — 他在**幫 MiTAC 給 Vinicius 台階下**。John 的位階高,他這句話等於告訴 Vinicius 「這題不要再追了,我們接受」。

## 旁白給 Kenny

> 你要記住這張矩陣 — **這是後續半年內所有 AI 相關話題的標準回覆**。
>
> 任何客戶問「我能不能...」,你心裡先對照這張表:
> - 在矩陣內 ✅ → 直接答可以
> - 在矩陣內 ❌ → 直接答 No,引導到可行模式
> - 不在矩陣內 → 「我回去確認」(然後找 Brian)
>
> **不要當場 freestyle**,客戶會記得你說過什麼。

---

# 階段 9 — Fleet Event Sensing 能力清單(§14)

## 對話重建

> **Brian**:「來看我們的 Fleet Event Sensing。**K220、K245、K265 三款都全部支援**以下偵測項目 — DMS:Distraction、Fatigue、Seatbelt、Phone、Smoking、Obstructed Camera、Burning。ADAS:FCWS、PCWS、LDWS、Stop and Go、Traffic Sign、Burning ADAS、Blind Spot、Burning。G-Sensor、Map、OBD-II 都有。Roadmap 上 BCWS、Traffic Light、LPR 在做。」

## PM 深度分析

Brian 這段做的是 **「能力轟炸」** — 一口氣鋪開幾十項偵測。為什麼?

因為前一階段(SDK + 客戶帶 AI)他連續說了幾個 No → **氣氛上被認為「保守」**。
能力清單一鋪開,客戶會想:「**算了,他們現成的能力夠用,我也不一定要客製**」。

這是話術節奏的關鍵:**No 之後立刻 Yes 一波**,平衡感才不會崩。

另外注意一個重要細節:**「三款都全部支援,沒有機型差異」**。

這句話的商業含意 = MiTAC 不用機型來做能力分層 → **價格分層用硬體規格(7 路 vs 3 路、4K vs 1080p)**。對客戶而言,他可以用便宜機種 + 同樣 AI 能力組合產品線。

## 旁白給 Kenny

> 這份偵測清單你要**每一項都知道對應的觸發條件、誤報率**。客戶之後一定會問「Distraction 是怎麼判定的?」、「Fatigue 偵測會不會誤觸發?」。
>
> 你現在不會也沒關係,**列成一張表,逐項找 Brian / AI team 補上**。這張表會是你接下來半年最常翻的文件。

---

# 階段 10 — 製造、樣品、測試(§15, §16)

## 對話重建

> **Vinicius**:「製造在哪?」
>
> **Conant**:「總部台北,新竹是主要製造基地,中國也有,**今年會新增一個新據點**。」
>
> **Vinicius**:「美國呢?」
>
> **Conant**:「目前沒有。」
>
> **Vinicius**:「OK。測試這邊我們希望 **Q2 完成所有測試**,Test Cases 已經寫好,只差相機上車。**Q3 / Q4 測試成功就推進量產**。優先序:K265 主、K165 次、K246 想試新世代、K245c + Hub 看 Pricing 決定。」
>
> **Conant**:「了解,Sales 會聯繫,Pricing Sheet 跟 K265 完整樣品(主機 + 擋風支架 + 擴充相機)會安排。」

## PM 深度分析

兩個重要訊號:

**訊號 1:「美國沒有」是關鍵商業變數**
北美關稅、Made in USA 政策壓力越來越大,Vinicius 問這題不是隨便問。**Platform Science 的客戶可能對「Made in China」敏感**(尤其 DOT、聯邦合約相關 fleet)。
Conant 含糊帶過「今年新增一個據點」 — 沒講地點,可能是因為:
- 真的還沒定
- 或敏感(例如越南、墨西哥),對外要先過內部
- 或就是怕透露給對手

**訊號 2:Vinicius 把球丟回 MiTAC,時間線非常硬**
- Q2 = 4-6 月,**從會議到 Q2 結束剩約 2 個月**
- Test Cases 「已經寫好,只差相機上車」 → 客戶端準備到位,**現在卡的是 MiTAC 出樣速度**
- Q3 / Q4 量產 → 任何拖延都會推遲整個合作

對 MiTAC 而言,**樣品出貨時間就是合作命脈**。如果出樣慢,客戶會把這個視為 MiTAC 執行力的訊號。

## 旁白給 Kenny

> 你立刻就要知道:
>
> 1. **K265 完整樣品最快多久能出?**(找 Conant)
> 2. **Side Camera 不是樣品,是 Validation 中(Q2 後期 ~ Q3 量產)— 客戶測試會缺這顆,要怎麼辦?**(這是會議裡的雷)
> 3. **新增製造據點地點 — 這個訊息對外公開嗎?**(找內部釐清)
>
> 樣品延遲 = 信任崩盤的起點。你身為 PM 即使不直接管出貨,也要當「催單的人」。

---

# 階段 11 — Action Items 收尾(§17)

## 對話重建

> **Vinicius**:「整理一下 Action Items。MiTAC 端要寄簡報、SDK 文件、Pricing Sheet、K265 完整樣品、K165 + Camera Cap 細節、MyDN 文件、確認 NDA、Side Pod Pricing 跟量產時程。SDK 整合模式 roadmap 你們內部評估後告訴我們。AI Accuracy 第三方驗證後續討論。」
>
> **Conant**:「OK,都記下來。」
>
> **Vinicius**:「我們這邊我會發 Follow-up Email,內部彙整 PO 清單,跟 Vikran 確認文件來源,規劃測試卡車安裝。」

## PM 深度分析

把 Action Items 對照「誰承諾了什麼」:

| 端 | 承諾項數 | 性質 |
|---|---|---|
| **MiTAC** | 9 項 | 多數是「給文件 / 給樣品 / 給報價 / 內部確認」 — **執行型** |
| **客戶** | 5 項 | 多數是「我們內部跑流程」— **配合型** |

意義:**這場會議結束後,壓力大半在 MiTAC 端**。

而且 MiTAC 的 9 項裡:
- **可立刻做的**:寄簡報、寄 SDK 文件、安排樣品 → 短期執行力檢驗
- **需要內部跑的**:NDA、SDK roadmap、Side Pod 量產時程 → 中期戰略檢驗
- **完全模糊的**:AI Accuracy 第三方驗證、新增製造據點 → 長期信任檢驗

每一項做到的速度與品質,都是 **Platform Science 對 MiTAC 的信任度評分**。

## 旁白給 Kenny

> 你做為 PM,**最該做的事是建一張 Action Item Tracker**:
>
> | Action | Owner | Due | Status | Note |
> |---|---|---|---|---|
> | 寄簡報 | Conant | T+3 days | | |
> | SDK 文件 | Brian | T+1 week | | |
> | K265 樣品 | Sales | T+2 weeks | | |
> | ... | | | | |
>
> **每週一更新一次,每兩週主動問 Conant 和 Brian 進度**。這張表會是你內部的價值來源 — 你不一定能解決問題,但你能讓事情**不掉**。

---

# 全場戰術總結

## MiTAC 在這場的「Yes / No / 拖」

| 客戶提的事 | MiTAC 表態 |
|---|---|
| K265 / K165 / Orion 樣品 | ✅ 直接 Yes |
| Camera Cap、規格細節、Pricing | ✅ Yes,執行中 |
| MyDN OTA 服務 | ⚠️ Yes,但文件成熟度可能不足 |
| K245c + Hub 是否納入測試 | ⚠️ 看 Pricing |
| **客戶帶 AI / fine-tune** | ❌ **明確 No** |
| **SDK 開放(Mode B)** | 🕐 **拖,內部評估** |
| NDA | 🕐 拖,內部確認 |
| AI Accuracy 第三方驗證 | 🕐 拖,後續討論 |
| 新增製造據點地點 | 🕐 沒答 |

## 三條「之後 6 個月主軸」

1. **樣品 + Pricing 速度線**:檢驗 MiTAC 執行力
2. **SDK Roadmap 表態**:檢驗 MiTAC 戰略意願
3. **NDA + 文件 + AI Accuracy**:檢驗 MiTAC 信任投資

這三條全部過關,Q3-Q4 量產合作機會大;任何一條卡住,合作會停滯或告吹。

## 給 Kenny 的最後一句話

> 你在這場會議是 Technical Support、是旁聽生。
> 但**這份分析做完之後,你要把自己升級成「會議翻譯機」** —
> 把客戶說的話翻譯成「他真正在意什麼」、把 MiTAC 說的話翻譯成「我們真正承諾了什麼」。
>
> 做到這件事的 PM,在組織裡的價值會直接跳階。
