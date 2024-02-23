@echo off
set "input=%~1"
set "output=%~dpn1_extracted"

if "%~1"=="" (
    set /p "input=File: "
) else (
    set "input=%~1"
)

echo Descomprimindo arquivo: %input%
echo Para pasta: %output%

mkdir "%output%"
offzip.exe -a "%input%" "%output%"

echo.
echo Processo concluído.
pause
