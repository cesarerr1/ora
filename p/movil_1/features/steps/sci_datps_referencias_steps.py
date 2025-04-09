from appium.webdriver.common.appiumby import AppiumBy
from behave import given, when, then
from pages.consulta_rapida_page import ConsultaRapida
from pages.sci_datos_pages import SCI
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils.utils as utilerias
import features.selectores as sel
from appium.webdriver.common.touch_action import TouchAction




@then(u'avanza hasta referencias personales')
def avanza_hasta_referencias_personales(context):
    driver.implicitly_wait(80)
    # Repetir el ciclo for 3 veces
    for i in range(3):
        driver.implicitly_wait(40)
        utilerias.scroll_vertical_por_tamaño_pantalla(driver, 950)

        btn_siguiente = (MobileBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_siguiente)
        utilerias.click_boton(driver, btn_siguiente)
    pass