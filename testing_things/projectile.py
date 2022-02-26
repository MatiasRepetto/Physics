# Constant

import matplotlib.pyplot as plt
import numpy as np

t = 0
dt = 1
grav = 9.18

print("Ingrese Velocidad del proyectil: ")
p_vel = int(input())

print("Ingrese Aceleracion del proyectil: ")
p_acc = int(input())

print("Ingrese Altitud del proyectil: ")
p_alt = int(input())


def velocidad(vel, acc, tiemp):
    aux = vel + (acc * tiemp)
    return aux


def pos_x(x_ini, vel_ini, acc_ini, tiemp):
    x_aux = x_ini + (vel_ini * tiemp) + ((1 / 2) * acc_ini * (tiemp ** 2))
    return x_aux


def pos_y(y_ini, vel_ini, acc_ini, tiemp):
    y_aux = y_ini - (vel_ini * tiemp) - ((1 / 2) * acc_ini * (tiemp ** 2))
    return y_aux


# Definimos objeto representativo de proyectil
plt.ion()
fig, ax = plt.subplots()
x, y = [],[]
sc = ax.scatter(x,y)
plt.xlim(0,30000)
plt.ylim(-30000,30000)
plt.draw()

while t<300:
    x_posi = pos_x(0, p_vel, p_acc, t)
    y_posi = pos_y(p_alt, 0, grav, t)
    x.append(x_posi)
    y.append(y_posi)
    sc.set_offsets(np.c_[x, y])
    fig.canvas.draw_idle()
    plt.pause(0.1)
    x.clear()
    y.clear()
    t=t+dt
