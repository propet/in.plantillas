import os
import glob
import math
import numpy as np

'''
	Postprocesado. Porosidad, densidad, permeabilidad.
'''

# Importacion de los ultimos datos con informacion de las particulas
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime)
A      = np.loadtxt(newest, skiprows=9)

# Las variables estan en micras, pero la masa esta en picogramos
x   = A[:,2]   # posicion x
y   = A[:,3]   # posicion y
z   = A[:,4]   # posicion z
r   = A[:,17]  # radio
m   = A[:,18]  # masa

zmax_index = np.where(z==max(z))
xmin_index = np.where(x==min(x))
xmax_index = np.where(x==max(x))
ymin_index = np.where(y==min(y))
ymax_index = np.where(y==max(y))
z_max = max(z)+r[zmax_index]
x_min = min(x)-r[xmin_index]
x_max = max(x)+r[xmax_index]
y_max = max(y)+r[ymin_index]
y_min = min(y)-r[ymax_index]
Diam_disco = (x_max+y_max)/2 - (x_min+y_min)/2

# Masa total
Mt = m.sum()
# Volumen del disco de particulas (cilindro)
Vd = (math.pi*(Diam_disco**2)/4)*z_max
# Volumen de las particulas sumado
Vp = (4/3*math.pi*np.power(r,3)).sum()

# Porosidad
e = (Vd-Vp)/Vd
# Densidad
rho = (Mt/Vd)*1000  # Multiplicado por 1000 para pasar de [pico_g/nu_m^3] a SI
# Permeabilidad
# k = 

print('Porosidad: ', e, 'Densidad: ', rho)
