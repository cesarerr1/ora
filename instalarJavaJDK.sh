#!/bin/bash

if ! command -v java &> /dev/null; then
    echo "Java no está instalado. Instalando Java 17..."
    
    # Instalar Java 17
    if sudo apt update && sudo apt install -y openjdk-17-jdk; then
        echo "Java 17 instalado correctamente"
        
        # Configurar la alternativa de java
        sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-17-openjdk-amd64/bin/java 1
        sudo update-alternatives --config java

        # Añadir Java al PATH
        echo 'export PATH="$PATH:/usr/lib/jvm/java-17-openjdk-amd64/bin"' >> ~/.bashrc
        echo 'export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64' >> ~/.bashrc

        # Recargar .bashrc
        source ~/.bashrc
    else
        echo "Error: No se pudo instalar Java"
        exit 1
    fi
else
    echo "Java ya está instalado"
fi
