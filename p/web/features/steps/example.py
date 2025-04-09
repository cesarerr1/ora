import time
from behave import given, when, then
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.functionsAuxiliarWeb import (
    capture_screenshot
)



@given('Que estoy en google')
def step_impl(context):
    # context.driver = webdriver.Chrome()

    # download_dir = "/home/cr/Documentos/InstalacionFramework/Lucy/web/docs"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Inicia maximizado
    chrome_options.add_argument("--disable-notifications")  # Desactiva notificaciones
    chrome_options.add_argument("--disable-popup-blocking")  # Desactiva bloqueador de pop-ups
    chrome_options.add_argument("--incognito")  # Modo incógnito
    chrome_options.add_argument("--headless")  # Modo sin interfaz gráfica (opcional)
    chrome_options.add_argument("--no-sandbox")  # Previene problemas en entornos restringidos
    chrome_options.add_argument("--disable-gpu")  # Desactiva GPU (necesario para Headless en algunos casos)
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-web-security")  # Desactiva extensiones
    # chrome_options.add_argument("--remote-debugging-port=9222")  # Puerto para depuración remota



    prefs = {
        # "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
        "useAutomationExtension": False,
        "headless":False,
        "profile.default_content_setting_values.notifications": 1,  # 1 para aceptar, 2 para bloquear
        "profile.default_content_setting_values.geolocation": 1,    # 1 para permitir, 2 para bloquear
        "profile.default_content_setting_values.media_stream": 1,    # 1 para permitir acceso a la cámara/micrófono
        "profile.default_content_settings.popups": 0,  # Desactiva pop-ups en descargas
    }
    chrome_options.add_experimental_option("prefs", prefs)


    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
    #  options.add_argument("--headless");

    # chrome_options = webdriver.ChromeOptions() 
    # chrome_options.add_experimental_option(
    #     "useAutomationExtension", False
    #     ) 
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    chrome_options.add_experimental_option("prefs", prefs)
    context.driver = webdriver.Chrome(options=chrome_options)

    context.driver.maximize_window()
    context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/")
    context.driver.implicitly_wait(15)
    # context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/")
    
    # btn_siguiente = (MobileBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_siguiente)
    # utilerias.click_boton(driver, btn_siguiente)
    
pass


# @given('Que estoy en google')
# def step_impl(context):
#     from selenium.webdriver.chrome.service import Service
#     service = Service('/path/to/chromedriver')
#     service.start()
#     driver = webdriver.Remote(service.service_url)
#     driver.get('http://www.google.com/');
#     time.sleep(5) # Let the user actually see something!
#     pass

@when('Inicio sesion')
def inciiando_sesion(context):
    time.sleep(2)
    # element = context.driver.find_element(By.ID, "passwd-id")

    element = context.driver.find_element(By.XPATH, "//button[normalize-space()='Continuar con Google']")
    element.click()
    time.sleep(1)
    element1 = context.driver.find_element(By.XPATH, "//div[@class='modal-body']//div//div//div//div//div//span[contains(text(),'Continue with Google')]")
    element1.click()
    label_usuario = context.driver.find_element(By.ID, "identifierId")
    label_usuario.send_keys("c.rojas@podemos.mx")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(3)

    label_pass = context.driver.find_element(By.NAME,"Passwd")
    label_pass.send_keys("55990Re123")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(6)
    pass


""" Iniciar sesion con perfil consejero"""
@when('Inicio sesion consejero')
def inciiando_sesion(context):
    time.sleep(2)
    # element = context.driver.find_element(By.ID, "passwd-id")

    element = context.driver.find_element(By.XPATH, "//button[normalize-space()='Continuar con Google']")
    element.click()
    time.sleep(1)
    element1 = context.driver.find_element(By.XPATH, "//div[@class='modal-body']//div//div//div//div//div//span[contains(text(),'Continue with Google')]")
    element1.click()
    label_usuario = context.driver.find_element(By.ID, "identifierId")
    label_usuario.send_keys("pruebas-luci-cs@podemos.mx")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(2)

    label_pass = context.driver.find_element(By.NAME,"Passwd")
    label_pass.send_keys("55990Re123")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(4)
    pass


@when('Inicio sesion analista')
def inciiando_sesion(context):
    time.sleep(2)
    # element = context.driver.find_element(By.ID, "passwd-id")

    element = context.driver.find_element(By.XPATH, "//button[normalize-space()='Continuar con Google']")
    element.click()
    time.sleep(1)
    element1 = context.driver.find_element(By.XPATH, "//div[@class='modal-body']//div//div//div//div//div//span[contains(text(),'Continue with Google')]")
    element1.click()
    label_usuario = context.driver.find_element(By.ID, "identifierId")
    label_usuario.send_keys("pruebas-luci-analista@podemos.mx")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(2)

    label_pass = context.driver.find_element(By.NAME,"Passwd")
    label_pass.send_keys("1qazxsw2Luci")
    btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    btn_siguiente.click()
    time.sleep(4)
    pass






@when('Realizar la busqueda del grupo')
def busqueda_tabla(context):

    
    ta_devueltos = context.driver.find_element(By.XPATH, "//button[normalize-space()='DEVUELTOS']")
    ta_devueltos.click()
    time.sleep(4)

    tap_revisado = context.driver.find_element(By.XPATH, "//button[normalize-space()='REVISADOS']")
    tap_revisado.click()

    time.sleep(4)

    tap_revisado = context.driver.find_element(By.XPATH, "//button[normalize-space()='PENDIENTES']")
    tap_revisado.click()


    
    time.sleep(4)
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys("4949")
    lbl_buscar.send_keys(Keys.ENTER)
    time.sleep(6)

   ## Tabla de resultadps
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(6)

    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//tbody//div[1]//button[1]")
    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='Common_Caret']")
    btn_abrir_grupo.click()
    time.sleep(7)

    input_nombre_gruṕ = context.driver.find_element(By.ID, "groupName")
    text_nombre_grupo = input_nombre_gruṕ.get_attribute('value')
    # text_nombre_grupo = 'VER42'
    
    # Validar nombre del grupo 
    # assert text_nombre_grupo == 'ver42'
    message = "First value and second value are not equal !"
    # assertEqual(text_nombre_grupo, 'ver42', message) 
    # assert_equal(text_nombre_grupo, 'ver42', message)
    # assertEqual(text_nombre_grupo,'ver42')
    # assert actual_value == expected_value, f"Expected value to be '{expected_value}' but got '{actual_value}'"

    # assert text_nombre_grupo == 'VER41'
    txt_comparar = 'TTTTTTTT'
    try:
        assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
    finally:
        context.driver.quit()
    pass

@when('Realizo la busqueda de un integrante')
def busqueda_integrante(context):
    time.sleep(1)
    # txt_seccion_integrantes_del_grupo = context.driver.find_element(By.XPATH, "//span[normalize-space()='Integrantes del grupo']")
    

    # txt_comparar = "Integrantes del grupo"
    # try:
    #     assert txt_seccion_integrantes_del_grupo == txt_comparar, f"Expected value to be '{txt_comparar}' but got '{txt_comparar}'"
    # finally:
    #     context.driver.quit()

    
    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//div[@class='InformationGroupSection_Inter']//span[@class='MemberCard_Name_Text1 css-16uqosh'][contains(text(),'CAZANDRA')]")
    
    
    
    
    # btn_editar_integrante = context.driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/main[1]/div[1]/div[3]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/img[1]")
    # btn_editar_integrante.click()
    time.sleep(10) 
    pass






@then('Taps en grupo')
def busqueda_tabla(context):

    time.sleep(4)
    context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/modulo/digitalizacion/grupo/detalle/vista-cruzada/bcd9342b-32d0-4ba5-8a9e-e97507cd111e")
    # ta_devueltos = context.driver.find_element(By.XPATH, "//button[normalize-space()='VISTA CRUZADA']")
    # ta_devueltos.click()
    # time.sleep(1)

    pass

@when('Cambiar taps2')
def navegar_taps (context):
    time.sleep(7)
    # Ad//button[normalize-space()='COMENTARIOS']o 
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//button[normalize-space()='ADJUNTOS']")
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//button[normalize-space()='COMENTARIOS']")
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//button[normalize-space()='COMENTARIOS']")
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//*[text() = \"Descargar expediente\"]")
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//button[normalize-space()='VISTA CRUZADA']")
    
    # tap_adjuntos = context.driver.find_element(By.XPATH, "//input[@id='groupName']")
    tap_adjuntos = context.driver.find_element(By.XPATH, "//button[normalize-space()='COMENTARIOS']")
    tap_adjuntos.clear()

    pass




@when('Descargar archivo')
def realizar_descarga_archivo (context):
    # download_dir = "/home/cr/Documentos/InstalacionFramework/Lucy/web/docs"
    
    # btn_descargar_expediente = context.driver.find_element(By.XPATH, "//button[normalize-space()='Descargar expediente']")
    # btn_descargar_expediente = context.driver.find_element(By.XPATH, "//button[normalize-space()='VISTA CRUZADA']")
    # btn_descargar_expediente.click()
    time.sleep(1)

    # # Confirmar descarga
    # btn_descargar_expediente = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    # btn_descargar_expediente.click()

    # time_to_wait = 30  # Tiempo máximo de espera en segundos
    # start_time = time.time()

    

    pass





@then('Ingreso "{busqueda}"')
def step_impl(context, busqueda):
    try:
        element = WebDriverWait(context.driver,10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        element.send_keys(busqueda)
        capture_screenshot(context,'Buscando WSL')
    except Exception as e:
        print("Error:", e)
    pass

@when('Hago click en buscar')
def step_impl(context):
    try:
        element = WebDriverWait(context.driver,10).until(
            EC.presence_of_element_located((By.NAME, "btnK"))
        )
        element.click()
    except Exception as e:
        print("Error:", e)
    pass

@then('Se muestran los resultados')
def step_impl(context):
    time.sleep(2)
    capture_screenshot(context,'Resultados')
    pass

@then('cierro el navegador')
def step_impl(context):
    context.driver.close()
    pass




@then(u'Btn asignar grupo')
def btn_asignar(context):
   
    btn_asignar = context.driver.find_element(By.XPATH, "//select[@name='tribe']")
    btn_asignar.click()
    time.sleep(2)

    btn_asignar = context.driver.find_element(By.XPATH, "//option[@value='c5864507-4675-44b8-b480-372e2603da5c']")
    btn_asignar.click()
    time.sleep(2)

    btn_asignar = context.driver.find_element(By.XPATH, "//select[@name='coordinadorDestinoId']")
    btn_asignar.click()
    time.sleep(2)

    btn_asignar = context.driver.find_element(By.XPATH, "//option[@value='6cf89bdf-f0d5-4aa9-8bf4-a932024bb87f']")
    btn_asignar.click()
    time.sleep(2)

    txt_motivo = context.driver.find_element(By.XPATH, "//textarea[@name='motivo']")
    txt_motivo.click()
    time.sleep(2)
    txt_motivo.send_keys("Prueba automatizada asignacion de grupo")
    time.sleep(2)    
    pass