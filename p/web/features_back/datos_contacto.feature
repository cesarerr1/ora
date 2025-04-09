# language: es
@datos_contacto
Característica: Datos de contacto

  Antecedentes:
    Dado hago clic en My Info
    Y hago clic en Contact Details

  @editar_datos_contacto
  Escenario: Editar datos de contacto
    Cuando ingreso la calle "Calle1" y la ciudad "Ciudad1"
    Y ingreso el estado "Estado 1", codigo postal "11111" y pais "Mexico"
    Y ingreso el telefono de casa "11111111111", el movil "2222222222" y el de trabajo "3333333333"
    Y ingreso el correo "admin@example.com"
    Y hago clic en guardar
    Entonces se muestra el mensaje de confirmación de datos de contacto

