Feature: Realizar la captura manual de un prospecto referido y posteriormente hacer la Cancelacion de solicitud

  Background:
    Given el usuario está en la pantalla principal

  # @mis-grupos-crea-grupo @skip
  # Scenario Outline: Genera el grupo nuevo
  #   When Selecciona la opcion: Consulta grupal
  #   Then Genera un nuevo grupo con el nombre: "<nombre_grupo>"
  #   Then Volver al inicio

    # Examples:
    #   | nombre_grupo |
    #   | NOPALERAS CON VINAGRE |
      
    # Then Genera CSG
    # Then Seleccionar casa de reunion 
    # Then Direccion de la reunion
    # Then Dia de la reunion
    # Then Horario de la reunion
    # Then La tesorera sera:

  


    # Then Agregar integrante dando clic en icono mas
    # Then Seleccionar btn prospecto existente
    # Then Buscar prospecta: "<prospecto>" y agregar al grupo
    # Then Seleccionar al prospecto del listado de la busqueda generada
    # Then el mensaje de confirmación es visible
    # Then Volver al inicio

  # @mis-grupos-validaciones-cruzadas 
  # Scenario Outline: Validaciones cruzadas
  #   When Selecciona la opcion: Mis grupos
  #   Then Genera un nuevo grupo con el nombre: "<nombre_grupo>"
  #   Then Volver al inicio


  @mis-grupos-devolucion-digitalizacion
  Scenario Outline: Devolucion digitalizacion
    When selecciono la opcion de mis grupos
    Then Hacer clic tap Devoluciones
    Then Buscar grupo devuelto: "<nombre_grupo>"
    Then Validar que se envio al mc seccion de mis grupos
    # Then Volver al inicio

