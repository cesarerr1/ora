# language: es
@dependientes
Característica: Dependientes

  Antecedentes:
    Dado hago clic en My Info
    Y hago clic en Dependents

  @agregar_dependientes
  Esquema del escenario: Agregar dependientes
    Cuando doy clic en agregar dependiente
    Y ingreso el nombre "<nombre>" del dependiente
    Y ingreso la relación "<relacion>" con el dependiente
    Y especifico la relación "<relacion_especifica>" con el dependiente
    Y ingreso la fecha de nacimiento "<fecha_nacimiento>" del dependiente
    Y hago clic en guardar dependiente
    Entonces se muestra el mensaje de confirmación de agregar dependiente

    Ejemplos:
      | nombre | relacion | relacion_especifica | fecha_nacimiento |
      | Maria | Other | Wife | 2000-01-01 |
      | Juan | Child | --- | 2020-01-01 |



