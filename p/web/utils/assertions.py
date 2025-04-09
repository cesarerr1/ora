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


