@echo off

setlocal
set "downloadUrl=https://github.com/Admos-the-HoV-Gluttony/Custom-T-Shirt-Tool-for-Heroes-of-Valor/archive/refs/heads/main.zip"
set "zipFile=%TEMP%\main.zip"
set "extractPath=.."
echo Download and extract the latest version of the Custom T-Shirt Tool for Heroes of Valor.
echo The previous version of the tool will be overwritten in the process.
echo.
choice /C YN /M "Do you want to proceed with the update? "

if errorlevel 2 (
    echo Download cancelled by user.
    exit /b 0
)

powershell -Command "(New-Object Net.WebClient).DownloadFile('%downloadUrl%', '%zipFile%')"

if not exist "%zipFile%" (
    echo Failed to download the ZIP file.
    exit /b 1
)

powershell -Command "Expand-Archive -Path '%zipFile%' -DestinationPath '%extractPath%' -Force"

if exist "%zipFile%" (
    echo Extraction complete.
) else (
    echo Failed to extract the ZIP file.
    exit /b 1
)

del "%zipFile%"

echo Process completed successfully.
endlocal