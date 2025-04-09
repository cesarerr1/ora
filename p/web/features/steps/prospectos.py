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



# @given('Que estoy en Podemos')
# def step_impl(context):
#     # context.driver = webdriver.Chrome()

#     download_dir = "/home/cr/Documentos/InstalacionFramework/Lucy/web/docs"

#     chrome_options = webdriver.ChromeOptions()
#     prefs = {
#         "download.default_directory": download_dir,
#         "download.prompt_for_download": False,
#         "directory_upgrade": True,
#         "safebrowsing.enabled": True,
#         "useAutomationExtension": False,
#         "headless":False
#     }
#     chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    
#     #  options.add_argument("--headless");

#     # chrome_options = webdriver.ChromeOptions() 
#     # chrome_options.add_experimental_option(
#     #     "useAutomationExtension", False
#     #     ) 
#     # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

#     chrome_options.add_experimental_option("prefs", prefs)
#     context.driver = webdriver.Chrome(options=chrome_options)

#     context.driver.maximize_window()
#     context.driver.get("https://www.google.com")
#     context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/")
#     # context.driver.get("https://staging.do4r3v17lb0gn.amplifyapp.com/")
    
#     # btn_siguiente = (MobileBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_siguiente)
#     # utilerias.click_boton(driver, btn_siguiente)
    
# pass

# @then('Ingresar al menu Prospection')
# def ingresar_digitalizacion(context):
#     time.sleep(4)


#     # btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[2]//div[1]//button[1]//img[1]")
#     # btn_despliega_menu = context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@data-testid='Layout-Test-Id']/div[@class='AsideBar_Container']/div[@class='AsideBar_Card css-1kz2nje']/div[1]/div[1]/button[1]")
#     btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[2]//div[1]//button[1]//img[1]")
#     btn_despliega_menu.click()
#     time.sleep(1)

#     # btn_digitalizacionelement = context.driver.find_element(By.XPATH, "//span[normalize-space()='Digitalización']")
#     # btn_digitalizacionelement = context.driver.find_element(By.XPATH, "//body//div[3]//div[1]//button[1]//img[1]")
#     btn_grupos = context.driver.find_element(By.XPATH, "//span[normalize-space()='Grupos de prospectos']")
#     btn_grupos.click()
#     time.sleep(1)

#     time.sleep(1)
#     btn_body = context.driver.find_element(By.ID, "root")
#     btn_body.click()
#     time.sleep(1)

#     pass



# @then(u'Realizar la busqueda del grupo prospectos')
# def busqueda_tabla(context):

    
#     time.sleep(2)
#     lbl_buscar = context.driver.find_element(By.NAME, "search")
#     lbl_buscar.click()
#     lbl_buscar.send_keys("24G00225")
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
#     txt_comparar = '24G00225'
#     # try:
#     #     assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
#     # finally:
#     #     context.driver.quit()
#     # pass



# @then(u'Tap comentarios')
# def cambiar_tap(context):
#     time.sleep(2)

#     btn_abrir_grupo = context.driver.find_element(By.XPATH, "//button[normalize-space()='COMENTARIOS']")
#     btn_abrir_grupo.click()
#     time.sleep(7)

#     pass

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
#     btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
#     btn_siguiente.click()
#     time.sleep(3)

#     label_pass = context.driver.find_element(By.NAME,"Passwd")
#     label_pass.send_keys("55990Re123")
#     btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
#     btn_siguiente.click()
#     time.sleep(6)
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
#     # assertEqual(text_nombre_grupo,'ver42')Ingresar al menu Digitalizacion
#     # assert actual_value == expected_value, f"Expected value to be '{expected_value}' but got '{actual_value}'"

#     # assert text_nombre_grupo == 'VER41'
#     txt_comparar = 'EMPRENDEDORAS'
#     try:
#         assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
#     finally:
#         context.driver.quit()
#     pass








