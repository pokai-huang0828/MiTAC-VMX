REM @echo off
cd %~dp0
adb devices
adb reboot bootloader

REM fastboot oem flashimage_enable

fastboot flash oem_a oem.img
fastboot flash oem_b oem.img
fastboot -w

fastboot reboot
pause
