import time
from behave import given, when, then
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import helpers.utils as utilerias
from helpers.functionsAuxiliarWeb import (
    capture_screenshot
)


@then(u'Editamos el num de telefono: "{num_celular}"')
def edit_num_celular(context,num_celular):
    time.sleep(2)

    lbl_num_celular = (By.CSS_SELECTOR, "input[name='telefonoCelular']")
    utilerias.insertar_y_limpiar_campo(context.driver,lbl_num_celular, num_celular)
    # context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(6)
    pass


@then(u'Tap Adjuntos')
def tap_adjuntos(context):
    time.sleep(2)

    tap_adjuntos= (By.XPATH, "//button[normalize-space()='ADJUNTOS']")
    utilerias.click_boton(context.driver,tap_adjuntos)
   
    time.sleep(6)
    pass

@then(u'Realizar la descarga de: SCI')
def descargar_sci(context):
    time.sleep(2)

    # btn_masopciones_doc = (By.XPATH, "//body/div[@id='root']/div[@data-testid='Layout-Test-Id']/main[@class='Layout_Main']/div[@class='IntegrantContainer']/div[@class='CardContent css-w2zj3k']/div[@data-testid='Attachments_Test_Id']/div[@class='DocSection']/div[2]/div[1]/div[2]/div[1]/button[1]")
    btn_masopciones_doc = (By.XPATH, "//img[@alt='opciones del documento']")
    utilerias.click_boton(context.driver,btn_masopciones_doc)
    time.sleep(3)

    # btn_descargar_sci= (By.XPATH, "//div[@data-testid='Attachments_Test_Id']//div[2]//div[1]//div[2]//div[2]//div[1]//button[1]")
    btn_descargar_sci= (By.XPATH, "//button[normalize-space()='Descargar']")
    utilerias.click_boton(context.driver,btn_descargar_sci)
    
    time.sleep(8)
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[0])
    pass


@then(u'Agrego el comentario: "{comentario}"')
def descargar_sci(context,comentario):
    time.sleep(2)

    label_agrego_comentario = (By.XPATH, "//div[@aria-label='rdw-editor']")
    utilerias.insertar_y_limpiar_campo(context.driver,label_agrego_comentario, comentario)

    btn_comentario = (By.XPATH, "//button[normalize-space()='Comentar']")
    utilerias.click_boton(context.driver,btn_comentario)

    time.sleep(6)
   
    pass


# # @given('Que estoy en google')
# # def step_impl(context):
# #     from selenium.webdriver.chrome.service import Service
# #     service = Service('/path/to/chromedriver')
# #     service.start()
# #     driver = webdriver.Remote(service.service_url)
# #     driver.get('http://www.google.com/');
# #     time.sleep(5) # Let the user actually see something!
# #     pass

# @when('Inicio sesion1')
# def inciiando_sesion(context):
#     time.sleep(2)
#     # element = context.driver.find_element(By.ID, "passwd-id")

#     element = context.driver.find_element(By.XPATH, "//button[normalize-space()='Continuar con Google']")
#     element.click()
#     time.sleep(1)
#     element1 = context.driver.find_element(By.XPATH, "//div[@class='modal-body']//div//div//div//div//div//span[contains(text(),'Continue with Google')]")
#     element1.click()
#     label_usuario = context.driver.find_element(By.ID, "identifierId")
#     label_usuario.send_keys("c.rojas@podemos.mx")
#     btn_siguiente = context.driver.find_elemeIngresar al menu Digitalizacion
#     pass


# @then('Realizar la busqueda del grupo prospection')
# def busqueda_tabla(context):

#     time.sleep(1)
#     lbl_buscar = context.driver.find_element(By.NAME, "search")
#     lbl_buscar.click()
#     lbl_buscar.send_keys("EMPRENDEDORAS")
#     lbl_buscar.send_keys(Keys.ENTER)
#     time.sleep(3)

#    ## Tabla de resultadps
#     tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
#     tr_tabla_resultados.click()
#     time.sleep(2)

#     # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//tbody//div[1]//button[1]")
#     btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='Common_Caret']")
#     btn_abrir_grupo.click()
#     time.sleep(7)

#     input_nombre_gruṕ = context.driver.find_element(By.ID, "groupName")
#     text_nombre_grupo = input_nombre_gruṕ.get_attribute('value')
#     # text_nombre_grupo = 'VER42'
    
#     # Validar nombre del grupo 
#     # assert text_nombre_grupo == 'ver42'
#     message = "First value and second value are not equal !"
#     # assertEqual(text_nombre_grupo, 'ver42', message) 
#     # assert_equal(text_nombre_grupo, 'ver42', message)
#     # assertEqual(text_nombre_grupo,'ver42')
#     # assert actual_value == expected_value, f"Expected value to be '{expected_value}' but got '{actual_value}'"

#     # assert text_nombre_grupo == 'VER41'
#     txt_comparar = 'EMPRENDEDORAS'
#     try:
#         assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
#     finally:
#         context.driver.quit()
#     pass








