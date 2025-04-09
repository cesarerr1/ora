import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.functionsAuxiliarWeb import (
    capture_screenshot
)






@then(u'Selecciono el nivel de riesgo: "{nivel_riesgo}"')
def select_nivel_riesgod(context,nivel_riesgo):
    time.sleep(2)
    # element = context.driver.find_element(By.ID, "passwd-id")



    # Encuentra todos los elementos <select> con el mismo atributo data-testid
    selectores = context.driver.find_elements(By.CSS_SELECTOR, 'select[data-testid="Select-testId"]')
    botones = context.driver.find_elements(By.CSS_SELECTOR, 'button[data-testid="Button_Test"]')


    for index, selector in enumerate(selectores):
        select = Select(selector)
        select.select_by_value(nivel_riesgo)  # Selecciona "MEDIO" (value="2")
        print(f"✅ Seleccionado 'MEDIO' en el select #{index + 1}")

    for index, boton in enumerate(botones):
        boton.click()
        print(f"✅ Clic realizado en el botón #{index + 1}")

    ### Anteriores
    # nivel_riesgo = context.driver.find_element(By.XPATH, "//div[3]//form[1]//div[1]//div[1]//div[1]//select[1]")
    # nivel_riesgo.click()
    # time.sleep(2)
    # # time.sleep(1)
    # selct_nivel_riesgo = context.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[2]/div[3]/form[1]/div[1]/div[1]/div[1]/select[1]/option[2]")
    # selct_nivel_riesgo.click()
    # time.sleep(3)

    # btn_guardar = context.driver.find_element(By.XPATH, "//div[3]//form[1]//div[1]//button[1]")
    # btn_guardar.click()
    # time.sleep(3)


    #   

    # label_usuario = context.driver.find_element(By.ID, "identifierId")
    # label_usuario.send_keys("pruebas-luci-analista@podemos.mx")
    # btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    # btn_siguiente.click()
    # time.sleep(3)

    # label_pass = context.driver.find_element(By.NAME,"Passwd")
    # label_pass.send_keys("1qazxsw2Luci")
    # btn_siguiente = context.driver.find_element(By.XPATH, "//span[normalize-space()='Siguiente']")
    # btn_siguiente.click()
    # time.sleep(6)
    pass




