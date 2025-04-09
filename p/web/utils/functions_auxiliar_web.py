from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from utils import errors as ERR
import time
import os

def clic(driver, web_elemento, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.element_to_be_clickable(web_elemento)
    )
    element.click()


def enviar_datos(driver, web_elemento, texto, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    element.send_keys(texto)

def limpiar(driver, web_elemento, tiempo_espera=10):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    content = element.get_attribute('value')
    content_length = len(content)
    element.send_keys(Keys.BACKSPACE * content_length)


def clic_elemento_por_texto(driver, web_elemento, texto, tiempo_espera=10):
    elements = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_all_elements_located(web_elemento)
    )
    for element in elements:
        if element.text == texto:
            element.click()
            return

def elemento_presente(driver, web_elemento, tiempo_espera=10):
    try:
        WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        return True
    except TimeoutException:
        return False

def obtener_archivo_carpeta(archivo):
    carpeta = os.path.abspath("./files/upload")
    ruta_completa = os.path.join(carpeta,archivo)
    if os.path.isfile(ruta_completa):
        return ruta_completa
    else:
        raise Exception("El archivo no existe")
    
def validar_campo(driver,web_elemento,tiempo_espera=3):
    try:
        elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        if elemento.is_displayed():
            message = elemento.text
            ERR.validacion(message)
    except TimeoutException:
        ERR.elemento_no_encontrado(web_elemento)
    except Exception as e:
        raise e
    
def validar_elemento(driver,web_elemento,mensaje_error_web,tiempo_espera=3):
    try:
        elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        try:
            elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(mensaje_error_web)
            )
            if elemento.is_displayed():
                message = elemento.text
                ERR.validacion(web_elemento,message)
        except TimeoutException:
            ERR.elemento_no_encontrado(web_elemento)
    except TimeoutException:
        ERR.elemento_no_encontrado(web_elemento)
    except Exception as e:
        raise e


def scroll_to_element(driver, by, value, step=200, delay=0.2, timeout=10):
    """
    Realiza un scroll vertical con velocidad media hasta encontrar un elemento en el DOM.
    
    :param driver: Instancia del WebDriver de Selenium.
    :param by: Estrategia de búsqueda (By.ID, By.XPATH, By.CLASS_NAME, etc.).
    :param value: Valor del selector para localizar el elemento.
    :param step: Número de píxeles por desplazamiento. (Por defecto: 200)
    :param delay: Tiempo en segundos entre desplazamientos. (Por defecto: 0.2)
    :param timeout: Tiempo máximo en segundos para localizar el elemento. (Por defecto: 10)
    :return: El elemento encontrado o lanza una excepción si no se encuentra.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            # Intentar localizar el elemento
            elemento = driver.find_element(by, value)
            if elemento.is_displayed():
                print("Elemento localizado y visible.")
                return elemento
        except Exception:   
            pass

        # Hacer scroll hacia abajo
        driver.execute_script(f"window.scrollBy(0, {step});")
        time.sleep(delay)

    raise Exception("Elemento no encontrado dentro del tiempo especificado.")