# Feature: Buscar un grupo formalizado y crear solicitud grupal
#     Como usuario 
#     Quiero crear la solicitud grupal 
#     Para realizar la peticion de desembolso

#   Background:
#     Given Valida que existan los elementos y que puedas hacer tap

#   @buscar-grupo-y-crear-solicitud-grupalusuarios-y-registrar-sci
#   Scenario Outline: Buscar usuario y registrar sci
#     When buscar a: "<usuario>"
#     Then selecciono al usuario "2" del listado busqueda realizada
#         # Then seleccionar opcion para continuar con capttura de datos sci
#     Then seleccionar btn continuar solicitud
#     # Then seleccionar btn emergentecontinuar solicitud Individual
#     Then comienzo con la captura de datos complementarios "<tel_recados>" "<estado_civil_soltera>" "<escolaridad_secundaria>" "<correo>"
#     Then captura datos domicilio antiguedad
#     Then acreditacion del domicilio INE:"<ine>" parentesco:"<parentesco>"
#     Then captura de datos familiar "<nombre_familiar>" "<tel_familiar>" "<caracteristicas_vivienda>" "<referencia_ubicacion>"
#     Then captura datos actividad economica "<direccion_del_negocio>" "<ganancia_semanal>" "<otros_ingresos>" "<monto_pago_semanal>"
#     Then captura datos referencia uno "<nombre_referencia>" "<tel_referencia_recardos>" "<tel_referencia_celular>"
#     Then captura datos referencia dos "<nombre_referencia2>" "<tel_referencia_recardos2>" "<tel_referencia_celular2>"
#     Then captura datos crediticios "<monto>" "<origen_recursos>" "<destino_recursos>"
#     Then Volver al inicio con scroll

#     Examples:
#       | usuario  | tel_recados | estado_civil_soltera | escolaridad_secundaria | correo                  | ine | parentesco | nombre_familiar | tel_familiar | caracteristicas_vivienda | referencia_ubicacion | direccion_del_negocio | ganancia_semanal | otros_ingresos | monto_pago_semanal | nombre_referencia | tel_referencia_recardos | tel_referencia_celular | nombre_referencia2 | tel_referencia_recardos2 | tel_referencia_celular2 | monto | origen_recursos  | destino_recursos                |
#       | carlos   |  5525065059 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886354 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Paciencia         |              5525825363 |             5521414254 | sajyla             |               5529195454 |              5522112554 |  6000 | negocio familiar | crecimiento de negocio familiar |
#       | caprio   |  5525065060 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886355 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Panfila           |              5525825364 |             5521414255 | sajyla             |               5529195455 |              5522112555 |  6000 | negocio familiar | crecimiento de negocio familiar |
#       | carlota  |  5525065061 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886356 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Palestina         |              5525825365 |             5521414256 | sajyla             |               5529195456 |              5522112556 |  6000 | negocio familiar | crecimiento de negocio familiar |
#       | cazandra |  5525065062 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886357 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Pancracia         |              5525825366 |             5521414257 | sajyla             |               5529195457 |              5522112557 |  6000 | negocio familiar | crecimiento de negocio familiar |
#       | camila   |  5525065063 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886358 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Patria            |              5525825367 |             5521414258 | sajyla             |               5529195458 |              5522112558 |  6000 | negocio familiar | crecimiento de negocio familiar |
#       | caren    |  5525065064 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886359 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Pacifica          |              5525825368 |             5521414259 | sajyla             |               5529195459 |              5522112559 |  6000 | negocio familiar | crecimiento de negocio familiar |

Feature: Buscar una prospecta y crear solicitud grupal
    Como usuario 
    Quiero crear la solicitud grupal 
    Para realizar poder integrar al grupo y formalizar

  Background:
    Given el usuario está en la pantalla principal
    When buscar a: "<usuario>"

    @buscar-grupo-y-crear-solicitud-grupalusuarios-y-registrar-sci
    Scenario Outline: Buscar usuario y registrar sci
#     When buscar a: "<usuario>"
#     Then selecciono al usuario "2" del listado busqueda realizada
#         # Then seleccionar opcion para continuar con capttura de datos sci
#     Then seleccionar btn continuar solicitud
#     # Then seleccionar btn emergentecontinuar solicitud Individual
#     Then comienzo con la captura de datos complementarios "<tel_recados>" "<estado_civil_soltera>" "<escolaridad_secundaria>" "<correo>"
#     Then captura datos domicilio antiguedad
#     Then acreditacion del domicilio INE:"<ine>" parentesco:"<parentesco>"
#     Then captura de datos familiar "<nombre_familiar>" "<tel_familiar>" "<caracteristicas_vivienda>" "<referencia_ubicacion>"
#     Then captura datos actividad economica "<direccion_del_negocio>" "<ganancia_semanal>" "<otros_ingresos>" "<monto_pago_semanal>"
#     Then captura datos referencia uno "<nombre_referencia>" "<tel_referencia_recardos>" "<tel_referencia_celular>"
#     Then captura datos referencia dos "<nombre_referencia2>" "<tel_referencia_recardos2>" "<tel_referencia_celular2>"
#     Then captura datos crediticios "<monto>" "<origen_recursos>" "<destino_recursos>"
#     Then Volver al inicio con scroll

      Examples:
        | usuario  | tel_recados | estado_civil_soltera | escolaridad_secundaria | correo                  | ine | parentesco | nombre_familiar | tel_familiar | caracteristicas_vivienda | referencia_ubicacion | direccion_del_negocio | ganancia_semanal | otros_ingresos | monto_pago_semanal | nombre_referencia | tel_referencia_recardos | tel_referencia_celular | nombre_referencia2 | tel_referencia_recardos2 | tel_referencia_celular2 | monto | origen_recursos  | destino_recursos                |
        | Ana   |  5525065059 | soltera              | secundaria             | c.rojaspde5@podemos.com | si  | Propio     | constancia      |   5529886354 | fachada piedra volcanica | frente a parque      | san jose              |             4000 |           2500 |               1500 | Paciencia         |              5525825363 |             5521414254 | sajyla             |               5529195454 |              5522112554 |  6000 | negocio familiar | crecimiento de negocio familiar |