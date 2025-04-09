from behave import given, when, then
from utils import functions_auxiliar_web as FAW
from utils import reports_allure as RA
from utils import assertions as AS
from pages.afiliaciones import Afiliaciones
from utils import errors as ERR
import time

@then('selecciono agregar afiliamiento')
def step_impl(context):
    try:
        FAW.clic(context.driver,Afiliaciones().assigned_membership)
        time.sleep(3)
        RA.agregar_captura_reporte(context)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)

@then('guardo los cambios')
def step_impl(context):
    try:
        FAW.clic(context.driver,Afiliaciones().save_btn_membership)
        time.sleep(3)
        RA.agregar_captura_reporte(context)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)

@then('edito los campos correspondientes "{afiliacion}" "{suscripcion}" "{monto}" "{divisa}" "{inicioAfiliacion}" "{finalAfiliacion}"')
def step_impl(context,afiliacion,suscripcion,monto,divisa,inicioAfiliacion,finalAfiliacion):
    try:
        FAW.clic(context.driver,Afiliaciones().membership)
        FAW.clic_elemento_por_texto(context.driver,Afiliaciones().membership_list,afiliacion)
        FAW.clic(context.driver,Afiliaciones().suscription)
        FAW.clic_elemento_por_texto(context.driver,Afiliaciones().suscription_list,suscripcion)
        FAW.limpiar(context.driver,Afiliaciones().suscription_mount)
        FAW.enviar_datos(context.driver,Afiliaciones().suscription_mount,monto)
        #FAW.validar_elemento(context.driver,Afiliaciones().suscription_mount,Afiliaciones().error_message)
        FAW.clic(context.driver,Afiliaciones().currency)
        FAW.clic_elemento_por_texto(context.driver,Afiliaciones().currency_list,divisa)
        FAW.enviar_datos(context.driver,Afiliaciones().date_suscription_start,inicioAfiliacion)
        FAW.enviar_datos(context.driver,Afiliaciones().date_suscription_final,finalAfiliacion)
        FAW.validar_campo(context.driver,Afiliaciones().error_message)
        time.sleep(3)
        RA.agregar_captura_reporte(context)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)

@then('selecciono borrar afiliacion')
def step_impl(context):
    try:
        FAW.clic(context.driver,Afiliaciones().delete_membership)
        FAW.clic(context.driver,Afiliaciones().confirmation_delete_membership)
        RA.agregar_captura_reporte(context)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)

@then('selecciono agregar un nuevo archivo "{archivo}"')
def step_impl(context,archivo):
    try:
        FAW.clic(context.driver,Afiliaciones().add_attachments_membership)
        archivo_a_subir = FAW.obtener_archivo_carpeta(archivo)
        FAW.enviar_datos(context.driver,Afiliaciones().add_file_membership,archivo_a_subir)
        FAW.clic(context.driver,Afiliaciones().save_btn_file)
        time.sleep(5)
    except Exception as e:
        ERR.error_ocurrido(e)

@then('selecciono descargar un archivo adjunto')
def step_impl(context):
    try:
        FAW.clic(context.driver,Afiliaciones().download_file)
        AS.verificar_archivo_descargado("abc.txt")
        time.sleep(3)
    except AssertionError as assertion_error:
        raise assertion_error
    except Exception as e:
        ERR.error_ocurrido(e)
