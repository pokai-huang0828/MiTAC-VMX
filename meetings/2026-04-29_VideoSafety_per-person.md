# MiTAC × Customer (Video Safety Solution) 會議紀錄 — 逐人需求 / 回覆彙整

- 會議日期:2026-04-29
- 平台:Webex
- 整理視角:依與會者拆分,呈現各自需求 + MiTAC 對應回覆
- 來源:會議字幕轉錄整理

---

## 與會者一覽

### MiTAC 端
| 姓名 | 角色 |
|---|---|
| Conant | Prime Manager / Product(單一窗口) |
| Brian | Software Head(VisionMax Platform / Cloud / Camera App / AI,團隊約 20 人) |
| PoKai Huang (Kenny) | Technical Support |

### 客戶端(Video Safety Solution)
| 姓名 | 角色 |
|---|---|
| John Smith Jr | Director of Product, Video Safety Solutions |
| Vinicius Francisquinho | Engineering Director(John 的 counterpart) |
| Peter (preetham) | Productivity Side / Mobile Lead |

---

# Part A — 客戶端三位

## A1. John Smith Jr — Director of Product, Video Safety Solutions

### 角色焦點
- 客戶端產品最高決策者,管 cameras / Web Portal / AI models 整體
- 在這場會議扮演**策略層 buy-in**角色,不細問技術
- 業務範圍:北美為主,LATAM、EU 也覆蓋

### 他明確表達 / 同意的點
| # | 議題 | 來源 |
|---|---|---|
| 1 | 對 MiTAC AI 模型「跨區訓練資料」表達不反對,認為對北美客戶不會造成負面影響 | §13 |
| 2 | 默認 Vinicius 在工程細節上的判斷,沒有提出反對或額外條件 | 全場 |

### MiTAC 對應回覆
- §13 Brian:同一套模型架構可用不同地區資料訓練,北美為主、涵蓋 EU/AU/India → John 認可

### 未解 / 對 John 而言仍待跟進
- 沒有明確未解項
- 但他位置最高,後續 Pricing Sheet、合作條款必經他這層

---

## A2. Vinicius Francisquinho — Engineering Director(這場真正的主問者)

### 角色焦點
- 工程總監,John 的 counterpart
- Platform Science 1 年多,從 Trimbo 併購進來,Video Safety 領域今年初接手 → **背景比較新**,所以問得細
- 這場會議的**主要技術提問者 + 推進者**(Action Items 大半是他喊出來的)

### 他明確提出的需求 / 問題
| # | 議題 | 細節 | 來源 |
|---|---|---|---|
| 1 | NDA 狀態 | 客戶端 Legal 已確認 NGA 端 OK | §2 |
| 2 | 整合架構長期偏好 | 量產想用「MiTAC CameraApp + Customer Comm APP via **VisionMax CDR SDK** + Customer Cloud」 | §12 |
| 3 | 整合架構文件來源 | 將回頭跟內部 Vikran 確認該文件圖出處 | §12 |
| 4 | AI 訓練資料地區涵蓋 | 想了解 MiTAC AI 訓練樣本的地區分布 | §13 |
| 5 | 測試樣品 | 要求 **K265 完整樣品**(主機 + 擋風玻璃支架 + 擴充相機) | §17 |
| 6 | 測試時程 | Q2 完成所有測試,Q3/Q4 進入合作 / 量產 | §16 |
| 7 | 機種測試優先序 | K265 為主、K165 次之、K246 想試新世代、K245c+Hub 視 Pricing | §16 |

### MiTAC 對應回覆
| 對應 | 回覆人 | 回覆要點 |
|---|---|---|
| #1 NDA | Conant | MiTAC 端待內部再次確認 → **沒當場給答案** |
| #2 SDK 整合架構 | Brian | 「目前**沒有客戶**以此模式整合」、文件圖來源 Brian 也不知道 → 內部評估 Roadmap 後回覆 |
| #4 AI 資料區域 | Brian | 北美主、EU/AU/India 次,模型架構同一套 |
| #5 K265 樣品 | Conant | 列入 Action Items,由 Sales 出貨 |
| #6 時程 | 雙方 | 一致同意 Q2 / Q3-Q4 節奏 |

### Vinicius 視角下,MiTAC 仍欠他的承諾
1. **SDK 模式是否進 Roadmap** — 量產架構的關鍵變數
2. NDA 確認
3. K265 樣品實際出貨時程
4. AI 模型 Accuracy 第三方驗證資料

---

## A3. Peter (preetham) — Productivity Side / Mobile Lead

### 角色焦點
- Android App / Android OS 長期開發者
- 客戶端要把 **Video Feed 整合進平板** → 他是 mobile 端的整合 owner
- 提問都聚焦在「我能不能在 MiTAC 機器上順利跑我自己的 App」

### 他明確提出的需求 / 問題
| # | 議題 | 細節 | 來源 |
|---|---|---|---|
| 1 | Android 版本支援與升級 | Sprint/Gemini SE/EVO 上的 Android 9/10 會不會升 | §9 |
| 2 | 客戶自家 App 部署 | 能不能在裝置上跑、權限怎麼解 | §9 |
| 3 | App OTA 管理 | 客戶 App 怎麼遠端更新 | §10 |
| 4 | CAN / OBD 資料抽取 | 用什麼介面取得車輛資料 | §11 |

### MiTAC 對應回覆
| 對應 | 回覆人 | 回覆要點 |
|---|---|---|
| #1 | Conant | 現有機種**不**年度升 Android;Orion 13 起跳、下一代 16 起跳;非 Play Certified,跑 Stock Android |
| #2 | Conant | 可在裝置跑;權限有問題可把 App 給 MiTAC 協助處理 |
| #3 | Conant | MyDN Service(正式名稱待確認)可協助 OS / 設定 / App 升級 |
| #4 | Conant | 兩款 Dongle:純硬體 vs 內建 Decoder;透過 **Standard SDK** 取 High-Level 資料 |

### Peter 視角下,仍待 MiTAC 補上的東西
1. **Standard SDK 文件** — 拿不到文件無法評估資料欄位夠不夠
2. **MyDN/MiDM 正式名稱 + API 文件** — 影響他能不能規劃 App OTA 流程
3. K165 配件相容性、Camera Cap 細節(間接相關)

---

# Part B — MiTAC 端三位

## B1. Conant — Prime Manager / Product(本場單一窗口)

### 他主導 / 回覆的議題
- 產品總覽、CDR Roadmap、Lineup 比較
- EVO / Orion Highlight
- K265 / K165 / Camera Cap
- Android 策略
- MyDN OTA
- OBD / CAN
- 製造供應鏈
- 商務面:Pricing、樣品、時程

### 他在會中對客戶的承諾
- 寄送本次簡報全套
- 提供 Standard SDK 文件
- Sales 提供完整 Pricing Sheet(全機型 + 配件)
- 安排 K265 完整樣品出貨
- 提供 K165 + Camera Cap 細節(含照片 / 樣品)
- 補 MyDN 正式名稱、能力、API 文件
- 確認 MiTAC 端 NDA 狀態
- Side Pod Camera(BSM)Q2 後期報價、量產時程
- 補今年新增製造據點地點

### 他刻意保留 / 沒當場回覆的點
- NDA 狀態 → 待內部確認
- MyDN 正式名稱 → 沒當場給確切名字
- 新增製造據點地點 → 整個沒講

---

## B2. Brian — Software Head(VisionMax Platform / Cloud / AI / 約 20 人團隊)

### 他主導 / 回覆的議題
- 整合架構
- AI 雙軌架構(Camera App + AI Application)
- 客戶帶 AI 可行性矩陣
- AI 訓練資料區域
- Fleet Event Sensing 偵測能力

### 他在會中對客戶的承諾
- 內部評估「MiTAC CameraApp + Customer Comm APP via VisionMax CDR SDK」整合模式 Roadmap → 後續回覆
- 後續討論 AI Accuracy Reporting / 第三方驗證是否可分享

### 他明確 NO 或保留的點
| 議題 | 表態 |
|---|---|
| 客戶自帶 AI 模型放進 MiTAC Camera App | 不行,SDK 尚未開放 |
| 客戶帶資料 fine-tune MiTAC 模型 | 不行,目前不可行(資料標註與合作模式) |
| 「High Level Integration Architecture」文件來源 | 不知道、沒人用過該模式 |
| SDK 對外開放時程 | 未承諾,僅說「內部評估」 |

> Brian 在 §13 把「能 / 不能」講得非常清楚,這張矩陣是後續對客戶溝通最重要的 reference。

---

## B3. Kenny (PoKai Huang) — Technical Support

### 這場的角色
- 旁聽 + 吸收
- 沒有主導任何回覆
- 公開定位:「目前仍在熟悉相關產品」

### 對 Kenny 的後續涵義
- 接下來客戶會持續來信問 Pricing / Sample / SDK / MyDN 細節 → 這些 Action Items 會被 Conant 拉進去處理
- 對外時不能用「不熟」當答案,只有對內可以這樣講 → 補課需要快

---

# Part C — 跨人交叉的關鍵共識與分歧

## C1. 雙方一致共識
1. **時程**:Q2 完成測試 → Q3/Q4 進入合作 / 量產
2. **測試主力**:K265(7 路、多側邊相機是差異化優勢)
3. **測試整合方式**:Cloud-to-Cloud(MiTAC CameraApp + VisionMax Cloud + Customer Cloud)
4. **AI 跨區資料**:不需為地區精準度做客製化

## C2. 仍有分歧 / 待 MiTAC 內部確認
| 議題 | 客戶立場 | MiTAC 立場 | 後續 |
|---|---|---|---|
| 量產整合架構 | 想用 SDK 模式(Customer Comm App + CDR SDK) | 目前沒人這樣做、SDK 未開放 | Brian 評估 Roadmap |
| NDA | 客戶端 OK | MiTAC 端待確認 | Conant 內部跑 |
| 客戶帶 AI fine-tune | 想試 | 明確不行 | 已 close |
| Side Pod / BSM | 想要 Pricing | Validation 中,Q2 後期 ~ Q3 量產 | Conant 補 |
| AI Accuracy 第三方驗證 | 想看 | Brian 沒當場答 | 後續討論 |

## C3. 雙方都不確定的事
- 「High Level Integration Architecture」那張圖的來源(Brian 不知道、Vinicius 要回頭問 Vikran)
- 這代表客戶端內部對 MiTAC 平台的理解可能來自更早期的舊資料,後續溝通要小心客戶基於舊圖的期待

---

# Part D — 對 Kenny 的補課提示

下次客戶若直接問你,以下幾題目前答不出來:

| # | 補課項目 | 為什麼重要 | 找誰 / 哪裡 |
|---|---|---|---|
| 1 | **VisionMax CDR SDK 現狀** — 對外公開哪些 API、文件在哪、有沒有 Customer Comm App 整合先例 | Vinicius 量產架構直接卡這題 | 找 Brian 要 Standard SDK 文件 |
| 2 | **MyDN / MiDM Service 正式名稱與能力** | Peter 要規劃 App OTA;Conant 自己也叫不出正式名 | 找 Conant / 內部 Device Management 團隊 |
| 3 | **AI 訓練資料地區分布細節** | 客戶會繼續挖(尤其拓展到 EU/LATAM 時) | NotebookLM / KB 翻 AI 模型訓練文件 |
| 4 | **BSM Side Pod Camera 規格 + Q2~Q3 量產時程** | 客戶要 Pricing 估算 | Conant / Side Camera 產品線 |
| 5 | **K165 vs K265 差異 + Camera Cap 樣品** | 客戶用來給「不接受駕駛艙鏡頭」的次客戶,屬於關鍵差異化 | 拍實機照片 / 找樣品 |
| 6 | **CAN Decoder 兩種 Dongle 模式差異** | Peter 在乎的資料抽取介面 | OBD Dongle 產品線 + SDK 文件 |
| 7 | **新增製造據點地點** | 連 Conant 都沒答,可能是商業敏感,先確認可否對外 | Conant / Sales 內部 |

---

## 自測:讀完這份,30 秒內應能回答

1. **Vinicius 在這場最在意的兩件事** — 量產整合架構是否能走 SDK 模式;Q2 完成測試所需的 K265 樣品到位
2. **Conant 對客戶的 deliverables** — 簡報、SDK 文件、Pricing Sheet、K265 樣品、K165/Camera Cap、MyDN 文件、NDA 確認、Side Pod Pricing/時程、製造據點
3. **MiTAC 故意沒當場答的題目** — NDA 狀態、SDK 是否開放、AI Accuracy 第三方驗證、新增製造據點地點(客戶帶資料 fine-tune AI 屬明確 No,不算「沒答」)
