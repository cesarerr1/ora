# language: es
@login
Característica: Buscar a un grupo y realizar la operativa

  Antecedentes:
    Dado Que estoy en Podemos

  @operativa
  Esquema del escenario: Buscar a un grupo y realizar la operativa
    # Cuando Inicio sesion analista
    Cuando Inicio sesion consejero
    Entonces Ingresar al menu: "<opcion_menu>"
    Entonces Busqueda del grupo: "<grupo>"
    Entonces ingresa al grupo
    Entonces moverme a la tap "<tap>"
    Entonces Validar ubicacion
    Entonces ir hasta el fonal de la pagina
    # Entonces Ir al final
    Entonces Aprobar

    # Entonces Seleccionar grupo para devolver
    # Entonces Seleccionar grupo para autorizar
    # Entonces Btn Valida el grupo
    # Entonces Confirmo accion de validacion del grupo
    # Cuando Inicio sesion consejero

    Ejemplos:
      | opcion_menu | grupo               | tap          |
      | Operativa   | ESTRELLAS_GUERRERAS_3359   | INFO CRÉDITO |

# REINAS
# PRINCESAS DEL MAR
# REINAS DE LUNA
# G_MUJERCITAS_002
