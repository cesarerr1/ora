# language: es
Característica: Buscar a un grupo y realizar la digitalizacion

  Antecedentes:
    Dado Que estoy en Podemos

  @valida-grupo-digitalizacion
  Esquema del escenario: Buscar a un grupo y realizar la digitalizacion
    Cuando Inicio sesion analista
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Ingresar al sub-menu: "<opcion_sub_menu>"
    Entonces Realizar la busqueda del grupo: "<grupo>"
    # Entonces Busqueda del grupo: "<grupo>"
    Entonces Btn Valida el grupo
    Entonces Confirmo accion de validacion del grupo
    # Cuando Inicio sesion consejero

    Ejemplos:
      | opcion_menu    | opcion_sub_menu | grupo             |
      | Digitalizacion | Grupos          | ESTRELLAS_GUERRERAS_3359   |
