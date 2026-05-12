# 三層真相框架

## 核心命題

**對外用 Roadmap、對內用 Sheet、實際是否能用看 KB**。

```
┌─────────────────────────────────────────┐
│  KB         → 已 ship 的事實              │   對客戶可具體承諾
├─────────────────────────────────────────┤
│  Sheet      → 內部進行中                  │   PM 內部判斷依據
├─────────────────────────────────────────┤
│  Roadmap    → 對外規劃故事                │   客戶 / 主管的版本
└─────────────────────────────────────────┘
```

## 衝突處理規則

### 時程衝突 → Sheet 為真實時程(對 PM 內部判斷)
- 例:VLM,sheet 寫 2026 Q3,Roadmap 寫 2H'2027 → 內部知道是 Q3,但跟客戶 / 主管講就講 2H'2027

### 功能成熟度 → Sheet 為真實狀態
- 例:Smoking,sheet 顯示 active dev / Edge 70% 準確,Roadmap 列 Basic 已 ship → 對外可參照 Roadmap,**不能對客戶具體承諾上線時間**

### PIC / 沒人扛的 task → Sheet 才看得到
- Roadmap 永遠不會講「沒人扛」,Sheet No PIC 是 PM 真實情報
- ⚠️ 但 **Sheet hidden row = 不在使用**,別當「介入空間」(2026-05-05 校正)

### 跟客戶 / 主管 demo / PR → Roadmap 敘事
- ❌ 不要把 Sheet 內部 ETA / 客戶名 / 衝突狀態講出去

### 跟 RD / 內部 PM 討論 → Sheet 數據
- ✅ 拿 Sheet 進度、PIC、ticket 號講事實

## 踩線警告

- ❌ 把 Sheet ETA(VLM 2026 Q3)直接告訴客戶 → 過早承諾
- ❌ 把 Roadmap 的「Basic tier 有 Smoking / Yawning」當成「production 已支援」對客戶講 → 後面客戶測不到會炸
- ✅ 對客戶說「在我們 Roadmap 裡的 Basic tier」+「實際上線時間請我內部確認」

## 已知三層不一致(2026-05-07 更新)

| 主題 | KB | Sheet | Roadmap | 對客戶口徑 |
|------|----|----|---------|-----------|
| Yawning | 沒寫 | 內部測試,效果不如預期 / **5/7:加灰階模型,考慮改辨識整張臉 / UI = [VMX-7432](https://jira.navman.co.nz/jira/browse/VMX-7432)(Lucy)** | Basic 2025 已 ship | Roadmap planned, 內部測試中 |
| Smoking | **(in development)** | row 隱藏 / 4 ticket open | Basic 2025 已 ship | Roadmap planned, KB 列開發中 |
| MMF | 沒寫 | 沒上線 | overview 列 | 不對客戶承諾 |
| VLM | 沒寫 | 2026 Q3(內部目標,但 5/7 仍 pending pending pending)| 2H'2027 | 講 2027 |
| Eating/Drinking | 沒寫 | [HAWK-562](https://jira.navman.co.nz/jira/browse/HAWK-562) / **5/7:BMS 客訴 17x 量級(ID 6652),6/15 前 7000+ 案例緊急重訓** | Advanced 2027 | 對外講 2027,**對 BMS 講 6/15 內部緊急重訓** |
| Server LDWS | 沒寫 | **Q1 deploy prod / Device-side YOLO Pending 暫緩(5/7)** | Stage 2 已上 | 「Server-side 已部屬,device 端持續改善」 |
| Speed Sign | (in development) | **5/7:Flip 參數關閉 + 擴增降至 10x 重訓**(Jay)| Advanced 2027 | KB 列開發中 |
| Lens Cover BMS / Azuga 雙軌 | 沒寫 | **5/7 規格分歧**:Azuga = 解除車速 / BMS = 車速 > 0 | Basic | 對 Azuga 講標準版,對 BMS 講「車速 > 0」 |
