@echo off

REM Verifica se foram arrastados arquivos para o script
if "%~1"=="" (
    echo No files were dragged into the script.
    pause
    exit /b
)

REM Define o caminho para o executável etc1tool
set ETC1_TOOL_PATH="./etc1tool.exe"

REM Processa cada arquivo arrastado
:process_files
if "%~1"=="" goto :end_processing
if not "%~x1"==".png" (
    echo The file "%~1" is not a PNG file. Ignoring.
) else (
    %ETC1_TOOL_PATH% --encodeNoHeader "%~1"
)
shift
goto :process_files

:end_processing
echo Processamento concluído.
pause
