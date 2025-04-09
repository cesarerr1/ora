from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from utils import assertions as AS
from pages.pagina_datos_personales import DatosPersonales
import time


@when('ingreso el primer nombre "{primer_nombre}", el segundo nombre "{segundo_nombre}" y el apellido "{apellido}"')
def step_impl(context, primer_nombre, segundo_nombre, apellido):
    FAW.limpiar(context.driver, DatosPersonales.first_name_input)
    FAW.enviar_datos(
        context.driver, DatosPersonales.first_name_input, primer_nombre)
    FAW.limpiar(
        context.driver, DatosPersonales.middle_name_input)
    FAW.enviar_datos(
        context.driver, DatosPersonales.middle_name_input, segundo_nombre)

    FAW.limpiar(context.driver, DatosPersonales.last_name_input)
    FAW.enviar_datos(
        context.driver, DatosPersonales.last_name_input, apellido)
    FAW.validar_campo(context.driver,DatosPersonales.error_message)


@when('ingreso el id de empleado "{id_empleado}" y otro id "{otro_id}"')
def step_impl(context, id_empleado, otro_id):
    FAW.limpiar(context.driver, DatosPersonales.employee_id_input)
    FAW.enviar_datos(
        context.driver, DatosPersonales.employee_id_input, id_empleado)

    FAW.limpiar(context.driver, DatosPersonales.other_id_input)
    FAW.enviar_datos(context.driver, DatosPersonales.other_id_input, otro_id)


@when('ingreso el número de licencia de conducir "{no_licencia_conducir}" y la fecha de expiración de la licencia "{fecha_expiracion_licencia}"')
def step_impl(context, no_licencia_conducir, fecha_expiracion_licencia):
    FAW.limpiar(context.driver, DatosPersonales.driver_license_number_input)
    FAW.enviar_datos(context.driver, DatosPersonales.driver_license_number_input, no_licencia_conducir)

    FAW.limpiar(context.driver, DatosPersonales.license_expiry_date)
    FAW.enviar_datos(context.driver, DatosPersonales.license_expiry_date, fecha_expiracion_licencia)


@when('ingreso la nacionalidad "{nacionalidad}", el estado marital "{estado_marital}", la fecha de nacimiento "{fecha_nacimiento}" y el genero "{genero}"')
def step_impl(context, nacionalidad, estado_marital, fecha_nacimiento, genero):
    FAW.clic(context.driver, DatosPersonales.nationality)
    FAW.clic_elemento_por_texto(
        context.driver, DatosPersonales.nationality_list, nacionalidad)

    FAW.clic(context.driver, DatosPersonales.marital_status)
    FAW.clic_elemento_por_texto(
        context.driver, DatosPersonales.marital_status_list, estado_marital)
    FAW.limpiar(context.driver, DatosPersonales.birth_date)
    FAW.enviar_datos(context.driver, DatosPersonales.birth_date, fecha_nacimiento)
    if genero == "Male":
        FAW.clic(context.driver, DatosPersonales.gender_male_radio)
    elif genero == "Female":
        FAW.clic(context.driver, DatosPersonales.gender_female_radio)
    FAW.validar_campo(context.driver,DatosPersonales.error_message)
    


@when("hago clic en guardar datos personales")
def step_impl(context):
    FAW.clic(context.driver, DatosPersonales.save_personal_details_button)


@then("se muestra el mensaje de confirmación")
def step_impl(context):
    assert FAW.elemento_presente(context.driver, DatosPersonales.success_message)
    RA.agregar_captura_reporte(context)
    

