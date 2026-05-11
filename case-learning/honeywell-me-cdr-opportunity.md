# Case Learning: Honeywell MiddleEast CDR Opportunity(2026-05-08 啟動)

> 新案 — Stark 2026-05-08 23:27 啟動,Brian 2026-05-09 10:09 FW 給 Kenny 等人,週一(5/11)上工後開始執行。

---

## 1. 案件基本資料

| 項目 | 內容 |
|------|------|
| 客戶 | Honeywell MiddleEast |
| 案件類型 | CDR(Commercial Dash-cam)新機會 |
| 啟動人 | Stark Yang(楊永吉 - MDT,Video Telematics Director)|
| 對外 sales | Paul Lee(李世博 - MDT,Account Sales Manager)|
| HW PM 對接 | Kevin Yhwang(王耀賢 - MDT)|
| VMX PM 對接 | **Brian Chienlee + Kenny Huang(本人)** |
| MiTAC RD 對接 | Righter Song / Conant Ho |
| 樣機機種 | **K220 × 1 + K265 × 1**(下週一 5/11 出樣)|
| 後續樣機 | K220 × 4 + K265 × 4 set |
| 第一單規模 | **5 月 6,000 pcs**(客戶要求先做這個量級報價)|
| 對外品牌 | **White-label Honeywell**(login logo + 機殼貼紙)|

---

## 2. Stark 5/8 23:27 給 Paul 的指令清單

1. **下週一(5/11)準備樣機**
   - K220 × 1 + K265 × 1
   - 含 open wires cable / OBD power cable / 點菸頭 cable
   - 跟 Brian 申請 **webbing SIM card**
   - 後面再準備 K220 × 4 + K265 × 4 set

2. **機構評估**:PM/機構 討論機構殼上能否貼 Honeywell logo sticker(或更好做法)

3. **Setup VisionMax Honeywell testing account**
   - Master & Fleet portal
   - sample import 至該 fleet 下
   - **Login logo 換 Honeywell logo**(white-label 雙 portal)

4. **K220 / K265 tier pricing**:週一上午會議討論,客戶要求先以第一單 5 月 6K pcs 量做報價

### Stark 分工 cc
- Hi Kevin:support Paul on sample preparation(cables / space mounting kit)
- Hi Brian:support SIM、VisionMax setup、sample field try、確保品質

---

## 3. Kenny 對接點(Brian FW 5/9 10:09)

Brian 把 Kenny 加進 list,意思是 **VisionMax setup(Master & Fleet portal + white-label login logo + sample import)** 這條線 Kenny 要實際做。

### Kenny 具體任務(待 Brian 5/11 上午對齊)

| 任務 | 對應 portal 操作 | 已知技術依據 |
|------|----------------|------------|
| 建 Honeywell main fleet | Master Portal > Management > Fleets > Create | 5/8 Sync-up 已 walk 過 |
| 換 login logo 為 Honeywell | Master Portal > (white-label config 位置) | **待確認**:Plan Type 是否影響 logo 客製 |
| Sample import 至 Honeywell fleet | Master Portal > (Inventory) | K220 + K265 SN 拿到後 |
| Plan type 對應 CDR + ADAS/DMS 啟用 | Fleet Portal > Plan Type config | 跟 Vinicius case 同議題,要拿 Brian / Conant 答案 |

### 跟現有 portal 知識的對位

- **Plan Type 議題**:5/6 Q2 review 提過 Plan Type 影響哪些 event / feature 啟用,Honeywell setup 是第一個實案
- **Contract Fleet 結構**:5/8 Sync-up Cary/Elvis 提的 per-contract-fleet config — Honeywell 若 reseller 客戶分 contract fleet,要看 VMX-5908 / VMX-6586 是否升級
- **Master Portal manual 撰寫**:Phil 5/8 已開始 Fleet Portal manual,**Master Portal manual 下週開工** → Honeywell setup 流程可變成 Phil manual 的實例範本

---

## 4. 風險點

| 風險 | 描述 | 對應動作 |
|-----|------|---------|
| White-label login logo 機制 KB 沒寫 | 不確定是 Master Portal 自助開關還是要 Spencer / Brian 後端改 config | 5/11 上午 Brian 對齊 |
| K220 + K265 tier pricing 沒拍板 | 客戶第一單 6K 要報價,定價人在 Stark / Paul | Kenny 不主導,但記下價格區間 |
| 5 月 6K 第一單交付風險 | 庫存 / 產能 / SIM 配發節奏 | Kevin Yhwang + Brian SIM 申請 |
| 機殼貼 Honeywell logo | 是否有 minimum order quantity / 客製週期 | PM/機構 評估 |
| 跟 Vinicius / Platform Science 機型重疊 | K220 + K265 也是 PS 測試機種,產能 / firmware 版本要對齊 | Brian / Conant 統一管 |

---

## 5. 利害關係人地圖

| 角色 | 人 | 任務 |
|------|----|------|
| 戰略 / Director | Stark Yang(楊永吉)| 啟動者,週一上午 tier pricing 拍板 |
| 主對外 sales | Paul Lee(李世博)| Honeywell 主對接 |
| HW PM | Kevin Yhwang(王耀賢)| Sample / cable / mounting kit |
| VMX 解決方案 | Brian Chienlee(李健)| 全責 — SIM、VMX setup、品質 |
| VMX PM | **Kenny Huang(本人)** | VMX setup 落地操作 |
| RD inventory / FW | Righter Song(宋祐全)| 樣機 inventory + firmware |
| RD 技術 PM | Conant Ho(何肇峯)| 技術窗口 |
| Marketing | Alicia Shih / Milky Ko | cc thread,可能後續 white-label brand 規劃 |

---

## 6. Action Items

### 🔥 P0(5/11 週一)
- [ ] 上午跟 Brian 對齊 Kenny 在 VMX setup 的具體 step
- [ ] 確認 white-label login logo 是 Master Portal 自助 / 後端 config / 還是要排開發
- [ ] 確認 Honeywell fleet 的 Plan Type 設定(對應 ADAS/DMS 啟用、Live View、Privacy Mode 等)
- [ ] 等 Righter / Kevin 把樣機 SN 給出來

### 📅 P1(本週 5/11–5/15)
- [ ] Honeywell fleet 建好 + 樣機 import + logo 換好(若 white-label 可自助)
- [ ] 把 Honeywell setup 流程記下來 → 給 Phil 當 Master Portal manual 範例

### 🎯 P2(下個 sprint)
- [ ] 跟 5 月 6K 出貨節奏對齊,確保 firmware 版本對得上
- [ ] 跟 Vinicius / PS 案的 K220 + K265 機種共用部分對齊

---

## 7. 跨檔案連結

- 5/8 Sync up Kenny/Cary/Elvis(per-contract-fleet 議題):[`meetings/2026-05-08_syncup-cary-elvis_meeting-record.md`](../meetings/2026-05-08_syncup-cary-elvis_meeting-record.md)
- Plan Type 議題:[`knowledge/03_systems-architecture/plan-types.md`](../knowledge/03_systems-architecture/plan-types.md)
- 5/6 Q2 review(戰略翻案 + Plan Type):[`meetings/2026-05-06_q2-request-review_meeting-record.md`](../meetings/2026-05-06_q2-request-review_meeting-record.md)
- 機種規格(K220 / K265):[`knowledge/01_product-knowledge/machines-spec.md`](../knowledge/01_product-knowledge/machines-spec.md)
- Vinicius / PS 案(機種共用):[`case-learning/vinicius-platform-science.md`](vinicius-platform-science.md)
- 本週 Weekly Summary:[`weekly-summary/2026-05-11_week-of-may-8.md`](../weekly-summary/2026-05-11_week-of-may-8.md)

---

_Created: 2026-05-11 by Kenny。等 5/11 上午 Brian 對齊後補 Section 3 具體任務拆解。_
