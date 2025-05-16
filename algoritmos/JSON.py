import json;
import requests;
##Serializar: pasar de diccionario a JSON
##Deserializar: JSON a diccionario
JSON = {
    "Nombre": "Andres",
    "Apellido":"Wilches",
    "pasatiempo":["Jugar","Tocar musica","dormir"],
    "edad":22,
    "empleado":False,
    "jefe":None,
    "hijos":None
}

##Para cargar el diccionario a JSON (serializar)
with open("json/data_file.json","w") as write_file:
    json.dump(JSON,write_file)
##Ir a /json/data_file.json para ver que fue con exito

##El objeto se puede asignar a un string:
json_string = json.dumps(JSON,indent=4);
print(json_string,type(json_string));


##Para pasar el JSON a un diccionario (deserializar)
with open("json/data_file.json","r") as read_file:
    JSON = json.load(read_file);

print(JSON["Nombre"])
##Deserializar desde texto
json_string = '''{"Nombre":{"nombre":"Alan Mathison Turing","edad":"41"}}''';
data = json.loads(json_string);
print(data)

##Json placeholder (para leer request archivos JSON de internet)
response = request.get(url);
##Cargar
json.loads(response.text)