from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
import features.selectores as sel






def desplazar_hasta_elemento(driver, locator, intentos=3):
    """Desplaza la pantalla hasta que el elemento sea visible."""
    for _ in range(intentos):
        try:
            elemento = driver.find_element(*locator)
            if elemento.is_displayed():
                return
        except:
            pass
        scroll_hasta_abajo(driver)

def scroll_hasta_abajo(driver):
    """Desplaza la pantalla hacia abajo."""
    dimensiones = driver.get_window_size()
    ancho = dimensiones['width']
    alto = dimensiones['height']
    inicio_x = ancho // 2
    inicio_y = alto - 100
    fin_y = 100
    scroll_action = TouchAction(driver)
    scroll_action.press(x=inicio_x, y=inicio_y).move_to(x=inicio_x, y=fin_y).release().perform()

def obtener_elemento(driver, locator, tiempo_espera=10):
    """Espera hasta que el elemento sea visible."""
    return driver.find_element(*locator)

# def esperar_elemento_desaparecido(driver, locator, tiempo_espera=10):
#     """Espera hasta que el elemento desaparezca."""
#     return WebDriverWait(driver, tiempo_espera).until_not(EC.presence_of_element_located(locator))

def obtener_titulo(driver):
    """Obtiene el título de la página."""
    return driver.title


def scroll_vertical_por_tamaño_pantalla(driver, distancia):
    size = driver.get_window_size()

    # Coordenadas para el inicio y fin del scroll
    start_y = size['height'] * 0.8
    end_y = size['height'] * 0.2

    # Realizar el scroll vertical
    driver.swipe(size['width'] // 2, start_y, size['width'] // 2, end_y, distancia)

"""
Scroll horizontal tamaño pantala Firefox
"""
def scroll_horizontal_by_screen_size(driver, start_x_ratio, end_x_ratio, y_ratio=0.5, duration=800):
    """
    Realiza un scroll horizontal basado en un porcentaje del tamaño de la pantalla.

    :param driver: La instancia del driver de Appium.
    :param start_x_ratio: Relación de la posición inicial en el eje X (0 a 1, donde 0 es el extremo izquierdo y 1 es el extremo derecho).
    :param end_x_ratio: Relación de la posición final en el eje X (0 a 1).
    :param y_ratio: Relación de la posición en el eje Y para realizar el scroll (0 a 1, donde 0 es la parte superior y 1 es la parte inferior).
    :param duration: Tiempo del deslizamiento en milisegundos (por defecto es 800ms).
    """
    size = driver.get_window_size()
    start_x = int(size['width'] * start_x_ratio)
    end_x = int(size['width'] * end_x_ratio)
    y_position = int(size['height'] * y_ratio)

    action = TouchAction(driver)
    action.press(x=start_x, y=y_position).wait(ms=duration).move_to(x=end_x, y=y_position).release().perform()

    pass

def scroll_vertical_distancia(driver,selector,start,end):
    # Obten las coordenadas del elemento
    campo = driver.find_element(*selector)
    location = campo.location

    # Calcula las coordenadas para el scroll (puedes ajustar el desplazamiento según tus necesidades)
    start_y = location['y'] + int(start)
    end_y = location['y'] - int(end)

    # Realiza el scroll
    driver.swipe(location['x'], start_y, location['x'], end_y, duration=500)
    pass



def insertar_y_limpiar_campo(driver, selector, texto):
    driver.implicitly_wait(17)
    campo = driver.find_element(*selector)
    campo.click()
    campo.clear()  # Limpiar el campo
    campo.send_keys(texto)  # Insertar texto en el campo

    # campo.hide_keyboard(key_name='Done')

    # Alternativamente, puedes tocar fuera del campo para desenfocarlo y ocultar el teclado
    # TouchAction(driver).tap(x=100, y=100).perform()

    # Enviar la tecla "Enter" o "Return" para ocultar el teclado
    # campo.send_keys("\n")  # Esto puede variar dependiendo del teclado del dispositivo

    pass


def scroll_10_por_ciento(driver, direccion):
    dimensiones = driver.get_window_size()
    ancho = dimensiones['width']
    alto = dimensiones['height']
    inicio_x = ancho // 2
    inicio_y = int(alto * 0.9)  # 90% del alto de la pantalla
    fin_x = inicio_x
    fin_y = int(alto * 0.1)  # 10% del alto de la pantalla

    if direccion == 'abajo':
        scroll_action = TouchAction(driver)
        scroll_action.press(x=inicio_x, y=inicio_y).move_to(x=fin_x, y=fin_y).release().perform()
    # Agrega más casos para otras direcciones si es necesario


def presionar_return(driver):
    try:
        # Envía la secuencia de escape para la tecla "Return"
        driver.press_keycode(66)  # Código de tecla para "Return"
    except:
        pass  # Manejar la excepción si no se puede simular la tecla "Return"


def click_boton(driver,selector):
    driver.implicitly_wait(50)
    campo = driver.find_element(*selector)
    campo.click()
    pass


def clic_coordenadas(driver,x,y):
    x_coordinate = x
    y_coordinate = y
    driver.tap([(x_coordinate, y_coordinate)])
    pass



def scroll_vertical_por_coordenadas(driver,y):
    start_x = 300
    start_y = 800
    end_x   = 900
    end_y   = y
    # driver.swipe(start_x, start_y, end_x, end_y, duration=200)
    driver.swipe(start_x, start_y, end_x, end_y)
    pass

def scroll_vertical_por_coordenadas_2(driver,x_int,y_int,x_fin,y_fin):
    start_x = x_int
    start_y = y_int
    end_x   = x_fin
    end_y   = y_fin
    # driver.swipe(start_x, start_y, end_x, end_y, duration=200)
    driver.swipe(start_x, start_y, end_x, end_y)
    pass



def calendario_fechas(driver,aend_y,mend_y,dend_y):
    driver.implicitly_wait(50)
    # AÑO - 1997
    start_x = 562
    start_y = 1340
    end_x   = 562
    end_y   = aend_y 
    driver.swipe(start_x, start_y, end_x, end_y, duration=800)
    driver.implicitly_wait(40)
    # valor    
    # MES - Mayo
    start_x = 313
    start_y = 1370
    end_x   = 313
    end_y   = mend_y  # valor   
    
    
    driver.swipe(start_x, start_y, end_x, end_y, duration=800)
    driver.implicitly_wait(30) 
                
    # DIA - 16    > 70 por cada uno
    start_x = 100
    start_y = 1370
    end_x   = 100
    end_y   = dend_y # valor  
    
    driver.swipe(start_x, start_y, end_x, end_y, duration=800)  
    pass
    

        




    # Ejemplo de uso

    
    
    def validar_string_en_lista(driver,lugar_nacimiento_curp):
        lista = ["HIDALGO", "JALISCO", "MICHOACAN DE OCAMPO", "MORELOS", "NAYARIT", "NUEVO LEON", "OAXACA", "PUEBLA","QUERETARO", "QUINTANA ROO", "SAN LUIS POTOSI", "SINALOA", "SONORA", "TABASCO", "TAMAULIPAS", "TLAXCALA", "VERACRUZ DE IGNACIO DE LA LLAVE","YUCATAN", "ZACATECAS", "EXTRANJERO"]

        if lugar_nacimiento_curp in lista:
            return True
        else:
            return False
        


    

    
            




# Scroll horizontal
def scroll_horizontal_between_elements(driver, start_element, end_element, duration=800):
    """
    Realiza un scroll horizontal desde un elemento inicial hasta un elemento final.

    :param driver: La instancia del driver de Appium.
    :param start_element: El elemento inicial desde el cual comenzar el scroll.
    :param end_element: El elemento final hasta el cual realizar el scroll.
    :param duration: Tiempo del deslizamiento en milisegundos (por defecto es 800ms).
    """
    start_location = start_element.location
    end_location = end_element.location

    action = TouchAction(driver)
    action.press(x=start_location['x'], y=start_location['y']) \
          .wait(ms=duration) \
          .move_to(x=end_location['x'], y=end_location['y']) \
          .release() \
          .perform()


def scroll_horizontal_25_percent(driver, start_y_ratio=0.5, duration=800):
    """
    Realiza un scroll horizontal avanzando un 25% del ancho de la pantalla.

    :param driver: La instancia del driver de Appium.
    :param start_y_ratio: Relación de la posición en el eje Y para realizar el scroll (0 a 1, donde 0 es la parte superior y 1 es la parte inferior).
    :param duration: Tiempo del deslizamiento en milisegundos (por defecto es 800ms).
    """
    size = driver.get_window_size()
    start_x = size['width'] * 0.75  # Comienza desde el 75% del ancho de la pantalla
    end_x = size['width'] * 0.5  # Termina en el 50% del ancho de la pantalla
    start_y = size['height'] * start_y_ratio

    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=start_y).release().perform()

    pass



def scroll_horizontal_custom(driver, start_x, start_y, end_x, end_y, duration=800):
    """
    Realiza un scroll horizontal desde una coordenada específica hasta otra coordenada específica.

    :param driver: La instancia del driver de Appium.
    :param start_x: Coordenada X inicial desde donde comenzará el scroll.
    :param start_y: Coordenada Y inicial desde donde comenzará el scroll.
    :param end_x: Coordenada X final donde terminará el scroll.
    :param end_y: Coordenada Y final donde terminará el scroll.
    :param duration: Tiempo del deslizamiento en milisegundos (por defecto es 800ms).
    """
    action = TouchAction(driver)
    action.press(x=start_x, y=start_y).wait(ms=duration).move_to(x=end_x, y=end_y).release().perform()
    pass




""" Clic en elemento por coordenadas"""
def click_by_coordinates(driver, x, y):
    """
    Realiza un clic en la pantalla en las coordenadas especificadas.

    :param driver: La instancia del driver de Appium.
    :param x: Coordenada X donde se realizará el clic.
    :param y: Coordenada Y donde se realizará el clic.
    """
    action = TouchAction(driver)
    action.tap(x=x, y=y).perform()
    pass





# Clic por coordenadas
def find_element_in_coordinates_and_click(driver, elements, x_min, x_max, y_min, y_max):
    """
    Encuentra un elemento dentro de un rango de coordenadas y realiza un clic en él.

    :param driver: La instancia del driver de Appium.
    :param elements: Lista de elementos a evaluar (por ejemplo, obtenidos con find_elements_by_*).
    :param x_min: Coordenada X mínima del rango.
    :param x_max: Coordenada X máxima del rango.
    :param y_min: Coordenada Y mínima del rango.
    :param y_max: Coordenada Y máxima del rango.
    :return: True si se encontró un elemento y se hizo clic en él, False si no se encontró.
    """
    for element in elements:
        location = element.location
        size = element.size

        # Calcular las coordenadas del elemento
        x_center = location['x'] + size['width'] / 2
        y_center = location['y'] + size['height'] / 2

        # Verificar si el centro del elemento está dentro del rango especificado
        if x_min <= x_center <= x_max and y_min <= y_center <= y_max:
            if element.is_displayed() and element.is_enabled():
                element.click()
                return True
            else:
                print("Elemento encontrado, pero no está visible o habilitado.")
                return False

    print("No se encontró ningún elemento en el rango especificado.")
    return False
