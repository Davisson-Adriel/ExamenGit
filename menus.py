menu_principal ="""
---------------------- BIENVENIDO A PHOTOCAMPUS ----------------------
Seleccione la opcion que desea.
1. Registrar Paquete
2. Registrar Servicios
3. Editar Paquetes
4. Eliminar Paquetes
5. Salir
"""

def mostrar_menu_principal():
    print(menu_principal)


def ejecucion_menu_principal():
    while True:
        mostrar_menu_principal()
        opc = input("Ingrese la opcion que desea: ")
        if opc == "1":
            print("hola")
        elif opc == "2":
            print("")
        elif opc == "3":
            print("")
        elif opc == "4":
            print("")
        elif opc == "5":
            print("¡Hasta Luego! Saliendo...")
            break
        else:
            print("Lea Bien, Ingrese una opcion valida. ")
            
       