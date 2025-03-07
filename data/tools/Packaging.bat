@echo off
:menu

cls
echo ============================================
echo             Packaging Tools Menu
echo ============================================
echo.
echo 1. Unpackage
echo 2. Repackage
echo 3. Quit
echo.
echo ============================================
echo.
set /p choice=Choose an option (1-3): 

if "%choice%"=="1" (
    call "data\tools\Unpackage.bat"
) else if "%choice%"=="2" (
    call "data\tools\Repackage.bat"
) else if "%choice%"=="3" (
    echo Quitting the program.
    exit /b 0
) else (
    echo Invalid option. Please select a number between 1 and 3.
)

goto menu
