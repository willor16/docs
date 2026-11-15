@echo off
title SCAN SPACE - AstroCow Standalone Simulator
echo =======================================================
echo    SCAN SPACE - AstroCow Flight Simulator & Telemetry
echo    NASA Space Apps Challenge 2026
echo =======================================================
echo.
cd /d "%~dp0"
echo Starting game server...
python server.py 2>nul || C:\msys64\ucrt64\bin\python.exe server.py
pause
