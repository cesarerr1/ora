# language: es

@login
Característica: Iniciar sesión

Antecedentes:
    Dado Que estoy en Podemos

  @mis-grupos-hacer-devolucion-digitalizacion
  Esquema del escenario: Buscar grupo y Devolucion digitalizacion
    Cuando Inicio sesion analista
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Ingresar al sub-menu: "<opcion_sub_menu>"
    Entonces Busqueda del grupo: "<grupo>"
    Entonces Seleccionar opcion para devolver el grupo
    Entonces Seleccionar motivo de devolucion
    Entonces Ingresar comentario de la devolucion: "<motivo_devolucion>"
    Entonces Aceptar la devolucion

    # Entonces Btn Valida el grupo
    # Entonces Confirmo accion de validacion del grupo
    # Cuando Inicio sesion consejero
    

    Ejemplos:
      |opcion_menu    | opcion_sub_menu |grupo     |   motivo_devolucion |
      |Digitalizacion | Grupos          |ESTRELLAS_GUERRERAS_3359  | Direccíon incorrecta|
