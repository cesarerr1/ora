from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class TextValidationError(Exception):
    """Excepción personalizada para errores en la validación de texto."""
    pass

def is_element_visible_and_text_in_list(self, by, locator, text_list):
    """
    Verifica si un elemento es visible en la pantalla y valida si su texto está en una lista dada.
    Si la validación falla, genera una excepción personalizada.
    """
    try:
        # Intentar encontrar el elemento
        element = self.driver.find_element(by, locator)
        
        # Verificar si el elemento es visible
        if element.is_displayed():
            # Obtener el texto del elemento
            element_text = element.text.strip()
            print(f"Texto del elemento encontrado: {element_text}")

            # Validar si el texto está en la lista usando assertIn
            if element_text not in text_list:
                raise TextValidationError(f"Error: El texto '{element_text}' no está en la lista esperada: {text_list}")

            print(f"El texto '{element_text}' está en la lista esperada.")
            return True
        else:
            raise TextValidationError(f"Error: El elemento con el locator {locator} no está visible.")

    except NoSuchElementException:
        raise TextValidationError(f"Error: No se pudo encontrar el elemento con el locator {locator}.")