
Genera Consultas
    ENV=stg behave --tags=@consulta_rapida_basica features/consulta_rapida.feature
    ENV=stg behave --tags=@consulta_rapida_basica_completa features/consulta_rapida.feature
Realiza la SCI
    ENV=stg behave --tags=@buscar-usuarios-y-registrar-sci features/buscar_usuario_reg_sci.feature
Adjunta documentos SCI
    ENV=stg behave --tags=@buscar-usuarios-adjuntar-doc features/buscar_usuario_adjuntar_doc.feature


Coloca nombre a nuevo grupo
    ENV=stg behave --tags=@mis-grupos-crea-grupo features/mis_grupos.feature
Formaliza un grupo
    ENV=stg behave --tags=@formalizar-grupo features/formalizar_grupo.feature



Genera nuevo grupo y formaliza
    ENV=stg behave --tags=@mis-grupos-crea-grupo-y-formaliza features/mis_grupos.feature




ENV=stg behave --tags=@mis-grupos-crea-solicitud-grupal features/mis_grupos.feature


# Escenario de flujo 
1.- Consulta rapida
2.- Genero grupo
3.- Ingreso prospecta de Consulta rapida
4.- Agrego prospecta de OCR
5.- Agrego prospecta inactiva
6.- Prospecta Asignada
	(Prospecta previamente asignada)
7.- Formalizar grupo
8.- Cruzadas
9.- Genera grupal y envia a MC