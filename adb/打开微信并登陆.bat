sleep 1
::ping 0.0.0.0  -n 1
adb -s %1 shell am start com.tencent.mm/com.tencent.mm.ui.LauncherUI 

sleep 1
ping 0.0.0.0  -n 3
adb -s %1 shell input tap 548 762


::ping 0.0.0.0  -n 1
adb -s %1 shell input tap 548 762




adb -s %1 shell input tap 182 1193


adb -s %1 shell input tap 116 602


@echo off

adb -s %1 shell input text %2


:: adb shell input tap 230 823
adb -s %1 shell input tap 351 498
 sleep 1


adb -s %1 shell input text %3


adb -s %1 shell input tap 360 670


