@echo off

:menu
cls
echo ============================================
echo           	 Setup Menu
echo ============================================
echo.
echo 1. DL and Extract repak v0.2.2
echo 2. DL, Extract and Fix UE4 DDS Tools v0.6.1
echo 3. Set Path to Game Files
echo 4. Import Game Files
echo 5. Quit
echo.
echo ============================================
echo.

set /p choice="Select an option (1-5): "

if "%choice%" == "1" (
    call "data\tools\DL & Extract repak v0.2.2.bat"
) else if "%choice%" == "2" (
    call "data\tools\DL, Extract & Fix UE4-DDS-Tools-v0.6.1-Batch.bat"
) else if "%choice%" == "3" (
    call "data\tools\Set Path"
) else if "%choice%" == "4" (
    call "data\tools\Import.bat"
) else if "%choice%" == "5" (
    echo Quitting the program.
    exit /b
) else (
    echo Invalid option. Please select a number between 1 and 5.
)

goto menu
