#!/bin/bash

main(){
    read -p "¿Ya tienes un proyecto existente? (s/n): " existing_project
    existing_project=$(echo "$existing_project" | tr '[:upper:]' '[:lower:]') # Convertir a minúsculas

    if [[ "$existing_project" == "s" ]]; then
        extend_project
    elif [[ "$existing_project" == "n" ]]; then
        create_new_project
    else
        echo "Respuesta inválida. Por favor, ingresa 's' o 'n'."
    fi
}

extend_project(){
    read -p "Ingrese el nombre del proyecto a extender: " project_name
    cd "$project_name"
    configurarVSCode
    missing_projects=$(get_missing_projects)
    mostrar_menu ${missing_projects[@]}

    cd ..
    for element in "${proyectos_seleccionados[@]}"; do
        case "$element" in
            "WEB")
                echo "---Realizando configuraciones para WEB---"
                mkdir -p "$project_name"/web
                "$PWD/web.sh"  "$project_name" # Ejecutar el script web.sh
                ;;
            "DESKTOP")
                echo "---Realizando configuraciones para DESKTOP---"
                mkdir -p "$project_name"/desktop
                "$PWD/desktop.sh" "$project_name" # Ejecutar el script desktop.sh
                ;;
            "MOVIL")
                mkdir -p "$project_name"/movil
                echo "---Realizando configuraciones para movil---"
                log_appium="appium_server_log.txt"
                rm -f "$log_appium"
                echo "------Iniciando Appium server ------" | tee -a "$log_appium"
                nohup ./iniciarAppium.sh >> "$log_appium" 2>&1 < /dev/null &
                "$PWD/obtenerDispositivos.sh" "$project_name"  # Ejecutar el script movil.sh
                ;;
            "SERVICIOS")
                echo "------Realizando configuraciones para servicios------"
                mkdir -p "$project_name"/servicios
                "$PWD/servicios.sh" "$project_name"
                ;;
            *)
                ;;
        esac
    done

    ejecutar_pruebas "${proyectos_seleccionados[@]}"
}

create_new_project(){
    read -p "Ingrese el nombre del nuevo proyecto: " project_name
    mkdir "$project_name"
    cd "$project_name" || exit
    configurarVSCode
    mkdir web
    mkdir desktop
    mkdir movil
    mkdir allure-results

    # Mensaje de confirmación
    echo "¡La estructura de carpetas para el proyecto '$project_name' ha sido creada con éxito!"
    cd ..

    show_menu
    ejecutarPruebas
}

get_missing_projects(){
    missingprojects=()

    existe_web=$(folder_exists "pages")
    existe_escritorio=$(folder_exists "imgs")
    existe_movil=$(folder_exists "appium")

    if !($existe_web); then
        missingprojects+=("WEB")
    fi
    if !($existe_escritorio); then
        missingprojects+=("DESKTOP")
    fi
    if !($existe_movil); then
        missingprojects+=("MOVIL")
    fi

    echo "${missingprojects[@]}"
}

folder_exists(){
    local folder_to_search=$1

    if find . -type d -name "$folder_to_search" -print -quit | grep -q .; then
        existe=true
    else
        existe=false
    fi

    echo $existe
}

mostrar_menu() {
    local proyectos=("$@")

    # Inicializar selecciones (inicialmente todas desmarcadas)
    declare -a selected=()

    for ((i = 0; i < ${#proyectos[@]}; i++)); do
        selected[$i]=0
    done

    # Bucle para mostrar los elementos y obtener selecciones
    while true; do
        clear
        echo "Selecciona los proyectos que deseas instalar (Presiona 'q' para finalizar selección):"
        for i in "${!proyectos[@]}"; do
            if [ "${selected[$i]}" -eq 1 ]; then
                echo "[X] ${proyectos[$i]}"
            else
                echo "[ ] ${proyectos[$i]}"
            fi
        done

        read -n 1 -p "Selecciona un proyecto (1-${#proyectos[@]}) para cambiar su estado de selección: " choice
        echo

        case "$choice" in
            "q"|"Q")
                break
                ;;
            [1-9])
                index=$((choice - 1))
                if [ $index -ge 0 ] && [ $index -lt ${#proyectos[@]} ]; then
                    selected[$index]=$((1 - ${selected[$index]}))
                else
                    echo "Selección inválida."
                    sleep 1
                fi
                ;;
            *)
                echo "Selección inválida. Presiona 'q' para finalizar selección."
                sleep 1
                ;;
        esac
    done

    # Almacenar los proyectos seleccionados en un array
    proyectos_seleccionados=()
    for i in "${!proyectos[@]}"; do
        if [ "${selected[$i]}" -eq 1 ]; then
            proyectos_seleccionados+=("${proyectos[$i]}")
        fi
    done

    # Devolver el array de proyectos seleccionados
    echo ${proyectos_seleccionados[@]}
}

ejecutar_pruebas(){
    local proyectos=("$@")

    echo "Ejecutando pruebas..."

    cd "$project_name" || exit
    
    for proyecto in "${proyectos[@]}"; do
        case $proyecto in
            "WEB")
                if [ -d "web" ]; then
                    cd "web" || exit
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                    cd ..
                    cp -r ./web/allure-results/* ./allure-results
                else
                    echo "No se encontró el directorio 'web' en '$project_name'. Saltando..."
                fi
                ;;
            "DESKTOP")
                if [ -d "desktop" ]; then
                    cd "desktop" || exit
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                    cd ..
                    cp -r ./desktop/allure-results/* ./allure-results
                else
                    echo "No se encontró el directorio 'desktop' en '$project_name'. Saltando..."
                fi
                ;;
            "MOVIL")
                if [ -d "movil" ]; then
                    cd "movil" || exit
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                    cd ..
                    cp -r ./movil/allure-results/* ./allure-results                    else
                    echo "No se encontró el directorio 'movil' en '$project_name'. Saltando..."
                fi
                ;;
            "SERVICIOS")
                if [ -d "servicios/jmeter" ]; then
                    cd servicios
                    cd jmeter
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                    cd ..
                    cd ..
                    cp -r ./servicios/jmeter/allure-results/* ./allure-results
                else
                    echo "No se encontró el directorio 'jmeter' en '$project_name'. Saltando..."
                fi

                if [ -d "servicios/postman" ]; then
                    cd servicios
                    cd postman
                    behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                    cd ..
                    cd ..
                    cp -r ./servicios/postman/allure-results/* ./allure-results
                else
                    echo "No se encontró el directorio 'postman' en '$project_name'. Saltando..."
                fi
                ;;
            *)
                ;;
        esac
    done

    #servir reporte 
    allure serve
}

show_menu() {
    # Lista de elementos
    items=("WEB" "DESKTOP" "MOVIL" "SERVICIOS")
    $web="web"
    $desktop="desktop"

    # Selecciones (inicialmente todas desmarcadas)
    selected=(0 0 0 0)

    # Bucle para mostrar los elementos y obtener selecciones
    while true; do
        clear
        echo "Selecciona las pruebas que deseas instalar (Presiona 'q' para finalizar selección):"
        for i in "${!items[@]}"; do
            if [ "${selected[$i]}" -eq 1 ]; then
                echo "[X] ${items[$i]}"
            else
                echo "[ ] ${items[$i]}"
            fi
        done

        read -n 1 -p "Selecciona un elemento (1-4) para cambiar su estado de selección: " choice
        echo

        case "$choice" in
            "q"|"Q")
                break
                ;;
            "1")
                selected[0]=$((1-${selected[0]}))
                ;;
            "2")
                selected[1]=$((1-${selected[1]}))
                ;;
            "3")
                selected[2]=$((1-${selected[2]}))
                ;;
            "4")
                selected[3]=$((1-${selected[3]}))
                ;;
            *)
                echo "Selección inválida. Presiona 'q' para finalizar selección."
                sleep 1
                ;;
        esac
    done

    # Leer las selecciones y realizar acciones en consecuencia
    for i in "${!selected[@]}"; do
        if [ "${selected[$i]}" -eq 1 ]; then
            python3 -m venv venv
            source venv/bin/activate
            # Si se selecciona alguna opción, crear la estructura
            if ! $estructura_creada; then
                estructura_creada=true
            fi

            case "${items[$i]}" in
                "WEB")
                    echo "---Realizando configuraciones para WEB---"
                    "$PWD/web.sh"  "$project_name" # Ejecutar el script web.sh
                    ;;
                "DESKTOP")
                    echo "---Realizando configuraciones para DESKTOP---"
                    "$PWD/desktop.sh" "$project_name" # Ejecutar el script desktop.sh
                    ;;
                "MOVIL")
                    echo "---Realizando configuraciones para movil---"
                    log_appium="appium_server_log.txt"
                    rm -f "$log_appium"
                    echo "------Iniciando Appium server ------" | tee -a "$log_appium"
                    nohup ./iniciarAppium.sh >> "$log_appium" 2>&1 < /dev/null &
                    "$PWD/obtenerDispositivos.sh" "$project_name"  # Ejecutar el script movil.sh
                    ;;
                "SERVICIOS")
                    echo "------Realizando configuraciones para servicios------"
                    mkdir -p "$project_name"/servicios
                    seleccionarServicios
                    ;;
                *)
                    ;;
            esac
        fi
    done
}



configurarVSCode() {
  
    mkdir .vscode
    touch .vscode/extensions.json

    cat >.vscode/extensions.json <<EOF
{
    "recommendations": [
        "cucumberopen.cucumber-official"
    ]
}
EOF

    # Preguntar si se instalara las extensiones

    respuesta=""

    while [[ "$respuesta" != "s" && "$respuesta" != "n" ]]; do
        read -p "¿Quiere instalar las extensiones? (s/n): " respuesta
        respuesta=$(echo "$respuesta" | tr '[:upper:]' '[:lower:]') # Convertir a minúsculas
        if [[ "$respuesta" == "s" ]]; then
            echo "Instalando extensiones de Visual Studio Code"
            
            # Verificar si jq está instalado
            if ! command -v jq &> /dev/null; then
                echo "jq no está instalado. Instalando..."
                sudo apt install -y jq
            else
                echo "jq ya está instalado."
            fi

            jq -r '.recommendations[]' .vscode/extensions.json | xargs -I {} code --install-extension {}
        
        elif [[ "$respuesta" == "n" ]]; then
            echo "No se instalaran las extensiones de Visual Studio Code"
        else
            echo "Respuesta inválida. Por favor, ingresa 's' o 'n'."
        fi
    done
}

ejecutarPruebas() {
    echo "Ejecutando pruebas..."
    cd "$project_name" || exit
    for i in "${!selected[@]}"; do
        if [ "${selected[$i]}" -eq 1 ]; then
            case "${items[$i]}" in
                "WEB")
                    if [ -d "web" ]; then
                        cd "web" || exit
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                        cd ..
                        cp -r ./web/allure-results/* ./allure-results
                    else
                        echo "No se encontró el directorio 'web' en '$project_name'. Saltando..."
                    fi
                    ;;
                "DESKTOP")
                    if [ -d "desktop" ]; then
                        cd "desktop" || exit
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                        cd ..
                        cp -r ./desktop/allure-results/* ./allure-results
                    else
                        echo "No se encontró el directorio 'desktop' en '$project_name'. Saltando..."
                    fi
                    ;;
                "MOVIL")
                    if [ -d "movil" ]; then
                        cd "movil" || exit
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                        cd ..
                        cp -r ./movil/allure-results/* ./allure-results
                    else
                        echo "No se encontró el directorio 'movil' en '$project_name'. Saltando..."
                    fi
                    ;;
                *)
                    ;;
            esac
        fi
    done
    ejecutarServicios
    #servir reporte 
    allure serve
}

ejecutarServicios(){
    for i in "${!select[@]}"; do
        if [ "${select[$i]}" -eq 1 ]; then
            case "${item[$i]}" in
                "POSTMAN")
                    if [ -d "servicios/postman" ]; then
                        cd servicios
                        cd postman
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                        cd ..
                        cd ..
                        cp -r ./servicios/postman/allure-results/* ./allure-results
                    else
                        echo "No se encontró el directorio 'postman' en '$project_name'. Saltando..."
                    fi
                    ;;
                "JMETER")
                    if [ -d "servicios/jmeter" ]; then
                        cd servicios
                        cd jmeter
                        behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features
                        cd ..
                        cd ..
                        cp -r ./servicios/jmeter/allure-results/* ./allure-results
                    else
                        echo "No se encontró el directorio 'jmeter' en '$project_name'. Saltando..."
                    fi
                    ;;
                
                *)
                    ;;
            esac
        fi
    done
}

seleccionarServicios(){
    # Lista de elementos
    item=("JMETER" "POSTMAN")
    $jmeter="jmeter"
    $postman="postman"

    # Selecciones (inicialmente todas desmarcadas)
    select=(0 0)

    # Bucle para mostrar los elementos y obtener selecciones
    while true; do
        clear
        echo "Selecciona el entorno para servicios que deseas instalar (Presiona 'q' para finalizar selección):"
        for i in "${!item[@]}"; do
            if [ "${select[$i]}" -eq 1 ]; then
                echo "[X] ${item[$i]}"
            else
                echo "[ ] ${item[$i]}"
            fi
        done

        read -n 1 -p "Selecciona un elemento (1-2) para cambiar su estado de selección: " choice
        echo

        case "$choice" in
            "q"|"Q")
                break
                ;;
            "1")
                select[0]=$((1-${select[0]}))
                ;;
            "2")
                select[1]=$((1-${select[1]}))
                ;;
            *)
                echo "Selección inválida. Presiona 'q' para finalizar selección."
                sleep 1
                ;;
        esac
    done

    # Leer las selecciones y realizar acciones en consecuencia
    for i in "${!select[@]}"; do
        if [ "${select[$i]}" -eq 1 ]; then
            # Si se selecciona alguna opción, crear la estructura
            if ! $estructura_creada; then
                estructura_creada=true
            fi

            case "${item[$i]}" in
                "JMETER")
                    echo "---Realizando configuraciones para realizar servicios con Jmeter---"
                    "$PWD/jmeter.sh"  "$project_name"
                    ;;
                "POSTMAN")
                    echo "---Realizando configuraciones para realizar servicios con Postman---"
                    "$PWD/postman.sh" "$project_name"
                    ;;
                *)
                    ;;
            esac
        fi
    done
}

main