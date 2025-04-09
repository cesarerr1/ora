from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import features.selectores as sel
class HomePage(BasePage):
    tap_consultas = (AppiumBy.XPATH, sel.Home.tap_consultas)
    img_btn_consulta_rapida = (AppiumBy.ACCESSIBILITY_ID, sel.Home.img_btn_consulta_rapida)
    img_btn_consulta_grupal = (AppiumBy.XPATH, sel.Home.img_btn_consulta_grupal)
    btn_img_menu_renovaciones = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Home.img_btn_mis_renovaciones)

    def btn_menu_consulta_rapida(self):
        self.click(*self.img_btn_consulta_rapida)


    def btn_menu_consulta_grupal(self):
        
        self.click(*self.img_btn_consulta_grupal)
        pass

    def btn_menu_renovaciones(self): 
        self.click(*self.btn_img_menu_renovaciones)
        pass



    # ele_index = driver.find_element(AppiumBy.XPATH, sel.Home.tap_consultas)
    # ele_index.click()
