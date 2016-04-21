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

z_max = max(z)
x_min = min(x)
x_max = max(x)
y_max = max(y)
y_min = min(y)
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
