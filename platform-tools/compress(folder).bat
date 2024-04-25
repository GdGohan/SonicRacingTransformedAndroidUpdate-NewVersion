@echo off

REM Verifica se foi arrastada uma pasta para o script
if "%~1"=="" (
    echo No folder was dragged into the script.
    pause
    exit /b
)

REM Define o caminho para o executável etc1tool
set ETC1_TOOL_PATH="./etc1tool.exe"

REM Cria a pasta 'converted' se ainda não existir
if not exist "converted" mkdir "converted"

REM Processa todos os arquivos PNG na pasta arrastada
for %%I in ("%~1\*.png") do (
    echo Processando arquivo: %%I
    %ETC1_TOOL_PATH% --encodeNoHeader "%%I" -o "converted\%%~nI.pkm"
)

echo Processamento concluído.
pause
