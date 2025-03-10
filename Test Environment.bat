@echo off

if exist "data\Imported Game Files\HeroesOfValor.exe" (
    echo HeroesOfValor.exe found. Proceeding to menu.
) else (
    echo HeroesOfValor.exe not found. Running Setup Menu.bat.
    call "Setup Menu.bat"
    exit %errorlevel%
)

:menu
cls
echo ============================================
echo               Test Environment
echo ============================================
echo.
echo 1. Run Test Environment
echo 2. Help
echo.
echo 3. Texture Converter
echo 4. Setup Menu
echo.
echo 5. Exit
echo.
echo ============================================
echo.

set /p choice="Please select an option (1-5): "

if "%choice%" == "1" (
    start "" "data\Imported Game Files\HeroesOfValor.exe"
    pause > nul
    goto menu
) else if "%choice%" == "2" (
    call "data\tools\TE Help.bat"
    goto menu
) else if "%choice%" == "3" (
    call "Texture Converter.bat"
) else if "%choice%" == "4" (
    call "Setup Menu.bat"
) else if "%choice%" == "5" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto menu
)
