from behave import given, when, then
from pages.home_page import HomePage
from pages.mis_grupos_pages import MisGrupos
# from utils.scroll_utils import scroll_vertical



@when(u'selecciono la opcion de mis grupos')
def step_nenu_mis_grupos(context):
    context.clic_menu_mis_grupos = MisGrupos(context.driver)
    context.clic_menu_mis_grupos.btn_menu_mis_grupos()  
    pass

@then(u'buscar al grupo: "{grupo}"')
def step_buscar_al_grupo(context, grupo):
    context.busca_nombre_grupo = HomePage(context.driver)
    context.busca_nombre_grupo.ingresa_nombre_grupo(grupo)  
    pass


@then(u'Formalizar grupo')
def btn_formalizar_grupo(context):
    context.formaliza_grupo = MisGrupos(context.driver)
    context.formaliza_grupo.btn_para_formalizar_grupo()  
    pass

@then(u'Seleccionar el grupo del listado')
def step_seleccionar_grupo_listado(context):
    context.seleccionar_grupo_listado = MisGrupos(context.driver)
    context.seleccionar_grupo_listado.seleccionar_grupo_del_listado()
    pass


@then(u'Hacer clic tap Devoluciones')
def tap_devoluciones(context):
    context.devolucion_digitalizacion = MisGrupos(context.driver)
    context.devolucion_digitalizacion.tap_para_devolucion_digitalizacion()  
    pass


@then(u'Buscar grupo devuelto: "{nombre_grupo}"')
def buscar_grupo_devoluciones(context, nombre_grupo):
    context.grupo_devolucion_digitalizacion = MisGrupos(context.driver)
    context.grupo_devolucion_digitalizacion.buscar_grupo_devolucion_digitalizacion(nombre_grupo)
    pass


@then(u'Validar que se envio al mc seccion de mis grupos')
def validar_seccion_mis_grupos(context):
    context.validar_grupo_enviado_digitalizacion = MisGrupos(context.driver)
    context.validar_grupo_enviado_digitalizacion.validar_seccion_mis_grupos()
    pass

