def clic(driver, elemento):
    by, value = elemento  
    elemento = driver.find_element(by=by, value=value)  
    elemento.click()

def mandar_datos(driver,elemento,dato):
    by, value = elemento  
    elemento = driver.find_element(by=by, value=value)  
    elemento.send_keys(dato)
