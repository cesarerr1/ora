from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, locator, timeout=1):
        """Espera hasta que el elemento esté presente y lo devuelve."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
    
    def find_elements(self, by, locator):
        return self.driver.find_elements(by, locator)
    
    def is_element_displayed(self, by, locator):
        element = self.find_element(by, locator)
        return element.is_displayed() if element else False
    


    # def click(self, by, locator):
    def click_s(self, by, locator, lugar,*args):
        element = self.find_elements(by, locator)
        element[lugar].click()

    def click(self, by, locator, *args):
        element = self.find_element(by, locator)
        element.click()

    def click_btn(self, by, locator, timeout=2, *args):
        element = self.find_element(by, locator)
        sleep(timeout)
        element.click()

    def interactura_elemento(self, by, value, text):
        element= self.find_element(by, value)
        element.click()
        element.clear()
        element.send_keys(text)
        self.driver.press_keycode(66)

    def interactura_elemento_y_limpia(self, by, value):
        element= self.find_element(by, value)
        element.click()
        element.clear()
        


    def send_keys(self, by, value, text):
        self.find_element(by, value).send_keys(text)
    
    def scroll(self, start_x, start_y, end_x, end_y):
        self.driver.swipe(start_x, start_y, end_x, end_y, 700)

    def clic_coordenadas(self, x_coordinate1, y_coordinate1):
    
        
        # x_coordinate1 = 611
        # y_coordinate1 = 984
        self.driver.tap([(x_coordinate1, y_coordinate1)])
        # driver.implicitly_wait(90)
        
    def tap_by_coordinates(self, x, y):
        """
        Simula un clic en una posición específica de la pantalla usando coordenadas.

        :param x: Coordenada X donde se realizará el clic.
        :param y: Coordenada Y donde se realizará el clic.
        """
        try:
            action = TouchAction(self.driver)
            action.tap(x=x, y=y).perform()
            print(f"Tocando en las coordenadas: ({x}, {y})")
        except Exception as e:
            print(f"Error al realizar el tap en las coordenadas ({x}, {y}): {e}")









    def is_element_visible(self, by, locator):
        """
        Verifica si un elemento es visible en la pantalla.
        """
        try:
            element = self.driver.find_element(by, locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False


    # Notion Valida si el elemento existe y da clic
    def is_element_visible_and_click(self, by, locator):
        """
        Verifica si un elemento es visible en la pantalla y hace clic en él si es visible.
        """
        try:
            # Intentar encontrar el elemento
            element = self.driver.find_element(by, locator)
            
            # Verificar si el elemento es visible
            if element.is_displayed():
                # Si el elemento es visible, hacer clic en él
                element.click()
                print(f"Elemento con el locator {locator} ha sido clickeado.")
                return True
            else:
                print(f"Elemento con el locator {locator} no está visible.")
                return False
        except NoSuchElementException:
            print(f"No se pudo encontrar el elemento con el locator {locator}.")
            return False



    #Notion Valida si el elemento existe y contine el texto
    def is_element_visible_and_text_in_list(self, by, locator, text_list):
        """
        Verifica si un elemento es visible en la pantalla y valida si su texto está en una lista dada.
        Usa assertIn para validar si el texto del elemento está presente en la lista de valores esperados.
        """
        try:
            # Intentar encontrar el elemento
            element = self.driver.find_element(by, locator)
            
            # Verificar si el elemento es visible
            if element.is_displayed():
                # Obtener el texto del elemento
                element_text = element.text
                print(f"Texto del elemento encontrado: {element_text}")
                
                # Validar si el texto está en la lista usando assertIn
                assert element_text in text_list, f"El texto '{element_text}' no está en la lista de valores esperados."
                print(f"El texto '{element_text}' está en la lista esperada.")
                return True
            else:
                print(f"Elemento con el locator {locator} no está visible.")
                return False
        except NoSuchElementException:
            print(f"No se pudo encontrar el elemento con el locator {locator}.")
            return False
        except AssertionError as e:
            # Captura el error de la aserción si el texto no está en la lista
            print(str(e))
            return False




    def scroll_to_element(self, by, locator):
        """
        Realiza un scroll hasta que el elemento sea visible.
        """
        while not self.is_element_visible(by, locator):
            # Realiza un scroll vertical hacia abajo
            self.driver.swipe(500, 1500, 500, 500, 800)
    
    def click_if_visible(self, by, locator):
        """
        Verifica si un elemento es visible y hace clic en él.
        """
        if self.is_element_visible(by, locator):
            self.driver.find_element(by, locator).click()
        else:
            print(f"Elemento con locator {locator} no encontrado o no visible.")







    def wait_and_click(self, by, locator, timeout=7):
        """Espera hasta que el elemento sea clickeable y hace clic."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, locator))
        )
        element.click()

    def click_by_coordinates(self, x, y):
        """Hace clic en las coordenadas especificadas."""
        TouchAction(self.driver).tap(x=x, y=y).perform()

    def find_element(self, by, locator, timeout=7):
        """Encuentra un elemento con espera explícita."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, locator))
        )
    




    def get_text_by_description(self, by, locator):       
        """
        Obtiene el texto de un elemento basado en el atributo `contentDescription`.
        """
        element = self.driver.find_element(by, locator)
        return element.get_attribute("contentDescription")
    


    """ Validando secciones"""
    def validar_seccion(self, by, locator, seccion_valida, timeout=1):       
        try:
            # elemento = self.find_element(*self.val_seccion_mis_grupos)
            elemento = self.find_element(by, locator)
            if not elemento.is_displayed():
                raise AssertionError(f"\033[91m ❌ La sección: {seccion_valida} existe pero no está visible\033[0m")
            print(f"\033[92m ✓ Validación exitosa: La sección: {seccion_valida} está presente y visible\033[0m")
        except AssertionError as ae:
            raise AssertionError(f"\033[91m ❌ Fallo en la validación 1: {str(ae)}\033[0m")
        except NoSuchElementException:
            raise AssertionError(f"\033[91m ❌ Fallo en la validación 2: La sección: {seccion_valida} no existe en la página\033[0m")
        except TimeoutException:
            raise AssertionError(f"\033[91m ❌ Fallo en la validación 3: Tiempo de espera agotado buscando la sección: {seccion_valida}\033[0m")
        except Exception as e:
            raise AssertionError(f"\033[91m ❌ Fallo inesperado en la validación: {str(e)}\033[0m")
        

    """ Validando texto por description"""
    def assert_element_contains_text(self, by, locator, expected_text="NO COLOCASTE NINGUN VALOR"):
        """
        Verifica si un elemento es visible y contiene un texto específico.
        
        - `by`: Tipo de localizador (By.XPATH, By.ID, etc.)
        - `locator`: Selector del elemento.
        - `expected_text`: Texto esperado dentro del elemento (por defecto: "CAPTURA").
        
        Lanza un AssertionError si el elemento no está visible o si el texto no coincide.
        """
        try:
            # Buscar el elemento
            element = self.driver.find_element(by, locator)
            
            # Verificar si el elemento está visible
            assert element.is_displayed(), f"\033[91m ❌ ERROR: El elemento {locator} no está visible en la pantalla.\033[0m"

            # Obtener el texto del elemento
            descripcion = element.get_attribute("content-desc") or element.text

            # Convertir a mayúsculas y hacer la validación
            # assert expected_text in descripcion.upper(), f"❌ ERROR: La descripción no contiene '{expected_text}'. Texto encontrado: {descripcion}"
            assert expected_text and descripcion, "\033[91m ❌ ERROR: 'expected_text' o 'descripcion' es None.\033[0m"

            assert expected_text.strip().upper() in descripcion.strip().upper(), f"\033[91m ❌ ERROR: La descripción no contiene '{expected_text}'. Texto encontrado: {descripcion}\033[0m"


            print(f"\033[92m ✅ Validación exitosa: El texto '{expected_text}' está presente en el elemento {locator}.\033[0m")
            return True  # Devuelve True si la validación es exitosa

        except NoSuchElementException:
            raise AssertionError(f"\033[91m ❌ ERROR: No se encontró el elemento {locator}\033[0m")
