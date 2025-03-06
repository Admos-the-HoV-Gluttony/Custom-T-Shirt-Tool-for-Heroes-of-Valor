@echo off
setlocal

set "url=https://github.com/trumank/repak/releases/download/v0.2.2/repak_cli-x86_64-pc-windows-msvc.zip"
set "zipFile=repak_cli-x86_64-pc-windows-msvc.zip"
set "destinationFolder=data\tools\repak"

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
)

echo Download and unpack completed successfully.

endlocal
