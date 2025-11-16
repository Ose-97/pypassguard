```batch
@echo off
echo PyPassGuard - Password Security Toolkit
echo =======================================
echo.

REM Check if Python is available
python --version >nul 2>nul
if %errorlevel% equ 0 (
    echo Python is installed!
    python --version
    echo.
    python main.py %*
    goto :end
)

echo.
echo ERROR: Python not found!
echo.
echo Please install Python from https://python.org/downloads/
echo.
echo After installation, close and reopen this terminal.
echo.
pause

:end