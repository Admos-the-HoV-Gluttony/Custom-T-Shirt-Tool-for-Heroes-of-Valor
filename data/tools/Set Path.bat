@echo off
setlocal

REM Check if path.txt exists and is not empty
if exist path.txt (
    for /f %%i in (path.txt) do set "savedPath=%%i"
    if defined savedPath (
        echo Path to Heroes of Valor Playtest already provided: %savedPath%
        goto :eof
    )
)

set /p userPath="Please enter the path to 'Heroes of Valor Playtest' Game Files: "

REM Save the provided path in path.txt
echo %userPath% > data\tools\path.txt

echo Path saved successfully!
goto :eof
