Feature: Adjunta los documento basicos de la integrante
    Como un usuario
    Quiero agregar los documentos de un prospecto
    Para finalizar el registro de forma satisfecha

  Background:
    Given el usuario está en la pantalla principal

  @buscar-usuarios-adjuntar-doc-basica
  Scenario Outline: Agregar los documentos del prospecto
    When buscar a: "<prospecto>"
    Then seleccionar al usuario del listado de la busqueda realizada
    Then seleccionar solicitud individual
    Then seleccionar btn documentos
    
    # # Then selecciona btn para adjuntar foto
    # # Then selecciona btn cargar
    # # Then seleccionar opcion almacenamiento
    # # Then selecciona y confirma imagen de google imagenes

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
    #     # Then seleccionar opcion de camara
    #     # Then regresa al inicio

    # Examples:
    #   | prospecto  |
    #   # | ARMITA    |
    #   | BEBA      |
    #   | CAMILA    |


    # | DOROTEA    |
    # | EVELARDA   |
    # | FREMIDA    |
    # | GUSABIA    |
    # | HILARIA    |
    # | INDONECIA  |
    # | JEREMIOS   |
    # | KAZAMIA    |
    # | LORETANA   |
    # | MONIQUILLA |
    # | NIONDIDA   |
    # | OPOLINA    |
    # | PULPANA    |
    # | QUESADIRIA |
    # | RAMONA     |
    # | SAMILA     |
    # | TRIGULA    |
    # | ULARIA     |
    # | VIVIANA    |
    # | XINA       |
    # | YADIRA     |
