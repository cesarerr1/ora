from appium.webdriver.common.appiumby import AppiumBy
import time
from behave import given, when, then
from pages.consulta_rapida_page import ConsultaRapida
from pages.sci_datos_pages import SCI
from pages.documentos_pages import SCIDocumentos
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import features.selectores as sel
from appium.webdriver.common.touch_action import TouchAction



@when(u'buscar a: "{usuario}"')
def consultas_buscar(context, usuario ):  
    context.comienza_sci = SCI(context.driver)
    context.comienza_sci.busca_prospecta(usuario)
    pass

@then(u'seleccionar al usuario del listado de la busqueda realizada')
def selecciona_usuaior_del_listado(context):

    context.home_page = SCI(context.driver)
    context.home_page.selecciona_usuaior_del_listado_de_busqueda()

    pass


@then(u'seleccionar solicitud individual')
def continuar_solicitud_individual(context):
    context.comienza_sci = SCI(context.driver)
    # context.comienza_sci.btn_emg_solicitud_individual()
    context.comienza_sci.click_dynamic_button()
    """BUG cambiar nombre elemento y validar donde impacta el cambio"""
    

    pass


@then(u'comienzo con la captura de datos complementarios de la prospecta "{estado_civil_soltera}" "{escolaridad}"')
def comienza_captura_datos_complementarios_uno(context, estado_civil_soltera, escolaridad):  
    context.datos_complementarios_prospecta = SCI(context.driver)
    context.datos_complementarios_prospecta.captura_datos_complementarios_prospecta(estado_civil_soltera, escolaridad)
    pass

@then(u'captura datos domicilio antiguedad')
def datos_domicilio(context):   
    context.datos_complementarios_domicilio = SCI(context.driver)
    context.datos_complementarios_domicilio.captura_datos_complementarios_prospecta_domicilio()   
    pass

@then(u'acreditacion del domicilio INE:"{ine}" parentesco:"{parentesco}"')
def datos_domicilio(context,ine,parentesco):
    context.datos_complementarios_parentesco = SCI(context.driver)
    context.datos_complementarios_parentesco.captura_datos_complementarios_parentesco(ine, parentesco) 
    pass
    

@then(u'captura de datos familiar "{nombre_familiar}" "{tel_familiar}" "{caracteristicas_vivienda}" "{referencia_ubicacion}"')
def datos_domicilio(context,nombre_familiar, tel_familiar, caracteristicas_vivienda, referencia_ubicacion):
    context.datos_complementarios_familiares = SCI(context.driver)
    context.datos_complementarios_familiares.captura_datos_complementarios_de_familiares(nombre_familiar, tel_familiar, caracteristicas_vivienda, referencia_ubicacion)
    pass

@then(u'captura datos actividad economica "{direccion_del_negocio}" "{ganancia_semanal}" "{otros_ingresos}" "{monto_pago_semanal}"')
def datos_actividad_econimica(context, direccion_del_negocio, ganancia_semanal, otros_ingresos, monto_pago_semanal):
    context.datos_complementarios_actividad_economica = SCI(context.driver)
    context.datos_complementarios_actividad_economica.captura_datos_complementarios_de_actividad_economica(direccion_del_negocio, ganancia_semanal, otros_ingresos, monto_pago_semanal)
    pass


@then(u'captura datos referencia uno "{nombre_referencia}" "{tel_referencia_celular}"')
def datos_referencia_uno(context, nombre_referencia, tel_referencia_celular):
    context.datos_complementarios_referencia_personal_uno = SCI(context.driver)
    context.datos_complementarios_referencia_personal_uno.captura_datos_complementarios_de_referencia_uno(nombre_referencia, tel_referencia_celular)
    pass


@then(u'captura datos referencia dos "{nombre_referencia2}" "{tel_referencia_celular2}"')
def datos_referencia_dos(context, nombre_referencia2, tel_referencia_celular2):
    context.datos_complementarios_referencia_personal_dos = SCI(context.driver)
    context.datos_complementarios_referencia_personal_dos.captura_datos_complementarios_de_referencia_dos(nombre_referencia2, tel_referencia_celular2)
    pass
    
    
@then(u'captura datos crediticios "{monto_credito}" "{origen_recursos_credito}" "{destino_recursos_credito}"')
def datos_crediticios(context, monto_credito, origen_recursos_credito, destino_recursos_credito):
    context.datos_complementarios_crediticios = SCI(context.driver)
    context.datos_complementarios_crediticios.captura_datos_complementarios_crediticios(monto_credito, origen_recursos_credito, destino_recursos_credito)
    pass


@then(u'Volver al inicio con scroll')
def regresa_inicio(context):
    context.link_regresa_inicio = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.link_regresa_inicio.link_regresa_inicio_fin()
    pass





"""DENTRO DE LA sci PARA EDICION"""
@then(u'seleccionar btn documentos')
def btn_documentos(context):
    context.tap_sci_documnetos = SCI(context.driver)
    context.tap_sci_documnetos.tap_documentos_sci()

    pass


@then(u'selecciona btn para adjuntar comprobante frontal')
def btn_adjunta_comp_domicilio_frontal(context):
    context.tap_sci_documnetos = SCIDocumentos(context.driver)
    context.tap_sci_documnetos.btn_adjunta_comp_domicilio_frontal()

    pass


@then(u'seleccionar opcion almacenamiento')
def btn_opt_almacenamiento(context):
    context.sel_btn_almacenamiento = SCIDocumentos(context.driver)
    context.sel_btn_almacenamiento.btn_almacenamiento()
    pass


@then(u'selecciona y confirma imagen de google imagenes')
def btn_opt_almacenamiento_img_google(context):    
    context.sel_img_google = SCIDocumentos(context.driver)
    context.sel_img_google.btn_opt_almacenamiento_imagen()

    pass




@then(u'selecciona btn para adjuntar comprobante reverso')
def btn_adjunta_comp_domicilio_reverso(context):
    context.adjunta_comp_domicilio_reverso = SCIDocumentos(context.driver)
    context.adjunta_comp_domicilio_reverso.btn_opt_adjunta_comp_domicilio_reverso()
    
    pass


@then(u'selecciona btn para adjuntar ine frontal')
def btn_adjunta_ine_frontal(context):
    context.adjunta_ine_frontal = SCIDocumentos(context.driver)
    context.adjunta_ine_frontal.btn_opt_adjunta_ine_frontal()
    
    pass

@then(u'selecciona btn para adjuntar ine reverso')
def btn_adjunta_ine_reverso(context):
    context.adjunta_ine_reversio = SCIDocumentos(context.driver)
    context.adjunta_ine_reversio.btn_opt_adjunta_ine_reverso()
    
    pass

@then(u'finalizar registro')
def btn_finaliza_registro(context):
    
    context.finaliza_registro = SCIDocumentos(context.driver)
    context.finaliza_registro.btn_finaliza_registro()
    
    pass