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

@then('Ingresar al menu Operativa')
def ingresar_operativa(context):
    time.sleep(6)
    # btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[2]//div[1]//button[1]//img[1]")
    # btn_despliega_menu = context.driver.find_element(By.XPATH, "//body/div[@id='root']/div[@data-testid='Layout-Test-Id']/div[@class='AsideBar_Container']/div[@class='AsideBar_Card css-1kz2nje']/div[1]/div[1]/button[1]")
    btn_despliega_menu = context.driver.find_element(By.XPATH, "//body//div[4]//div[1]//button[1]//img[1]")
    btn_despliega_menu.click()
    time.sleep(2)

    # btn_sub_grupos = context.driver.find_element(By.XPATH, "(//span[normalize-space()='Grupos'])[1]")
    btn_sub_grupos = context.driver.find_element(By.XPATH, '//*[text() = \"Grupos\"]')
    btn_sub_grupos.click()
    
    time.sleep(3)
   

    # time.sleep(1)
    # btn_body = context.driver.find_element(By.ID, "root")
    # btn_body.click()

    pass



@then(u'Realizar la busqueda del grupo de operativa: "{id_grupo}"')
def busqueda_tabla(context, id_grupo):
 
    time.sleep(3)
    lbl_buscar = context.driver.find_element(By.NAME, "search")
    lbl_buscar.click()
    lbl_buscar.send_keys(id_grupo)
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

    pass











