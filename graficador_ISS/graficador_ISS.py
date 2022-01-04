# -*- coding: utf-8 -*-
"""
@author: MatiasRepetto
"""
import json
import urllib.request
import matplotlib.pyplot as plt
import numpy as np
import keyboard as keyb

#Preparamos el grafico tanto como fondo como demas atributos
plt.ion()
img = plt.imread("detailed-satellite-map-of-the-world.jpg")
fig, ax = plt.subplots()
ax.imshow(img, extent=[-180, 180, -180, 180])
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(-180,180)
plt.ylim(-180,180)
plt.draw()

#loop de puntos para actualizar el plot en tiempo real
while True:
    #Obtenemos ubicacion de ISS mediante un json
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result["iss_position"]
    #Parseamos a float porque recibimos string y no podemos operar con string en append
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    x.append(lon)
    y.append(lat)
    sc.set_offsets(np.c_[x,y])
    fig.canvas.draw_idle()
    plt.pause(0.1)
    x.clear()
    y.clear()
    if keyb.is_pressed("p"):
        break



