REM @echo off
cd %~dp0
adb devices
adb reboot bootloader

fastboot flash boot_a boot.img
fastboot flash boot_b boot.img
fastboot flash system_a system.img
fastboot flash system_b system.img
fastboot flash vendor_a vendor.img
fastboot flash vendor_b vendor.img
fastboot flash dtbo_a dtbo.img
fastboot flash dtbo_b dtbo.img
fastboot flash vbmeta_a vbmeta.img
fastboot flash vbmeta_b vbmeta.img
fastboot flash oem_a oem.img
fastboot flash oem_b oem.img
fastboot flash userdata userdata.img

fastboot reboot
pause
