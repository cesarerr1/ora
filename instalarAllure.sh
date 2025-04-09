#!/bin/bash

# Descargar la última versión de Allure
echo "Descargando la versión de Allure 2.27.0 ..."
wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.zip -O /tmp/allure.zip

# Descomprimir el archivo
echo "Descomprimiendo Allure..."
unzip /tmp/allure.zip -d /tmp/

# Detectar la ubicación de instalación de Allure
ALLURE_INSTALL_DIR=$(find /tmp/ -type d -name "allure-*" | head -n 1)

# Verificar si se encontró la ubicación de instalación
if [ -z "$ALLURE_INSTALL_DIR" ]; then
    echo "Error: No se pudo detectar la ubicación de instalación de Allure."
    exit 1
fi

# Mover el directorio de instalación a /opt/allure
sudo mv "$ALLURE_INSTALL_DIR" /opt/allure

# Agregar Allure al PATH
if ! grep -q "/opt/allure/bin" "$HOME/.bashrc"; then
    echo 'export PATH="$PATH:/opt/allure/bin"' >> "$HOME/.bashrc"
    source ~/.bashrc
fi

# Actualizar el PATH para la sesión actual
export PATH="$PATH:/opt/allure/bin"

# Limpiar
rm /tmp/allure.zip

echo "Allure se ha instalado correctamente y se ha agregado al PATH."

# Comprobación de la versión de Allure
echo "Versión de Allure instalada:"
allure --version
