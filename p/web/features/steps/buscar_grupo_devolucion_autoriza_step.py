import time
from behave import given, when, then
from selenium import webdriver
import os
from datetime import datetime, timedelta

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.functionsAuxiliarWeb import (
    capture_screenshot
)


@then(u'ingresa al grupo')
def devolver_grupo(context):
    time.sleep(2)

    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(3)
    # lbl_buscar = context.driver.find_element(By.XPATH, "//input[@placeholder='Buscar']")
    # lbl_buscar = context.driver.find_element(By.XPATH, "//form[@class='SearchContainer GroupsMainAuthorization_Filters_Search']")
    lbl_devolucion = context.driver.find_element(By.XPATH, "//img[@alt='Mas informacion']")
    lbl_devolucion.click()
    
    time.sleep(2)
    pass


@then(u'Ingresa al grupo para autorizar')
def devolver_grupo(context):
    time.sleep(2)

    tr_tabla_resultados = context.driver.find_element(By.XPATH, "//tbody//tr[@class='Table_Row']")
    tr_tabla_resultados.click()
    time.sleep(3)
    
    lbl_devolucion = context.driver.find_element(By.XPATH, "//img[@class='CommonAuthTable_Caret']")
    lbl_devolucion.click()
    
    time.sleep(2)
    pass





@then(u'moverme a la tap "{tap}"')
def moverme_tap(context,tap):
    time.sleep(4)
    tap = context.driver.find_element(By.XPATH, "//button[normalize-space()='"+tap+"']")
    tap.click()
    pass

@then(u'Validar ubicacion')
def validar_ubicacion(context):
   
    ubicacion = context.driver.find_elements(By.XPATH, "//button[normalize-space()='Ir a la ubicación']")

    if len(ubicacion) > 0:
        print("El elemento está presente en el DOM.")
        
        ir_a_ubicacion = context.driver.find_element(By.XPATH, "//button[normalize-space()='Ir a la ubicación']")
        ir_a_ubicacion.click()

        ingresa_ubicacion(context)
        tap = context.driver.find_element(By.XPATH, "//button[normalize-space()='INFO CRÉDITO']")
        tap.click()
        datos_del_credito(context)
       
    else:
        print("El elemento no está presente en el DOM.")   
        datos_del_credito(context)
        
    pass




@then(u'Aprobar')
def aprobar_devolucion(context):
    btn_aprobar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aprobar']")
    btn_aprobar.click()
    time.sleep(1)

    """
    ¿Estas seguro de aprobar el grupo?
    """
    btn_aceptar = context.driver.find_element(By.XPATH, "//button[normalize-space()='Aceptar']")
    btn_aceptar.click()
    time.sleep(7)
    pass

def datos_del_credito(context):
    
    producto = context.driver.find_element(By.XPATH, "(//select[@id='selector'])[1]")
    producto.click()
    # PRODUCTO
    select_producto = context.driver.find_element(By.XPATH, "//option[@value='4']")   
    select_producto.click()

    # CANAL
    canal = context.driver.find_element(By.XPATH, "(//select[@id='selector'])[3]")
    canal.click()
    select_canal = context.driver.find_element(By.XPATH, "//div[@class='css-1r3jwfx']//option[@value='1'][normalize-space()='BBVA']")
    select_canal.click()
  
    # # HORA DE REUNIÓN*    
    # hora_reunion = context.driver.find_element(By.NAME, "horaReunion")
    # hora_reunion.click()
    # select_hora_reunion = context.driver.find_element(By.XPATH, "//option[@value='09:00:00']")    
    # select_hora_reunion.click()
    

     # FECHA TENTATIVA DE DESEMBOLSO*
    elemento = context.driver.find_element(By.ID, "fechaDesembolso")
    elemento.click()  # Cambia "campo-de-texto" por el ID real
    
    # # Obtener la fecha de hoy
    hoy = datetime.today()

    mañana = hoy + timedelta(days=1)
    dai_renovacion = mañana.strftime("%d-%m-%Y")

    # elemento.send_keys(mañana)
    elemento.send_keys(dai_renovacion)  
    
    pass




def ingresa_ubicacion(context):
    coloca_ubicacion = context.driver.find_element(By.XPATH, "//input[@id='locationUrl']")
    time.sleep(1)
    coloca_ubicacion.click()
    coloca_ubicacion.clear()
    ubicacion_maps ="https://www.google.com/maps?q=19.2937,-99.2434"

    coloca_ubicacion.send_keys(ubicacion_maps)
    coloca_ubicacion.send_keys(Keys.ENTER)


    btn_guardar_ubicacion = context.driver.find_element(By.XPATH, "//button[normalize-space()='Guardar enlace de ubicación']")
    btn_guardar_ubicacion.click()
    time.sleep(13)
    pass




