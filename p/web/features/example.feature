# language: es

@login
Característica: Iniciar sesión

Antecedentes:
    Dado Que estoy en google

  @loginValido
  Esquema del escenario: Buscar en google
    Cuando Inicio sesion
    Entonces Ingresar al menu Digitalizacion
    Cuando Realizar la busqueda del grupo
    # Entonces Taps en grupo
    # Entonces Tap Adjuntos
    # Cuando Descargar archivo
    # Cuando Realizo la busqueda de un integrante 

    # Cuando edito los datos personales de un integrante
    # Cuando Ingreso "<busqueda>"
    # Y Hago click en buscar
    # Entonces Se muestran los resultados
    # Entonces cierro el navegador

    Ejemplos:
      | busqueda      |
      | wsl           |
