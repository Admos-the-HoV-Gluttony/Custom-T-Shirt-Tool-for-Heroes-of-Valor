@echo off
setlocal enabledelayedexpansion

echo Unpacking...
"data\tools\repak\repak.exe" unpack "data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor.pak"
if %errorlevel% equ 0 (
    echo Unpacking successful.
) else (
    echo Unpacking failed. Check the input file and try again.
)