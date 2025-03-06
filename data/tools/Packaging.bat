@echo off
:menu
cls
echo =========================================================
echo  		     Packaging Tools
echo =========================================================
echo 1. Unpackage
echo 2. Repackage
echo 3. Return to Texture Converter
echo =========================================================

set /p choice=Choose an option [1-3]: 

if "%choice%"=="1" goto unpackage
if "%choice%"=="2" goto repackage
if "%choice%"=="3" goto exit

:unpackage
cls
echo Unpacking...
call "data\tools\Unpackage.bat"
goto menu

:repackage
cls
echo Repacking...
call "data\tools\Repackage.bat"
goto menu

:exit
cls
exit /b 0
