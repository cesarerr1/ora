from pages.pagina_datos_contacto import DatosContacto
from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
import time


@when('ingreso la calle "{calle}" y la ciudad "{ciudad}"')
def step_impl(context, calle, ciudad):
    FAW.limpiar(context.driver, DatosContacto.street_1_input)
    FAW.enviar_datos(context.driver, DatosContacto.street_1_input, calle)
    
    FAW.limpiar(context.driver, DatosContacto.city_input)
    FAW.enviar_datos(context.driver, DatosContacto.city_input, ciudad)

@when('ingreso el estado "{estado}", codigo postal "{codigo_postal}" y pais "{pais}"')
def step_impl(context, estado, codigo_postal, pais):
    FAW.limpiar(context.driver, DatosContacto.state_input)
    FAW.enviar_datos(context.driver, DatosContacto.state_input, estado )
    
    FAW.limpiar(context.driver, DatosContacto.pc_input)
    FAW.enviar_datos(context.driver, DatosContacto.pc_input, codigo_postal )
    
    FAW.clic(context.driver, DatosContacto.country_input)
    FAW.clic_elemento_por_texto(context.driver, DatosContacto.country_list, pais)

@when('ingreso el telefono de casa "{telefono_casa}", el movil "{telefono_movil}" y el de trabajo "{telefono_trabajo}"')
def step_impl(context, telefono_casa, telefono_movil, telefono_trabajo):
    FAW.limpiar(context.driver, DatosContacto.tel_home_input )
    FAW.enviar_datos(context.driver, DatosContacto.tel_home_input, telefono_casa )
    
    FAW.limpiar(context.driver, DatosContacto.tel_mobil_input )
    FAW.enviar_datos(context.driver, DatosContacto.tel_mobil_input, telefono_movil )
    
    FAW.limpiar(context.driver, DatosContacto.tel_work_input )
    FAW.enviar_datos(context.driver, DatosContacto.tel_work_input, telefono_trabajo )

@when('ingreso el correo "{correo}"')
def step_impl(context, correo):
    FAW.limpiar(context.driver, DatosContacto.work_email_input)
    FAW.enviar_datos(context.driver, DatosContacto.work_email_input, correo)

@when('hago clic en guardar')
def step_impl(context):
    FAW.clic(context.driver, DatosContacto.save_button)

@then('se muestra el mensaje de confirmación de datos de contacto')
def step_impl(context):
    assert FAW.elemento_presente(context.driver, DatosContacto.success_message)
    RA.agregar_captura_reporte(context)
