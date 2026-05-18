# [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure 追蹤

> Jira:[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)
> 評估期最大籌碼,Kenny 主追。
> 最後更新:**2026-05-18 · 加 VMX-7470 ANR crash 同根因(jay.qiu 5/15 confirm root cause = HAWK-574)→ 證據強化:不是「Webfleet 特殊安裝」,是 SDK 層 race condition,所有客戶都暴露**

---

## 現況

- **8/10 設備** ADAS AI Health = ADAS Failure(包含 Kenny 的 K245 L3024290010)
- 真因(2026-05-05 校正):**30 km/h × 3 mins** 行駛條件門檻沒滿足 → 市區走停會反覆觸發
  - 詳細校正見 [critical-facts-log.md](critical-facts-log.md#adas-觸發時間--calibration-條件)
- **🆕 2026-05-13 跨客戶撞線**:**Platform Science (Vinicius Francisquinho)** 在 K265 L1225380005 撞同根因
  - 5/13 06:2X Vinicius mail thread 反映 ADAS Failure + reboot 無效
  - Righter 5/13 11:41 reply 已給 install + 30 km/h drive on lane-markings SOP
  - **意義**:VMX-7404 不只是 Kenny 自測 + Webfleet [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501),現在 PS 也是 = **第三家客戶撞同根因**,跨客戶影響範圍擴大

## Evidence

### Trip-level(Kenny 自測 K245 L3024290010)
| Trip | 平均速度 | ADAS Started | 韌體 | 結論 |
|------|---------|--------------|------|------|
| 7028714 | ~25 km/h | 缺 | 同 | 市區走停 → 觸發 ADAS Failure |
| 7079470 | 30+ km/h | 有 | 同 | 滿足條件 → 正常運作 |

### 跨客戶撞線(2026-05-13 新增 / 2026-05-18 強化)
| 客戶 | 設備 | 狀況 | 來源 thread |
|------|------|------|------------|
| Kenny 自測(MiTAC 內部)| K245 L3024290010 | 8/10 trip 為 ADAS Failure,30 km/h × 3 mins 門檻 | repo 內 trip 7028714/7079470 對照 |
| Webfleet (HAWK 線) | — | 安裝高度 / 行駛條件議題 | [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) self-calibration wrong height + [HAWK-574](https://jira.navman.co.nz/jira/browse/HAWK-574) DMS calibration loop + [HAWK-401](https://jira.navman.co.nz/jira/browse/HAWK-401) low install position |
| Platform Science(VMX 線) | K265 L1225380005 | OTA + SDK ✅ 但 ADAS Failure 持續 · reboot 無效 | Vinicius 5/13 06:2X mail → Righter 5/13 11:41 install + 30 km/h SOP reply · **5/14 12:17 Vinicius ack「Thanks Righter. I will do that!」** |
| **🆕 MiTAC 自測 K245 跑 11.2.27.5(VMX-7470)** | K245 (MiTAC 內部 / righter.song reporter)| ANR crash on camera App 11.2.27.5(5/12 開) | **5/15 12:00 jay.qiu 在 [VMX-7470](https://jira.navman.co.nz/jira/browse/VMX-7470) confirm:此 Crash 根本原因與 [HAWK-574](https://jira.navman.co.nz/jira/browse/HAWK-574) 相同 = Race Condition + Dangling Pointer Read + Memory Corruption** · fix 在 MiAIServiceApp 1.4.43.3 + SdkMiAIService 1.4.44(build 11.2.27.7) |

### 🎯 2026-05-18 重大證據強化
- 過去 3 家撞線(Kenny / Webfleet / PS)當下還可以辯「客戶側安裝環境特殊」
- **現在第四條證據 = VMX-7470 是 MiTAC 自家 K245 跑同一個 build 也撞同 root cause** → **客戶端環境不是主因,SDK 層 race condition 是主因**
- HAWK-574 已被 jay.qiu 標為「同一個地方的 Race Condition + Dangling Pointer Read + Memory Corruption」→ 證明 HAWK-501/574/401 + VMX-7470 + VMX-7404 都暴露同類 SDK 層 concurrency bug
- **對 Brian 1on1 戰略**:這是 evaluation 期最強籌碼 — 「不是 single customer 客訴,是 SDK 層 systemic bug,影響所有客戶」

## 待動作

- [ ] 把 evidence 寫成 Jira comment 貼進 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)(現在更有價值 — 3 客戶 + MiTAC 自測 4 條 cross-customer 證據 + jay.qiu confirm SDK race condition)
- [ ] Coffee chat 找 Jimmy 確認 Face Not Found Issue 是否同根因(見 [coffee-chat-questions.md](../02_organization-map/coffee-chat-questions.md))
- [ ] **🆕 觀察 PS Vinicius 5/14 ack 後**:5/14 12:17 Vinicius 已回「Thanks Righter. I will do that!」→ 等他實測 install + drive after 30 km/h 結果。若仍 fail,**升級成 Jira ticket 由 Kenny 領 root cause** — 評估期重大 PM 表現機會
- [ ] **🆕 跟 Brian 下次 1on1 提**:VMX-7404 跨客戶影響範圍 4 條(Kenny / Webfleet HAWK-501/574/401 / PS / MiTAC 自測 VMX-7470)+ jay.qiu SDK 層 race condition 確認 → Steve KPI 100K 評估期戰略點
- [ ] **🆕 確認 fix 已 ship 給所有客戶**:`MiAIServiceApp 1.4.43.3` + `SdkMiAIService 1.4.44`(build 11.2.27.7)是否已 rollout 到 Webfleet / Azuga / PS。若沒,主動推 release

## 相關文件

- [01_product-knowledge/diagnostics.md](../01_product-knowledge/diagnostics.md#vmx-7404-adas-failure) — KB 對應 Location Function 問題
- [05_workflows/troubleshooting.md](../05_workflows/troubleshooting.md) — 多重原因 troubleshoot 流程
- [01_product-knowledge/voice-alerts.md](../01_product-knowledge/voice-alerts.md) — `"Can't detect the road level, ADAS off"` 觸發語音

---

## H. HAWK 側平行案(2026-05-11 補)

| Jira | Title | 對 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 的關聯 |
|------|-------|------------------|
| [HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) | ADAS Self-calibration resolves wrong height resulting inacurate ADAS event detection | **同族問題,HAWK 客戶側現象** — self-calibration 算出來的高度錯誤,導致 ADAS event 偵測不準。可能跟 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 同根因(行駛條件 + calibration 資料不足)|
| [HAWK-574](https://jira.navman.co.nz/jira/browse/HAWK-574) | WEBFLEET Alpha Fleet Cameras Sporadically Looping "DMS Calibration Completed" Message | DMS 側 calibration UX 異常,跟 ADAS calibration 同類但 DMS 端 |
| [HAWK-401](https://jira.navman.co.nz/jira/browse/HAWK-401) | Support proper DMS AI detection with low installation position | 安裝位置低時 DMS 失準 — 跟 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 一樣是「安裝/條件」議題 |

**洞察**:[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) 是 PS / Kenny 個人測試曝光的問題,[HAWK-501](https://jira.navman.co.nz/jira/browse/HAWK-501) 是 Webfleet 客戶端同問題的對應 ticket。Kenny 寫 Jira comment 時可以 cross-reference,把「行駛條件 30 km/h × 3 mins」這條 root cause 同步給 HAWK assignee。

---

_2026-05-11 update:加 H 段 HAWK 側對照(由 weekly summary 2026-05-11 衍生)。_
