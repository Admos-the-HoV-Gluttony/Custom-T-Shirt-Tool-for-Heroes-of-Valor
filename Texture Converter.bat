@echo off

:menu
cls
echo ============================================
echo            Texture Converter Menu
echo ============================================
echo.
echo 1. Packaging Tools
echo 2. Inject Texture
echo 3. Export Modified Files
echo 4. Help
echo.
echo 5. Test Environment
echo 6. Setup Menu
echo.
echo 7. Exit
echo.
echo ============================================
echo.

set /p choice="Please select an option (1-7): "

if "%choice%" == "1" (
    call "data\tools\Packaging.bat"
) else if "%choice%" == "2" (
    call "data\tools\Inject.bat"
) else if "%choice%" == "3" (
    call "data\tools\Export.bat"
) else if "%choice%" == "4" (
    call "data\tools\TC Help.bat"
) else if "%choice%" == "5" (
    call "Test Environment.bat"
) else if "%choice%" == "6" (
    call "Setup Menu.bat"
) else if "%choice%" == "7" (
    exit
) else (
    echo Invalid Input. Please select a number between 1 and 7.
    pause
)

goto menu
