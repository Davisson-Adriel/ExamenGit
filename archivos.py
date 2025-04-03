import json
from funcionalidades import servicios,paquetes

paquetes_json="paquetes1.json"
servicios_json="servicios1.json"

def cargarjson(archivo):
    datos={}
    try:
        with open(archivo,"r") as file:
            datos=json.load(file)
    except Exception:
        print("")
        datos = None
    
    if archivo=="paquetes1.json":
        paquetes.update(datos)
    elif archivo=="servicios1.json":
        servicios.update(datos)
    
def guardarjson():
    with open(paquetes_json,"w") as archivo:
        json.dump(paquetes,archivo,indent=4)

    with open(servicios_json,"w") as archivo:
        json.dump(servicios,archivo,indent=4)