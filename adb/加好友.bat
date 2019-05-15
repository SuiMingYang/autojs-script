
adb -s %1 shell input tap 660 107


adb -s %1 shell input tap 515 291


adb -s %1 shell input tap 332 250


@echo off

set /p userphone=phone number:


:: 输入手机号

adb -s %1 shell input text %userphone%


adb -s %1 shell input tap 353 218


:: adb shell input tap 385 825

:: 添加好友偏上
:: adb shell input tap 376 616
:: 添加好友偏下
adb -s %1 shell input tap 376 716
:: 发送
:: adb shell input tap 661 119
adb -s %1 shell input tap 39 101


adb -s %1 shell input tap 39 101


adb -s %1 shell input tap 39 101


adb -s %1 shell input tap 635 1223


adb -s %1 shell input tap 379 900


adb -s %1 shell input tap 398 1229

adb -s %1 shell input tap 543 809
adb -s %1 shell input tap 500 675

ping 0.0.0.0  -n 10
adb -s %1 shell input tap 106 609