@echo off
setlocal enabledelayedexpansion

cls

:checkForFolder
if exist "data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor" (
    echo Unpackaged Game Files have been detected.
    echo Removing the Unpackaged Game Files before exporting is recommended!
    echo.
    set /p "deleteChoice=Do you want to delete the Unpackaged Game Files? (y/n): "

    if /i "!deleteChoice!"=="y" (
        echo Deleting the folder "HeroesOfValor-WindowsNoEditor" and its contents...
        rmdir /s /q "data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"
        echo Folder deleted successfully.
    ) else if /i "!deleteChoice!"=="n" (
        echo Skipping deletion of the folder.
    ) else (
        echo Invalid input. Please enter 'y' or 'n'.
        goto :checkForFolder
    )
) else (
    goto :loop
)

:loop
cls
echo Warning: Automatic exporting is not yet supported. User intervention is required.
echo Please note that you need to copy all contents from "Imported Game Files" to "Heroes of Valor Playtest".
echo.
set /p "userChoice=Do you want to open both Folders? (y/n): "

if /i "!userChoice!"=="y" (
    for /f "delims=" %%i in (data\tools\path.txt) do (
        set "extractedPath=%%i"
    )

    echo The extracted path is: !extractedPath!
    explorer "!extractedPath!"

    set "secondPath=data\Imported Game Files"

    echo The second path is: !secondPath!
    explorer "!secondPath!"
) else if /i "!userChoice!"=="n" (
    echo Opening paths cancelled.
) else (
    echo Invalid input. Please enter 'y' or 'n'.
    goto :loop
)

endlocal
