# language: es

@login
Característica: Iniciar sesión

Antecedentes:
    Dado Que estoy en Podemos

  @loginValido
  Esquema del escenario: Realiza la busqueda de un prospecto
    Cuando Inicio sesion1
    Entonces Ingresar al menu Prospection
    Entonces Realizar la busqueda del grupo prospectos
    Entonces Tap comentarios

    # Entonces Realizar la busqueda del grupo prospection
    

    Ejemplos:
      | busqueda      |
      | wsl           |
