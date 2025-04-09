import allure

def agregar_captura_reporte(context, titulo=''):
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name=titulo,
        attachment_type=allure.attachment_type.PNG,
    )
