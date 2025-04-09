#!/bin/bash

# Directorio de instalación
INSTALL_DIR="/opt/android-sdk"

if ! command -v sdkmanager &> /dev/null; then
    echo "Instalando Android SDK..."

    # Crear el directorio de instalación si no existe
    sudo mkdir -p "$INSTALL_DIR/cmdline-tools"

    # Descargar los command line tools
    echo "Descargando command line tools..."
    if ! wget https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip -O /tmp/commandlinetools-linux.zip; then
        echo "Error: No se pudo descargar los command line tools."
        exit 1
    fi

    # Extraer los archivos en el directorio temporal
    echo "Descomprimiendo command line tools..."
    if ! unzip /tmp/commandlinetools-linux.zip -d /tmp/android-sdk-tmp; then
        echo "Error: No se pudo extraer los command line tools."
        exit 1
    fi

    # Mover los archivos al directorio de instalación
    sudo mkdir -p "$INSTALL_DIR/cmdline-tools/latest"
    if ! sudo mv /tmp/android-sdk-tmp/cmdline-tools/* "$INSTALL_DIR/cmdline-tools/latest/"; then
        echo "Error: No se pudo mover los archivos al directorio de instalación."
        exit 1
    fi

    # Configurar las variables de entorno
    if ! grep -q "$INSTALL_DIR/cmdline-tools/latest/bin" "$HOME/.bashrc"; then
        echo 'export ANDROID_SDK_ROOT="/opt/android-sdk"' | sudo tee -a "$HOME/.bashrc"
        echo 'export PATH="$PATH:/opt/android-sdk/cmdline-tools/latest/bin"' | sudo tee -a "$HOME/.bashrc"
        source "$HOME/.bashrc"
    fi

    # Actualizar el PATH para la sesión actual
    export ANDROID_SDK_ROOT="/opt/android-sdk"
    export PATH="$PATH:/opt/android-sdk/cmdline-tools/latest/bin"
    source "$HOME/.bashrc"

    # Usar el PATH completo de sdkmanager
    SDKMANAGER_PATH="$INSTALL_DIR/cmdline-tools/latest/bin/sdkmanager"

    # Instalar las plataformas y herramientas necesarias
    echo "Instalando plataformas y herramientas..."
    if ! sudo "$SDKMANAGER_PATH" "platforms;android-34" "platform-tools" "build-tools;34.0.0" "emulator"; then
        echo "Error: No se pudieron instalar las plataformas y herramientas necesarias."
        exit 1
    fi

    # Aceptar las licencias
    echo "Aceptando licencias..."
    if ! yes | sudo "$SDKMANAGER_PATH" --licenses; then
        echo "Error: No se pudieron aceptar las licencias."
        exit 1
    fi

    # Limpiar archivos temporales
    rm -rf /tmp/commandlinetools-linux.zip /tmp/android-sdk-tmp

    echo "Android SDK se ha instalado correctamente en $INSTALL_DIR y se ha agregado al PATH."
else
    echo "Android SDK ya está instalado"
fi

# Comprobación de la versión de sdkmanager
echo "Versión de sdkmanager instalada:"
sdkmanager --version
