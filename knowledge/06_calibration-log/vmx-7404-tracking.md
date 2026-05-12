# [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404) ADAS Failure 追蹤

> Jira:[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)
> 評估期最大籌碼,Kenny 主追。
> 最後更新:2026-05-11

---

## 現況

- **8/10 設備** ADAS AI Health = ADAS Failure(包含 Kenny 的 K245 L3024290010)
- 真因(2026-05-05 校正):**30 km/h × 3 mins** 行駛條件門檻沒滿足 → 市區走停會反覆觸發
  - 詳細校正見 [critical-facts-log.md](critical-facts-log.md#adas-觸發時間--calibration-條件)

## Evidence

| Trip | 平均速度 | ADAS Started | 韌體 | 結論 |
|------|---------|--------------|------|------|
| 7028714 | ~25 km/h | 缺 | 同 | 市區走停 → 觸發 ADAS Failure |
| 7079470 | 30+ km/h | 有 | 同 | 滿足條件 → 正常運作 |

## 待動作

- [ ] 把 evidence 寫成 Jira comment 貼進 [VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)
- [ ] Coffee chat 找 Jimmy 確認 Face Not Found Issue 是否同根因(見 [coffee-chat-questions.md](../02_organization-map/coffee-chat-questions.md))

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
