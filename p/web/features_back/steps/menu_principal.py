from behave import given, when, then
from utils import reports_allure as RA
from utils import functions_auxiliar_web as FAW
from pages.menu_principal import MenuPrincipal
import time


@given('hago clic en Search')
@when('hago clic en Search')
@then('hago clic en Search')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.search_input)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Admin')
@when('hago clic en Admin')
@then('hago clic en Admin')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.admin_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en PIM')
@when('hago clic en PIM')
@then('hago clic en PIM')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.pim_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Leave')
@when('hago clic en Leave')
@then('hago clic en Leave')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.leave_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Time')
@when('hago clic en Time')
@then('hago clic en Time')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.time_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Recruitment')
@when('hago clic en Recruitment')
@then('hago clic en Recruitment')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.recruitment_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en My Info')
@when('hago clic en My Info')
@then('hago clic en My Info')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.my_info_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Performance')
@when('hago clic en Performance')
@then('hago clic en Performance')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.performance_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Dashboard')
@when('hago clic en Dashboard')
@then('hago clic en Dashboard')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.dashboard_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Directory')
@when('hago clic en Directory')
@then('hago clic en Directory')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.directory_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@when('hago clic en Maintenance')
@then('hago clic en Maintenance')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.maintenance_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@when('hago clic en Claim')
@then('hago clic en Claim')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.claim_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@when('hago clic en Buzz')
@then('hago clic en Buzz')
def step_impl(context):
    FAW.clic(context.driver, MenuPrincipal.buzz_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)

