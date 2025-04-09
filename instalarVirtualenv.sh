#!/bin/bash
# Verificar si Pip está instalado
if ! command -v pip &> /dev/null; then
    if sudo apt install -y python3-pip; then
        echo "Pip instalado correctamente"
    else
        echo "Error: No se pudo instalar Pip"
        exit 1
    fi
else
    echo "Pip ya está instalado"
fi

if ! dpkg -s python3-venv &> /dev/null; then
    echo "Instalando python3-venv..."
    if sudo apt install -y python3-venv; then
        echo "python3-venv instalado correctamente"
    else
        echo "Error: No se pudo instalar python3-venv"
        exit 1
    fi
else
    echo "python3-venv ya está instalado"
fi