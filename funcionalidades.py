paquetes={}

def agpaquete():
    
    while True:

        nom=input("Escriba el nombre del paquete: ")
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

