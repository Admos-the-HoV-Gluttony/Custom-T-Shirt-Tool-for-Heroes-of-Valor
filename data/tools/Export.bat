@echo off
setlocal enabledelayedexpansion

:loop
echo Warning: Automatic exporting is not yet supported. User intervention is required.
echo Please note that you need to copy all contents from "Imported Game Files" to "Heroes of Valor Playtest".
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