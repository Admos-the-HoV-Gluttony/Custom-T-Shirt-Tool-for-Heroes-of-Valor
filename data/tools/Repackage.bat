@echo off
setlocal enabledelayedexpansion

echo Repackaging...
"data\tools\repak\repak.exe" pack "data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"
if %errorlevel% equ 0 (
    echo Repackaging successful.
) else (
    echo Repackaging failed.
)
