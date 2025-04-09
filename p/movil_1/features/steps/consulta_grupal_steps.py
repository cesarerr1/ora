from behave import given, when, then
from pages.home_page import HomePage
from pages.consulta_grupal_pages import ConsultaGrupal

# from utils.scroll_utils import scroll_vertical

@when(u'Selecciona la opcion: Consulta grupal')
def genera_grupo(context):
    context.clic_menu_consulta_grupal = HomePage(context.driver)
    context.clic_menu_consulta_grupal.btn_menu_consulta_grupal()
    pass


@then(u'clic agregar a un grupo existente')
def clic_agregar_integrante_grupo_existente(context):
    context.lnk_agegar_a_grupo_existente = ConsultaGrupal(context.driver)
    context.lnk_agegar_a_grupo_existente.lnk_agegar_a_grupo()
    pass
@then(u'Genera un nuevo grupo con el nombre: "{nombre_grupo}"')
def genera_nuevo_grupo(context,nombre_grupo):
    context.nombre_grupo = ConsultaGrupal(context.driver)
    context.nombre_grupo.lbl_ingresar_nombre_grupo(nombre_grupo)
    pass


@then(u'Agregar integrante dando clic en icono mas')
def clic_agregar_integrante(context):
    context.btn_agregar_integrante = ConsultaGrupal(context.driver)
    context.btn_agregar_integrante.btn_para_buscar_integrantes()
    
    pass


@then(u'Seleccionar btn prospecto existente')
def btn_tipo_de_prospecto_existente(context):
    context.btn_para_agregar_prospecto_existente = ConsultaGrupal(context.driver)
    context.btn_para_agregar_prospecto_existente.prospeto_existente()
    pass




@then(u'buscar el grupo creado: "{nombre_grupo}"')
def buscar_grupo_creado_con_anterioridad(context, nombre_grupo):
    context.buscar_grupo_creado_anteriormente = ConsultaGrupal(context.driver)
    context.buscar_grupo_creado_anteriormente.buscar_grupo_para_agregar_integrantes(nombre_grupo)
    pass



@then(u'Buscar prospecta: "{prospecta}" y agregar al grupo')
def buscar_integrante_para_grupo(context, prospecta ):  
    context.buscar_integrante_para_grupo = ConsultaGrupal(context.driver)
    context.buscar_integrante_para_grupo.buscar_integrante_para_agregar_al_grupo(prospecta)
    pass


@then(u'Seleccionar al prospecto del listado de la busqueda generada')
def selecciona_prospecto_del_listado(context):
    context.selecciona_prospecta_de_los_resultados = ConsultaGrupal(context.driver)
    context.selecciona_prospecta_de_los_resultados.card_prospecta_de_los_resultados()
    pass


@then(u'Agrega al prospecto del resultado de la busqueda')
def agregar_prospecto_existente_de_la_busqueda(context):
    context.selecciona_prospecta_encontrado = ConsultaGrupal(context.driver)
    context.selecciona_prospecta_encontrado.card_prospecta_encontrada()
    pass




@then(u'Utilizar grupo')
def btn_utilizar_grupo(context):
    context.utiliza_grupo = ConsultaGrupal(context.driver)
    context.utiliza_grupo.utiliza_el_grupo()
    pass


@then("el mensaje de confirmación es visible")
def step_validar_mensaje_confirmacion(context):
    context.Validar_integrante_para_agregar_al_grupo = ConsultaGrupal(context.driver)
    context.Validar_integrante_para_agregar_al_grupo.obtener_mensaje_confirmacion()
    pass

 
@then("Validacion de duplicidad de grupo")
def step_validar_duplicidad_de_grupo(context):
    context.Validar_duplicidad_de_grupo = ConsultaGrupal(context.driver)
    context.Validar_duplicidad_de_grupo.validar_duplicidad_de_grupo()
    pass
 