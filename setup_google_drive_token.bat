@echo off
setlocal
title Google Drive Token Generator
cd /d "%~dp0" || (
    echo ERROR: Could not open the project folder.
    pause
    exit /b 1
)

if not exist "generate_token.py" (
    echo ERROR: generate_token.py was not found in this folder.
    pause
    exit /b 1
)

if not exist "requirements.txt" (
    echo ERROR: requirements.txt was not found in this folder.
    pause
    exit /b 1
)

echo Installing required Python libraries...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo WARNING: pip upgrade failed; trying to install requirements anyway.
)

python -m pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Dependency installation failed.
    pause
    exit /b 1
)

if not exist "credentials.json" (
    echo ERROR: credentials.json was not found.
    echo Save your OAuth Desktop app JSON beside this BAT file.
    pause
    exit /b 1
)

echo.
echo Starting Google Drive authentication...
python generate_token.py
if errorlevel 1 (
    echo.
    echo ERROR: Token generation failed. Review the message above.
)
echo.
pause
endlocal
