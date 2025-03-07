@echo off
setlocal

cls

set /p userPath="Please enter the path to 'Heroes of Valor Playtest' Game Files: "

echo %userPath% > data\tools\path.txt

echo Path saved successfully!
goto :eof
