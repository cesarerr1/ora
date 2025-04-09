from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from utils import assertions as AS
from utils import errors as ERR
from pages.pagina_dependientes import Dependientes
import time

@when('doy clic en agregar dependiente')
def step_impl(context):
    try:
        FAW.clic(context.driver, Dependientes.add_dependent_button)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)
        
@when('ingreso el nombre "{nombre}" del dependiente')
def step_impl(context, nombre):
    FAW.enviar_datos(context.driver, Dependientes.name_input, nombre)
    # try:
    #     FAW.enviar_datos(context.driver, Dependientes.name_input, nombre)
    # except AssertionError as assertion_error:
    #     raise assertion_error
    # except Exception as e:
    #     ERR.error_ocurrido(e)
        


@when('ingreso la relación "{relacion}" con el dependiente')
def step_impl(context, relacion):
    try:
        FAW.clic(context.driver, Dependientes.relationship_input)
        FAW.clic_elemento_por_texto(context.driver, Dependientes.relationship_list, relacion)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)


@when('especifico la relación "{relacion_especifica}" con el dependiente')
def step_impl(context, relacion_especifica):
    try:
        if relacion_especifica != '---':
            FAW.enviar_datos(context.driver, Dependientes.please_specify_input, relacion_especifica)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)


@when('ingreso la fecha de nacimiento "{fecha_nacimiento}" del dependiente')
def step_impl(context, fecha_nacimiento):
    try:
        FAW.enviar_datos(
            context.driver, Dependientes.date_birth_input, fecha_nacimiento)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)


@when('hago clic en guardar dependiente')
def step_impl(context):
    try:
        FAW.clic(context.driver, Dependientes.save_dependent_button)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)


@then('se muestra el mensaje de confirmación de agregar dependiente')
def step_impl(context):
    try:
        FAW.elemento_presente(context.driver, Dependientes.success_message)
        RA.agregar_captura_reporte(context)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)

