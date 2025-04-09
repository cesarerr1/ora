from pages.base_page import BasePage
from pages.text_validation_error import TextValidationError
from appium.webdriver.common.appiumby import AppiumBy
import features.selectores as sel
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Renovaciones(BasePage):
    btn_img__menu_renovaciones = (AppiumBy.XPATH, sel.Home.img_btn_mis_renovaciones)

    #Filtro
    btn_abrir_menu_filtro = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.btn_menu_filtro)
    btn_abrir_opciones_filtro_estatus = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.abrir_opciones_filtro_estatus)
    btn_quitar_check_filtro = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.quitar_check_filtro)
    btn_aplicar_filtro_estatus = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.aplicar_filtro_estatus)
    lbl_ingresar_nombre_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.buscador_grupo_renovacion)
    primer_grupo_encontrado = (AppiumBy.CLASS_NAME, sel.Renovaciones.primer_grupo_encontrado)
    
    #Inicio de renovacion
    tap_historial_credito = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.tap_historial_credito)
    btn_iniciar_renovacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.btn_iniciar_renovacion)
    msj_validar_renovacion_iniciada = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.msj_renovacion_iniciada)
    btn_aceptar_aceptar_renovacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_confir_aceptar)

    check_acciones_renovacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.check_acciones_renovacion)
    btn_aceptar_incio_renovacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.btn_aceptar_incio_renovacion)
    car_mas_opciones6 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.car_mas_opciones6)
    car_mas_opciones7 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.car_mas_opciones7)
    car_mas_opciones8 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.car_mas_opciones8)
    actualizar_sci_renovacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Renovaciones.actualizar_sci_renovacion)


    
    # lbl_ingresar_nombre_grupo = (AppiumBy.XPATH, 'new UiSelector().className("android.widget.EditText")')
    # lbl_buscar_grupo_devolucion = (AppiumBy.XPATH, '//android.widget.EditText')

    # btn_formalizar_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_formaliza_grupo)
    # btn_aceptar_formalizar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_confir_aceptar)
    # tap_devoluciones = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.tap_devolucion)
    # clic_card_grupo_devuelto = (AppiumBy.CLASS_NAME, sel.Grupo.clic_card_grupo_devuelto)

    # btn_actualizar_solicitud_grupal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_actualizar_solicitud_grupal)
    # btn_actualizar_solicitud_grupal_2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_actualizar_solicitud_grupal_2)
    # btn_continuar_devolucion_mc = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_continuar_devolucion)

    # #Validadndo que se envio al mc
    # val_seccion_mis_grupos = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Mis grupos")')
    

    def btn_menu_renovaciones(self): 
        self.click(*self.btn_img__menu_renovaciones)
        pass

    def btn_filtro(self): 
        self.click(*self.btn_abrir_menu_filtro)
        self.click(*self.btn_abrir_opciones_filtro_estatus)
        self.click(*self.btn_quitar_check_filtro)
        self.click(*self.btn_aplicar_filtro_estatus)
        time.sleep(2)
        pass


    def buscar_grupo(self, nombre_grupo):
        self.interactura_elemento(*self.lbl_ingresar_nombre_grupo,nombre_grupo)
        time.sleep(3)

        self.is_element_visible_and_click(*self.primer_grupo_encontrado)
        self.click(*self.tap_historial_credito)
        self.click(*self.btn_iniciar_renovacion)
        
      
        # expected_texts = ["Guardar2", "Cancelar3", "Confirmar4"]

        # try:
        #     if self.is_element_visible_and_text_in_list(*self.msj_validar_renovacion_iniciada, expected_texts):
        #         print("El texto del elemento está en la lista esperada.")
        # except TextValidationError as e:
        #     print(str(e))        
        # pass
        self.click(*self.btn_aceptar_aceptar_renovacion)
        time.sleep(3)
        self.click(*self.check_acciones_renovacion)
        time.sleep(7)
        self.click(*self.btn_aceptar_incio_renovacion)
        self.click(*self.tap_historial_credito)
        self.click(*self.btn_iniciar_renovacion)
        time.sleep(4)
        self.click(*self.car_mas_opciones6)
        self.click(*self.actualizar_sci_renovacion)


    """
    
    
    """

    # def ingresa_nombre_grupo(self,nombre_grupo): 
    #     self.interactura_elemento(*self.lbl_ingresar_nombre_grupo,nombre_grupo)
    #     pass


    # def btn_para_formalizar_grupo(self):

    #     count_btn_formalizar_grupo = self.find_elements(*self.btn_formalizar_grupo)
        
    #     if len(count_btn_formalizar_grupo) >= 13:
    #         # Verificar que el botón esté visible
    #         if self.is_element_visible(self.find_element(*self.btn_formalizar_grupo), timeout=10):
    #             self.click(*self.btn_formalizar_grupo)
    #             return True
    #         else:
    #             raise Exception(f"El elemento {self.find_element(*self.btn_formalizar_grupo)} no está visible.")
    #     else:
    #         # raise Exception(
    #         #     f"Solo se encontraron {len(btn_formalizar_grupo)} elementos con {validate_locator}, se requieren al menos {min_count}."
    #         # )
    #         return False


    #     self.click(*self.btn_formalizar_grupo)
    #     self.click(*self.btn_aceptar_formalizar)

    #     pass

    # def tap_para_devolucion_digitalizacion(self): 
    #     time.sleep(3)
    #     self.click(*self.tap_devoluciones)
    #     pass

    # def buscar_grupo_devolucion_digitalizacion(self, nombre_grupo):
    #     time.sleep(3)
    #     self.interactura_elemento(*self.lbl_buscar_grupo_devolucion,nombre_grupo)
    #     self.click(*self.clic_card_grupo_devuelto)
    #     time.sleep(2)
    #     #ACTUALIZAR SOLICITUD GRUPAL
    #     self.click(*self.btn_actualizar_solicitud_grupal)
    #     time.sleep(3)
    #     self.scroll(500, 1200, 500, 200)
    #     time.sleep(1)
    #     self.click(*self.btn_actualizar_solicitud_grupal_2)
    #     time.sleep(1)
    #     self.click(*self.btn_continuar_devolucion_mc)
    #     time.sleep(5)

 


    # def validar_seccion_mis_grupos(self):
    #     try:
    #         elemento = self.find_element(*self.val_seccion_mis_grupos)
    #         if not elemento.is_displayed():
    #             raise AssertionError("La sección 'Mis grupos' existe pero no está visible")
    #         print("✓ Validación exitosa: La sección 'Mis grupos' está presente y visible")
    #     except AssertionError as ae:
    #         raise AssertionError(f"❌ Fallo en la validación: {str(ae)}")
    #     except NoSuchElementException:
    #         raise AssertionError("❌ Fallo en la validación: La sección 'Mis grupos' no existe en la página")
    #     except TimeoutException:
    #         raise AssertionError("❌ Fallo en la validación: Tiempo de espera agotado buscando la sección 'Mis grupos'")
    #     except Exception as e:
    #         raise AssertionError(f"❌ Fallo inesperado en la validación: {str(e)}")
