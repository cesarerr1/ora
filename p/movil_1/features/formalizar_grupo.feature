Feature: Formalizar Grupo
Como un usuario
Quiero formalizar a un grupo existente
Para poder continuar con la CSG

  Background:
    Given el usuario está en la pantalla principal
    When Selecciona la opcion: Consulta grupal

  
  @buscar-grupo-y-agrega-prospecta
  Scenario Outline: Buscar grupo y agregar prospecta
    Then clic agregar a un grupo existente
    Then buscar el grupo creado: "<nombre_grupo>"
    Then Utilizar grupo
    Then Agregar integrante dando clic en icono mas
    Then Seleccionar btn prospecto existente
    Then Buscar prospecta: "<prospecto>" y agregar al grupo
    Then Seleccionar al prospecto del listado de la busqueda generada
    Then el mensaje de confirmación es visible
    # Then Hacer clic en el btn formalizar grupo
    # Then Agrega al prospecto del resultado de la busqueda
    Then Volver al inicio


  @buscar-grupo-y-formaliza
  Scenario Outline: Buscar grupo y formalizar
    Then clic agregar a un grupo existente
    Then buscar el grupo creado: "<nombre_grupo>"
    Then Utilizar grupo
    
    Then Formalizar grupo
    Then Seleccionar el grupo del listado

