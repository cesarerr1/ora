@feature=Consulta_rapida
Feature: Prueba de Consulta rapida
  Como usuario, quiero realizar una consulta rapida.
  Para validar el flujo de consulta y CDC.

  @consulta_rapida_basica
  Scenario Outline: Realizar consulta rápida basica hasta el CDC
  # Scenario Outline: Hacer clic en el botón de Consulta Grupal
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    Then opcion de captura de datos manual
    Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"
    Then Confirmar datos para enviar NIP
    Then Acepta TYC
    Then Respuesta de OTP
    Then Realiza la consulta de CDC 
    Then Volver al inicio
    Then Validar que el prospecto se encuentra en la lista de consultas: "<prospecto>" "<ap_paterno>" "<ap_materno>"
    Then Volver al inicio 
    
     
  @consulta_rapida_basica_completa
  Scenario Outline: Consulta rápida completa de una prospecta
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    Then opcion de captura de datos manual
    Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"
    Then Confirmar datos para enviar NIP
    Then Acepta TYC
    Then Respuesta de OTP
    Then Realiza la consulta de CDC
    Then Volver al inicio
    # Then Validar que el prospecto se encuentra en la lista de consultas: "<prospecto>" "<ap_paterno>" "<ap_materno>"
    # Then Volver al inicio 

    When buscar a: "<prospecto>"
    Then seleccionar al usuario del listado de la busqueda realizada
    Then seleccionar solicitud individual
    Then comienzo con la captura de datos complementarios de la prospecta "<estado_civil_soltera>" "<escolaridad>"
    Then captura datos domicilio antiguedad
    Then acreditacion del domicilio INE:"<ine>" parentesco:"<parentesco>"
    Then captura de datos familiar "<nombre_familiar>" "<tel_familiar>" "<caracteristicas_vivienda>" "<referencia_ubicacion>"
    Then captura datos actividad economica "<direccion_del_negocio>" "<ganancia_semanal>" "<otros_ingresos>" "<monto_pago_semanal>"
    Then captura datos referencia uno "<nombre_referencia>" "<tel_referencia_celular>"
    Then captura datos referencia dos "<nombre_referencia2>" "<tel_referencia_celular2>"
    Then captura datos crediticios "<monto_credito>" "<origen_recursos_credito>" "<destino_recursos_credito>"
    
    Then seleccionar btn documentos
    Then selecciona btn para adjuntar comprobante frontal
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    # Then selecciona btn para adjuntar comprobante reverso
    # Then seleccionar solicitud individual
    # Then seleccionar opcion almacenamiento
    # Then selecciona y confirma imagen de google imagenes
    Then selecciona btn para adjuntar ine frontal
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    Then selecciona btn para adjuntar ine reverso
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    Then finalizar registro






  @consulta_rapida_y_grupo_mixto_completa
  Scenario Outline: Consulta rápida completa de una prospecta
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    Then opcion de captura de datos manual
    Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"
    Then Confirmar datos para enviar NIP
    Then Acepta TYC
    Then Respuesta de OTP
    Then Realiza la consulta de CDC
    Then Volver al inicio

    When buscar a: "<prospecto>"
    Then seleccionar al usuario del listado de la busqueda realizada
    Then seleccionar solicitud individual
    Then comienzo con la captura de datos complementarios de la prospecta "<estado_civil_soltera>" "<escolaridad>"
    Then captura datos domicilio antiguedad
    Then acreditacion del domicilio INE:"<ine>" parentesco:"<parentesco>"
    Then captura de datos familiar "<nombre_familiar>" "<tel_familiar>" "<caracteristicas_vivienda>" "<referencia_ubicacion>"
    Then captura datos actividad economica "<direccion_del_negocio>" "<ganancia_semanal>" "<otros_ingresos>" "<monto_pago_semanal>"
    Then captura datos referencia uno "<nombre_referencia>" "<tel_referencia_celular>"
    Then captura datos referencia dos "<nombre_referencia2>" "<tel_referencia_celular2>"
    Then captura datos crediticios "<monto_credito>" "<origen_recursos_credito>" "<destino_recursos_credito>"
    
    Then seleccionar btn documentos
    Then selecciona btn para adjuntar comprobante frontal
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    # Then selecciona btn para adjuntar comprobante reverso
    # Then seleccionar solicitud individual
    # Then seleccionar opcion almacenamiento
    # Then selecciona y confirma imagen de google imagenes
    Then selecciona btn para adjuntar ine frontal
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    Then selecciona btn para adjuntar ine reverso
    Then seleccionar solicitud individual
    Then seleccionar opcion almacenamiento
    Then selecciona y confirma imagen de google imagenes
    Then finalizar registro


  @consulta_rapida_ocr @story=Login_exitoso @critical
  Scenario Outline: Consulta rápida desde OCR
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    # Then opcion de captura de datos manual
    Then opcion de captura de datos desde OCR

    # Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    # Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    # Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"




  
  @consulta_rapida_lista_negra
  Scenario Outline: Realizar consulta rápida lista negra
  # Scenario Outline: Hacer clic en el botón de Consulta Grupal
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    Then opcion de captura de datos manual
    Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    Then Validar curp lista negra
    # Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"
    # Then Confirmar datos para enviar NIP
    # Then Acepta TYC
    # Then Respuesta de OTP
    # Then Realiza la consulta de CDC 
    # Then Volver al inicio
    # Then Validar que el prospecto se encuentra en la lista de consultas: "<prospecto>" "<ap_paterno>" "<ap_materno>"
    Then Volver al inicio


      @consulta_rapida_basica
  Scenario Outline: Realizar consulta rápida basica y cancelar
  # Scenario Outline: Hacer clic en el botón de Consulta Grupal
    Given el usuario está en la pantalla principal
    When el usuario hace clic en Consulta Rapida
    Then opcion de captura de datos manual
    Then Ingresar datos de la emprendedora: "<prospecto>" "<ap_paterno>" "<ap_materno>" "<curp>" "<lugar_nacimiento>"
    Then Ingresar numero de telefono: "<telefono>" y su confirmación: "<confirmacion>"
    Then Ingresar direccion CP: "<cp>" calle: "<calle>" "<num_ext>"
    Then Confirmar datos para enviar NIP
    Then Acepta TYC
    Then Respuesta de OTP
    # Then Realiza la consulta de CDC 
    # Then Volver al inicio
    # Then Validar que el prospecto se encuentra en la lista de consultas: "<prospecto>" "<ap_paterno>" "<ap_materno>"
    Then Volver al inicio 
    Then Validar emprendedora como rechazada