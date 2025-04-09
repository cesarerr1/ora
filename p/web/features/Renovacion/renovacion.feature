# language: es
@login
Característica: Iniciar sesión

  Antecedentes:
    Dado Que estoy en Podemos
    Cuando Inicio sesion analista

  @califica-cdc
  Esquema del escenario: Realizar la busqueda y clonacion de un grupo
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Realizar la busqueda del grupo de operativa: "<id_grupo>"
    Entonces Cambiarme al tap: "<tap>"
    # Entonces Selecciono el nivel de riesgo: "<nivel_riesgo>"

    Ejemplos:
      | opcion_menu | id_grupo      |tap    |
      | Renovacion  | 24G07534	    |CDC      | 
