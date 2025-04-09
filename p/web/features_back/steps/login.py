from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from pages.pagina_login import PaginaLogin
import time


@given('que estoy en la página "{url}"')
def step_impl(context, url):
    context.driver.get(url)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@when('ingreso el usuario "{usuario}" y la contraseña "{password}"')
def step_impl(context, usuario, password):
    FAW.enviar_datos(context.driver, PaginaLogin().usuario_input, usuario)
    FAW.enviar_datos(context.driver, PaginaLogin().password_input, password)

    RA.agregar_captura_reporte(context)


@when("hago clic en login")
def step_impl(context):
    FAW.clic(context.driver, PaginaLogin().login_btn)

@then('se muestra la página "{url}"')
def step_impl(context, url):
    time.sleep(3)
    assert url == context.driver.current_url

    time.sleep(3)

    RA.agregar_captura_reporte(context)

