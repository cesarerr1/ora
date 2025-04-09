import argparse
import subprocess
import sys

def run_command(command):
    """Ejecuta un comando en la línea de comandos y muestra el resultado."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}", file=sys.stderr)

def install_apk():
    # package_name = "horus.dev"
    device_id= "ZY2275RWC2"
    ruta_apk="/home/cr/Documentos/Podemos/Proyectos/POD/p/movil_1/app/"
    # nombre_apk="app-release-staging-13-agosto-24-15_39.apk"
    """Instala una APK en el dispositivo especificado."""
    command = ["adb", "-s", device_id, "install", "-r", ruta_apk+version_apk]
    run_command(command)

def permisos():
    package_name = "horus.dev"
    device_id= "ZY2275RWC2"
    # package_name = "horus.dev"
    # dispositivo ="ANDROID_SERIAL=" 
    # command = ["export",  dispositivo+device_id]
    # run_command(command)

    """Instala una APK en el dispositivo especificado."""
    # adb shell pm grant horus.dev android.permission.CAMERA 

    # command = ["adb", "-s", device_id, "install", "-r", ruta_apk+nombre_apk]
    # command = ["adb", "-s", device_id, "shell", "pm", "grant", "horus.dev", "android.permission.CAMERA" ]
    commands = [
        ["adb", "shell", "pm", "grant", package_name, "android.permission.CAMERA"],
        ["adb", "shell", "pm", "grant", package_name, "android.permission.ACCESS_FINE_LOCATION"],
        ["adb", "shell", "pm", "grant", package_name, "android.permission.ACCESS_COARSE_LOCATION"],
        ["adb", "shell", "pm", "grant", package_name, "android.permission.RECORD_AUDIO"],
        ["adb", "shell", "pm", "grant", package_name, "android.permission.WRITE_EXTERNAL_STORAGE"],       
        # ["adb", "shell", "pm", "grant", package_name, "android.permission.POST_NOTIFICATIONS "]
    ]
    
    for command in commands:
        run_command(command)
        
        # run_command(command)

    # run_command(command)


def uninstall_apk():
    """Desinstala una APK en el dispositivo especificado."""
    # package_name = get_package_name(apk_path)
    package_name = "horus.dev"
    # device_id= "R9YRA0NXZAY"
    # adb uninstall horus.dev
    if package_name:
        command = ["adb", "-s", device_id, "uninstall", package_name]
        run_command(command)
    else:
        print("Error: No se pudo obtener el nombre del paquete de la APK.", file=sys.stderr)

def get_package_name(apk_path):
    """Obtiene el nombre del paquete de la APK."""
    command = ["aapt", "dump", "badging", apk_path]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        for line in result.stdout.splitlines():
            if line.startswith("package:"):
                package_name = line.split("name='")[1].split("'")[0]
                return package_name
    except subprocess.CalledProcessError as e:
        print(f"Error al obtener el nombre del paquete: {e.stderr}", file=sys.stderr)
    return None

def show_menu():
    """Muestra el menú principal y maneja la selección del usuario."""
    while True:
        print("\nAPK Manager")
        print("1. Instalar APK")
        print("2. Desinstalar APK")
        print("3. Permisos APK")
        print("0. Salir")
        
        choice = input("Seleccione una opción (1/2/3/0): ").strip()
        
        if choice == '1':
            # device_id = input("Ingrese el ID del dispositivo: ").strip()
            # apk_path = input("Ingrese la ruta del archivo APK: ").strip()
            install_apk()
        elif choice == '2':
            # device_id = input("Ingrese el ID del dispositivo: ").strip()
            # apk_path = input("Ingrese la ruta del archivo APK: ").strip()
            # uninstall_apk(device_id, apk_path)
            uninstall_apk()
        elif choice == '3':
            permisos()
        elif choice == '0':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    device_id = "ZY2275RWC2"            # Motorola Podemos
    # device_id = "R9YRA0NXZAY"         # Samsung Cesar
    # device_id = "WPQBB20724204709"    # Reemplaza Huaweiodemos
    # device_id = "ZY2275RWC2"          # Reemplaza POO Podemos
    # package_name = "horus.dev"        # Reemplaza con el nombre del paquete de la APK

    version_apk = "stg_20241224_2-0-27.apk" # STG  Ultima version para validar
    # version_apk = "stg_20241221_2-0-27.apk" # STG  Ultima version para validar
    # version_apk = "prd_20241224_2-0-25.apk" # STG  Ultima version para validar


    # version_apk = "prd_20241202_2-0-25.apk" # PROD  Ultima version para validar
    # version_apk = "stg_20241012_2-0-26.apk" # STG  Ultima version para validar
    
    # version_apk = "spore-staging-33.apk" # STG Viejita
    # version_apk = "prd_20240923_2-0-25.apk" # SPORE_LOGIN_CE's
    show_menu()

# bORRAR CACHE DE ADB
# adb shell pm clear horus.dev1
