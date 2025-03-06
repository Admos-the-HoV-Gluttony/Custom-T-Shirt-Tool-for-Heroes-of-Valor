@echo off
setlocal

set "url=https://github.com/matyalatte/UE4-DDS-Tools/releases/download/v0.6.1/UE4-DDS-Tools-v0.6.1-Batch.zip"
set "zipFile=UE4-DDS-Tools-v0.6.1-Batch.zip"
set "destinationFolder=data\tools\DDS-Tools-v0.6.1-Batch"

if not exist "%destinationFolder%" (
    mkdir "%destinationFolder%"
)

pushd "%destinationFolder%"

curl -L -o "%zipFile%" "%url%"

if errorlevel 1 (
    echo Failed to download the file.
    popd
    exit /b 1
)

powershell -Command "Expand-Archive -Path '%zipFile%' -DestinationPath '.'"

if errorlevel 1 (
    echo Failed to unpack the file.
    del "%zipFile%"
    popd
    exit /b 1
)

del "%zipFile%"

popd

copy "data\tools\dds.py" "%destinationFolder%\src\directx\dds.py"

if errorlevel 1 (
    echo Failed to overwrite dds.py.
    exit /b 1
)

echo Download, unpack, and overwrite completed successfully.

endlocal