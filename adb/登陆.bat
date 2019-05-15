sleep 1

@echo off

:: 修改微信账户名

adb -s %1 shell input text %2


adb -s %1 shell input tap 326 490

sleep 1

adb -s %1 shell input text %3

adb -s %1 shell input tap 360 670