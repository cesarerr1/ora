#!/bin/bash

# Obtener el valor de $project_name pasado como argumento
project_name="$1"

cd "$project_name" || exit
cd "web"

# Mensaje de pipenv entorno virtual
echo "Creando el entorno virtual de web, espere por favor..."


# Entorno virtual
echo "Entorno virtual creado satisfactoriamente"
echo 

# Instalación de dependencias 
echo "Instalando dependencias, espere por favor..."

# Ejecutar los comandos y redirigir la salida para que no sea visible
{
    pip install behave 
    pip install selenium 
    pip install allure-behave
} > /dev/null 2>&1

# Dependencias instaladas
echo "Las dependencias fueron instaladas correctamente"
echo

####################################################################
#                Creación de estrutura de carpetas                 #
####################################################################

mkdir -p data

cat > data/dependinetes.csv<<END
nombre,relacion,relacion_especifica,fecha_nacimiento
Maria,Other,Wife,2000-01-01
Juan,Child,---,2020-01-01
END

mkdir -p features

cat > features/afiliaciones.feature<<END
# language: es

@Afiliaciones
Característica: Afiliaciones

@agregarAfiliamiento
    Esquema del escenario: Agregar nueva afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar afiliamiento
        Y edito los campos correspondientes "<afiliacion>" "<suscripcion>" "<monto>" "<divisa>" "<inicioAfiliacion>" "<finalAfiliacion>"
        Y guardo los cambios

        Ejemplos:
            | afiliacion | suscripcion | monto | divisa       |   inicioAfiliacion    |   finalAfiliacion |
            | CIMA       | Individual  | 1000  | Mexican Peso |   2024-05-15          |   2024-10-25      |

@editarAfiliamiento
    Esquema del escenario: Editar afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar afiliamiento
        Y edito los campos correspondientes "<afiliacion>" "<suscripcion>" "<monto>" "<divisa>" "<inicioAfiliacion>" "<finalAfiliacion>"
        Y guardo los cambios

        Ejemplos:
            | afiliacion | suscripcion | monto | divisa       |   inicioAfiliacion    |   finalAfiliacion |
            | ACCA       | Company     | 5000  | Mexican Peso |   2024-01-01          |   2024-12-24      |

@eliminarAfiliacion
    Escenario: Eliminar afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono borrar afiliacion

@subirArchivoAfiliacion
    Esquema del escenario: Subir archivo de afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar un nuevo archivo "<archivo>"

        Ejemplos:
            |     archivo     |
            |  Bluetooth.png  |
        
@descargarArchivoAdjunto
    Escenario: Descargar archivo de afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono descargar un archivo adjunto
END

cat > features/datos_contacto.feature<<END
# language: es
@datos_contacto
Característica: Datos de contacto

  Antecedentes:
    Dado hago clic en My Info
    Y hago clic en Contact Details

  @editar_datos_contacto
  Escenario: Editar datos de contacto
    Cuando ingreso la calle "Calle1" y la ciudad "Ciudad1"
    Y ingreso el estado "Estado 1", codigo postal "11111" y pais "Mexico"
    Y ingreso el telefono de casa "11111111111", el movil "2222222222" y el de trabajo "3333333333"
    Y ingreso el correo "admin@example.com"
    Y hago clic en guardar
    Entonces se muestra el mensaje de confirmación de datos de contacto

END

cat > features/datos_personales.feature<<END
# language: es
@datos_personales
Característica: Datos personales

  Antecedentes:
    Dado hago clic en My Info
    Entonces se muestra la página "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"

  @editar_datos_personales
  Escenario: Editar detalles personales exitosamnete
    Cuando ingreso el primer nombre "Maria", el segundo nombre "Jose" y el apellido "Landa"
    Y ingreso el id de empleado "11111" y otro id "22222"
    Y ingreso el número de licencia de conducir "12345" y la fecha de expiración de la licencia "2025-01-01"
    Y ingreso la nacionalidad "Mexican", el estado marital "Other", la fecha de nacimiento "2000-01-01" y el genero "Female"
    Y hago clic en guardar datos personales
    Entonces se muestra el mensaje de confirmación

END

cat > features/dependientes.feature<<END
# language: es
@dependientes
Característica: Dependientes

  Antecedentes:
    Dado hago clic en My Info
    Y hago clic en Dependents

  @agregar_dependientes
  Esquema del escenario: Agregar dependientes
    Cuando doy clic en agregar dependiente
    Y ingreso el nombre "<nombre>" del dependiente
    Y ingreso la relación "<relacion>" con el dependiente
    Y especifico la relación "<relacion_especifica>" con el dependiente
    Y ingreso la fecha de nacimiento "<fecha_nacimiento>" del dependiente
    Y hago clic en guardar dependiente
    Entonces se muestra el mensaje de confirmación de agregar dependiente

    Ejemplos:
      | nombre | relacion | relacion_especifica | fecha_nacimiento |
      | Maria | Other | Wife | 2000-01-01 |
      | Juan | Child | --- | 2020-01-01 |



END

cat > features/environment.py<<END
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from utils import functions_auxiliar_web as FAW
from pages.pagina_login import PaginaLogin
import time 

def before_all(context):
    download_ruta = os.path.abspath("./files/download")
    ##################################
    chrome_options = Options()
    chrome_prefs = {
        "download.default_directory": download_ruta,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True, 
        "safebrowsing.enabled": True
    }
    chrome_options.add_experimental_option("prefs", chrome_prefs)
    context.driver = webdriver.Chrome(options=chrome_options)
    ##################################

    context.driver.maximize_window()
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    usuario = "Admin"
    password = "admin123"

    context.driver.get(url)
    time.sleep(5)
    FAW.enviar_datos(context.driver, PaginaLogin.usuario_input, usuario)
    FAW.enviar_datos(context.driver, PaginaLogin.password_input, password)
    FAW.clic(context.driver, PaginaLogin.login_btn)

def before_feature(context, feature):
    pass
    
def before_step(context, step):
    context.current_step_name = step.name

    
def after_feature(context, feature):
    pass

def after_all(context):
    context.driver.quit()
END

cat > features/login.feature.txt<<END
# language: es
@login
Característica: Iniciar sesión

  Antecedentes:
    Dado que estoy en la página "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

  @loginValido
  Escenario: Login válido
    Cuando ingreso el usuario "Admin" y la contraseña "admin123"
    Y hago clic en login
    Entonces se muestra la página "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    Y hago clic en Admin
    Y hago clic en Leave
    Y hago clic en Recruitment
    Y hago clic en My Info
    Y hago clic en Job

END

mkdir -p features/steps

cat > features/steps/afiliaciones.py<<END
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
END

cat > features/steps/datos_contactos.py<<END
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
END

cat > features/steps/datos_personales.py<<END
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
    

END

cat > features/steps/dependientes.py<<END
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

END

cat > features/steps/login.py<<END
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

END

cat > features/steps/menu_mi_informacion.py<<END
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

END

cat > features/steps/menu_principal.py<<END
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

END

mkdir -p files

mkdir -p files/download

cat > files/download/abc.txt<<END
testing

END

mkdir -p files/upload

mkdir -p pages

cat > pages/afiliaciones.py<<END
from selenium.webdriver.common.by import By  # type: ignore


class Afiliaciones:
    def __init__(self):

        xpath_membership = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/'
        
        self.assigned_membership = (
            By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button')
        
        
        self.membership = (
            By.XPATH,xpath_membership +'div[1]/div/div[1]/div/div[2]/div/div[1]/div[1]')
        
        self.membership_list = (
            By.XPATH, xpath_membership +'div[1]/div/div[1]/div/div[2]/div/div[2]/div[*]/span') 
        
        self.suscription = (
            By.XPATH, xpath_membership + 'div[1]/div/div[2]/div/div[2]/div/div/div[1]')
        
        self.suscription_list = (
            By.XPATH, xpath_membership + 'div[1]/div/div[2]/div/div[2]/div/div[2]/div[*]/span')
        
        self.suscription_mount = (
            By.XPATH, xpath_membership + 'div[1]/div/div[3]/div/div[2]/input'
        )

        self.currency = (
            By.XPATH, xpath_membership + 'div[1]/div/div[4]/div/div[2]/div/div[1]/div[1]'
        )

        self.currency_list = (
            By.XPATH, xpath_membership + 'div[1]/div/div[4]/div/div[2]/div/div[2]/div[*]/span'
        )

        self.date_suscription_start = (
            By.XPATH, xpath_membership + 'div[1]/div/div[5]/div/div[2]/div/div/input'
        )

        self.date_suscription_final = (
            By.XPATH, xpath_membership + 'div[1]/div/div[6]/div/div[2]/div/div/input'
        )

        self.save_btn_membership = (
            By.XPATH, xpath_membership + 'div[2]/button[2]'
        )

        self.add_file_membership = (
            
            By.CSS_SELECTOR,".oxd-file-input"
        )

        self.add_attachments_membership = (
            By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[5]/div[1]/div/button'
        )

        self.save_btn_file = (
            By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-attachment > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space"
        )

        self.delete_membership = (
            By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space' and i[@class='oxd-icon bi-trash']]"
        )

        self.confirmation_delete_membership = (
            By.XPATH, '/html/body/div/div[3]/div/div/div/div[3]/button[2]'
        )

        self.download_file = (
            By.XPATH, "//button[@class='oxd-icon-button oxd-table-cell-action-space' and i[@class='oxd-icon bi-download']]"
        )

        self.error_message = (
            By.XPATH, ".//span[contains(@class, 'oxd-input-field-error-message')]"
        )

        



        

        
        
        

END

cat > pages/menu_mi_informacion.py<<END
from selenium.webdriver.common.by import By


class MenuMiInformacion:
    xpath_menu = "//a[contains(@class, 'orangehrm-tabs-item') and contains(text(), '{}')]"

    personal_details_button = (By.XPATH, xpath_menu.format("Personal Details"))
    contact_details_button = (By.XPATH, xpath_menu.format("Contact Details"))
    emergency_contacts_button = (By.XPATH, xpath_menu.format("Emergency Contacts"))
    dependents_button = (By.XPATH, xpath_menu.format("Dependents"))
    immigration_button = (By.XPATH, xpath_menu.format("Inmigration"))
    job_button = (By.XPATH, xpath_menu.format("Job"))
    salary_button = (By.XPATH, xpath_menu.format("Salary"))
    report_to_button = (By.XPATH, xpath_menu.format("Report-to"))
    qualifications_button = (By.XPATH, xpath_menu.format("Qualifications"))
    memberships_button = (By.XPATH, xpath_menu.format("Memberships"))

END

cat > pages/menu_principal.py<<END
from selenium.webdriver.common.by import By

class MenuPrincipal:
    xpath_menu = "//span[text()='{}' and contains(@class, 'oxd-main-menu-item--name')]"

    search_input = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div')
    admin_button = (By.XPATH, xpath_menu.format("Admin"))
    pim_button = (By.XPATH, xpath_menu.format("PIM"))
    leave_button = (By.XPATH, xpath_menu.format("Leave"))
    time_button = (By.XPATH, xpath_menu.format("Time"))
    recruitment_button = (By.XPATH, xpath_menu.format("Recruitment"))
    my_info_button = (By.XPATH, xpath_menu.format("My Info"))
    performance_button = (By.XPATH, xpath_menu.format("Performance"))
    dashboard_button = (By.XPATH, xpath_menu.format("Dashboard"))
    directory_button = (By.XPATH, xpath_menu.format("Directory"))
    maintenance_button = (By.XPATH, xpath_menu.format("Maintenance"))
    claim_button = (By.XPATH, xpath_menu.format("Claim"))
    buzz_button = (By.XPATH, xpath_menu.format("Buzz"))
END

cat > pages/pagina_datos_contacto.py<<END
from selenium.webdriver.common.by import By

class DatosContacto:

    xpath_address = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[{}]/div/div[2]/input'
    street_1_input = (By.XPATH, xpath_address.format(1))
    city_input = (By.XPATH, xpath_address.format(2))
    state_input = (By.XPATH, xpath_address.format(3))
    pc_input = (By.XPATH, xpath_address.format(4))

    xpath_country = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div'
    country_input = (By.XPATH, xpath_country)
    country_list = (By.XPATH, xpath_country + '[2]/div[*]/span')

    xpath_telephone = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[{}]/div/div[2]/input'
    tel_home_input = (By.XPATH, xpath_telephone.format(1))
    tel_mobil_input = (By.XPATH, xpath_telephone.format(2))
    tel_work_input = (By.XPATH, xpath_telephone.format(3))

    xpath_email = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    work_email_input = (By.XPATH, xpath_email)

    save_button = (
        By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button')

    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')

END

cat > pages/pagina_datos_personales.py<<END
from selenium.webdriver.common.by import By


class DatosPersonales:

    first_name_input = (By.NAME, 'firstName')
    middle_name_input = (By.NAME, 'middleName')
    last_name_input = (By.NAME, 'lastName')

    xpath_personal_details = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/'

    employee_id_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[1]/div[1]/div/div[2]/input')

    other_id_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[1]/div[2]/div/div[2]/input')
    driver_license_number_input = (
        By.XPATH, xpath_personal_details + 'div[2]/div[2]/div[1]/div/div[2]/input')
    license_expiry_date = (
        By.XPATH, xpath_personal_details + 'div[2]/div[2]/div[2]/div/div[2]/div/div/input')

    nationality = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[1]/div/div[2]/div/div[1]')
    nationality_list = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[1]/div/div[2]/div/div[2]/div[*]/span')

    marital_status = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[2]/div/div[2]/div/div[1]')
    marital_status_list = (
        By.XPATH, xpath_personal_details + 'div[3]/div[1]/div[2]/div/div[2]/div/div[2]/div[*]/span')

    birth_date = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[1]/div/div[2]/div/div/input')
    gender_male_radio = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div')
    gender_female_radio = (
        By.XPATH, xpath_personal_details + 'div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div')

    save_personal_details_button = (
        By.XPATH, xpath_personal_details + 'div[4]/button')

    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')

    error_message = (By.XPATH,".//span[contains(@class, 'oxd-input-field-error-message')]")

END

cat > pages/pagina_dependientes.py<<END
from selenium.webdriver.common.by import By


class Dependientes:
    xpath_dependents = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]'

    add_dependent_button = (By.XPATH, xpath_dependents + '/div/button')
    save_dependent_button =(By.XPATH, xpath_dependents + '/form/div[3]/button[2]')

    name_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[1]/div/div[2]/input')
    relationship_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]')
    relationship_list =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[*]/span')
    please_specify_input =(By.XPATH, xpath_dependents + '/form/div[1]/div/div[3]/div/div[2]/input')
    date_birth_input =(By.XPATH, xpath_dependents + '/form/div[2]/div/div/div/div[2]/div/div/input')
    
    success_message = (By.XPATH, '//*[@id="oxd-toaster_1"]/div')
END

cat > pages/pagina_login.py<<END
from selenium.webdriver.common.by import By

class PaginaLogin:
    usuario_input = (By.NAME, 'username')
    password_input = (By.NAME, 'password')
    login_btn = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')


END

mkdir -p pages/__pycache__

mkdir -p scripts

cat > scripts/update_feature.py<<END
import csv
import os

def update_feature_file(feature_file, scenario_name, csv_file):
    # Leer el CSV y guardar los datos en una lista de diccionarios
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    # Leer el archivo .feature
    with open(feature_file, 'r') as file:
        lines = file.readlines()

    # Encontrar el escenario y la tabla de ejemplos correspondiente
    new_lines = []
    inside_scenario = False
    inside_examples = False
    scenario_found = False
    
    for line in lines:
        if scenario_name in line:
            inside_scenario = True
            scenario_found = True
            new_lines.append(line)
        elif inside_scenario and line.strip().startswith('Ejemplos:'):
            inside_examples = True
            new_lines.append(line)
            # Añadir la nueva tabla de ejemplos
            header = " | ".join(data[0].keys())
            new_lines.append(f"      | {header} |\n")
            for row in data:
                values = " | ".join(row.values())
                new_lines.append(f"      | {values} |\n")
        elif inside_examples and line.strip().startswith('|'):
            # Ignorar las líneas de la tabla de ejemplos existente
            continue
        else:
            if inside_examples:
                inside_examples = False
                inside_scenario = False
            new_lines.append(line)

    if not scenario_found:
        raise ValueError(
            f"Scenario '{scenario_name}' not found in '{feature_file}'")

    # Escribir los cambios en el archivo .feature
    with open(feature_file, 'w') as file:
        file.writelines(new_lines)


files = [
    {
        'path_feature': 'features/dependientes.feature',
        'scenario_outline': 'Esquema del escenario: Agregar dependientes',
        'data': 'data/dependinetes.csv'
    }
]

for file in files:
    update_feature_file(file['path_feature'], file['scenario_outline'], file['data'])
END

mkdir -p utils

cat > utils/assertions.py<<END
import time
import os

def asercion_titulo_pagina(context, titulo):
    titulo_actual = context.title
    assert titulo == titulo_actual, f"El titulo esperado era '{titulo}', pero el titulo de la pagina es '{titulo_actual}'"

def asercion_dato_no_vacio(dato):
    assert dato != "", f"El dato introducido esta vacío"

def verificar_url(context,url):
    url_actual = context.current_url
    assert url_actual == url, f"La URL esperada era '{url}', pero la URL actual es '{url_actual}'"

def verificar_archivo_descargado(nombre_archivo):
    time.sleep(5)
    ruta_descarga = r"./files/download"
    ruta_completa = os.path.join(ruta_descarga, nombre_archivo)
    if os.path.isfile(ruta_completa):
        print("archivo descargado")
    else:
        raise AssertionError (f"No se pudo descargar el archivo '{nombre_archivo}'")
    
def verificar_exitencia_archivo(archivo):
    if os.path.exists(archivo):
        return True
    else:
        raise AssertionError (f"El archivo '{archivo}' no existe")


END

cat > utils/errors.py<<END
def error_ocurrido(error):
    raise Exception (f"Ha ocurrido un error: '{error}'")

def validacion(campo,message):
    raise Exception(f"El Campo: '{campo}' '{message}'")

def validacion(message):
    raise Exception(f"Mensaje: '{message}'")

def elemento_no_encontrado(web_elemento):
    print(f"No se encontró mensaje de error para el campo {web_elemento}")

END

cat > utils/functions_auxiliar_web.py<<END
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from utils import errors as ERR
import os

def clic(driver, web_elemento, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.element_to_be_clickable(web_elemento)
    )
    element.click()


def enviar_datos(driver, web_elemento, texto, tiempo_espera=10,):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    element.send_keys(texto)

def limpiar(driver, web_elemento, tiempo_espera=10):
    element = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_element_located(web_elemento)
    )
    content = element.get_attribute('value')
    content_length = len(content)
    element.send_keys(Keys.BACKSPACE * content_length)


def clic_elemento_por_texto(driver, web_elemento, texto, tiempo_espera=10):
    elements = WebDriverWait(driver, tiempo_espera).until(
        EC.presence_of_all_elements_located(web_elemento)
    )
    for element in elements:
        if element.text == texto:
            element.click()
            return

def elemento_presente(driver, web_elemento, tiempo_espera=10):
    try:
        WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        return True
    except TimeoutException:
        return False

def obtener_archivo_carpeta(archivo):
    carpeta = os.path.abspath("./files/upload")
    ruta_completa = os.path.join(carpeta,archivo)
    if os.path.isfile(ruta_completa):
        return ruta_completa
    else:
        raise Exception("El archivo no existe")
    
def validar_campo(driver,web_elemento,tiempo_espera=3):
    try:
        elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        if elemento.is_displayed():
            message = elemento.text
            ERR.validacion(message)
    except TimeoutException:
        ERR.elemento_no_encontrado(web_elemento)
    except Exception as e:
        raise e
    
def validar_elemento(driver,web_elemento,mensaje_error_web,tiempo_espera=3):
    try:
        elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(web_elemento)
        )
        try:
            elemento = WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located(mensaje_error_web)
            )
            if elemento.is_displayed():
                message = elemento.text
                ERR.validacion(web_elemento,message)
        except TimeoutException:
            ERR.elemento_no_encontrado(web_elemento)
    except TimeoutException:
        ERR.elemento_no_encontrado(web_elemento)
    except Exception as e:
        raise e
END

cat > utils/reports_allure.py<<END
import allure

def agregar_captura_reporte(context, titulo=''):
    if titulo == '':
        titulo = f'{context.scenario.name} [{context.current_step_name}]'
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name=titulo,
        attachment_type=allure.attachment_type.PNG,
    )

def agregar_texto_reporte(texto, nombre):
    allure.attach(texto, name=nombre, attachment_type=allure.attachment_type.TEXT)
END

cat > utils/__init__.py<<END

END

mkdir -p utils/__pycache__


# Guarda la representación base64 de la imagen en una variable
base64_image="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"

# Decodifica la imagen base64 y la guarda en un archivo
echo "$base64_image" | base64 -d > files/upload/Bluetooth.png

####################################################################
####################################################################

# Mensaje de confirmación
echo 
echo "¡La estructura de carpetas para usar web en '$project_name' ha sido creada con éxito!"
echo 


cd ..
