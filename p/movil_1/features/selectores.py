
class SelectorTipo:
    ID = "ID"
    XPATH = "XPATH"
    ANDROID_UIAUTOMATOR = 'ANDROID_UIAUTOMATOR'
    # Otros tipos de selectores que puedas necesitar, como class_name, css_selector, etc.


class AccrionesMobile:
    btn_regresa = 'new UiSelector().className("android.widget.Button").instance(0)'


class ValidacionesConsultaRapida:
    txt_validacion_curp_lista_negra = 'new UiSelector().description("Lo sentimos")'
    txt_validacion_curp_lista_negra_razon = 'new UiSelector().description("El CURP entra dentro del listado de palabras inconvenientes de renapo, favor de revisar")'
    
class DatosEmprendedora:
    # NOMBRE = '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[1]'  # noqa: E501
    NOMBRE = '//android.widget.ScrollView/android.widget.EditText[1]'  # noqa: E501
    #NOMBRE = 'UiSelector().description("Quedan 50 caracteres")'  # noqa: E501
    # APELLIDO_PATERNO = '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[2]'  # noqa: E501
    APELLIDO_PATERNO = '//android.widget.ScrollView/android.widget.EditText[2]'  # noqa: E501
    # APELLIDO_MATERNO = '//android.view.View[@content-desc=\"NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo\"]/android.widget.EditText[3]'  # noqa: E501
    APELLIDO_MATERNO = '//android.widget.ScrollView/android.widget.EditText[3]'  # noqa: E501
    # CURP = 'UiSelector().className("android.widget.EditText").instance(2)'
    CURP = '//android.widget.ScrollView/android.widget.EditText[4]'
    FECHA_NACIMIENTO  = 'UiSelector().className("android.view.View").instance(11)'
    CONFIRMAR_FECHA_NACIMIENTO = '//android.widget.Button[@content-desc="Confirmar"]'
    # ENTIDAD_NACIMIENTO = '//android.widget.Button[@content-desc="Seleccione Estado"]'
    ENTIDAD_NACIMIENTO = '//android.widget.Button[@content-desc="Selecciona Opcion"]'
    # ENTIDAD_NACIMIENTO = '//android.widget.Button[@content-desc="Seleccione Estado"]'
    ENTIDAD_NACIMIENTO_ESTADO = '//android.view.View[@content-desc="CIUDAD DE MÉXICO"]'



class Genericos:
    selecciona_elemento_segun_el_orden = 'android.view.View'
    selecciona_elemento_segun_el_orden_2 = 'android.widget.EditText'

class ValidaDatosEmprendedoraRechazada:
    txt_rechazada ='UiSelector().description("Lo sentimos")'
    txt_rechazada_razon ='UiSelector().description("Lo sentimos la información de esta emprendedora ya fue consultada.")'
      #  UiSelector().description("Lo sentimos")'
class Direccion:
    CP = 'new UiSelector().className("android.widget.EditText").instance(3)'
    DIR_CALLE = 'UiSelector().className("android.widget.EditText").instance(0)'
    N_EXTERIOR = 'new UiSelector().className("android.widget.EditText").instance(1)'
    N_INTERIOR = 'new UiSelector().className("android.widget.EditText").instance(2)'
    COLONIA_POBLACION = 'new UiSelector().description("Selecciona Opcion")'
    SELECT_UNA_COLONIA_POBLACION = 'UiSelector().description("Olivar de los Padres")'
    # COLONIA_POBLACION = 'new UiSelector().description("SELECCIONE COLONIA")'
    # SELECT_UNA_COLONIA_POBLACION = 'UiSelector().description("OlIVAR DE LOS PADRES")'
    # SELECT_UNA_COLONIA = 'UiSelector().description("Olivar de los Padres")'
    # Otros selectores de SeekBar si los necesitas

class DatosContacto:
    # NUMERO_TELEFONO = '//android.view.View[@content-desc="NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo"]/android.widget.EditText[4]'
    NUMERO_TELEFONO = '//android.widget.ScrollView/android.widget.EditText[4]'
    # NUMERO_TELEFONO2 = '//android.view.View[@content-desc="NOMBRE(S)\nAPELLIDO PATERNO\nAPELLIDO MATERNO\nCURP\nFECHA DE NACIMIENTO\nENTIDAD DE NACIMIENTO\nTELÉFONO\nCONFIRMACIÓN\n¿LA EMPRENDEDORA ES REFERIDA?\nSi\nNo"]/android.widget.EditText[1]'
    NUMERO_TELEFONO2 = '//android.widget.ScrollView/android.widget.EditText[5]'
    CONFIRMACION_NUMERO = '//android.widget.ScrollView/android.widget.EditText[3]'


class AccionFormulario:
    # btn_continuar = '//android.widget.Button[@content-desc="Continuar"]'
       
    btn_cancelar = 'UiSelector().description("Cancelar Solicitud")'
    btn_enviar_nip = 'UiSelector().description("Enviar NIP")'
    btn_edit_datos_emprendedora = 'UiSelector().classNae("android.widget.Button").instance(2)'
    btn_edit_direccion_emprendedora = 'UiSelector().className("android.widget.Button").instance(3)'
    btn_confir_cancelar_datos_emprendedora ='UiSelector().description("Aceptar")'
    btn_confir_aceptar ='UiSelector().description("Aceptar")'   
    btn_continuar2 ='UiSelector().description("Sí, Continuar")'
    btn_consultar ='UiSelector().description("Consultar")'
    link_regresa_inicio = '//android.widget.Button[@content-desc="Volver al inicio"]'
    btn_siguiente = 'UiSelector().description("Siguiente")'
    btn_guardar = 'UiSelector().description("Guardar")'
    btn_finalizar_registro = '//android.widget.Button[@content-desc="Finalizar registro"]'
    btn_continuar = 'new UiSelector().description("Continuar")'

class Home:
    """
    Elementos incicio de apk
    Carrusel, no puede inciar sesion, login
    """
    carrussel_paso_01 ='//android.widget.ImageView[@content-desc="Consultas rápidas y grupales\nRealiza consultas más fácil y rápido, a una sola persona o por grupo."]'
    carrussel_paso_02 ='//android.widget.ImageView[@content-desc="Trabaja sin conexión\nAhora puedes trabajar desconectado, guarda la información y consulta después"]'
    carrussel_paso_03 ='//android.widget.ImageView[@content-desc="Listado de consultas\nPuedes encontrar y buscar todas las consultas realizadas, incluyendo las que dejes pendientes."]'
    carrussel_paso_04 ='//android.widget.ImageView[@content-desc="Atajos a pendientes\nIdentifica el estatus, realiza consultas pendientes de manera ágil y rápida"]'
    btn_inisiar_sesion = 'UiSelector().description("Iniciar sesión con Google")'
    lnk_no_puede_acceder = '//android.widget.Button[@content-desc="No puedo acceder"]'


    # Botones
    img_btn_consulta_rapida = 'Consulta\nRápida'
    img_btn_consulta_grupal = '//android.widget.ImageView[@content-desc="Consulta\nGrupal"]'
    img_btn_mis_grupos = '//android.widget.ImageView[@content-desc="Mis\nGrupos"]'
    img_btn_mis_renovaciones = 'new UiSelector().description("Mis\nRenovaciones")'

    # Consultas
    tap_consultas = '//android.view.View[@content-desc="Consultas\nPestaña 1 de 3"]'
    #tap_consultas = "00000000-0000-062d-0000-001100000003"
    # Pendientes
    tap_pendientes = '//android.view.View[@content-desc="Pendientes\nPestaña 2 de 3"]'

    # Asignadas
    tap_asignadas = '//android.view.View[@content-desc="Asignadas\nPestaña 3 de 3"]'

    #Menú hamburgesa
    btn_menu_hamburgesa ='UiSelector().description("Abrir el menú de navegación")'
   
    # Salir del menu haciendo tap en otro lugar
    tap_salir_menu_hamburgesa = ''
    
    
    lbl_consulta_buscar = '//android.view.View[@content-desc="Buscar"]'

    btn_opt_acerca_de = 'UiSelector().description("Acerca de")'
    lbl_version_apk = 'UiSelector().description("Desarrollado por\nPodemos Progresar\nVersión:\n2.0.26+45.1\nSTAGING\nFECHA: 2024-06-19 13:37:01")'


    

class Otp:
    caracter_otp_1 = 'UiSelector().className("android.widget.EditText").instance(0)'
    caracter_otp_2 = 'UiSelector().className("android.widget.EditText").instance(1)'


class Grupo:
    nuevo_nombre_del_grupo = 'UiSelector().className("android.widget.EditText").instance(0)'
    link_agregar_a_grupo = 'UiSelector().description("Agregar a un grupo existente")'
    primer_grupo_existente = 'UiSelector().description("Utilizar").instance(0)'
    btn_agregar_integrante = 'UiSelector().className("android.view.View").instance(7)'
    btn_tipo_de_integrante_existente = 'UiSelector().description("Prospecto existente")'
    btn_prospecto_existente = '//android.widget.Button[@content-desc="Prospecto existente"]'
    select_primer_prospecto_existente = 'android.view.View'
    
    select_primer_prospecto_existente_en_grupo = 'UiSelector().className("android.widget.Button").instance(1)'
    sacar_del_grupo ='UiSelector().description("Sacar del grupo")'
    
    #Formalizar grupo
    btn_utilizar_grupo ='new UiSelector().description("Utilizar")' 
    btn_formaliza_grupo ='UiSelector().description("Formalizar grupo")' 
    btn_cruzadas = 'new UiSelector().description("Validar solicitudes")'
    lbl_buscar_grupo = 'new UiSelector().className("android.widget.EditText")'

    btn_genera_grupal = 'new UiSelector().description("Crear Solicitud Grupal")'
    
    primer_grupo_en_listado = 'android.widget.ImageView'

    #Devoluciones
    tap_devolucion = 'new UiSelector().description("Devueltos\nPestaña 2 de 2")'
    clic_card_grupo_devuelto = 'android.widget.ImageView'
    btn_actualizar_solicitud_grupal = 'new UiSelector().description("Actualizar Solicitud Grupal")'
    btn_actualizar_solicitud_grupal_2 = 'new UiSelector().description("Actualizar solicitud grupal")'
    btn_continuar_devolucion = 'new UiSelector().description("Continuar")'


    """Validaciones"""
    txt_validacion_duplicidad_grupo = 'new UiSelector().description("El nombre de grupo ingresado ya existe")'

class TapConsultas:
    select_primer_usuario = 'UiSelector().className("android.widget.Button").instance(2)'
    btn_continuar_solicitud ='UiSelector().description("Continuar Solicitud")'
    btn_busqueda_continuar_sci ='UiSelector().description("Solicitud Individual")'


class OCR:
    txt_valida_seccion_datos_personales = 'new UiSelector().description("Captura datos personales")'
    btn_captura_datos_desde_ocr = 'new UiSelector().description("Escanear IFE/INE\nAgregar información más rápido")'


class SCI:

    # Pag 1
    tel_recados = 'UiSelector().className("android.widget.EditText").instance(0)'
    # estado_civil = 'UiSelector().description("ESTADO CIVIL*\nSelecciona Opcion")'
    estado_civil = 'UiSelector().description("Selecciona Opcion").instance(0)'
    
    select_estado_civil_union_libre = 'UiSelector().description("Union Libre")'
    select_estado_civil_soltera = 'UiSelector().description("Soltera")'
    select_estado_civil_casada = 'UiSelector().description("Casada")'

    escoladidad = 'UiSelector().description("Selecciona Opcion")'
    select_escoladidad_secundaria = 'UiSelector().description("Secundaria")'

    correo = 'UiSelector().className("android.widget.EditText").instance(1)'
    # tel_celular = 'new UiSelector().text("5516688525")'
    tel_celular_colocando_valor = 'new UiSelector().className("android.widget.EditText").instance(2)'
    # tel_celular = 'UiSelector().className("android.widget.EditText").instance(2)'
    # tel_celular = 'UiSelector().className("android.widget.EditText").instance(1)'
    firma_electronica = ''
    btn_siguiente = 'UiSelector().description("Prospecto existente")'

    #Acreditación domicilio 
    radio_ine_si = 'new UiSelector().className("android.widget.RadioButton").instance(0)'
    radio_ine_no = 'new UiSelector().className("android.widget.RadioButton").instance(1)'
    parentesco_comprobante_entrega = 'new UiSelector().description("Seleccione parentesco")'
    select_parentesco_comprobante_entrega = 'new UiSelector().description("PROPIO")'
    
    # Datos Documentos
    # antigduedad_domicilio = 'UiSelector().description("ANTIGÜEDAD EN EL DOMICILIO*\nSelecciona Opcion")'
    antigduedad_domicilio = 'UiSelector().description("Ingresa antigüedad")'
    select_antigduedad_domicilio = 'UiSelector().description("3 años")'
    tipo_domicilio = 'UiSelector().description("Seleccione tipo")'
    select_tipo_domicilio = 'UiSelector().description("Propia")'
    
    # Datos Cónyuge o familiar
    nombre_familiar = 'UiSelector().className("android.widget.EditText").instance(0)'
    tel_familiar = 'UiSelector().className("android.widget.EditText").instance(1)'
    parentesco_familiar = 'new UiSelector().description("Seleccione parentesco")'
    select_parentesco_familiar = 'UiSelector().description("Tio (a)")'
    dependentes_familiares = 'new UiSelector().description("Seleccione cantidad")'
    select_dependentes_familiares = 'new UiSelector().description("3")'
    caracteristicas_vivienda = '//android.widget.ScrollView/android.widget.EditText[3]'
    referencia_ubicacion = '//android.widget.ScrollView/android.widget.EditText[4]'
    
    # Actividad economica
    actividad_economica = 'new UiSelector().description("Seleccione actividad")'
    select_actividad_economica = 'new UiSelector().description("Abarrotes")'

    actividad_adiciional = 'new UiSelector().description("Seleccione actividad adicional")'
    select_actividad_adiciional = 'new UiSelector().description("Abarrotes")'

    antiguedad_negocio = 'new UiSelector().description("Ingresa antigüedad")'
    select_antiguedad_negocio = 'UiSelector().description("3 años")'
    
    dia_venta_lu= 'UiSelector().description("L")'
    dia_venta_ma= 'UiSelector().description("M").instance(0)'
    dia_venta_mi = 'UiSelector().description("M").instance(1)'
    
    ubicacion_negocio = 'new UiSelector().description("Seleccione ubicación")'
    select_ubicacion_negocio = 'UiSelector().description("VENTA POR CATALOGO")'

    direccion_del_negocio = 'UiSelector().className("android.widget.EditText").instance(0)'
        
    #Datos economicos
    ganancia_semanal = 'UiSelector().className("android.widget.EditText").instance(1)'
    otros_ingresos = 'UiSelector().className("android.widget.EditText").instance(1)'
    total_ingresos = 'UiSelector().className("android.widget.EditText").instance(2)'

    fuentes_otros_ingresos = 'new UiSelector().className("android.widget.Button").instance(2)'
    select_fuentes_otros_ingresos = 'UiSelector().description("Gasto familiar")'
    monto_pago_semanal = '//android.widget.ScrollView/android.widget.EditText[4]'
    # 
    
    #Referencia 1 y Referencia 2
    select_referncia_uno = 'UiSelector().description("Referencia personal 1")'
    select_referncia_dos = 'UiSelector().description("Referencia personal 2")'
    nombre_referencia = 'UiSelector().className("android.widget.EditText").instance(0)'

    parentesco_referencia = 'new UiSelector().description("PARENTESCO*\nSelecciona Opcion")'
    select_parentesco_referencia = 'new UiSelector().description("Familiar")'

    tel_referencia_recardos = 'new UiSelector().className("android.widget.EditText").instance(1)'
    tel_referencia_celular = 'new UiSelector().className("android.widget.EditText").instance(2)'
    
    #Datos Crediticioas 
    monto = 'new UiSelector().className("android.widget.EditText").instance(0)'
    sera_tu_primer_credito = ''
    tienes_otro_credito_activo = ''
    
    ascienden_ingresos_mensuales_= ''
    propietarios_real_recursos = ''
    
    origen_recursos = 'new UiSelector().className("android.widget.EditText").instance(0)'
    destino_recursos = 'new UiSelector().className("android.widget.EditText").instance(1)'
    liquidar_anticipado = ''
    persona_fisica = ''
    persona_policca = ''
    
class Cdc:
    txt_felicidades = 'new UiSelector().description("¡FELICIDADES!")'
    txt_nueva_consulta = 'new UiSelector().description("Nueva Consulta")'
    txt_ver_info_adicional = 'new UiSelector().description("Ver información adicional")'

class PerfilIntegrante:
    btn_documentos = 'new UiSelector().className("android.widget.Button").instance(6)'
    
    btn_cargar = 'new UiSelector().description("Cargar")'
    # btn_adjunta_foto = '//android.view.View[@content-desc="FOTO DE INTEGRANTE\nAgrega una imagen\nPendiente"]/android.widget.Button'
    btn_adjunta_foto = 'new UiSelector().className("android.widget.Button").instance(8)'
    btn_adjunta_comp_domicilio_frontal = 'new UiSelector().className("android.widget.Button").instance(9)'
    btn_adjunta_comp_domicilio_reverso = 'new UiSelector().className("android.widget.Button").instance(10)'
    btn_adjunta_ine_frontal = 'new UiSelector().className("android.widget.Button").instance(11)'
    btn_adjunta_ine_reverso = 'new UiSelector().className("android.widget.Button").instance(10)'
    
    # btn_adjunta_adicional = 'new UiSelector().className("android.widget.Button").instance(11)'
      
    
    btn_opt_almacenamiento = '//android.widget.Button[@content-desc="Almacenamiento"]'
    btn_opt_galeria = '//android.widget.Button[@content-desc="Galería"]'
    # btn_opt_imagen_google = 'UiSelector().resourceId("com.google.android.documentsui:id/icon_thumb").instance(1)'
    btn_opt_imagen_google = 'UiSelector().className("android.widget.LinearLayout").instance(13)'

    # btn_confirma_imagen_select = 'com.google.android.documentsui:id/action_menu_select'
    btn_confirma_imagen_select = 'UiSelector().resourceId("com.android.documentsui:id/action_menu_select")'
        
    select_opcion_camara = 'UiSelector().description("Cámara")'

class AccionCamara:
    btn_tomar_foto = '//android.widget.ImageView[@content-desc="Listo"]'


class SCG:
    btn_crear_solicitud_grupal = 'UiSelector().description("Crear Solicitud Grupal")'
    casa_reunion = 'new UiSelector().description("Seleccione una opción")'
    
    
    direccion='UiSelector().className("android.view.View").instance(11)'
    dia='new UiSelector().description("Elegir Día")'
    dia_viernes = 'UiSelector().description("Viernes")'
    hora_reunion=''
    # Roles grupo
    lider = 'new UiSelector().description("Seleccionar Líder")'
    
    tesorera = 'new UiSelector().description("Seleccionar Tesorera")'
    #Montos
    monto_solicitado_uno = ''
    monto_solicitado_dos = ''
    monto_solicitado_tres = ''
    monto_solicitado_cuatro = ''
    monto_solicitado_cinco = ''
    btn_enviar_pre_autorizacion = 'UiSelector().description("Enviar a pre-autorización")'
    btn_enviar_a_mc = 'UiSelector().description("Enviar a MC")'

class Cruzadas:
    btn_valida_cruzadas = 'UiSelector().description("Validar solicitudes")'



class Renovaciones:
    btn_menu_filtro = 'new UiSelector().className("android.widget.Button").instance(2)'
    
    abrir_opciones_filtro_estatus = 'new UiSelector().description("Estatus")'
    quitar_check_filtro = 'new UiSelector().description("Sin buró")'
   
    aplicar_filtro_estatus = 'new UiSelector().description("Filtro")'
    buscador_grupo_renovacion = 'new UiSelector().className("android.widget.EditText")'
    primer_grupo_encontrado = 'android.widget.ImageView'

    #Inicio de renovacion
    tap_historial_credito = 'new UiSelector().className("android.widget.Button").instance(5)'
    btn_iniciar_renovacion = 'new UiSelector().description("Iniciar renovación")'
    msj_renovacion_iniciada = 'new UiSelector().description("No puedes iniciar la renovación")'

    check_acciones_renovacion = 'new UiSelector().className("android.widget.CheckBox")'
    btn_aceptar_incio_renovacion = 'new UiSelector().description("Actualizar")'
    car_mas_opciones6 = 'new UiSelector().className("android.widget.Button").instance(6)'
    car_mas_opciones7 = 'new UiSelector().className("android.widget.Button").instance(7)'
    car_mas_opciones8 = 'new UiSelector().className("android.widget.Button").instance(8)'
    actualizar_sci_renovacion = 'new UiSelector().description("Actualizar SCI")'

class NavegadorFireFox:
    btn_continuar_con_google = 'UiSelector().text("Google Logo Continuar con Google")'
    btn_asociar_con_google = 'UiSelector().text("Continue with Google")'

    lbl_cuenta_de_correo = 'UiSelector().resourceId("identifierId")'
    btn_siguiente_login = 'UiSelector().text("Siguiente")'
    lbl_pass = 'UiSelector().className("android.widget.EditText")'

    btn_menu_hamburgesa = 'UiSelector().className("android.widget.Image").instance(0)'
    btn_menu_operativa = 'UiSelector().text("Operativa")'
    lbl_filtrar_grupos = 'UiSelector().className("android.widget.EditText")'
    btn_select_grupo = 'UiSelector().className("android.view.View").instance(13)'


    # Scroll orizontal
    tap_info_grupo = 'UiSelector().text("INFO GRUPO")'
    tap_incidencias = 'UiSelector().text("INCIDENCIAS")'
    tap_info_credeito = 'UiSelector().text("INFO CRÉDITO")'    
    select_producto = 'UiSelector().resourceId("selector")'
    select_tipo_producto = 'UiSelector().text("interes_mixto_insoluto_cep")'    

    """Detalle desembolso"""
    #Canal de desembolso
    canal_desembolso = 'UiSelector().resourceId("selector").instance(3)'
    canal_select_desembolso = 'UiSelector().text("BBVA")'

    # Fecha desembolso
    fecha_tentativa_desembolso = 'UiSelector().resourceId("fechaDesembolso")'
    acepto_fecha_tentativa_desembolso = 'UiSelector().text("ACEPTAR")'
    btn_obtener_ubicacion = 'UiSelector().text("Obtener ubicación actual")'