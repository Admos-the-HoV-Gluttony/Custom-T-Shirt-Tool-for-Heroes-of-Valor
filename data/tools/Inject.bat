@echo off
setlocal enabledelayedexpansion

set /a count=0

set "uassetList[1]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_NightCamo.uasset"
set "uassetList[2]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_GreenCamo.uasset"
set "uassetList[3]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Dracula_C.uasset"
set "uassetList[4]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Frankenstein_C.uasset"
set "uassetList[5]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Wolf.uasset"
set "uassetList[6]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Banana.uasset"
set "uassetList[7]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Playtest_Axis.uasset"
set "uassetList[8]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Shirt_Playtest_Allied.uasset"
set "uassetList[9]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_AxisFTWShirt.uassets"
set "uassetList[10]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_AlliesFTWShirt.uasset"
set "uassetList[11]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_TankTop_C.uasset"
set "uassetList[12]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Balaclava_A.uasset"
set "uassetList[13]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_SkullBandana.uasset"
set "uassetList[14]=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems\T_Bandana.uasset"


for /L %%i in (1,1,14) do (
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
set /p pngFile=Enter the path to a PNG file: 

set "pngFile=%pngFile:"=%"

if not exist "%pngFile%" (
    echo The specified PNG file does not exist.
    pause
    goto :menu
)

data\tools\DDS-Tools-v0.6.1-Batch\python\python.exe data\tools\DDS-Tools-v0.6.1-Batch\src\main.py "!selectedUasset!" "%pngFile%" --save_folder="data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor\HeroesOfValor\Content\Textures\CosmeticItems" --version=4.27 --skip_non_texture --image_filter=cubic

exit /b
