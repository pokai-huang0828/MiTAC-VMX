Update tool:
- ADB tools
- QFIL
- qualcomm-driver
- image download site:
base: http://mdt-jenkins01.mic.com.tw/ReleaseImages/n702-android-dev/release/S40.19.2.7020.0.1.2.20251113-user-5651N7020004-FlashImage_2SD.zip

- region: http://mdt-jenkins01.mic.com.tw/ReleaseImages/n702-android-dev/RegionImage/VisionMaxPrecise/RGIMG_R00_5651N7020098_VisionMax_PreciseMRM_Prod_IMG.zip
 
Step:
01. 下載base/region image解壓縮後,將region 內的”oem.img” “rawprogram_keep_persist_region.xml”兩個檔案先複製到base image的資料夾中
02. 開啟cmd, 輸入”adb reboot edl”
03. Click “QFIL” tool and select “Flat Build”
04. a.Click “Select Port…”  b.Select port then click “OK”
05. a.Select Programmer   b.Click “Browse…”   c.Select “prog_firehose_ddr.elf”
06. Click “Load XML…”
07. Select “rawprogram_keep_persist_region.xml”
08. Then select “patch0.xml”
09. Click “Configuration”  and make sure that do not select “Erase All Before Download ”
10. Click “Download”
11. When status display “Download Succeed” , updating is finished
12. 使用Vysor or QTscrcpy tool 連線機器在app about確認base/region版本是否正確

==========================================================

安裝MMF，安裝版本如下.

ftp://PDA@10.87.105.205/VisionMax/MMF/TomTom/NA_2024Q3/mini_map_NA_9903.zip

pw: sc0ncs

01. 將mini_map.zip, debug.json放入SD Card根目錄
02. 將SD Card插入Device
03. 若Device沒有開機可直接到下個步驟，若已開機則需重起Device或Camera App(可直接搓Reset按鍵)
03. Device啟動後會聽到"Factory mode"後表示進入Factory mode
04. 安裝中, 需花費數分鐘...
05. 聽到"MMF initialization completed"後表示map安裝完成

*如在第五步驟後聽到以下語音表示安裝失敗:
01. "Please check MMF resource": 需要檢查放入SD Card的mini_map.zip和md5.txt是不是同一組。
02. "MMF resource installation failed: 可能mini_map.zip有問題。
03. "MMF Initialization failed": 安裝成功但mini_map.zip裡的檔案可能有問題, MMF無法進行初始化。
