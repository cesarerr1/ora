#!/bin/bash

PORT=4723
HOST="127.0.0.1"

# Iniciar Appium en segundo plano con las opciones especificadas
echo "Iniciando Appium en segundo plano en $HOST:$PORT con CORS habilitado..."
nohup appium --address $HOST --port $PORT --allow-cors

# Confirmar que Appium se está ejecutando
if pgrep -x "appium" > /dev/null; then
    echo "Appium se está ejecutando en $HOST:$PORT en segundo plano."
else
    echo "Error: Appium no se está ejecutando."
    exit 1
fi