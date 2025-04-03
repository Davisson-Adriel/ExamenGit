paquetes={}
servicios={}

def agpaquete():
    
    while True:

        nom=input("Escriba el nombre del paquete: ")
        nom=nom.capitalize()
        eva=paquetes.get(nom,1)

        if eva!=1:
            break
        else:
            print("Paquete ya existente")
        
    while True:

        prec=input("Ingrese el precio del paquete: ")
        if prec.isdigit():
            break
        else:
            print("El dato ingresado no corresponde a un valor numerico")

    tip=input("Ingrese el tipo de evento del paquete: ")
    dura=input("Ingrese la duración del paquete: ")

    paquetes[nom]={"Nombre":nom,"Precio":prec,"Tipo":tip,"Duración":dura}
    print("PAQUETE REGISTRADO CON EXITO")

def agservicio():
    
    while True:
        while True:
            print("Digite el codigo del servicio")
            cod=input("CS-")
            if cod.isdigit():
                cod=f"CS-{cod}"
                break
            else:
                print("Solo Numeros")
        
        eva=servicios.get(cod,1)
        if eva!=1:
            break
        else:
            print("Servicio ya existente")
    
    while True:

        noms=input("Ingrese el nombre del paquete:")
        noms=noms.capitalize()
        eva=paquetes.get(noms,1)
        if eva!=1:
            print("Paquete no existente")
        else:
            break
    
    nombre=input("Ingrese el nombre del titular del servicio: ")
    servicios[cod]={"Nombre del Titular":nombre,"Paquete":noms}
    print("SERVICIO REGISTRADO CON EXITO")

def deletpaquete():

    while True:

            noms=input("Ingrese el nombre del paquete que desea eliminar:")
            noms=noms.capitalize()
            eva=paquetes.get(noms,1)
            if eva!=1:
                print("Paquete no existente")
            else:
                break
    print("------------------------")
    for j in paquetes[noms]:
        print(j,"-",paquetes[noms][j])
    print("------------------------")
        
    while True:
        try:
            print("----------------------------------------------")      
            print("¿Esta seguro que desea eliminar este paquete?")
            print("""
                1. SI
                2. NO
                    """)
            opc=int(input("Ingrese el numero de acuerdo a su elección"))
            if opc==1:
                print("Paquete eliminado con exito")
                paquetes.pop(noms)
                break
            elif opc==2:
                break
            else:
                print("Valor no valido")
        except ValueError:
            print("Valor no valido")