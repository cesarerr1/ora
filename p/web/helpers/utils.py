


from selenium.webdriver.support.wait import WebDriverWait
# import features.selectores as sel


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



def scroll_vertical_por_coordenadas(driver,y):
    start_x = 300
    start_y = 800
    end_x   = 300
    end_y   = y
    # driver.swipe(start_x, start_y, end_x, end_y, duration=200)
    driver.swipe(start_x, start_y, end_x, end_y)




def calendario_fechas(driver,aend_y,mend_y,dend_y):
    driver.implicitly_wait(50)
    # AÑO - 1997
    start_x = 562
    start_y = 1340
    end_x   
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
        
    pass

    
def test_negative(self): 
    firstValue = "geeks"
    secondValue = "gfg"
    # error message in case if test case got failed 
    message = "First value and second value are not equal !"
    # assertEqual() to check equality of first & second value 
    self.assertEqual(firstValue, secondValue, message) 
    pass

    
            



