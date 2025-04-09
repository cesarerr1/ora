# language: es
@datos_personales
Característica: Datos personales

  Antecedentes:
    Dado hago clic en My Info
    Entonces se muestra la página "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7"

  @editar_datos_personales
  Escenario: Editar detalles personales exitosamnete
    Cuando ingreso el primer nombre "Maria", el segundo nombre "Jose" y el apellido "Landa"
    Y ingreso el id de empleado "11111" y otro id "22222"
    Y ingreso el número de licencia de conducir "12345" y la fecha de expiración de la licencia "2025-01-01"
    Y ingreso la nacionalidad "Mexican", el estado marital "Other", la fecha de nacimiento "2000-01-01" y el genero "Female"
    Y hago clic en guardar datos personales
    Entonces se muestra el mensaje de confirmación

