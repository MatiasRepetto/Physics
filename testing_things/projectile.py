'''
Este es un ejercicio que omite muchos detalles del comportamiento fisico real de un proyectil en un ambiente verdadero.
No debe ser tomado como una descripcion verdadera de la trayectoria de un proyectil, solo como una aproximacion muy general.
'''

# Constante
import matplotlib.pyplot as plt
import numpy as np
import math as mp

t = 0
dt = 1
grav = 9.8

print("Ingrese Velocidad del proyectil (metros por segundo): ")
p_vel = float(input())

print("Ingrese Aceleracion del proyectil (metros por segundo): ")
p_acc = float(input())

print("Ingrese Altitud del proyectil (metros): ")
p_alt = float(input())

print("Ingrese Coeficiente aerodinamico del proyectil: ")
p_coef = float(input())

print("Ingrese area(Volumen fisico) del proyectil (metros cuadrados): ")
p_vol = float(input())

print("Ingrese Densidad del aire: ")
p_dens = float(input())

print("Ingrese Velocidad del viento (kilometros por hora): ")
p_vvel = float(input())

print("Ingrese Angulo de ataque del viento: ")
p_vang = float(input())


def velocidad(vel, acc, tiemp):
    aux = vel + (acc * tiemp)
    return aux


def pos_x(x_ini, vel_ini, acc_ini, tiemp):
    x_aux = x_ini + (vel_ini * tiemp) + ((1 / 2) * acc_ini * (tiemp ** 2))
    return x_aux


def pos_y(y_ini, vel_ini, acc_ini, tiemp):
    y_aux = y_ini - (vel_ini * tiemp) - ((1 / 2) * acc_ini * (tiemp ** 2))
    return y_aux

# A pesar de representar esta fuerza con una funcion, en este ejercicio dicha fuerza es constante
def x_draft(p_coef, p_dens, p_vol, p_vvel, p_vang):
    x_auxdraft = (p_coef * p_dens * ((p_vvel ** 2)/2) * p_vol) * mp.cos(p_vang)
    return x_auxdraft

# A pesar de representar esta fuerza con una funcion, en este ejercicio dicha fuerza es constante
def y_draft(p_coef, p_dens, p_vol, p_vvel, p_vang):
    y_auxdraft = (p_coef * p_dens * ((p_vvel ** 2)/2) * p_vol) * mp.sin(p_vang)
    return y_auxdraft

# Definimos objeto representativo de proyectil
plt.ion()
fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(0,100000)
plt.ylim(-100000,100000)
plt.draw()

while t<300:
    x_posi = pos_x(0, p_vel, p_acc, t) - x_draft(p_coef, p_dens, p_vol, p_vvel, p_vang)
    y_posi = pos_y(p_alt, 0, grav, t) - y_draft(p_coef, p_dens, p_vol, p_vvel, p_vang)
    x.append(x_posi)
    y.append(y_posi)
    sc.set_offsets(np.c_[x, y])
    fig.canvas.draw_idle()
    plt.pause(0.1)
    t=t+dt
