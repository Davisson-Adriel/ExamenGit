import json
from funcionalidades import servicios,paquetes

paquetes_json="paquetes1.json"
servicios_json="servicios1.json"

def cargarjson(archivo):
    datos={}
    with open(archivo,"r") as file:
        datos=json.load(file)
    
    if archivo=="paquetes1.json":
        paquetes.update(datos)
    elif archivo=="servicios1.json":
        servicios.update(datos)
    
