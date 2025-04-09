from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from pages.menu_mi_informacion import MenuMiInformacion
import time


@given('hago clic en Personal Details')
@when('hago clic en Personal Details')
@then('hago clic en Personal Details')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.personal_details_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Contact Details')
@when('hago clic en Contact Details')
@then('hago clic en Contact Details')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.contact_details_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Emergency Contacts')
@when('hago clic en Emergency Contacts')
@then('hago clic en Emergency Contacts')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.emergency_contacts_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Dependents')
@when('hago clic en Dependents')
@then('hago clic en Dependents')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.dependents_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Immigration')
@when('hago clic en Immigration')
@then('hago clic en Immigration')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.immigration_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Job')
@when('hago clic en Job')
@then('hago clic en Job')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.job_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Salary')
@when('hago clic en Salary')
@then('hago clic en Salary')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.salary_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Report-to')
@when('hago clic en Report-to')
@then('hago clic en Report-to')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.report_to_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Qualifications')
@when('hago clic en Qualifications')
@then('hago clic en Qualifications')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.qualifications_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)


@given('hago clic en Memberships')
@when('hago clic en Memberships')
@then('hago clic en Memberships')
def step_impl(context):
    FAW.clic(context.driver, MenuMiInformacion.memberships_button)
    time.sleep(5)
    RA.agregar_captura_reporte(context)

