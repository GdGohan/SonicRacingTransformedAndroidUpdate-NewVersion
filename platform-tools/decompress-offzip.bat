@echo off
set "input=%~1"
set "output=%~dpn1_extracted"

if "%~1"=="" (
    set /p "input=Por favor, digite o nome do arquivo de entrada (sem a extensão): "
) else (
    set "input=%~1"
)

echo Descomprimindo arquivo: %input%
echo Para pasta: %output%

mkdir "%output%"
offzip.exe -a "%input%" "%output%" 0

echo.
echo Processo concluído.
pause
