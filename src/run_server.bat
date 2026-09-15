@echo off
title Supply Chain Assistant - DO NOT CLOSE THIS WINDOW
cd /d "%~dp0"
echo ================================================
echo  Supply Chain Disruption Assistant
echo  Server starting on http://127.0.0.1:5000
echo  KEEP THIS WINDOW OPEN WHILE TESTING
echo ================================================
:loop
python app.py
echo.
echo [!] Server stopped. Restarting in 3 seconds...
timeout /t 3 >nul
goto loop