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
echo 5. Exit
echo.
echo ============================================
echo.
set /p choice="Select an option (1-5): "

if "%choice%"=="1" (
    call "data\tools\Packaging.bat"
) else if "%choice%"=="2" (
    call "data\tools\Inject.bat"
    REM Add the code to inject texture here
) else if "%choice%"=="3" (
    call "data\tools\Export.bat"
) else if "%choice%"=="4" (
    call "data\tools\TC Help.bat"
) else if "%choice%"=="5" (
    echo Exiting the program.
    exit /b
) else (
    echo Invalid option. Please select a number between 1 and 5.
    pause
)

goto menu
