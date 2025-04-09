#!/bin/bash

if ! command -v adb &> /dev/null; then
    if sudo apt install -y adb; then
        echo "adb instalado correctamente"
    else
        echo "Error: No se pudo adb"
        exit 1
    fi
else
    echo "adb ya está instalado"
fi