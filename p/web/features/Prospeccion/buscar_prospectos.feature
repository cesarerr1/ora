# language: es
@login
Característica: Iniciar sesión

  Antecedentes:
    Dado Que estoy en Podemos
    Cuando Inicio sesion1
    Entonces Ingresar al menu Prospeccion
    Entonces Ingresar a la opcion Prospeccion

  @loginValido
  Esquema del escenario: Realiza la busqueda de un prospecto
    Entonces Realizar la busqueda del prospecto: "<prospecto>"
    Entonces Editamos el num de telefono: "<num_celular>"
    Entonces Tap Adjuntos
    Entonces Realizar la descarga de: SCI
    Entonces Tap comentarios
    Entonces Agrego el comentario: "<comentario>"
    # Entonces Realizar la busqueda del grupo prospection

    Ejemplos:
      | prospecto | num_celular | comentario                                             |
      | Aren      |  5525194378 | Este es un comentario desde el poder de automatizacion |
      # | juana |  5525194378 | Este es un comentario desde el poder de automatizacion |
