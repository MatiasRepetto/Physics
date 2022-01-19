# -*- coding: utf-8 -*-
"""
@author: MatiasRepetto

"""
import requests
import pprint

print("Introduzca la fecha de interes para los objetos (YY-MM-DD): ")
obj_ini_date = input()

print("Introduzca la fecha final (7 dias despues de la inicial, YY-MM-DD): ")
obj_fin_date = input()

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date="+obj_ini_date+"&end_date="+obj_fin_date+"&api_key=aqzWdEZSKyIcaFVKdy0wUj5lT0Mus4fExkNAwW4E")
result = response.json()
obj_cant = result["element_count"]
obj_id = result["near_earth_objects"]
print("Cantidad de objetos: ", obj_cant)
print("informacion de objetos: ")
pprint.pprint(obj_id)


