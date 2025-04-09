from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, signal

from utils import functions_auxiliar_web as FAW
from pages.pagina_login import PaginaLogin
import time 

def before_all(context):

    download_dir = "/home/cr/Documentos/InstalacionFramework/Lucy/web/docs"

    chrome_options = webdriver.ChromeOptions()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Inicia maximizado
    chrome_options.add_argument("--no-sandbox")  # Evita problemas de permisos
    chrome_options.add_argument("--disable-notifications")  # Desactiva notificaciones
    chrome_options.add_argument("--disable-software-rasterizer")  # Evita problemas de renderizado
    chrome_options.add_argument("--no-sandbox")  # Evita problemas de permisos
    chrome_options.add_argument("--disable-dev-shm-usage")  # Usa memoria en disco en lugar de /dev/shm
    chrome_options.add_argument("--disable-software-rasterizer")  # Evita problemas de renderizado
    chrome_options.add_argument("--disable-extensions")  # Desactiva extensiones
    chrome_options.add_argument("--disable-infobars")  # Oculta la barra de "Chrome está controlado por una prueba automática"
    chrome_options.add_argument("--disable-popup-blocking")  # Evita bloqueos de ventanas emergentes

    # chrome_options.add_argument("--disable-popup-blocking")  # Desactiva bloqueador de pop-ups
    # chrome_options.add_argument("--incognito")  # Modo incógnito
    # chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica (opcional)
    # chrome_options.add_argument("--no-sandbox")  # Previene problemas en entornos restringidos
    # chrome_options.add_argument("--disable-gpu")  # Desactiva GPU (necesario para Headless en algunos casos)
    # chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("--disable-web-security")  # Desactiva extensiones
    # chrome_options.add_argument("--remote-debugging-port=9222")  # Puerto para depuración remota


    prefs = {
        # "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "useAutomationExtension": False,
        "headless":False,
        "profile.default_content_setting_values.notifications": 1,  # 1 para aceptar, 2 para bloquear
        "profile.default_content_setting_values.geolocation": 1,    # 1 para permitir, 2 para bloquear
        "profile.default_content_setting_values.media_stream": 1,    # 1 para permitir acceso a la cámara/micrófono
        "profile.default_content_settings.popups": 0,  # Desactiva pop-ups en descargas
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    

    chrome_options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/")
    context.driver.implicitly_wait(13)

    pass
def before_feature(context, feature):
    pass
    
def before_step(context, step):
    context.current_step_name = step.name
    pass

    
def after_feature(context, feature):
    pass

def after_all(context):
    time.sleep(3)
    """
    Finalizar el WebDriver después de todos los escenarios.
    """
    if hasattr(context, "driver"):
        context.driver.quit()  # Cierra el navegador
    else:
        print("El atributo 'driver' no está definido en el contexto.")

    try:
        context.driver.quit()  # Cierra el navegador y detiene el proceso
    except Exception as e:
        print(f"Error al cerrar WebDriver: {e}")

    # # Obtiene el PID del WebDriver y lo mata manualmente
    # pid = context.driver.service.process.pid
    # os.kill(pid, signal.SIGTERM)  # Forzar cierre del proceso
    # print(f"🛑 WebDriver detenido con PID {pid}")

    pass
