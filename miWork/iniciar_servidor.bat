@echo off
title Servidor Local en Tiempo Real - SCAN SPACE
cls
echo ======================================================
echo   Servidor Web Colaborativo en Tiempo Real
echo ======================================================
echo.
echo Tu checklist interactivo esta transmitiendose en:
echo.
echo   [En tu computadora]:   http://localhost:8000
echo   [En celulares / red]:  http://192.168.1.50:8000
echo.
echo   * Los cambios que marque cualquier integrante
echo     se sincronizan al instante en todos los dispositivos.
echo.
echo (Para apagar el servidor cuando termines, solo cierra esta ventana)
echo ======================================================
echo.
"C:\msys64\ucrt64\bin\python.exe" "%~dp0server.py"
pause
