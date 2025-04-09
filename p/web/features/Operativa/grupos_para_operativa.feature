# language: es
@login
Característica: Iniciar sesión

  Antecedentes:
    Dado Que estoy en Podemos
    Cuando Inicio sesion1
    Entonces Ingresar al menu Operativa

  @loginValido
  Esquema del escenario: Realiza la busqueda de un prospecto
    Entonces Realizar la busqueda del grupo de operativa: "<id_grupo>"


    Ejemplos:
      | id_grupo |
      | 24G00238 |

