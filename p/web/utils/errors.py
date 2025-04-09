def error_ocurrido(error):
    raise Exception (f"Ha ocurrido un error: '{error}'")

def validacion(campo,message):
    raise Exception(f"El Campo: '{campo}' '{message}'")

def validacion(message):
    raise Exception(f"Mensaje: '{message}'")

def elemento_no_encontrado(web_elemento):
    print(f"No se encontró mensaje de error para el campo {web_elemento}")

