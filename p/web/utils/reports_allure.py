import allure

def agregar_captura_reporte(context, titulo=''):
    if titulo == '':
        titulo = f'{context.scenario.name} [{context.current_step_name}]'
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name=titulo,
        attachment_type=allure.attachment_type.PNG,
    )

def agregar_texto_reporte(texto, nombre):
    allure.attach(texto, name=nombre, attachment_type=allure.attachment_type.TEXT)
