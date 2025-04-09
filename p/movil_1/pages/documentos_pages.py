from pages.base_page import BasePage
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction
import utils.utils as utilerias
import features.selectores as sel


class SCIDocumentos(BasePage):

    solicitud_individual = (AppiumBy.CLASS_NAME, "android.view.View")
    def __init__(self, driver):
        super().__init__(driver)
    
    opt_adjunta_comp_domicilio_frontal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_adjunta_comp_domicilio_frontal)
    btn_opt_almacenamiento = (AppiumBy.XPATH, sel.PerfilIntegrante.btn_opt_galeria)
    opt_almacenamiento_imagen = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_opt_imagen_google)
    opt_adjunta_comp_domicilio_reverso = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_adjunta_comp_domicilio_reverso)
    opt_adjunta_ine_frontal = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_adjunta_ine_frontal)
    opt_adjunta_ine_reverso = (AppiumBy.ANDROID_UIAUTOMATOR, sel.PerfilIntegrante.btn_adjunta_ine_reverso)
    btn_finalizar_registro_prospecta = (AppiumBy.XPATH, sel.AccionFormulario.btn_finalizar_registro)
   
    def btn_adjunta_comp_domicilio_frontal(self):
        self.click_btn(*self.opt_adjunta_comp_domicilio_frontal,timeout=7)
        pass

    def btn_almacenamiento(self):
        self.click(*self.btn_opt_almacenamiento)
        pass

    def btn_opt_almacenamiento_imagen(self):
        self.click(*self.opt_almacenamiento_imagen)
        time.sleep(10)
        
        pass

    def btn_opt_adjunta_comp_domicilio_reverso(self):
        time.sleep(3)
        
        self.click(*self.opt_adjunta_comp_domicilio_reverso)
        pass

    def btn_opt_adjunta_ine_frontal(self):
        time.sleep(3)
        self.click(*self.opt_adjunta_ine_frontal)        
        pass

    def btn_opt_adjunta_ine_reverso(self):
        time.sleep(3)
        self.scroll(500, 1200, 500, 300)
        
        self.click(*self.opt_adjunta_ine_reverso)
        pass


    def btn_finaliza_registro(self):
        time.sleep(3)
        
        self.click(*self.btn_finalizar_registro_prospecta)
        time.sleep(6)
        pass