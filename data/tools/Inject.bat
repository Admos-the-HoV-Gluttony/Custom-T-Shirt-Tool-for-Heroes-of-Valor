@echo off
setlocal enabledelayedexpansion

set /a count=0

set "uassetList[1]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_NightCamo.uasset"
set "uassetList[2]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_GreenCamo.uasset"
set "uassetList[3]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Frankenstein_C.uasset"
set "uassetList[4]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Dracula_C.uasset"
set "uassetList[5]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Banana.uasset"
set "uassetList[6]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Wolf.uasset"
set "uassetList[7]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Playtest_Axis.uasset"
set "uassetList[8]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Playtest_Allied.uasset"

for /L %%i in (1,1,8) do (
    set /a count+=1
)

:menu
cls
echo Please select one of the following UASSET files to override:
echo.
for /L %%i in (1,1,%count%) do (
    for %%f in ("!uassetList[%%i]!") do (
        set "filename=%%~nxf"
    )
    echo [%%i] !filename!
)
echo.
echo [0] Exit
echo.
set /p choice=Enter your choice: 

if %choice% equ 0 (
    echo Exiting.
    exit /b

)

if not defined uassetList[%choice%] (
    echo Invalid choice. Returning to menu.
    goto :menu
)

set "selectedUasset=!uassetList[%choice%]!"

cls
echo Please provide the path to a PNG file or drag and drop it here:
echo.
echo If a PNG file isn't working, consider simplifying the filename to something like 'texture'.
echo.
set /p pngFile=Enter the path to a PNG file: 

data\tools\DDS-Tools-v0.6.1-Batch\python\python.exe data\tools\DDS-Tools-v0.6.1-Batch\src\main.py "%selectedUasset%" "%pngFile%" --save_folder="data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems" --version=4.27

exit /b
