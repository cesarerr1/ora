
# # ejecutar_feature(archivo_feature)
# ejecutar_feature('--tags=@cap-varios-prospectos','features/ConsultaRapida/captura_manual.feature')
         

from behave.__main__ import main as behave_main

# Función para ejecutar un archivo .feature usando la API de Behave
def ejecutar_feature(tag, archivo_feature):
    try:
        # Se ejecuta el archivo .feature usando la API de Behave
        behave_main([tag,archivo_feature])
    except Exception as e:
        print(f"Error al ejecutar {archivo_feature}: {e}")

# Submenú para la opción 1
def submenu_opcion_1():
    while True:
        print("\nSubmenú - Opción 1: Consulta Rapida")
        print("1. CRM correcta")
        print("2. CRM y Cancelar")
        print("3. Validar Usuarios rechazados")
        print("0. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-99): "))
            
            if opcion == 1:
                print("\nEjecutando 'Consulta Rapida Manual'...\n")
                ejecutar_feature('--tags=@cap-varios-prospectos','features/ConsultaRapida/captura_manual.feature')
            elif opcion == 2:
                print("\nEjecutando 'Consulta Rapida Manual y Cancelar'...\n")
                ejecutar_feature('--tags=@cap-manual-cancelar','features/ConsultaRapida/captura_manual.feature')
                #  
            elif opcion == 3:
                print("\nEjecutando 'Consulta Rapida Manual y Cancelar'...\n")
                ejecutar_feature('--tags=@cap-varios-prospectos','features/ConsultaRapida/captura_manual_usuario_registrado.feature')
                #  cr@cr:~/Documentos/Podemos/Proyectos/Spore$ behave --tags=@cap-varios-prospectos features/ConsultaRapida/captura_manual_usuario_registrado.feature
            elif opcion == 0:
                print("\nVolviendo al menú principal...\n")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

# Submenú para la opción 2
def submenu_opcion_2():
    while True:
        print("\nSubmenú - Opción 2: SCI")
        print("1. Ejecutando 'Registro SCI Completa...")
        print("2. Mostrar nombre del archivo")
        print("3. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-3): "))
            
            if opcion == 1:
                print("\nEjecutando 'Registro SCI Completa'...\n")
                ejecutar_feature('--tags=@buscar-usuarios-y-registrar-sci','features/buscar_usuario_reg_sci.feature')
                
            elif opcion == 2:
                print("\nNombre del archivo: 'feature2.feature'")
            elif opcion == 3:
                print("\nVolviendo al menú principal...\n")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

# Submenú para la opción 3
def submenu_opcion_3():
    while True:
        print("\nSubmenú - Opción 3: features/feature3.feature")
        print("1. Ejecutar este archivo")
        print("2. Mostrar el contenido del archivo (simulado)")
        print("3. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-3): "))
            
            if opcion == 1:
                print("\nEjecutando 'features/feature3.feature'...\n")
                ejecutar_feature('features/feature3.feature')
            elif opcion == 2:
                print("\nSimulando el contenido del archivo 'features/feature3.feature'")
                print("[Feature: Login]\nScenario: User logs in successfully...")
            elif opcion == 3:
                print("\nVolviendo al menú principal...\n")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

def submenu_opcion_4():
    while True:
        print("\nSubmenú - Opción 4: features/feature3.feature")
        print("1. Ejecutar completo CR SCI Adjuntos")
        print("2. Mostrar el contenido del archivo (simulado)")
        print("3. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-3): "))
            
            if opcion == 1:
                print("\nEjecutando 'Consulta Rapida Manual'...\n")
                ejecutar_feature('--tags=@cap-varios-prospectos','features/ConsultaRapida/captura_manual.feature')
                print("\nEjecutando 'SCI'...\n")
                ejecutar_feature('--tags=@buscar-usuarios-y-registrar-sci','features/buscar_usuario_reg_sci.feature')
                print("\nEjecutando 'Adjuntos SCI'...\n")
                ejecutar_feature('-tags=@buscar-usuarios-adjuntar-doc','features/buscar_usuario_adjuntar_doc.feature')
            elif opcion == 2:
                print("\nSimulando el contenido del archivo 'features/feature3.feature'")
                print("[Feature: Login]\nScenario: User logs in successfully...")
            elif opcion == 3:
                print("\nVolviendo al menú principal...\n")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")
def submenu_opcion_5():
    while True:
        print("\nSubmenú - Opción 5: Operativa")
        print("1. Ejecutar Operativa")
        print("2. Mostrar el contenido del archivo (simulado)")
        print("0. Volver al menú principal")
        
        try:
            opcion = int(input("\nSeleccione una opción (1-99): "))
            
            if opcion == 1:
                print("\nEjecutando 'Operativa'...\n")
                ejecutar_feature('--tags=@consejero','features/Consejero/consejero.feature')
            elif opcion == 2:
                print("\nSimulando el contenido del archivo 'features/feature3.feature'")
                print("[Feature: Login]\nScenario: User logs in successfully...")
            elif opcion == 0:
                print("\nVolviendo al menú principal...\n")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")



# Función para mostrar el menú principal
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Consulta Rapida Manual")
    print("2. Seleccionar y ejecutar 'features/feature2.feature'")
    print("3. Seleccionar y ejecutar 'features/feature3.feature'")
    print("4. Completos")
    print("5. Consejero")
    print("0. Salir")

# Función principal
def main():
    while True:
        mostrar_menu()

        try:
            seleccion = int(input("\nSeleccione una opción (1-4): "))

            if seleccion == 1:
                submenu_opcion_1()
            elif seleccion == 2:
                submenu_opcion_2()
            elif seleccion == 3:
                submenu_opcion_3()
            elif seleccion == 4:
                submenu_opcion_4()
            elif seleccion == 5:
                submenu_opcion_5()
            elif seleccion == 0:
                print("Saliendo...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")

if __name__ == "__main__":
    main()
