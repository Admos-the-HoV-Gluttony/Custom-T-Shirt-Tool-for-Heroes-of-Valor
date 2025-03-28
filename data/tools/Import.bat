@echo off
setlocal enabledelayedexpansion

cls

:loop
echo Warning: Automatic importing is not yet supported. User intervention is required.
echo Please note that you need to copy all contents from "Heroes of Valor Playtest" to "Imported Game Files".
echo.
set /p "userChoice=Do you want to open both Folders? (y/n): "

if /i "!userChoice!"=="y" (
    set "secondPath=data\Imported Game Files"

    if not exist "!secondPath!" (
        echo The directory "!secondPath!" does not exist. Creating it now...
        mkdir "!secondPath!"
    )

    echo The second path is: !secondPath!
    explorer "!secondPath!"

    for /f "delims=" %%i in (data\tools\path.txt) do (
        set "extractedPath=%%i"
    )

    echo The extracted path is: !extractedPath!
    explorer "!extractedPath!"
) else if /i "!userChoice!"=="n" (
    echo Opening paths cancelled.
) else (
    echo Invalid input. Please enter 'y' or 'n'.
    goto :loop
)

endlocal
