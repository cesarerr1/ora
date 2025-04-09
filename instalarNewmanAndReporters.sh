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

install_package() {
    package_name=$1
    if npm list -g --depth=0 | grep -q $package_name; then
        print_color 32 "$package_name ya está instalado."
    else
        print_color 34 "\nInstalando $package_name\n"
        sudo npm install -g $package_name
    fi
}

print_color 34 '\nVerificando e instalando los paquetes necesarios...\n'

install_package "newman"
install_package "newman-reporter-htmlextra"
install_package "newman-reporter-allure"

print_color 32 '\nInstalación finalizada.\n'
