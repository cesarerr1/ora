from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
import features.selectores as sel
import time
from features.steps.txt_valida import VALIDACION_DUPLICIDAD_GRUPO

class ConsultaGrupal(BasePage):
    lbl_nombre_grupo = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    time.sleep(2)
    btn_continuar_nombre_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.AccionFormulario.btn_continuar)
    time.sleep(4)
    btn_agregar_integrante = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_agregar_integrante)
    btn_agregar_integrante_emergente = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Prospecto existente"]')
    btn_tipo_de_prospecto_existente = (AppiumBy.ANDROID_UIAUTOMATOR, '//android.widget.Button[@content-desc="Prospecto existente"]')

    lbl_buscar_prospecto = (AppiumBy.XPATH, sel.Home.lbl_consulta_buscar)
    btn_opcion_prospecto = (AppiumBy.CLASS_NAME, "android.widget.EditText")
    usuario_encontrado = (AppiumBy.CLASS_NAME, "android.view.View")

    lnk_agregar_integrante_grupo_existente = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Agregar a un grupo existente"]')
    
    btn_buscar_al_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    primer_elemento_grupo = (AppiumBy.CLASS_NAME, "android.widget.ImageView")
    btn_utilizar_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_utilizar_grupo)
    lbl_buscar_prospecta = (AppiumBy.XPATH,'//android.widget.EditText')
    prospecto_encontrado =(AppiumBy.CLASS_NAME, "android.view.View")
    
    confirm_mensage_con_prospecta =(AppiumBy.XPATH, '//android.view.View[@content-desc="¿Deseas agregar a SOFIA MARIANA LOZANO ALVAREZ al grupo?"]')
    btn_aceptar_prospecta =(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Aceptar"]')


    #VALIDACIONES
    txt_validacion_duplicidad_grupo = (AppiumBy.ANDROID_UIAUTOMATOR, sel.Grupo.txt_validacion_duplicidad_grupo)

    
    # btn_agregar_integrante = (MobileBy.ANDROID_UIAUTOMATOR, sel.Grupo.btn_agregar_integrante)

    def lbl_ingresar_nombre_grupo(self,nombre_grupo): 
        self.clic_coordenadas(288, 582)
        self.interactura_elemento(*self.lbl_nombre_grupo,nombre_grupo)
        time.sleep(2)
        self.click(*self.btn_continuar_nombre_grupo)
        time.sleep(4)
        pass

    def btn_para_buscar_integrantes(self):
        self.click(*self.btn_agregar_integrante)
        pass

    def prospeto_existente(self):
        self.click(*self.btn_agregar_integrante_emergente)
        # self.click(*self.btn_agregar_integrante)
        pass
    
    # def btn_para_Buscar_integrantes(self):
    #     self.click(*self.btn_tipo_de_prospecto_existente)
    #     pass

    def buscar_integrante_para_agregar_al_grupo(self,usuario):
        
        self.interactura_elemento(*self.lbl_buscar_prospecta, usuario)
        pass

    def card_prospecta_de_los_resultados(self):
        self.click_s(*self.prospecto_encontrado,2)
        time.sleep(6)
        pass
    


     

    # def click_consulta_rapida(self):
    #     self.click(*self.img_btn_consulta_rapida)



    # ele_index = driver.find_element(AppiumBy.XPATH, sel.Home.tap_consultas)
    # ele_index.click()

    def lnk_agegar_a_grupo(self):
        # self.clic_coordenadas(346, 770)
        self.click(*self.lnk_agregar_integrante_grupo_existente)
        pass

    def buscar_grupo_para_agregar_integrantes(self,nombre_grupo):  
        self.interactura_elemento(*self.btn_buscar_al_grupo,nombre_grupo)
        pass


    def utiliza_el_grupo(self):  
        self.click(*self.btn_utilizar_grupo)
        pass




    def obtener_mensaje_confirmacion(self):
        """
        Obtiene el texto del mensaje de confirmación.
        """
        # mensaje = self.get_text_by_description(*self.confirm_mensage_con_prospecta)
        # print("El mensaje de confirmación es:", mensaje)

        self.click(*self.btn_aceptar_prospecta)

        # assert mensaje == "¿Deseas agregar a JARINTIA  ANAYA GRILLOS  al grupo?", \
        # "El mensaje de confirmación no es el esperado."
       
        pass

    def validar_duplicidad_de_grupo(self):
        self.assert_element_contains_text(*self.txt_validacion_duplicidad_grupo, VALIDACION_DUPLICIDAD_GRUPO)
        
        pass