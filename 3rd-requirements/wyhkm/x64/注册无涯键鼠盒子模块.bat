@echo off
if exist %windir%\System32\wyhkm.dll goto reg1
if exist %windir%\SysWOW64\wyhkm.dll goto reg2
if exist wyhkm.dll goto reg1
echo δ�ҵ����ļ������ģ��,�뽫���������ļ������ļ������ģ�����ͬһ�ļ�����
pause
exit
:reg1
regsvr32.exe /n /i:user wyhkm.dll
if %errorlevel%==0 (
 echo ע��ɹ�
) else (
 echo ע��ʧ��
)
pause
exit
:reg2
%windir%\SysWOW64\regsvr32.exe /n /i:user wyhkm.dll
if %errorlevel%==0 (
 echo ע��ɹ�
) else (
 echo ע��ʧ��
)
pause
exit