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

@then('Ingresar al menu: "{opcion_menu}"')
def ingresar_digitalizacion(context,opcion_menu):
    time.sleep(9)

    btn_abrir_menu = context.driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
    btn_abrir_menu.click()
    time.sleep(1)

    opcion_menu = str(opcion_menu)
    
    if opcion_menu == 'Prospeccion':
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[2]//div[1]//button[1]//img[1]")
    elif opcion_menu == 'Asignacion':
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Asignación']")
    elif opcion_menu == 'Digitalizacion':
        # btn_despliega_menu = context.driver.find_element(By.XPATH, "(//button[@type='button'])[10]")
        btn_despliega_menu = context.driver.find_element(By.XPATH, "(//*[name()='svg'][@alt='Digitalización'])[1]")
        # btn_sub_grupos.click()
        time.sleep(2)
    elif opcion_menu == 'Operativa':
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Operativa']")
    elif opcion_menu == 'Autorizacion':
        # btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[5]//div[1]//button[1]//img[1]")
        # btn_despliega_menu = context.driver.find_element(By.XPATH, "(//button[@type='button'])[11]")
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Autorización']")
    elif opcion_menu == 'Renovacion':
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Grupos a renovar']")
    else:
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[1]//div[1]//button[1]//img[1]")
    

    btn_despliega_menu.click()
    time.sleep(1)
  
    # btn_body = context.driver.find_element(By.ID, "root")
    # btn_body.click()

    pass



@then('Ingresar al sub-menu: "{opcion_sub_menu}"')
def ingresar_sub_menu(context,opcion_sub_menu):
    time.sleep(1)

    opcion_sub_menu = str(opcion_sub_menu)
    
    if opcion_sub_menu == 'Grupos':      
        btn_sub_grupos = context.driver.find_element(By.XPATH, '//*[text() = \"Grupos\"]')
    elif opcion_sub_menu == 'Renovacion':
        btn_sub_grupos = context.driver.find_element(By.XPATH, "//span[normalize-space()='Grupos a renovar']")
    else:
        btn_sub_grupos = context.driver.find_element(By.XPATH, "//body//div[1]//div[1]//button[1]//img[1]")
    

    btn_sub_grupos.click()
    time.sleep(2)

    # btn_body = context.driver.find_element(By.ID, "root")
    # btn_body.click()

    pass




@then('Ingresar al menu Digitalizacion')
def ingresar_digitalizacion(context):
    time.sleep(10)

    # btn_despliega_menu = context.driver.find_element(By.XPATH, "//div[@class='AsideBar_Card css-1kz2nje']//div[1]//div[1]//button[1]//img[1]")
    # btn_despliega_menu.click()
    # time.sleep(1)
    
    # btn_digitalizacion = context.driver.find_element(By.XPATH, "//div[4]//div[1]//button[1]//img[1]")
    # btn_digitalizacion = context.driver.find_element(By.XPATH, "//span[normalize-space()='Digitalización']")
    # btn_digitalizacion = context.driver.find_element(By.XPATH, "(//*[name()='svg'][@alt='Digitalización'])[1]")
    # btn_digitalizacion = context.driver.find_element(By.XPATH, "//div[5]//div[1]//button[1]")
    btn_digitalizacion = context.driver.find_element(By.XPATH, "(//button[@type='button'])[9]")
    btn_digitalizacion.click()
    time.sleep(5)
    # 4 | click | css=.AsideBar_SubOptions_Item:nth-child(3) > .AsideBar_Text | 

    btn_sub_grupos = context.driver.find_element(By.XPATH, '//*[text() = \"Grupos\"]')
    # btn_sub_grupos = context.driver.find_element(By.XPATH, '(//span[normalize-space()='Grupos'])[1]')
    btn_sub_grupos.click()
    

    time.sleep(5)
    pass



@then('Ingresar al menu Autorizacion')
def ingresar_digitalizacion(context):
    time.sleep(10)

    # btn_despliega_menu = context.driver.find_element(By.XPATH, "//div[@class='AsideBar_Card css-1kz2nje']//div[1]//div[1]//button[1]//img[1]")
    # btn_despliega_menu.click()
    # time.sleep(1) 
    
    
    

    # btn_digitalizacion = context.driver.find_element(By.XPATH, "//div[5]//div[1]//button[1]//img[1]")
    btn_digitalizacion = context.driver.find_element(By.XPATH, "//span[normalize-space()='Autorización']")
    btn_digitalizacion.click()
    # 4 | click | css=.AsideBar_SubOptions_Item:nth-child(3) > .AsideBar_Text | 

    # btn_sub_grupos = context.driver.find_element(By.XPATH, '//*[text() = \"Grupos\"]')
    # btn_sub_grupos.click()
    

    time.sleep(5)
    pass



@then(u'Realizar la busqueda del grupo: "{grupo}" para asignar')
def busqueda_tabla(context, grupo):
    time.sleep(5)
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys(grupo)
    lbl_buscar.send_keys(Keys.ENTER)
    time.sleep(3)

   ## Tabla de resultadps
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//tbody//div[1]//button[1]")
    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@alt='Mas informacion']")
    btn_asignar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Asignar']")
    btn_asignar.click()
    time.sleep(3)

    pass


@then(u'Realizar la busqueda del grupo: "{grupo}"')
def busqueda_tabla(context, grupo):
    time.sleep(5)
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys(grupo)
    lbl_buscar.send_keys(Keys.ENTER)
    time.sleep(3)

   ## Tabla de resultadps
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//tbody//div[1]//button[1]")
    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@alt='Mas informacion']")
    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='Common_Caret']")
    btn_abrir_grupo.click()
    time.sleep(3)

    pass


@then(u'Busqueda del grupo: "{grupo}"')
def busqueda_tabla(context, grupo):
    time.sleep(4)
    # lbl_buscar = context.driver.find_element(By.XPATH, "//input[@placeholder='Buscar']")
    # lbl_buscar = context.driver.find_element(By.XPATH, "//form[@class='SearchContainer GroupsMainAuthorization_Filters_Search']")
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys(grupo)
    lbl_buscar.send_keys(Keys.ENTER)
    time.sleep(1)
    pass


@then(u'Seleccionar opcion para devolver el grupo')
def busqueda_tabla(context):
    ## Tabla de resultadps
    time.sleep(2)
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='Common_Cancell']")
    btn_abrir_grupo.click()
    pass

@then(u'Seleccionar grupo')
def busqueda_tabla(context):
    ## Tabla de resultadps
    time.sleep(2)
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='Common_Caret']")
    btn_abrir_grupo.click()
    pass


@then(u'Seleccionar grupo para autorizar')
def busqueda_tabla(context):
    ## Tabla de resultadps
    time.sleep(2)
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@class='CommonAuthTable_Caret']")
    btn_abrir_grupo.click()
    time.sleep(10)
    pass




@then(u'Seleccionar motivo de devolucion')
def motivo_devolucion(context):
    ## Tabla de resultadps
    time.sleep(3)
    select_motivo_devolucion = context.driver.find_element(By.XPATH, "//div[@class='Select null']//select[@id='selector']")
    select_motivo_devolucion.click()
    time.sleep(2)

    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//option[@value='Entrega posterior a último corte']")
    btn_abrir_grupo.click()
    pass


@then(u'Ingresar comentario de la devolucion: "{txt_motivo_devolucion}"')
def comentario_devolucion(context,txt_motivo_devolucion):
    time.sleep(3)
    ingresa_motivo_devolucion = context.driver.find_element(By.XPATH, "//textarea[@name='comment']")

    ingresa_motivo_devolucion.click()
    ingresa_motivo_devolucion.send_keys(txt_motivo_devolucion)
    time.sleep(1)
    # lbl_buscar.send_keys(Keys.ENTER)
    pass



@then(u'Aceptar la devolucion')
def aceptar_devolucion(context):
    btn_aceptar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    btn_aceptar.click()
    time.sleep(3)
    pass






@then(u'Btn Valida el grupo')
def validar_grupo_luci(context):
    time.sleep(1)
    btn_validar_grupo = context.driver.find_element(By.XPATH, "//button[normalize-space()='Validar grupo']")
    btn_validar_grupo.click()
    pass


@then(u'Confirmo accion de validacion del grupo')
def Confirmo_validacion_grupal(context):
    btn_validar_grupo = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    btn_validar_grupo.click()
    time.sleep(5)
    pass















@then('Ingresar a la opcion Prospeccion')
def ingresar_digitalizacion(context):
    time.sleep(6)

    # btn_digitalizacionelement = context.driver.find_element(By.XPATH, "//span[normalize-space()='Digitalización']")
    # btn_digitalizacionelement = context.driver.find_element(By.XPATH, "//body//div[3]//div[1]//button[1]//img[1]")
    btn_grupos = context.driver.find_element(By.XPATH, "//span[normalize-space()='Prospectos']")
    btn_grupos.click()

    time.sleep(1)
    btn_body = context.driver.find_element(By.ID, "root")
    btn_body.click()
    time.sleep(1)
    pass



@then(u'Realizar la busqueda del prospecto: "{prospecto}"')
def busqueda_tabla(context, prospecto):
    time.sleep(3)
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys(prospecto)
    lbl_buscar.send_keys(Keys.ENTER)
    time.sleep(3)

   ## Tabla de resultadps
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)

    # btn_abrir_grupo = context.driver.find_element(By.XPATH, "//tbody//div[1]//button[1]")
    btn_abrir_grupo = context.driver.find_element(By.XPATH, "//img[@alt='Mas informacion']")
    btn_abrir_grupo.click()
    time.sleep(7)

    # input_nombre_gruṕ = context.driver.find_element(By.ID, "groupName")
    # text_nombre_grupo = input_nombre_gruṕ.get_attribute('value')
    # text_nombre_grupo = 'VER42'
    
    # Validar nombre del grupo 
    # assert text_nombre_grupo == 'ver42'
    # message = "First value and second value are not equal !"
    # assertEqual(text_nombre_grupo, 'ver42', message) 
    # assert_equal(text_nombre_grupo, 'ver42', message)
    # assertEqual(text_nombre_grupo,'ver42')
    # assert actual_value == expected_value, f"Expected value to be '{expected_value}' but got '{actual_value}'"

    # assert text_nombre_grupo == 'VER41'
    # txt_comparar = '24G00225'
    # try:
    #     assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
    # finally:
    #     context.driver.quit()
    # pass






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
#     # assertEqual(text_nombre_grupo,'ver42')
#     # assert actual_value == expected_value, f"Expected value to be '{expected_value}' but got '{actual_value}'"

#     # assert text_nombre_grupo == 'VER41'
#     txt_comparar = 'EMPRENDEDORAS'
#     try:
#         assert text_nombre_grupo == txt_comparar, f"Expected value to be '{text_nombre_grupo}' but got '{txt_comparar}'"
#     finally:
#         context.driver.quit()
#     pass









@then('Ingresar al menu Renovacion')
def ingresar_digitalizacion(context):
    time.sleep(10)

    btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[6]//div[1]//button[1]//img[1]")
    btn_despliega_menu.click()
    time.sleep(1)

    btn_body = context.driver.find_element(By.ID, "root")
    btn_body.click()
  
  
    time.sleep(5)
    pass




@then(u'Cambiarme al tap: "{tap}"')
def ingresar_digitalizacion(context,tap):
    time.sleep(2)

    # tap = context.driver.find_element(By.XPATH, "//button[normalize-space()='ADJUNTOS']")
    # tap.click()

    # btn_abrir_menu = context.driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
    # btn_abrir_menu.click()
    # time.sleep(3)

    opcion_tap = str(tap)
    
    if opcion_tap == 'CDC':
        # btn_despliega_menu = context.driver.find_element(By.XPATH, "//button[normalize-space()='CDC\\'s']")
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//button[@data-testid='Tab_Button_Test_1']")
    elif opcion_tap == 'Asignacion':
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//span[normalize-space()='Asignación']")
    else:
        btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[1]//div[1]//button[1]//img[1]")
    

    btn_despliega_menu.click()
    time.sleep(1)






    pass


@then(u'Aprobar grupo para mambu')
def ingresar_digitalizacion(context):
    btn_aprobar_grupo_mambu = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aprobar grupo']")
    btn_aprobar_grupo_mambu.click()
    time.sleep(2)

    txt_valida = context.driver.find_element(By.XPATH, "(//span[@class=' css-1sv7px7'])[1]")
    texto_obtenido = txt_valida.text

    texto_esperado = "Tomará algunos minutos para que veas reflejado tu grupo en Mambu, agradecemos tu paciencia."
    assert texto_obtenido == texto_esperado, f"Texto no coincide: esperado '{texto_esperado}', obtenido '{texto_obtenido}'"
    time.sleep(2)
    
    btn_aceptar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    btn_aceptar.click()
    time.sleep(10)
    pass