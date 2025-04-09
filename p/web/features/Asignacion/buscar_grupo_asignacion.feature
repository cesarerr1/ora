# language: es

@login
Característica: Iniciar sesión

Antecedentes:
    Dado Que estoy en Podemos

  @asignar-grupo
  Esquema del escenario: Realiza la busqueda de un grupo de prospecto
    Cuando Inicio sesion analista
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Realizar la busqueda del grupo: "<grupo>" para asignar
    Entonces Btn asignar grupo
    # Entonces Confirmo accion de validacion del grupo
    # Cuando Inicio sesion consejero
    

    Ejemplos:
      | opcion_menu  | grupo    | 
      | Asignacion | VENGADORAS_DEL_BAL_N_4069 |
