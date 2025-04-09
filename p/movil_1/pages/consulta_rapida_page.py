from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import features.selectores as sel
import utils.utils as utilerias
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from features.steps.txt_valida import VAL_SECCION_TEXTO_CAPTURA_DATOS,FELICIDADES,NUEVA_CONULSTA,INFO_ADICIONAL,VALIDACION_CURP_LISTA_NEGRA,VALIDACION_CURP_LISTA_NEGRA_RAZON


class ConsultaRapida(BasePage):
   
    def __init__(self, driver, lugar_nacimiento):
        super().__init__(driver)
        self.lugar_nacimiento = lugar_nacimiento
        # self.select_entidad_nacimiento = (AppiumBy.XPATH, f'//android.view.View[@content-desc="{self.lugar_nacimiento}"]')
        self.select_entidad_nacimiento = (AppiumBy.XPATH, f'//android.view.View[@content-desc="AGUASCALIENTES"]')
        

    opt_captura_manual = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="RECOMENDADO\nManualmente\nLlena la información de forma manual"]')
    input_nombre_emprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.NOMBRE)
    input_ap_paterno_emprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.APELLIDO_PATERNO)
    input_ap_materno_emprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.APELLIDO_MATERNO)
    input_curp_emprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.CURP)
    select_fecha_nacimiento_mprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.DatosEmprendedora.FECHA_NACIMIENTO)
    btn_confirmo_fechacimiento_eprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.CONFIRMAR_FECHA_NACIMIENTO)
    entidad_nacimiento_emprendedora = (AppiumBy.XPATH, sel.DatosEmprendedora.ENTIDAD_NACIMIENTO)
    input_telefono_emprendedora = (AppiumBy.XPATH, sel.DatosContacto.NUMERO_TELEFONO)
    input_confirma_telefono_emprendedora = (AppiumBy.XPATH, sel.DatosContacto.CONFIRMACION_NUMERO)
    btn_continuar_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_continuar)

    # Direccion
    input_calle_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Direccion.DIR_CALLE)
    input_exterior_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Direccion.N_EXTERIOR)
    input_cp_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Direccion.CP)
    btn_colonia_poblacion = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Direccion.COLONIA_POBLACION)    
    els2 = (AppiumBy.CLASS_NAME, "android.view.View")
    btn_continuar_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_continuar)

    btn_continuar_solicitud_emprendedora = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_continuar2)
    btn_enviar_nip = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_enviar_nip)
    input_otp_nip1 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Otp.caracter_otp_1)
    input_otp_nip2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Otp.caracter_otp_2)
    btn_consultar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_consultar)
    link_regresa_inicio = (AppiumBy.XPATH, sel.AccionFormulario.link_regresa_inicio)
    
    """Validando consulta rapida"""
    primer_elemento_de_la_lista = (AppiumBy.CLASS_NAME, sel.Genericos.selecciona_elemento_segun_el_orden)
    txt_felicidades = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Cdc.txt_felicidades)
    txt_ver_info_adicional = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Cdc.txt_ver_info_adicional)
    txt_nueva_consulta = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Cdc.txt_nueva_consulta)
    
    """Validaciones lista negra"""
    txt_validacion_curp_lista_negra = (AppiumBy.ANDROID_UIAUTOMATOR, sel.ValidacionesConsultaRapida.txt_validacion_curp_lista_negra)
    txt_validacion_curp_lista_negra_razon = (AppiumBy.ANDROID_UIAUTOMATOR, sel.ValidacionesConsultaRapida.txt_validacion_curp_lista_negra_razon)
    
    
    """OCR"""
    btn_captura_datos_desde_ocr = (AppiumBy.ANDROID_UIAUTOMATOR, sel.OCR.btn_captura_datos_desde_ocr)
    txt_valida_seccion_datos_personales = (AppiumBy.ANDROID_UIAUTOMATOR, sel.OCR.txt_valida_seccion_datos_personales)
    

       
    def click_consulta_rapida(self):
        self.click(*self.opt_captura_manual)

    def click_select_entidad_nacimiento(self):
        self.click(*self.select_entidad_nacimiento)

    def captura_datos_manuales_de_emprendedora(self, nombre_emprendedora,ap_paterno_emprendedora,ap_materno_emprendedora, curp_emprendedora, lugar_nacimiento):
        self.interactura_elemento(*self.input_nombre_emprendedora,nombre_emprendedora)
        self.interactura_elemento(*self.input_ap_paterno_emprendedora,ap_paterno_emprendedora)
        self.interactura_elemento(*self.input_ap_materno_emprendedora,ap_materno_emprendedora)     
        self.interactura_elemento(*self.input_curp_emprendedora,curp_emprendedora)
        self.click(*self.select_fecha_nacimiento_mprendedora)
        self.click(*self.btn_confirmo_fechacimiento_eprendedora)
        self.click(*self.entidad_nacimiento_emprendedora)
        # self.click(*self.select_entidad_nacimiento_emprendedora)
        self.click(*self.select_entidad_nacimiento)
        
        pass

 
    def telefono_emprendedora_y_confirmacion(self, telefono, confirmacion):       
        self.interactura_elemento(*self.input_telefono_emprendedora,telefono)
        # self.scroll(500, 1200, 500, 300)
        self.interactura_elemento(*self.input_confirma_telefono_emprendedora,confirmacion)
        self.click(*self.btn_continuar_emprendedora)
        pass


    def direccion_emprendedora(self, cp, calle, n_exterior):
        self.interactura_elemento(*self.input_calle_emprendedora,calle)
        self.interactura_elemento(*self.input_exterior_emprendedora,n_exterior)
        self.scroll(500, 1200, 500, 300)
        self.interactura_elemento(*self.input_cp_emprendedora,cp)
        time.sleep(4)
        self.click(*self.btn_colonia_poblacion)
        time.sleep(1)
        self.click_s(*self.els2,1)
        # self.scroll(500, 1200, 500, 300)     
        self.click(*self.btn_continuar_emprendedora)
        pass


    def continuar_confirmar_envio_nip(self):
        self.click(*self.btn_continuar_solicitud_emprendedora)
        pass

    def confirmar_envio_nip(self):
        self.click(*self.btn_enviar_nip)
        pass

    

    def acepta_tyc(self):
        time.sleep(1)
        
        self.tap_by_coordinates(611,984)    
        pass

    def confirmar_otp(self):
        self.interactura_elemento(*self.input_otp_nip1, "0")
        self.interactura_elemento(*self.input_otp_nip2, "0")
        pass
    def consulta_cdc(self):
        self.click(*self.btn_consultar)
        pass

    def link_regresa_inicio_fin(self):
        time.sleep(10)
        
        
        if self.is_element_visible(*self.link_regresa_inicio):
            self.click_if_visible(*self.link_regresa_inicio)
        else:
            self.scroll(500, 1000, 500, 100)

            self.click_if_visible(*self.link_regresa_inicio)
            print("El botón dinámico no está presente en la pantalla.")
        
        # self.scroll(500, 1200, 500, 300)
        # self.click(*self.link_regresa_inicio)
        pass

    """OCR"""
    def captura_datos_desde_ocr(self):
        # elemento = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Captura datos personales")')  # Mejor usar descriptionContains
        # descripcion = elemento.get_attribute("contentDescription")
        # assert "CAPTURA" in descripcion.upper(), f"❌ ERROR: La descripción no contiene 'Captura'. Texto encontrado: {descripcion}"
        
        self.assert_element_contains_text(*self.txt_valida_seccion_datos_personales, VAL_SECCION_TEXTO_CAPTURA_DATOS)
        
        self.click(*self.btn_captura_datos_desde_ocr)
        pass


    def validar_prospecta_en_consultas(self,nombre,ap_paterno,ap_materno):
        time.sleep(3)
        self.click_s(*self.primer_elemento_de_la_lista,10)
        time.sleep(2)
        nombre_completo_prospecta = f"{nombre} {ap_paterno} {ap_materno}"
        self.assert_element_contains_text(*self.txt_felicidades, FELICIDADES)       
        self.assert_element_contains_text(*self.txt_nueva_consulta, NUEVA_CONULSTA)
        self.assert_element_contains_text(*self.txt_ver_info_adicional, INFO_ADICIONAL)
        pass
    

    def validar_curp_lista_negra(self):
        self.assert_element_contains_text(*self.txt_validacion_curp_lista_negra, VALIDACION_CURP_LISTA_NEGRA)
        self.assert_element_contains_text(*self.txt_validacion_curp_lista_negra_razon, VALIDACION_CURP_LISTA_NEGRA_RAZON)
        pass


    def valida_rechazo(self):

        
        pass