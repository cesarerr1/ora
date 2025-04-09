from behave import given, when, then
from pages.home_page import HomePage    
from pages.renovaciones_pages import Renovaciones
# from utils.scroll_utils import scroll_vertical



@when(u'selecciono la opcion: renovaciones')
def step_nenu_mis_grupos(context):
    context.clic_menu_renovaciones = HomePage(context.driver)
    context.clic_menu_renovaciones.btn_menu_renovaciones()  
    pass

@then(u'Filtrar estatus por: renovar')
def step_filtrar_estatus(context): 
    context.clic_menu_filtro_renovaciones = Renovaciones(context.driver)
    context.clic_menu_filtro_renovaciones.btn_filtro()
    pass

@then(u'Buscar grupo: "{grupo}"')
def step_buscar_grupo(context, grupo):
    context.renovaciones_buscar_grupo = Renovaciones(context.driver)
    context.renovaciones_buscar_grupo.buscar_grupo(grupo)
    pass

# @when(u'selecciono la opcion de mis grupos')
# def step_nenu_mis_grupos(context):
#     context.clic_menu_mis_grupos = Renovaciones(context.driver)
#     context.clic_menu_mis_grupos.btn_menu_renovaciones()  
#     pass

# @then(u'buscar al grupo: "{grupo}"')
# def step_buscar_al_grupo(context, grupo):
#     context.busca_nombre_grupo = HomePage(context.driver)
#     context.busca_nombre_grupo.ingresa_nombre_grupo(grupo)  
#     pass
