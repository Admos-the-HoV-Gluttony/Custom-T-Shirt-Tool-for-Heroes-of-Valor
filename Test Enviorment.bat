@echo off

if exist "data\Imported Game Files\HeroesOfValor.exe" (
    echo HeroesOfValor.exe found. Proceeding to menu.
) else (
    echo HeroesOfValor.exe not found. Running Setup Menu.bat.
    call "Setup Menu.bat"
    exit /b %errorlevel%
)

:menu
cls
echo ============================================
echo             Test Enviorment Menu
echo ============================================
echo.
echo 1. Run Test Environment
echo 2. Help
echo 3. Exit
echo.
echo ============================================
echo.

set /p choice = Please select an option (1-3):

if "%choice%" == "1" (
    start "" "data\Imported Game Files\HeroesOfValor.exe"
    pause > nul
    goto menu
) else if "%choice%" == "2" (
    call "data\tools\TE Help.bat"
    goto menu
) else if "%choice%" == "3" (
    exit /b 0
) else (
    echo Invalid choice. Please try again.
    pause
    goto menu
)
