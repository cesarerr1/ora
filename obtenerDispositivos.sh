#!/bin/bash

project_name="$1"

# Obtener la lista de dispositivos conectados
dispositivos=$(adb devices | grep -v 'List of devices attached' | awk '{print $1}')

# Verificar si hay dispositivos conectados
if [ -z "$dispositivos" ]; then
    echo "No hay dispositivos conectados."
    exit 1
fi

# Convertir la lista en un array
IFS=$'\n' read -r -d '' -a array_dispositivos <<< "$dispositivos"

# Contar el número de dispositivos
num_dispositivos=${#array_dispositivos[@]}

# Verificar si hay más de un dispositivo
if [ "$num_dispositivos" -eq 1 ]; then
    # Solo un dispositivo conectado, seleccionar automáticamente
    dispositivo_seleccionado=${array_dispositivos[0]}
else
    # Más de un dispositivo, solicitar al usuario que seleccione uno
    echo "Dispositivos conectados:"
    select dispositivo_seleccionado in "${array_dispositivos[@]}"; do
        if [ -n "$dispositivo_seleccionado" ]; then
            break
        else
            echo "Selección inválida. Inténtalo de nuevo."
        fi
    done
fi

# Recuperar la versión de Android del dispositivo seleccionado
version_android=$(adb -s "$dispositivo_seleccionado" shell getprop ro.build.version.release)

# Mostrar el ID del dispositivo y la versión de Android
echo "Dispositivo seleccionado: $dispositivo_seleccionado"
echo "Versión de Android: $version_android"

"$PWD/movil.sh" "$project_name" "$version_android" "$dispositivo_seleccionado"
