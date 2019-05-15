@echo off
:S
echo 1.��΢�Ų���½
echo 2.��½
echo 3.��ͼ
echo 4.�Ӻ���
set /p commend=����ָ�

echo start
if %commend% == 1  (
    call ��΢�Ų���½.bat %1 %2 %3
) else if %commend% == 2  (
    call ��½.bat %1 %2 %3
) else if %commend% == 3  (
    call ��ͼ.bat %1 %2 %3
) else if %commend% == 4  (
    call �Ӻ���.bat %1 %2 %3
) else (
    echo ����������
)
echo end

goto S