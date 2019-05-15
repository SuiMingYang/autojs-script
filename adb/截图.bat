adb -s %1 shell /system/bin/screencap -p /sdcard/screenshot.png

IF NOT EXIST c:\screenshot md c:\screenshot

::set timestamp = %date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time~6,2%

@echo off

::set /p timestamp=filename:


adb pull /sdcard/screenshot.png C:/screenshot/

adb shell getprop | findstr meid


