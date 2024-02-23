@echo off
set "input=%~1"
set "output=%~dpn1_extracted"
set "backup=%~dpn1_backup%~x1"

echo Criando backup do arquivo: %input%
copy "%input%" "%backup%"

echo Descomprimindo arquivo: %input%
echo Para pasta: %output%

if "%~1"=="" (
    set /p "input=File: "
) else (
    set "input=%~1"
)

offzip.exe -a -r "%input%" "%output%"

echo.
echo Processo concluído.
pause
