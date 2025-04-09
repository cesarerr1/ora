# language: es

Característica: Buscar un grupo para realizar la autorizacion

  Antecedentes:
    Dado Que estoy en Podemos

  @aprobar-grupo-mambu
  Esquema del escenario: Realiza la busqueda de un grupo y enviar a mambu
    Cuando Inicio sesion analista
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Busqueda del grupo: "<grupo>"
    Entonces Ingresa al grupo para autorizar
    Entonces Aprobar grupo para mambu

    Ejemplos:
      | opcion_menu  | grupo          |
      | Autorizacion | ESTRELLAS_GUERRERAS_3359         |
      




    # Entonces hacer la devolucion con el motivo: "<motivo>" y justificacion: "<justificacion>"
    # Entonces Seleccionar grupo para devolver
    # Entonces Seleccionar grupo para autorizar
    # Entonces Btn Valida el grupo
    # Entonces Confirmo accion de validacion del grupo
    # Cuando Inicio sesion consejero


      # |motivo| justificacion|
      # |CAMBIO EN MONTOS| texto de prueba de la justificacion|