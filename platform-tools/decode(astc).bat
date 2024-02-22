@echo off

REM Verifica se foram arrastados arquivos para o script
if "%~1"=="" (
    echo No files were dragged into the script.
    pause
    exit /b
)

REM Define o caminho para o executável etc1tool
set ETC1_TOOL_PATH="./astcenc.exe"

REM Processa cada arquivo arrastado
:process_files
if "%~1"=="" goto :end_processing
    %ETC1_TOOL_PATH% -d "%~1" "%~1".tga
shift
goto :process_files

:end_processing
echo Processamento concluído.
pause
