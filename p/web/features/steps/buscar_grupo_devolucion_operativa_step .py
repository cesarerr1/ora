import time
from behave import given, when, then
from selenium import webdriver
import os
from utils import functions_auxiliar_web as utilerias
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.functionsAuxiliarWeb import (
    capture_screenshot
)


@then(u'hacer la devolucion con el motivo: "{motivo}" y justificacion: "{justificacion}"')
def devolver_grupo(context, motivo, justificacion):
    time.sleep(6)
    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(2)
    # lbl_buscar = context.driver.find_element(By.XPATH, "//input[@placeholder='Buscar']")
    # lbl_buscar = context.driver.find_element(By.XPATH, "//form[@class='SearchContainer GroupsMainAuthorization_Filters_Search']")
    lbl_devolucion = context.driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[1]/td[10]/div[1]/button[1]")
    lbl_devolucion.click()
    time.sleep(3)
    # lbl_buscar.send_keys(grupo)
    # lbl_buscar.send_keys(Keys.ENTER)

    select_opcion_motivo = context.driver.find_element(By.XPATH, "//div[@class='Select null']//select[@id='selector']")
    select_opcion_motivo.click()

    select_motivo = context.driver.find_element(By.XPATH, "//option[@value='"+motivo+"']")
    select_motivo.click()



    txt_comentario_devolucion = context.driver.find_element(By.XPATH, "//textarea[@name='comment']")
    txt_comentario_devolucion.click()


    txt_comentario_devolucion.send_keys(justificacion)
    txt_comentario_devolucion.send_keys(Keys.ENTER)


        # btn_aceptar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    # btn_aceptar.click()

    # btn_aceptar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    # btn_aceptar.click()
    time.sleep(3)
    pass


@then(u'ir hasta el fonal de la pagina')
def it_al_final_pagina(context):
    # context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Obtener la altura inicial de la página
    last_height = context.driver.execute_script("return document.body.scrollHeight")

# Itera haciendo scroll hacia abajo hasta que no haya más contenido que cargar
    while True:
    # Ejecuta JavaScript para hacer scroll hacia abajo
        context.driver.execute_script("window.scrollBy(0, 1000);")  # Cambia el valor 1000 si quieres hacer scroll más rápido o más lento
    
    # Espera a que la página cargue nuevo contenido (si es necesario)
        time.sleep(1)

    # Calcular la nueva altura después del scroll
        new_height = context.driver.execute_script("return document.body.scrollHeight")

    # Si la altura no cambió, llegaste al final de la página
        if new_height == last_height:
            break

        last_height = new_height


    time.sleep(10)

    pass



@then(u'Ir al final')
def ir_al_final(context):
    time.sleep(2)
    utilerias.scroll_to_element(context.driver, By.XPATH, "//button[normalize-space()='Aprobar']")
    time.sleep(6)
    pass