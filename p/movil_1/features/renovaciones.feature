Feature: Realizar la renovacion de un grupo

  Background:
    Given el usuario está en la pantalla principal

 
  @renovacion-de-grupo
  Scenario Outline: Realizando la renovacion de un grupo
    When selecciono la opcion: renovaciones
    Then Filtrar estatus por: renovar
    Then Buscar grupo: "<nombre_grupo>"
    # Then Validar que se envio al mc seccion de mis grupos
    # Then Volver al inicio

