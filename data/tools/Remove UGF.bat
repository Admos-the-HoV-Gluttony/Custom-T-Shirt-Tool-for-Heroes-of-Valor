@echo off
setlocal

cls

set "targetPath=data\Imported Game Files\HeroesOfValor\Content\Paks\HeroesOfValor-WindowsNoEditor"

if exist "%targetPath%" (
    echo The directory "%targetPath%" was found and will be deleted.
) else (
    echo The directory "%targetPath%" was not found.
    pause
    endlocal
    exit /b
)

:askConfirmation
set "userInput="
echo Do you want to proceed with the deletion? (y/n)
set /p userInput=
if /i "%userInput%"=="y" (
    rmdir /s /q "%targetPath%"
    if errorlevel 1 (
        echo Failed to delete the directory.
    ) else (
        echo The directory has been deleted successfully.
    )
) else if /i "%userInput%"=="n" (
    echo Deletion cancelled.
) else (
    echo Invalid input. Please enter 'y' or 'n'.
    goto askConfirmation
)

pause

endlocal