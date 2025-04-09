import json, time
from appium import webdriver
from appium.options.android import UiAutomator2Options
import os, sys, re, allure
import csv
from utils.csv_loader import load_csv
from behave.model import ScenarioOutline, Examples, Table

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'




# def before_scenario(context, scenario):
#     # Cargar el archivo CSV correspondiente según el escenario
#     if "consulta_rapida_basica" in scenario.tags:
#         context.data_file = "eatures/data/consulta_rapida.csv"
#     elif "Inicio de sesión inválido" in scenario.tags:
#         context.data_file = "features/data/invalid_logins.csv"
#     elif "Casos límite" in scenario.tags:
#         context.data_file = "features/data/edge_cases.csv"

#     # Leer los datos del archivo CSV y guardarlos en el contexto
#     with open(context.data_file, newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         context.data = [row for row in reader]


# def load_csv(file_path):
#     """Carga los datos desde un archivo CSV y los devuelve como una lista de diccionarios."""
#     try:
#         with open(file_path, mode="r", encoding="utf-8") as file:
#             reader = csv.DictReader(file)
#             data = [row for row in reader]
#             # Verificar que los datos fueron cargados correctamente
#             print(f"Datos cargados desde el CSV: {data}")
#             if not data:
#                 raise ValueError(f"El archivo CSV '{file_path}' está vacío o no tiene datos.")
#             return data
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Archivo CSV no encontrado: {file_path}")



def switch_example(value):
    match value:
        case 1:
            return "Valor es 1"
        case 2:
            return "Valor es 2"
        case 3 | 4:
            return "Valor es 3 o 4"
        case _:
            return "Valor desconocido"



def before_feature(context, feature):
    
    """Genera dinámicamente los ejemplos para los Scenario Outline desde un archivo CSV."""
    for scenario in feature.scenarios:
        # if isinstance(scenario, ScenarioOutline) and "Hacer clic en el botón de Consulta Grupal" in scenario.name:
        #     print(f"Procesando Scenario Outline: {scenario.name}")

        if isinstance(scenario, ScenarioOutline):
            print(f"Procesando Scenario Outline: {scenario.name}")

            # Asignar archivo CSV según el nombre del escenario
            if "Realizar consulta rápida basica hasta el CDC" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "consulta_rapida"

            #BASICOS VALIDACIONES
            elif "Realizar consulta rápida lista negra" in scenario.name:
                csv = "features/data/curp_lista_negra.csv"
                feature = "curp_lista_negra"
                
            elif "Buscar usuario y registrar sci" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "buscar_usuarios_reg_sci"

            elif "Agregar los documentos del prospecto" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "buscar_usuarios_reg_sci"

            elif "Consulta rápida completa de una prospecta" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "consulta_rapida"

            elif "Consulta rápida desde OCR" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "consulta_rapida"

            elif "Crear grupo nuevo" in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "mis_grupos"


            elif "Buscar grupo y agregar prospecta" in scenario.name:
                csv = "features/data/consulta_rapida_basica.csv"
                feature = "formalizar_grupo"
            
            elif "Buscar grupo y formalizar" in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "formalizar_grupo"

            elif "Genera grupo nuevo, formaliza y envia a MC" in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "mis_grupos"

            elif "Colocar el nombre a un grupo." in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "consulta_grupal"

            
            elif "Validar que no exista la posibilidad de crear un grupo con el mismo nombre." in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "consulta_grupal"


            
            elif "Devolucion digitalizacion" in scenario.name:
                csv = "features/data/grupo.csv"
                feature = "mis_grupos"

            elif "Realizando la renovacion de un grupo" in scenario.name:
                csv = "features/data/grupo_renovaciones.csv"
                feature = "renovaciones"

            else:
                print(f"Escenario {scenario.name} no requiere ejemplos dinámicos.")
                continue

            


            # Cargar datos desde el archivo CSV
            data = load_csv(csv)
            if not data:
                raise ValueError("El archivo CSV está vacío. No se pueden generar los ejemplos.")

            # Crear encabezado y filas para la tabla
            header = list(data[0].keys())
            rows = [[row[column] for column in header] for row in data]

            # Crear la tabla usando la clase Table
            table = Table(headings=header, rows=rows)
            print(f"Tabla generada dinámicamente: Encabezado - {table.headings}, Filas - {table.rows}")

            # Crear un objeto Examples y asignarlo al Scenario Outline
            example = Examples(
                filename=f"{feature}.feature",  # Nombre del archivo de la feature
                line=scenario.line,         # Número de línea donde se encuentra el ScenarioOutline
                keyword="Examples",         # Palabra clave 'Examples'
                name=scenario.name,       # Nombre que aparecerá en la tabla
                table=table                 # La tabla de datos que contiene los ejemplos
            )
            scenario.examples.append(example)
            # print(f"Ejemplos agregados dinámicamente a {scenario.name}: {example.table}")



    # for scenario in feature.scenarios:
    #     if isinstance(scenario, ScenarioOutline) and "Hacer clic en el botón de Consulta Grupal" in scenario.name:
    #         print(f"Procesando Scenario Outline: {scenario.name}")
            
    #         # Verifica si hay ejemplos
    #         if not scenario.examples:
    #             print(f"El escenario {scenario.name} no tiene ejemplos iniciales.")

    #         # Cargar datos desde el archivo CSV
    #         data = load_csv("features/data/cr.csv")
    #         if not data:
    #             raise ValueError("El archivo CSV está vacío. No se pueden generar los ejemplos.")
            


    #         # Crear encabezado y filas para la tabla
    #         header = list(data[0].keys())  # Extraer encabezados del primer registro
    #         rows = [[row[column] for column in header] for row in data]  # Crear las filas dinámicamente

            
    #         # Verificar si las filas se están generando correctamente
    #         print(f"Encabezado: {header}")
    #         print(f"Filas generadas para la tabla: {rows}")

    #         table = Table(headings=header, rows=rows)
            
    #         # Crear la tabla utilizando la clase Table
    #         # try:
    #         #     table = Table(header, rows)
    #         # except Exception as e:
    #         #     print(f"Error al crear la tabla: {e}")
    #         #     raise
            
    #         # Verificar la tabla
    #         # if not rows:
    #         #     print("Error: No se pudieron generar filas para la tabla. Revisa el archivo CSV.")
    #         # else:
    #         #     table = Table(header, rows)
    #         #     print(f"Tabla creada correctamente (encabezado): {table.headings}")
    #         #     print(f"Tabla creada correctamente (filas): {table.rows}")
            
    #         # # print(f"Datos cargados desde CSV: {data}")
            
    #         # # Crear y asignar la tabla de ejemplos
    #         # header = ["nombre", "ap_paterno", "ap_materno", "curp", "lugar_nacimiento"]
    #         # rows = [[row["nombre"], row["ap_paterno"], row["ap_materno"], row["curp"], row["lugar_nacimiento"]] for row in data]

    #         # print(f"Encabezado: {header}")
    #         # print(f"Filas generadas para la tabla: {rows}")
            
    #         # table = Table(header, rows)
    #         # print(f"Datos {rows}")

    #         # Asignar la tabla generada al Scenario Outline
    #         # Crear el objeto Examples con los argumentos necesarios
    #         example = Examples(
    #             filename="consulta_rapida.feature",  # Nombre del archivo de la feature
    #             line=scenario.line,         # Número de línea donde se encuentra el ScenarioOutline
    #             keyword="Examples",         # Palabra clave 'Examples'
    #             name="Hacer clic en el botón de Consulta Grupal",       # Nombre que aparecerá en la tabla
    #             table=table                 # La tabla de datos que contiene los ejemplos
    #         )

    #         # Verifica si los ejemplos han sido generados correctamente
    #         if not example.table:
    #             print(f"Error: No se generaron ejemplos para {scenario.name}")
    #         else:
    #             print(f"Ejemplos generados dinámicamente para {scenario.name}: {example.table}")
            
    #         # Agregar los ejemplos al Scenario Outline
    #         scenario.examples.append(example)
    #         # print(f"Ejemplos agregados a {scenario.name}: {example.table}")
            
    #         # print(f"Tabla creada (encabezado): {table.headings}")
    #         # print(f"Tabla creada (filas): {table.rows}")
    #         # Crear una tabla de Examples dinámicamente
           
            
           


# def before_scenario(context, scenario):
#     """Asocia datos CSV específicos al escenario basado en etiquetas."""
#     if "consulta_rapida_basica" in scenario.tags:
#         context.data = load_csv_to_examples("features/data/consulta_rapida.csv")
#     elif "dashboard" in scenario.tags:
#         context.data = load_csv_to_examples("features/data/dashboard_data.csv")
#     elif "settings" in scenario.tags:
#         context.data = load_csv_to_examples("features/data/settings_data.csv")

#     print(f"Datos cargados para {scenario.name}: {context.data}")


# def before_scenario(context, scenario):
#     # Usa una variable de entorno o cualquier lógica que determines
#     if os.environ.get("SKIP_SCENARIO", "false") == "true":
#         scenario.skip("Este escenario se ha saltado debido a la configuración.")


def before_all(context):
    """
    Configuración inicial para Appium según el entorno seleccionado.
    """
    # Leer el entorno desde la variable ENV o usar 'stg' por defecto
    # env = os.getenv("ENV", "prod")
    env = os.getenv("ENV", "stg")
    config_path = f"features/config/{env}_config.json"

    # Validar si el archivo de configuración existe
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Archivo de configuración no encontrado: {config_path}")

    # Cargar configuración
    with open(config_path, "r") as config_file:
        config = json.load(config_file)

    # Inicializar el WebDriver de Appium
    context.driver = webdriver.Remote("http://localhost:4723/wd/hub", config)
    
 

    context.env = env  # Guardar el entorno para referencia
    context.driver.implicitly_wait(4)
    time.sleep(1)


# def before_feature(context, feature):
#     pass
    
def before_step(context, step):
    # time.sleep(1)
    pass



    

def after_step(context, step):
    time.sleep(1)
    # Captura de pantalla después de cada paso
    
    screenshot_path = f"/home/cr/Documentos/Podemos/Proyectos/POD/p/movil_1/features/screenshots/{step.name.replace(' ', '_')}.png"
    context.driver.save_screenshot(screenshot_path)

    # Adjuntar la captura de pantalla a Allure
    allure.attach.file(screenshot_path, name=f"Screenshot: {step.name}", attachment_type=allure.attachment_type.PNG)

def after_scenario(context, scenario):
    # # Si el escenario falla, tomar captura de pantalla
    # if scenario.status == "failed":
    #     print(f"El escenario '{scenario.name}' falló.")
    #     screenshot_path = f"/home/cr/Documentos/Podemos/Proyectos/POD/p/movil_1/features/screenshots/{scenario.name}_failed.png"
    #     context.driver.save_screenshot(screenshot_path)

    #     # Adjuntar la captura de pantalla al reporte de Allure
    #     allure.attach.file(screenshot_path, name=f"Failed Scenario Screenshot: {scenario.name}", attachment_type=allure.attachment_type.PNG)
    #     sys.exit(1)  # Detiene la ejecución

    # Si el escenario falla, tomar captura de pantalla
    if scenario.status == "failed":
        print(f"❌ El escenario '{scenario.name}' falló. Deteniendo la ejecución.")

        # Reemplazar caracteres no válidos en el nombre del archivo
        valid_filename = re.sub(r'[^a-zA-Z0-9_\-]', '_', scenario.name)
        screenshot_path = f"/home/cr/Documentos/Podemos/Proyectos/POD/p/movil_1/features/screenshots/{valid_filename}_failed.png"

        # Capturar pantalla
        context.driver.save_screenshot(screenshot_path)

        # Adjuntar la captura de pantalla al reporte de Allure
        allure.attach.file(screenshot_path, name=f"Failed Scenario Screenshot: {scenario.name}", attachment_type=allure.attachment_type.PNG)

        # Detener la ejecución
        # sys.exit(1)  



def after_feature(context, feature):
    pass

def after_all(context):
    """
    Finaliza el WebDriver de Appium al final de todas las pruebas.
    Valida que el WebDriver se cierre correctamente.
    """
    if hasattr(context, "driver"):
        try:
            # Intenta cerrar el WebDriver
            context.driver.quit()
            print("WebDriver cerrado correctamente.")
            print("Termino el testing.")
        except Exception as e:
            # Captura cualquier excepción y la registra
            print(f"Error al cerrar el WebDriver: {e}")
        
    
