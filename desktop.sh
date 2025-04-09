#!/bin/bash

# Obtener el valor de $project_name pasado como argumento
project_name="$1"

# Crear la estructura de carpetas
cd "$project_name" || exit
cd "desktop"
mkdir features
mkdir features/steps
mkdir helpers
mkdir imgs
mkdir screenshots

# Mensaje de confirmación
echo 
echo "¡La estructura de carpetas para usar desktop en '$project_name' ha sido creada con éxito!"
echo 

# Verificar si tkinter ya está instalado
if ! dpkg -l | grep -qw python3-tk; then
    # Si no está instalado, instalar tkinter
    echo "Tkinter no está instalado. Instalando..."
    
    if sudo apt-get install python3-tk python3-dev; then
        echo "Tkinter instalado con éxito."
        source ~/.bashrc
    else
        echo "Error: No se pudo instalar Tkinter"
        exit 1
    fi
else
    echo "Tkinter ya está instalado."
fi

# Verificar si gnome-screenshot ya está instalado
if ! dpkg -l | grep -qw gnome-screenshot; then
    # Si no está instalado, instalar gnome-screenshot
    echo "gnome-screenshot no está instalado. Instalando..."
    if sudo apt install gnome-screenshot; then
        echo "gnome-screenshot instalado con éxito."
        source ~/.bashrc
    else
        echo "Error: No se pudo instalar gnome-screenshot"
        exit 1
    fi
else
    echo "gnome-screenshot ya está instalado."
fi


# Mensaje de pipenv entorno virtual
echo "Creando el entorno virtual de desktop, espere por favor..."

# Entorno virtual
echo "Entorno virtual creado satisfactoriamente"
echo 

# Instalación de dependencias 
echo "Instalando dependencias, espere por favor..."

# Ejecutar los comandos y redirigir la salida para que no sea visible
{
    pip install behave 
    pip install allure-behave
    pip install pyautogui
    pip install python-dotenv
    pip install opencv-python
} > /dev/null 2>&1

# Dependencias instaladas
echo "Las dependencias fueron instaladas correctamente"
echo

# Archivo de nivel de confianza para la identificación de imagenes
cat <<EOF > .env
# Configuración del nivel de confianza para la identificación de imágenes
CONFIDENCE_LEVEL=0.7

# Configuración del tiempo mínimo para la búsqueda de imágenes en pantalla acepta valores flotantes
MIN_SEARCH_TIME=5.0

# Configuración del tiempo de espera entre acciones del sistema con la librería pyautogui acepta valores flotantes
WAIT_TIME_UI=0.5

# Intervalo de tiempo en segundos, que se espera entre las letras al escribir una palabra, acepta valores flotantes
WRITE_INTERVAL=0.0
EOF

# Guarda la representación base64 de la imagen en una variable
base64_image="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"

# Decodifica la imagen base64 y la guarda en un archivo
echo "$base64_image" | base64 -d > ./imgs/bluetooth.png
# Entro en features
cd features

# Define el nombre del archivo .feature
nombre_archivo="exampleDesktop.feature"

# Redirige el contenido al archivo .feature
cat > "$nombre_archivo" <<END
# language: es

@login
Característica: Abrir configuración

Antecedentes:
    Dado Que estoy en el SO ubuntu

  @loginValido
  Esquema del escenario: Ver bluetooth
    Cuando Abro la aplicación de configuración "<app>"
    Y Hago click en bluetooth
    Entonces Se muestra el menu de bluetooth
    Entonces cierro configuración

    Ejemplos:
      | app                            |
      | gnome-control-center           |
END

cd steps

# Define el nombre del archivo de steps
nombre_steps="exampleDesktop.py"

# Redirige el contenido al archivo de steps
cat > "$nombre_steps" <<END
from behave import given, when, then
import subprocess
import time
from helpers.functionsAuxiliarDesktop import (
    click_centro_imagen,
    captura_allure,
    atajo_teclado,
    adjuntar_texto_allure,
    version_so
)

@given("Que estoy en el SO ubuntu")
def step_impl(context):
    try:
        adjuntar_texto_allure(str(version_so()),"Versión del SO")
    except Exception as e:
        print("Error al recuperar la versión del SO:", e)

@when("Abro la aplicación de configuración {app}")
def step_impl(context, app):
    try:
        subprocess.Popen(['gnome-control-center'])
        time.sleep(2)
        captura_allure("Configuración")
    except Exception as e:
        print("Error al abrir la aplicación de configuración:", e)

@when("Hago click en bluetooth")
def step_impl(context):
    click_centro_imagen("./imgs/bluetooth.png")

@then("Se muestra el menu de bluetooth")
def step_impl(context):
    time.sleep(2)
    captura_allure("bluetooth")

@then("cierro configuración")
def step_impl(context):
    atajo_teclado("alt", "f4")
    
END

# Entrar en la carpeta base del proyecto 
cd ..
cd ..

# Entrar a helpers
cd helpers

# Crear archivo __init__.py

nombre_init="__init__.py"

cat > "$nombre_init" <<END

END

# Crear archivo helpers 
nombre_helpers="functionsAuxiliarDesktop.py"

cat > "$nombre_helpers" <<END
import allure
import pyautogui
import os
from dotenv import load_dotenv

load_dotenv()

CONFIDENCE_LEVEL = os.getenv("CONFIDENCE_LEVEL")
MIN_SEARCH_TIME = float(os.getenv("MIN_SEARCH_TIME"))
WAIT_TIME_IU = float(os.getenv("WAIT_TIME_UI"))
WRITE_INTERVAL = float(os.getenv("WRITE_INTERVAL"))

def adjuntar_texto_allure(informacion, titulo):
    allure.attach(informacion, name=titulo, attachment_type=allure.attachment_type.TEXT)

def version_so():
    sistema_operativo = os.uname()
    return f"{sistema_operativo.sysname} {sistema_operativo.release} {sistema_operativo.version}"

def captura_allure(nombre_captura: str):
    if not nombre_captura or not isinstance(nombre_captura, str):
        raise ValueError(
            "El argumento 'nombre' es obligatorio y debe ser de tipo string."
        )
    screenshot_path = f"./screenshots/{nombre_captura}.png"
    pyautogui.screenshot(screenshot_path)
    # Adjunta la captura de pantalla al informe Allure
    allure.attach.file(
        screenshot_path,
        name="Captura de Pantalla",
        attachment_type=allure.attachment_type.PNG,
    )

def click_centro_imagen(ruta_imagen, confidence=CONFIDENCE_LEVEL):
    pyautogui.click(
        pyautogui.locateCenterOnScreen(
            ruta_imagen, confidence=confidence, minSearchTime=MIN_SEARCH_TIME
        )
    )

def atajo_teclado(*teclas):
    pyautogui.hotkey(teclas)
END
# Salir de helpers
cd ..
cd ..

