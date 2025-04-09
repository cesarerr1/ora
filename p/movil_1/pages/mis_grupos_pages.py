from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import features.selectores as sel
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class MisGrupos(BasePage):
    btn_img__menu_mis_grupos = (AppiumBy.XPATH, sel.Home.img_btn_mis_grupos)
    lbl_ingresar_nombre_grupo = (AppiumBy.XPATH, 'new UiSelector().className("android.widget.EditText")')
    lbl_buscar_grupo_devolucion = (AppiumBy.XPATH, '//android.widget.EditText')

    btn_formalizar_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_formaliza_grupo)
    btn_aceptar_formalizar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_confir_aceptar)
    tap_devoluciones = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.tap_devolucion)
    clic_card_grupo_devuelto = (AppiumBy.CLASS_NAME, sel.Grupo.clic_card_grupo_devuelto)

    btn_actualizar_solicitud_grupal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_actualizar_solicitud_grupal)
    btn_actualizar_solicitud_grupal_2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_actualizar_solicitud_grupal_2)
    btn_continuar_devolucion_mc = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_continuar_devolucion)

    """Formalizar grupo nuevo"""
    primer_grupo_en_listado = (AppiumBy.CLASS_NAME, sel.Grupo.primer_grupo_en_listado)
    btn_cruzadas = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_cruzadas)
    """Generar la grupal"""
    btn_crear_solicitud_grupal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.btn_crear_solicitud_grupal)
    casa_reunion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.casa_reunion)
    
    dia = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.dia)
    dia_viernes = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.dia_viernes)
    lider = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.lider)
    selecciona_elemento_segun_el_orden = (AppiumBy.CLASS_NAME, sel.Genericos.selecciona_elemento_segun_el_orden)

    tesorera = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.tesorera)

    btn_enviar_a_mc = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCG.btn_enviar_a_mc)
    btn_continuar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_continuar)

    #Validadndo que se envio al mc
    val_seccion_mis_grupos = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Mis grupos")')
    

    def btn_menu_mis_grupos(self): 
        self.click(*self.btn_img__menu_mis_grupos)
        pass


    def ingresa_nombre_grupo(self,nombre_grupo): 
        self.interactura_elemento(*self.lbl_ingresar_nombre_grupo,nombre_grupo)
        pass


    def btn_para_formalizar_grupo(self):

        # count_btn_formalizar_grupo = self.find_elements(*self.btn_formalizar_grupo)
        
        # if len(count_btn_formalizar_grupo) >= 13:
        #     # Verificar que el botón esté visible
        #     if self.is_element_visible(self.find_element(*self.btn_formalizar_grupo), timeout=4):
        #         self.click(*self.btn_formalizar_grupo)
        #         self.click(*self.btn_aceptar_formalizar)
        #         return True
        #     else:
        #         raise Exception(f"El elemento {self.find_element(*self.btn_formalizar_grupo)} no está visible.")
        # else:
        #     # raise Exception(
        #     #     f"Solo se encontraron {len(btn_formalizar_grupo)} elementos con {validate_locator}, se requieren al menos {min_count}."
        #     # )
        #     return False

        time.sleep(2)
        self.click(*self.btn_formalizar_grupo)
        time.sleep(2)
        self.click(*self.btn_aceptar_formalizar)
        time.sleep(2)
        pass

    """Seleccionar grupo y formalizar"""
    def seleccionar_grupo_del_listado(self):
        time.sleep(5)
        self.click_s(*self.primer_grupo_en_listado,0)
        self.click(*self.btn_cruzadas)
        time.sleep(4)   
        self.click(*self.btn_crear_solicitud_grupal)
        time.sleep(3)   
        
        self.click(*self.casa_reunion)
        self.click_s(*self.selecciona_elemento_segun_el_orden,1)


        self.click(*self.dia)
        self.click(*self.dia_viernes)

        self.click(*self.lider)
        self.click_s(*self.selecciona_elemento_segun_el_orden,1)
        
        self.click(*self.tesorera)
        self.click_s(*self.selecciona_elemento_segun_el_orden,2)
        
        self.scroll(500, 1200, 500, 100)
        self.click(*self.btn_enviar_a_mc)
        self.click(*self.btn_continuar)
        
        pass

    def tap_para_devolucion_digitalizacion(self): 
        time.sleep(3)
        self.click(*self.tap_devoluciones)
        pass

    def buscar_grupo_devolucion_digitalizacion(self, nombre_grupo):
        time.sleep(3)
        self.interactura_elemento(*self.lbl_buscar_grupo_devolucion,nombre_grupo)
        self.click(*self.clic_card_grupo_devuelto)
        time.sleep(2)
        #ACTUALIZAR SOLICITUD GRUPAL
        self.click(*self.btn_actualizar_solicitud_grupal)
        time.sleep(3)
        self.scroll(500, 1200, 500, 200)
        time.sleep(1)
        self.click(*self.btn_actualizar_solicitud_grupal_2)
        time.sleep(1)
        self.click(*self.btn_continuar_devolucion_mc)
        time.sleep(5)

    # def buscar_grupo_devolucion_digitalizacion(self, nombre_grupo):
    #     try:
    #         time.sleep(3)
    #         self.interactura_elemento(*self.lbl_buscar_grupo_devolucion,nombre_grupo)
    #         self.click(*self.clic_card_grupo_devuelto)
    #         time.sleep(2)
    #         self.click(*self.btn_actualizar_solicitud_grupal)
    #         time.sleep(3)
    #         self.scroll(500, 1200, 500, 200)
    #         time.sleep(1)
    #         self.click(*self.btn_actualizar_solicitud_grupal_2)
    #         time.sleep(1)
    #         self.click(*self.btn_continuar_devolucion_mc)
    #         time.sleep(5)
            
    #         # Agregar mensaje descriptivo y tiempo de espera más largo
    #         if not self.is_element_visible(self.find_element(*self.btn_continuar_devolucion_mc), timeout=3):
    #             print("El botón 'Actualizar solicitud grupal -> MC' no está visible después de 3 segundos")
    #             return False
            
    #     except Exception as e:
    #         # Agregar mensaje más descriptivo para Allure
    #         print(f"Error: NO SE PUEDE ENVIAR AL MC: {str(e)}")
    #         return False
    #     pass


    def validar_seccion_mis_grupos(self):
        try:
            elemento = self.find_element(*self.val_seccion_mis_grupos)
            if not elemento.is_displayed():
                raise AssertionError("La sección 'Mis grupos' existe pero no está visible")
            print("✓ Validación exitosa: La sección 'Mis grupos' está presente y visible")
        except AssertionError as ae:
            raise AssertionError(f"❌ Fallo en la validación: {str(ae)}")
        except NoSuchElementException:
            raise AssertionError("❌ Fallo en la validación: La sección 'Mis grupos' no existe en la página")
        except TimeoutException:
            raise AssertionError("❌ Fallo en la validación: Tiempo de espera agotado buscando la sección 'Mis grupos'")
        except Exception as e:
            raise AssertionError(f"❌ Fallo inesperado en la validación: {str(e)}")
