# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

print("Objeto celestial a observar")
var_objeto_amirar = input()

#obtener coordenadas del objeto a observar
objeto_amirar = SkyCoord.from_name(var_objeto_amirar)

# Ubicacion de el observatorio con fecha y hora de el momento a observar, momentaneamente hardcodeado

print("Horario y fecha especificado de la observacion ej: 2021-25-12 23:30:00")
var_objeto_fechayhora = input()


bear_mountain = EarthLocation(lat=41.3*u.deg, lon=-74*u.deg, height=390*u.m)
utcoffset = -4*u.hour  # Eastern Daylight Time
time = Time(var_objeto_fechayhora) - utcoffset

#conversion a sistema altitud por parametro altaz (Altitude-Azimuth system)
objeto_amirar_altaz = objeto_amirar.transform_to(AltAz(obstime=time,location=bear_mountain))
print(f"Altitud de el objeto truncado a dos numeros despues de coma = {objeto_amirar_altaz.alt:.2}")


#Corregimiento por si el objeto se encuentra cerca de el horizonte visual aun no claro si es necesario
#Trozo de codigo dedicado a encontrar la masa de aire del objeto a observar a lo largo de la noche

print("Medianoche y dia especificado de la observacion ej: 2021-25-12 (00:00:00)!!!")
var_objeto_fechaymedianoche = input()

'''
medianoche = Time(var_objeto_fechaymedianoche) - utcoffset
delta_medianoche = np.linspace(-2, 10, 100)*u.hour
marco_medianoche = AltAz(obstime=medianoche+delta_medianoche,
                          location=bear_mountain)
objeto_amirar_altaz_medianoche = objeto_amirar_altaz.transform_to(marco_medianoche)

#convertimos altaz a masa de aire con el atributo `~astropy.coordinates.AltAz.secz`:
objeto_amirar_altaz_medianoche = objeto_amirar_altaz_medianoche.secz

#Grafica masa aire

plt.plot(delta_medianoche, objeto_amirar_altaz_medianoche)
plt.xlim(-2, 10)
plt.ylim(1, 4)
plt.xlabel('Horas desde EDT medianoche')
plt.ylabel('Masa Aire [Sec(z)]')
plt.show()
'''

#Preparacion de grafica de movimiento en el tiempo de observacion y escalado
medianoche = Time(var_objeto_fechaymedianoche) - utcoffset
delta_medianoche = np.linspace(-12, 12, 1000)*u.hour
variacion_diamasmenos = medianoche + delta_medianoche
#conversion a altaz
marco_variacion_diamasmenos = AltAz(obstime=variacion_diamasmenos, location=bear_mountain)

#ubicacion del sol sobre el marco de grafica creado
from astropy.coordinates import get_sun
altazsol_marco = get_sun(variacion_diamasmenos).transform_to(marco_variacion_diamasmenos)

#ubicacion de la luna sobre el marco de grafica creado
from astropy.coordinates import get_moon
altazluna_marco = get_moon(variacion_diamasmenos).transform_to(marco_variacion_diamasmenos)

#ubicacion de nuestro objeto en esa linea de tiempo en ese marco
altazobjeto_marco = objeto_amirar.transform_to(marco_variacion_diamasmenos)

#hacemos finalmente la grafica con los datos anteriores

plt.plot(delta_medianoche, altazsol_marco.alt, color='r', label='Sun')
plt.plot(delta_medianoche, altazluna_marco.alt, color=[0.75]*3, ls='--', label='Moon')
plt.scatter(delta_medianoche, altazobjeto_marco.alt,
            c=altazobjeto_marco.az, label='Objeto Deseado', lw=0, s=8,
            cmap='viridis')
plt.fill_between(delta_medianoche, 0*u.deg, 90*u.deg,
                 altazsol_marco < -0*u.deg, color='0.5', zorder=0)
plt.fill_between(delta_medianoche, 0*u.deg, 90*u.deg,
                 altazsol_marco < -18*u.deg, color='k', zorder=0)
plt.colorbar().set_label('Azimuth [deg]')
plt.legend(loc='upper left')
plt.xlim(-12*u.hour, 12*u.hour)
plt.xticks((np.arange(13)*2-12)*u.hour)
plt.ylim(0*u.deg, 90*u.deg)
plt.xlabel('Horas desde EDT Medianoche')
plt.ylabel('Altitud [deg]')
plt.show()

