from behave import given, when, then
from pages.home_page import HomePage
from pages.consulta_rapida_page import ConsultaRapida
# from utils.scroll_utils import scroll_vertical
import allure


@given(u'el usuario está en la pantalla principal')
def step_impl(context):
    # context.home_page_menu_consulta_rapida = ConsultaRapida(context.driver, lugar_nacimiento="0")
    # context.home_page_menu_consulta_rapida.click_consulta_rapida()

    pass

@when(u'el usuario hace clic en Consulta Rapida')
def genera_grupo(context):
    context.clic_menu_consulta_rapida = HomePage(context.driver)
    context.clic_menu_consulta_rapida.btn_menu_consulta_rapida()
    pass

@then(u'opcion de captura de datos manual')
def captura_manual(context, lugar_nacimiento="0"):
    context.home_page = ConsultaRapida(context.driver, lugar_nacimiento="0")
    context.home_page.click_consulta_rapida()
    pass


# ---------- Anterior
# @then(u'Ingresar datos de la emprendedora: "{nombre_emprendedora}" "{ap_paterno_emprendedora}" "{ap_materno_emprendedora}" "{curp_emprendedora}" "{lugar_nacimiento}"')
# @then(u'Ingresar datos de la emprendedora: "{nombre}" "{ap_paterno}" "{ap_materno}" "{curp}" "{lugar_nacimiento}"')
# def step_impl(context, nombre, ap_paterno, ap_materno, curp, lugar_nacimiento):
    
#     context.captura_datos_emprendedora = ConsultaRapida(context.driver, lugar_nacimiento)
#     context.captura_datos_emprendedora.captura_datos_manuales_de_emprendedora(nombre,ap_paterno,ap_materno, curp, lugar_nacimiento)
#     pass

@then(u'Ingresar datos de la emprendedora: "{nombre}" "{ap_paterno}" "{ap_materno}" "{curp}" "{lugar_nacimiento}"')
def step_impl(context, nombre, ap_paterno, ap_materno, curp, lugar_nacimiento):
    context.captura_datos_emprendedora = ConsultaRapida(context.driver, lugar_nacimiento)
    context.captura_datos_emprendedora.captura_datos_manuales_de_emprendedora(nombre,ap_paterno,ap_materno,curp,lugar_nacimiento)
    pass




# @then(u'Ingresar datos de la emprendedora: "{nombre}" "{ap_paterno}" "{ap_materno}" "{curp}" "{lugar_nacimiento}"')
# def step_impl(context, nombre, ap_paterno, ap_materno, curp, lugar_nacimiento):
#     if not context.data:
#         raise ValueError("No hay datos disponibles en context.data")
#     data = context.data.pop(0)  # Obtener el primer conjunto de datos
#     context.captura_datos_emprendedora = ConsultaRapida(context.driver, lugar_nacimiento)
#     context.captura_datos_emprendedora.captura_datos_manuales_de_emprendedora(data['nombre'],data['ap_paterno'],data['ap_materno'],data['curp'],data['lugar_nacimiento'])
#     pass



# ---------- Anterior
@then(u'Ingresar numero de telefono: "{telefono}" y su confirmación: "{confirmacion}"')
def step_impl(context, telefono, confirmacion):
    context.captura_datos_emprendedora = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.captura_datos_emprendedora.telefono_emprendedora_y_confirmacion(telefono, confirmacion)
    pass


# @then(u'Ingresar numero de telefono: "{telefono}" y su confirmación: "{confirmacion}"')
# @then(u'Ingresar numero de telefono: "{telefono}" y su confirmación: "{confirmacion}" direccion CP: "{cp}" calle: "{calle}" "{num_ext}"')
# def step_impl(context,telefono,confirmacion, cp, calle, num_ext):
#     data = context.data.pop(0)
#     context.captura_datos_emprendedora = ConsultaRapida(context.driver,lugar_nacimiento="0")
#     context.captura_datos_emprendedora.telefono_emprendedora_y_confirmacion(data['telefono'],data['confirmacion'])
#     context.captura_datos_emprendedora.direccion_emprendedora(data['cp'],data['calle'],data['num_ext'])
#     pass




@then(u'Validar curp lista negra')
def step_impl(context):
    context.captura_datos_lista_negra_curp = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.captura_datos_lista_negra_curp.validar_curp_lista_negra()
    pass



# ---------- Anterior
@then(u'Ingresar direccion CP: "{cp}" calle: "{calle}" "{num_ext}"')
def ingresa_direccion_prospecto(context, cp, calle, num_ext):
    context.captura_direccion_emprendedora = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.captura_direccion_emprendedora.direccion_emprendedora(cp,calle,num_ext)
    pass



# @then(u'Ingresar direccion CP: "{cp}" calle: "{calle}" "{num_ext}"')
# def ingresa_direccion_prospecto(context,cp,calle,num_ext):
#     data = context.data.pop(0)
#     context.captura_direccion_emprendedora = ConsultaRapida(context.driver,lugar_nacimiento="0")
#     context.captura_direccion_emprendedora.direccion_emprendedora(data['cp'],data['calle'],data['num_ext'])
#     pass


@then(u'Confirmar datos para enviar NIP')
def enviar_nip(context):
    context.enviar_nip = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.enviar_nip.confirmar_envio_nip()
    context.enviar_nip.continuar_confirmar_envio_nip()
    pass
    
@then(u'Acepta TYC')
def chk_terminos_y_condiciones(context):
    context.acepta_tyc = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.acepta_tyc.acepta_tyc()
    pass
    
@then(u'Respuesta de OTP')
def respuesta_otp(context):
    context.enviar_nip = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.enviar_nip.confirmar_otp()
    pass

@then(u'Realiza la consulta de CDC')
def continuar(context):
    context.btn = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.btn.consulta_cdc()
    pass
    
@then(u'Volver al inicio')
def regresa_inicio(context):

    context.link_regresa_inicio = ConsultaRapida(context.driver,lugar_nacimiento="0")
    context.link_regresa_inicio.link_regresa_inicio_fin()
    pass


# @then(u'selecciono al usuario del listado busqueda realizada')
# def regresa_inicio(context):
#     context.link_regresa_inicio = ConsultaRapida(context.driver,lugar_nacimiento="0")
#     context.link_regresa_inicio.selecciona_usuaior_del_listado_de_busqueda()
#     pass


""" Consulta rapida OCR"""
@then(u'opcion de captura de datos desde OCR')
@allure.step("Verificar que me encuentro en la pantalla de captura de datos personales")
# @allure.severity(allure.severity_level.CRITICAL)
def captura_datos_desde_ocr(context):
    with allure.step("Captura de datos personales"):
        context.captura_datos_desde_ocr = ConsultaRapida(context.driver,lugar_nacimiento="0")
        context.captura_datos_desde_ocr.captura_datos_desde_ocr()
    pass




@then(u'Validar que el prospecto se encuentra en la lista de consultas: "{nombre}" "{ap_paterno}" "{ap_materno}"')
def step_valida_prospecto(context, nombre, ap_paterno, ap_materno):
    context.validar_datos_emprendedora_consultas = ConsultaRapida(context.driver, lugar_nacimiento="0")
    context.validar_datos_emprendedora_consultas.validar_prospecta_en_consultas(nombre,ap_paterno,ap_materno)
    pass





""" Valida cancelacion de registro en pendientes """
@then(u'Validar emprendedora como rechazada')
def valida_rechazo(context):
    context.validar_cancelacion_emprendedora= ConsultaRapida(context.driver, lugar_nacimiento="0")
    context.validar_cancelacion_emprendedora.valida_rechazo()
    pass