# Troubleshooting Checklist(對 fleet manager / 技術人員)

> 來源:KB Troubleshooting + Diagnostics + 各機種 LED Behaviors(2026-05-06 deep read)

## 客戶報修第一層 checklist

### Q1. 設備沒開機
**KB 線索**:
- LED 紅燈 60 秒以上閃 = camera 沒在錄 / 即將關機
- 數分鐘內會 shut down

**檢查**:
- 電源連接 / ignition line(loose contact)
- 保險絲(power line)
- Manual ignition switch(部分版本有,要 ON)

### Q2. GPS Function 失效(導致 ADAS / DMS 都不偵測)
**KB Diagnostic Q1**:Location Function — GPS 10 分鐘沒訊號
**影響**:不能建 trip / 不能偵測 ADAS / DMS / 不能記錄 video 位置
**Solution**:確保車輛在 open area,GPS 收得到

### Q3. ADAS 觸發失敗(常見!)
**症狀**:`"Can't detect the road level, ADAS off"` 語音
**真因 1**:速度沒滿足 **30 km/h × 3 分鐘 + 平坦少彎**
**真因 2**:Camera height 設錯(車種不對應)
**真因 3**:GPS 失效(連帶)
**Solution**:
- 開出市區到高速公路維持速度
- Master Portal Diagnostics 看 ADAS AI Health
- 確認 Vehicle Class 設對(passenger/medium/heavy)

### Q4. Sensor Events 不觸發
**KB Diagnostic Q2**:Sensor Events Detection 失敗
**Solution**:檢查 device 安裝是否正確

### Q5. SD card 找不到 / 錯誤
**KB**:
- 「No SD Card」語音 — 沒插
- 「SD Card Error」語音 — 讀寫錯誤
- 紅燈每 15 秒閃一次(K220/K245/K265)
**Solution**:
- 插 SD card / 換 SD card
- KB「SD Card Overwriting Mechanism」 — 看是否容量問題
- 紅色按鍵 hold 10-30s 重格式化(`"SD Card formatting, please wait"`)

### Q6. Network / APN 不通
**KB**:K265 orange LED 常亮 = 沒網路
**Solution**:VisionAgent app → 設 APN(海外 SIM 常見)

### Q7. Driver 卡讀不到
**KB**:「Failed to read the ID Card」語音
**Solution**:
- 對齊 NFC symbol
- 換 supported NFC 格式
- K220:確認用 QR Code(K220 不支援 RFID)
- K145(c):需 i25 才能 QR

### Q8. Privacy Mode 卡住(設備不錄)
**症狀**:`"Private Mode On"` 進去後沒再退
**KB**:Privacy Mode 不會自動退,**Restart 後仍維持**
**Solution**:Panic Button hold > 2s(KB)→ `"Private Mode Off"`

### Q9. Calibration 一直不完成
**KB**:
- ADAS:60 km/h × 3 min(KB 寫 — 注意這是 *初次 calibration* 條件,跟持續門檻 30 不同)
- DMS:20 km/h × 15 秒,臉穩定即可
- 完成語音「Calibration Completed」
**Solution**:開高速直線路段

### Q10. Camera 重置(最後手段)
**KB:How to reset device**:
- 用 paper clip 戳 reset button
- ⚠️ K245 / K145c / K245c:reset button 在 **tamper proof cover** 後面,要先拆

## 對技術人員 escalation
- VisionAgent → Diagnostic Scan → 看 health report
- 如果還不行 → Master Portal 看 Diagnostics 頁
- 還不行 → KB「How to export the system logs from K220」(K220 special)→ Submit Ticket

## 對應 PM ticket

- VMX-7404 ADAS Failure → Q3 多重原因
- VMX-7194 Rollover → Q4 sensor 系列
- VMX-7427 Quantatec obstruction → 屬 Q9 範疇(camera 看不到驅動者)
- VMX-7407 UVC RAW frame error → 屬 Q2 範疇(sensor 不識別)
