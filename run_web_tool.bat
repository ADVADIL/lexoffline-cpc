@echo off
title LexOffline CPC 1908 Web Tool
echo Starting LexOffline CPC 1908 Interactive Web Application...
cd /d "%~dp0"
start http://localhost:5000
python web\app.py
pause
