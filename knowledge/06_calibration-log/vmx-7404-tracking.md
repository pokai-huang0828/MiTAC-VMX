# VMX-7404 ADAS Failure 追蹤

> Jira:[VMX-7404](https://jira.navman.co.nz/jira/browse/VMX-7404)
> 評估期最大籌碼,Kenny 主追。
> 最後更新:2026-05-06

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
