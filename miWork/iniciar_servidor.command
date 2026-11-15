#!/bin/bash
cd "$(dirname "$0")"
clear

# Obtener la dirección IP local de la Mac
LOCAL_IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1)

echo "======================================================"
echo "  Servidor Web Colaborativo en Tiempo Real (SCAN SPACE)"
echo "======================================================"
echo ""
echo "Tu checklist interactivo está disponible en:"
echo ""
echo "  [En esta Mac]:        http://localhost:8000"
if [ -n "$LOCAL_IP" ]; then
echo "  [En la red local]:    http://$LOCAL_IP:8000"
fi
echo ""
echo "  * Comparte el enlace de red local con tu equipo o pruébalo"
echo "    desde tu celular conectado a la misma red Wi-Fi."
echo ""
echo "(Para apagar el servidor cuando termines, presiona Control + C o cierra esta ventana)"
echo "======================================================"
echo ""
python3 server.py
