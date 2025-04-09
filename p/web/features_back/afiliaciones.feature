# language: es

@Afiliaciones
Característica: Afiliaciones

@agregarAfiliamiento
    Esquema del escenario: Agregar nueva afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar afiliamiento
        Y edito los campos correspondientes "<afiliacion>" "<suscripcion>" "<monto>" "<divisa>" "<inicioAfiliacion>" "<finalAfiliacion>"
        Y guardo los cambios

        Ejemplos:
            | afiliacion | suscripcion | monto | divisa       |   inicioAfiliacion    |   finalAfiliacion |
            | CIMA       | Individual  | 1000  | Mexican Peso |   2024-05-15          |   2024-10-25      |

@editarAfiliamiento
    Esquema del escenario: Editar afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar afiliamiento
        Y edito los campos correspondientes "<afiliacion>" "<suscripcion>" "<monto>" "<divisa>" "<inicioAfiliacion>" "<finalAfiliacion>"
        Y guardo los cambios

        Ejemplos:
            | afiliacion | suscripcion | monto | divisa       |   inicioAfiliacion    |   finalAfiliacion |
            | ACCA       | Company     | 5000  | Mexican Peso |   2024-01-01          |   2024-12-24      |

@eliminarAfiliacion
    Escenario: Eliminar afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono borrar afiliacion

@subirArchivoAfiliacion
    Esquema del escenario: Subir archivo de afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono agregar un nuevo archivo "<archivo>"

        Ejemplos:
            |     archivo     |
            |  Bluetooth.png  |
        
@descargarArchivoAdjunto
    Escenario: Descargar archivo de afiliación
        Entonces hago clic en My Info
        Y hago clic en Memberships
        Y selecciono descargar un archivo adjunto
