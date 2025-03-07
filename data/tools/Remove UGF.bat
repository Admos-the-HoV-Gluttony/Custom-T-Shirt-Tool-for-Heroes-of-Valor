@echo off
setlocal

cls

set "targetPath=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"

if exist "%targetPath%" (
    echo The directory "%targetPath%" was found and will be deleted.
    echo.
) else (
    echo The directory "%targetPath%" was not found.
    echo.
    pause
    endlocal
    exit /b
)

:askConfirmation
cls
set "userInput="
echo Do you want to proceed with the deletion? (y/n)
echo.
set /p userInput=
if /i "%userInput%"=="y" (
    rmdir /s /q "%targetPath%"
    if errorlevel 1 (
        echo.
        echo Failed to delete the directory.
    ) else (
        echo.
        echo The directory has been deleted successfully.
    )
) else if /i "%userInput%"=="n" (
    echo.
    echo Deletion cancelled.
) else (
    echo.
    echo Invalid input. Please enter 'y' or 'n'.
    goto askConfirmation
)

pause

endlocal
