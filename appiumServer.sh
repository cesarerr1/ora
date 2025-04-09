#!/bin/bash

# Variables
REQUIRED_NODE_VERSION="v18.20.4"
REQUIRED_NPM_VERSION="10.8.2"
REQUIRED_APPIUM_VERSION="1.22.3"

# Función para verificar la versión
check_version() {
    local required_version=$1
    local command=$2
    local current_version

    # Obtener la versión actual, quitando espacios innecesarios, saltos de línea y 'v' en la versión de Node.js
    current_version=$($command --version | tr -d '[:space:]' | sed 's/^v//')

    # Comparar las versiones
    if [ "$current_version" != "$required_version" ]; then
        return 1
    fi
    return 0
}

# Actualizar el sistema e instalar dependencias
echo "Actualizando e instalando dependencias..."
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y curl unzip

# Verificar la versión de Node.js
if ! check_version "${REQUIRED_NODE_VERSION#v}" "node"; then
    echo "Versión incorrecta de Node.js. Desinstalando e instalando la versión correcta..."
    sudo apt-get remove --purge nodejs -y
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs
else
    echo "La versión de Node.js es la correcta (${REQUIRED_NODE_VERSION})."
fi

# Verificar la versión de npm
if ! check_version "$REQUIRED_NPM_VERSION" "npm"; then
    echo "Versión incorrecta de npm. Instalando la versión correcta..."
    sudo npm install -g npm@$REQUIRED_NPM_VERSION
else
    echo "La versión de npm es la correcta ($REQUIRED_NPM_VERSION)."
fi

# Verificar la instalación de Node.js y npm
if command -v node &> /dev/null && command -v npm &> /dev/null; then
    echo "Node.js y npm están instalados correctamente."
else
    echo "Error: Node.js o npm no se han instalado correctamente."
    exit 1
fi

# Verificar si la versión de Appium es la correcta
if ! check_version "$REQUIRED_APPIUM_VERSION" "appium"; then
    echo "Instalando Appium versión $REQUIRED_APPIUM_VERSION..."
    sudo npm install -g appium@$REQUIRED_APPIUM_VERSION
else
    echo "La versión de Appium instalada es la correcta ($REQUIRED_APPIUM_VERSION)."
fi
