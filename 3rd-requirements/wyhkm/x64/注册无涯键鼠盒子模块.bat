@echo off
if exist %windir%\System32\wyhkm.dll goto reg1
if exist %windir%\SysWOW64\wyhkm.dll goto reg2
if exist wyhkm.dll goto reg1
echo 未找到无涯键鼠盒子模块,请将该批处理文件与无涯键鼠盒子模块放在同一文件夹里
pause
exit
:reg1
regsvr32.exe /n /i:user wyhkm.dll
if %errorlevel%==0 (
 echo 注册成功
) else (
 echo 注册失败
)
pause
exit
:reg2
%windir%\SysWOW64\regsvr32.exe /n /i:user wyhkm.dll
if %errorlevel%==0 (
 echo 注册成功
) else (
 echo 注册失败
)
pause
exit