# VisionAgent App(技術人員 / 客戶端工具)

> 來源:KB VisionAgent 3 篇(2026-05-06 deep read)
> 用途:技術人員 / 客戶安裝 / 配置設備時用的 smartphone app

## 是什麼

VisionAgent = smartphone app(iOS / Android)用來配置 / 診斷 VMX 設備。

對應 sheet #195「[VisionAgent] 埋GA Code」/ #182「[VisionAgent] iOS Map Overview」等多筆 ticket。

## 連線方式

- **WiFi**(主要)— 設備開 hotspot,smartphone 連
- **BT**:KB 沒明確支援(待釐清)

## 主要功能

### 1. Camera Install Position 檢查
- KB 文章:How to Check Camera Install Position
- 用途:技術人員裝相機時用手機看 live view 確認位置 OK
- 對應 Vehicle Class 的 height 設定(passenger / medium / heavy 各有 height + AI param)

### 2. APN 設定(SIM 卡網路設定)
- KB 文章:How do I set APN for the SIM in the camera through VisionAgent?
- 用途:更換 SIM 卡 / 海外不同電信商時透過 VisionAgent 設定 APN
- 對應 OTA / connectivity 議題

### 3. Live View + Health Status + Diagnostic Scan
- KB 文章:Can I use a smartphone to connect to the device via WiFi or BT?
- 連線後可:
  - 看 live view(裝相機時對位置)
  - 觸發 device health status 上報
  - 跑 diagnostic scan

## 對 PM 議題的對應

### iOS App 開發中([VMX-7373](https://jira.navman.co.nz/jira/browse/VMX-7373) to 7381 多筆 ticket)
- [VMX-7373](https://jira.navman.co.nz/jira/browse/VMX-7373) [iOS] Add Parking Photo Button
- [VMX-7374](https://jira.navman.co.nz/jira/browse/VMX-7374) [iOS] Add Manual End Button on Trip Details
- [VMX-7375](https://jira.navman.co.nz/jira/browse/VMX-7375) [iOS] Add Manual End Button
- [VMX-7377](https://jira.navman.co.nz/jira/browse/VMX-7377) [iOS] Can't Access Driver Info from Map Overview
- [VMX-7381](https://jira.navman.co.nz/jira/browse/VMX-7381) [iOS] 無法刪除 Event
- → 對應 sheet 上 Fleet Mobile APP Push notification(#176 / [VMX-7030](https://jira.navman.co.nz/jira/browse/VMX-7030) / Pending)

### KB 跟 Sheet 不同層
- KB 對應的「VisionAgent」= 給技術人員裝相機用的 app
- Sheet「Fleet Mobile APP」= 給 fleet manager 用的管理 app
- **是兩個不同的 app**!別混淆

## 客戶口徑

> 「VisionAgent 是給安裝技術人員 / 客戶端 power user 用的工具,可以裝相機時看 live view、設 APN、跑 diagnostic。Fleet Manager 日常用 web portal,iOS App 在開發中。」
