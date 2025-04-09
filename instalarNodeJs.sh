#!/bin/bash

print_color() {
    color_code=$1
    text=$2
    echo -e "\e[1;${color_code}m${text}\e[0m"

    # Color codes
    # 30 Negro
    # 31 Rojo
    # 32 Verde
    # 33 Amarillo
    # 34 Azul
    # 35 Magenta
    # 36 Cian
    # 37 Blanco
}

verify_installation() {
    local app="$1"

    if command -v "$app" &> /dev/null; then
        return 0
    else
        return 1
    fi
}


if ! verify_installation 'curl'; then
    print_color 34 "\nInstalar curl\n"
    sudo apt-get install -y curl
else
    print_color 34 "\nCurl ya instalado\n"
fi


if ! verify_installation 'node'; then
    print_color 34 "\nDescargar el script de instalacion:\n"
    NODE_VERSION="18.x"
    curl -fsSL https://deb.nodesource.com/setup_$NODE_VERSION -o nodesource_setup.sh

    print_color 34 "\nEjecutar el script de instalación con sudo\n"
    sudo -E bash nodesource_setup.sh

    print_color 34 "\nInstalar Node.js\n"
    sudo apt-get install -y nodejs

    print_color 34 "\nVerificar la instalación\n"
    node -v

    print_color 34 "\nEliminar script de instalación\n"
    rm nodesource_setup.sh
else
    print_color 34 "\nNode ya instalado\n"
fi

