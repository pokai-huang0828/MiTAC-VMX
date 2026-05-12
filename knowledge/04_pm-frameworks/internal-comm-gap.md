# 內部溝通斷層

> 源自 Wendy 案 + 2026-05-06 Sheet/Jira 同步缺口發現

## 業務端不滿的根因表

| 業務感受 | 根因 | PM 解法 |
|---------|------|---------|
| 「不知道功能什麼時候出」 | 產品端沒主動輸出 roadmap | 建立定期 roadmap sync(每季) |
| 「不知道能否承諾」 | 承諾層次太粗,沒里程碑 | 提供「確認日期」而非「上線日期」 |
| 「功能說好有,但用不了」 | 原型 ≠ 可交付,差異未傳達 | 早期清楚說就緒條件 |
| 「感覺被蒙在鼓裡」 | 無常態資訊流,只有被動回應 | 主動推播,**沒進展也要說** |

## 核心洞察

**業務端的不滿通常是資訊不對稱,不是情緒問題**。

PM 有責任主動輸出資訊,即使功能沒進展,也要讓業務端知道「我們知道、目前狀態是 X」。

## Sheet ↔ Jira 雙向同步缺口(2026-05-06 發現)

PM 角色升級成「Sheet/Jira sync owner」,要處理兩個方向的落差:

### 方向 1:Sheet 落後 Jira(Jira 已關 Sheet 沒改)
- 例:[VMX-6754](https://jira.navman.co.nz/jira/browse/VMX-6754) / 7029 / 7161 / 7162 — 5/6 Q2 Review 前
- 業務端看 Sheet 以為「拖了 7 個月」,實際 RD 已交付

### 方向 2:Sheet 領先 Jira(口頭說完成,Jira 沒 close)
- 例:[VMX-7082](https://jira.navman.co.nz/jira/browse/VMX-7082) / 7233 / 6782 — 5/6 Q2 Review 後新生成
- 「我做完了」≠ Jira ticket transition

## PM 介入動作

每兩週做一次 Sheet × Jira sweep:
1. 撈 Sheet 顯示 In Process 的 ticket
2. 比對 Jira 真實狀態
3. 兩個方向 mismatch 都私訊 owner 確認
4. 同步後在 Sheet 加 sweep 紀錄

→ 這就是評估期 PM 真實的「沒人扛 = 我來扛」入口。

## 對應到 VMX 內部具體案件

| 案件 | 業務端感受 | PM 解法 |
|------|----------|---------|
| #11 OTA 17 個月 Brian 自己提 | 看似 stale | **不是內部問題,Akamai 設定錯,Brian 自己不在意** |
| Yawning(對外 Roadmap 已有 vs 內部測試中) | 客戶以為已 ship | 對外口徑統一改「Roadmap planned」/ **5/7 補:UI toggle 對應 [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(Lucy)** |
| Smoking(KB 標 in development / Sheet 隱藏 / Roadmap 列) | 業務不確定能否賣 | 給 sales 統一口徑「KB 列開發中」(KB 有官方依據)|
| #154 Server AI([VMX-6722](https://jira.navman.co.nz/jira/browse/VMX-6722))| API 沒釋出 | **5/7 校正:不是 label 漏 pick,是 transition discipline gap** — RD 寫 deploy comment 但沒按 Open→Resolved button。對 Brian 提改善從「transition 紀律」切入 |
| **Lens Cover 雙軌維護(5/7)**| 客戶規格分歧 | 對 Azuga 講「標準版解除車速」,對 BMS 講「車速 > 0」 — 別混 |
| **Eating 17x 客訴 ID 6652(5/7)**| BMS 客訴爆炸 | 對外 Roadmap 維持 2027,對 BMS 講 6/15 緊急重訓進度 |

## ✅ Wendy = wendy.hammond / MiTAC AU(2026-05-08 解密)

Wendy 是 Hub 第三 tab「資訊不對稱框架原型」對應的真實人物。

| 項目 | 值 |
|------|---|
| 全名 | wendy.hammond |
| Email | wendy.hammond@mitac.com.au |
| 部門 | **MiTAC AU(澳洲)** — 跟 Cary Lo 同部門 |
| 角色 | 業務 / 客戶代表(代 reseller 客戶端傳達需求) |
| 案件 | PASSENGER BLURRING / 跨 reseller feature reuse |
| 訴求 | 「conception stage 早期介入,save work 給 regional teams」(5/5 信原話) |

她的案 = **「資訊不對稱框架原型」最完整體現**:外部 stakeholder 只能在 feature 已 ship 後才知道,要從事後告知改成早期介入。Brian 5/4 回應提供 Sheet + AI Roadmap doc sync 入口,屬於「結構性解法」而非個案處理。

詳見 stakeholders.md MiTAC AU 列 + memory `reference_wendy_hammond_identity.md`。
