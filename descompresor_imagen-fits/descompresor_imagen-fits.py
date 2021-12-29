# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 20:20:48 2021

@author: MatiasRepetto
"""

import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

directorio_archivo = filedialog.askopenfilename()

archivo_imagen = get_pkg_data_filename(directorio_archivo)

fits.info(archivo_imagen)

data_imagen = fits.getdata(archivo_imagen, ext=0)

print(data_imagen.shape)

plt.figure()
plt.imshow(data_imagen, cmap='gray', vmin=0, vmax=255)
plt.colorbar()
plt.show()