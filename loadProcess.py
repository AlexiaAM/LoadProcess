import json

with open('datos.json') as archivo:
    datos = json.load(archivo)


print(datos['productos'])