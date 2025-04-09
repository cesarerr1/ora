from pages.base_page import BasePage
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction
import utils.utils as utilerias
import random
import features.selectores as sel


class SCI(BasePage):
    # solicitud_individual = (AppiumBy.XPATH, '//android.view.View[@content-desc="Sombreado"]')
    # solicitud_individual = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Continuar Solicitud")')
    solicitud_individual = (AppiumBy.CLASS_NAME, "android.view.View")
    def __init__(self, driver):
        super().__init__(driver)
        
    # btn_continuar_solicitud = (AppiumBy.ANDROID_UIAUTOMATOR, sel.TapConsultas.btn_busqueda_continuar_sci)
    buscar = (AppiumBy.ACCESSIBILITY_ID, "Buscar")
    ingresa_numre_prospecta = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    selecciona_primer_usuario_listado = (AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().className("android.widget.Button").instance(1)')
    

    # input_tel_recados = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_recados)
    select_estado_civil = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.estado_civil)
    soltera = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_estado_civil_soltera)
    select_escolaridad = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.escoladidad)
    secundaria = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_escoladidad_secundaria)
    input_tel_celular = (AppiumBy.CLASS_NAME, sel.Genericos.selecciona_elemento_segun_el_orden_2)
    tel_celular_colocando_valor = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_celular_colocando_valor)

    btn_siguiente = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_guardar)

    """DATOS DOMICILIO"""
    antigduedad_domicilio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.antigduedad_domicilio)
    select_antigduedad_domicilio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_antigduedad_domicilio)
    tipo_domicilio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tipo_domicilio)
    select_tipo_domicilio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_tipo_domicilio)

    """DATOS PARENTESCO"""
    radio_ine_si = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.radio_ine_si)
    radio_ine_no = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.radio_ine_no)
    parentesco_comprobante = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.parentesco_comprobante_entrega)
    select_parentesco_comprobante_entrega = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_parentesco_comprobante_entrega)

    """DATOS PARENTESCOS FAMILIARES"""
    lbl_nombre_familiar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.nombre_familiar)
    lbl_tel_familiar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_familiar)
    parentesco_familiar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.parentesco_familiar)
    select_parentesco_familiar = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_parentesco_familiar)
    dependentes_familiares = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.dependentes_familiares)
    select_dependentes_familiares = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_dependentes_familiares)
    lbl_caracteristicas_vivienda = (AppiumBy.XPATH, sel.SCI.caracteristicas_vivienda)
    lbl_referencia_ubicacion = (AppiumBy.XPATH, sel.SCI.referencia_ubicacion)

    """DATOS COMPLEMENTARIOS ACTIVIDAD ECONOMICA"""
    actividad_economica = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.actividad_economica)
    select_actividad_economica = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_actividad_economica)
    actividad_adiciional = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.actividad_adiciional)
    select_actividad_adiciional = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_actividad_adiciional)
    antiguedad_negocio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.antiguedad_negocio)
    select_antiguedad_negocio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_antiguedad_negocio)
    dia_venta_lu = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.dia_venta_lu)
    dia_venta_ma = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.dia_venta_ma)
    dia_venta_mi = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.dia_venta_mi)
    ubicacion_negocio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.ubicacion_negocio)
    select_ubicacion_negocio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_ubicacion_negocio)
    lbl_direccion_del_negocio = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.direccion_del_negocio)
    lbl_ganancia_semanal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.ganancia_semanal)
    lbl_otros_ingresos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.otros_ingresos)
    fuentes_otros_ingresos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.fuentes_otros_ingresos)
    select_fuentes_otros_ingresos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_fuentes_otros_ingresos)
    lbl_monto_pago_semanal = (AppiumBy.XPATH, sel.SCI.monto_pago_semanal)
    # btn_siguiente = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_guardar)

    """DATOS COMPLEMENTARIOS REFERENCIAS PERSONALES"""
    select_referncia_uno = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_referncia_uno)
    lbl_nombre_completo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.nombre_referencia)
    parentesco_referencia = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.parentesco_referencia)
    select_parentesco_referencia = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_parentesco_referencia)
    lbl_tel_referencia_recardos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_referencia_recardos)
    lbl_tel_referencia_celular = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_referencia_celular)

    select_referncia_dos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_referncia_dos)
    lbl_nombre_completo2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.nombre_referencia)
    parentesco_referencia2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.parentesco_referencia)
    select_parentesco_referencia2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.select_parentesco_referencia)
    lbl_tel_referencia_recardos2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_referencia_recardos)
    lbl_tel_referencia_celular2 = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.tel_referencia_celular)


    """DATOS COMPLEMENTARIOS CREDITICIOS"""
    lbl_monto_credito = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.monto)
    lbl_origen_recursos_credito = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.origen_recursos)
    lbl_destino_recursos_credito = (AppiumBy.ANDROID_UIAUTOMATOR, sel.SCI.destino_recursos)


    """ Home SCI """
    home_tap_documnetos = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_documentos)
    
    
    
    
    def get_dynamic_element(self, field_name):
        return (AppiumBy.XPATH, f"//android.widget.EditText[@content-desc='{field_name}']")
    def busca_prospecta(self,usuario):
        time.sleep(7)
        self.click(*self.buscar)
        self.interactura_elemento(*self.ingresa_numre_prospecta, usuario)
        pass

    def selecciona_usuaior_del_listado_de_busqueda(self):
        time.sleep(7)
        # try:
        # self.click(*self.selecciona_primer_usuario_listado)
        self.click_btn(*self.selecciona_primer_usuario_listado)
        #     return True
        # except  NameError:
        #     return False
        pass
    def btn_emg_solicitud_individual(self):
        time.sleep(1)
        # self.click_s(*self.solicitud_individual,0)
        self.click(*self.solicitud_individual)
        # self.tap_by_coordinates(300,1402) 
        time.sleep(10)

        pass
    def click_dynamic_button(self):
        try:
            # Intentar clic normal
            self.wait_and_click(*self.solicitud_individual)
            # self.tap_by_coordinates(300,1402) 
        except Exception as e:
            print(f"El botón no es clickeable directamente: {e}")
            # Hacer clic por coordenadas como alternativa
            element = self.find_element(*self.solicitud_individual)
            # self.tap_by_coordinates(300,1402) 
            location = element.location
            size = element.size
            center_x = location['x'] + size['width'] / 2
            center_y = location['y'] + size['height'] / 2
            self.click_by_coordinates(center_x, center_y)
        time.sleep(7)

    """BUG NO SE REALIZO EL ENVIO DEL NIP"""
    def continuar_solicitud(self):
        self.click(*self.solicitud_individual)
        pass

    """enado de primer formulario """
    def captura_datos_complementarios_prospecta(self, estado_civil_soltera, escolaridad):
        estado_civil_soltera = estado_civil_soltera
        self.click(*self.select_estado_civil)
        self.click(*self.soltera)
        escolaridad = escolaridad
        self.click(*self.select_escolaridad)
        self.click(*self.secundaria)

        numero_aleatorio = ''.join(random.choices('0123456789', k=10))
        # numero_aleatorio = random.randint(10**9, (10**10) - 1)
        # self.interactura_elemento_y_limpia(*self.input_tel_celular)
        self.click_s(*self.input_tel_celular,2)
        self.interactura_elemento(*self.tel_celular_colocando_valor,numero_aleatorio)
                
        
        self.scroll(500, 1200, 500, 300)
        # self.click(*self.btn_siguiente)
        # time.sleep(2)
        self.click_btn(*self.btn_siguiente,timeout=3)
        pass

    def captura_datos_complementarios_prospecta_domicilio(self):
        self.click(*self.antigduedad_domicilio)
        self.click(*self.select_antigduedad_domicilio)
        self.click(*self.tipo_domicilio)
        self.click(*self.select_tipo_domicilio)
        pass

    def captura_datos_complementarios_parentesco(self, ine, parentesco):
        ine = ine
        parentesco = parentesco
        self.click(*self.radio_ine_no)
        self.click(*self.parentesco_comprobante)
        self.click(*self.select_parentesco_comprobante_entrega)
        self.scroll(500, 1200, 500, 300)
        pass

    def captura_datos_complementarios_de_familiares(self, nombre_familiar, tel_familiar, caracteristicas_vivienda, referencia_ubicacion):
        
        self.interactura_elemento(*self.lbl_nombre_familiar,nombre_familiar)
        self.interactura_elemento(*self.lbl_tel_familiar,tel_familiar)
        self.scroll(500, 900, 500, 100)

        self.click(*self.parentesco_familiar)
        self.click(*self.select_parentesco_familiar)
        self.click(*self.dependentes_familiares)
        self.click(*self.select_dependentes_familiares)
        self.interactura_elemento(*self.lbl_caracteristicas_vivienda,caracteristicas_vivienda)
        self.interactura_elemento(*self.lbl_referencia_ubicacion,referencia_ubicacion)
        # self.click(*self.btn_siguiente)
        self.click_btn(*self.btn_siguiente,timeout=4)
        # time.sleep(2)
        pass

    def captura_datos_complementarios_de_actividad_economica(self, direccion_del_negocio, ganancia_semanal, otros_ingresos, monto_pago_semanal):    
        self.click(*self.actividad_economica)
        self.click(*self.select_actividad_economica)
        self.click(*self.actividad_adiciional)
        self.click(*self.select_actividad_adiciional)
        self.click(*self.antiguedad_negocio)
        self.click(*self.select_antiguedad_negocio)
        # self.click(*self.dia_venta_lu )
        self.click(*self.dia_venta_ma)
        
        self.scroll(500, 1200, 500, 300)
        self.click(*self.ubicacion_negocio)
        self.click(*self.select_ubicacion_negocio)
        self.interactura_elemento(*self.lbl_direccion_del_negocio,direccion_del_negocio)
        self.interactura_elemento(*self.lbl_ganancia_semanal,ganancia_semanal)
        self.scroll(500, 1200, 500, 300)
        self.interactura_elemento(*self.lbl_otros_ingresos,otros_ingresos)
        self.click(*self.fuentes_otros_ingresos)
        self.click(*self.select_fuentes_otros_ingresos)
        self.interactura_elemento(*self.lbl_monto_pago_semanal,monto_pago_semanal)
        # self.click(*self.btn_siguiente)
        # time.sleep(2)
        self.click_btn(*self.btn_siguiente,timeout=3)
        pass

    def captura_datos_complementarios_de_referencia_uno(self, nombre_referencia, tel_referencia_celular):
        self.click(*self.select_referncia_uno)
        self.interactura_elemento(*self.lbl_nombre_completo, nombre_referencia)
        self.click(*self.parentesco_referencia)
        self.click(*self.select_parentesco_referencia)
        self.interactura_elemento(*self.lbl_tel_referencia_celular,tel_referencia_celular)
        self.scroll(500, 1200, 500, 300)
        pass

    def captura_datos_complementarios_de_referencia_dos(self, nombre_referencia2, tel_referencia_celular2):
        self.click(*self.select_referncia_dos)
        self.scroll(500, 1200, 500, 300)
        self.interactura_elemento(*self.lbl_nombre_completo2,nombre_referencia2)
        self.click(*self.parentesco_referencia2)
        self.click(*self.select_parentesco_referencia2)
        self.interactura_elemento(*self.lbl_tel_referencia_celular2,tel_referencia_celular2)
        # self.click(*self.btn_siguiente)
        self.click_btn(*self.btn_siguiente,timeout=3)
        pass

    def captura_datos_complementarios_crediticios(self, monto_credito, origen_recursos_credito, destino_recursos_credito):
        time.sleep(5)
        self.interactura_elemento(*self.lbl_monto_credito,monto_credito)
        self.scroll(500, 1200, 500, 300)
        self.interactura_elemento(*self.lbl_origen_recursos_credito,origen_recursos_credito)
        self.interactura_elemento(*self.lbl_destino_recursos_credito,destino_recursos_credito)  
        # self.click(*self.btn_siguiente)
        self.click(*self.btn_siguiente)
        time.sleep(4)
        pass

    def tap_documentos_sci(self):
        time.sleep(4)
        self.click(*self.home_tap_documnetos)
        time.sleep(4)
        pass

    