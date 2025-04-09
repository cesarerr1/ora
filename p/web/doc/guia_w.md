behave --tags=@cap-valida-curp-cr features/ConsultaRapida/captura_manual.feature



(Luc) 


01 Digitalizacion - Analista
    behave --tags=@valida-grupo-digitalizacion features/Digitalizacion/buscar_grupo_digitalizacion.feature


02 Operativa - consejero
    behave --tags=@operativa features/Operativa/buscar_grupo_devolucion_op.feature
 

03 Autorizacion - Analista
    behave --tags=@aprobar-grupo-mambu features/Autorizacion/autorizacion.feature



 behave --tags=@devolucion-grupo features/Operativa/buscar_grupo_devolucion_op.feature

Asignar grupo
 behave --tags=@asignar-grupo features/Asignacion/buscar_grupo_asignacion.feature




 behave --tags=@califica-cdc features/Renovacion/renovacione.feature




Calificas CDC
 behave --tags=@califica-cdc features/Renovacion/renovacion.feature




behave --tags=@valida-grupo-digitalizacion features/Digitalizacion/buscar_grupo_digitalizacion.feature
