import os
import glob
import math
import numpy as np

# Poder manipular la carpeta sin que me vuelvan a pedir permiso
os.system('sudo chmod -R 777 ./scripts')

MgO = '75.0'
directorioProporcion = './scripts/input_MgO-' + MgO
fuerzas = [1000, 100000, 10000000] # Newtons -> 1kN, 100kN, 10T

for fuerza in fuerzas:
	os.system("sed -e 's/FUERZA/%d/g' in.plantilla2.0 > in.plantilla2" % (fuerza))
	os.system("sed -e 's/PROPMGO/%.0f/g' -e 's/FUERZA/%d/g' ejecuta0.py > ejecuta.py" % (float(MgO), fuerza))
	os.system('python plantilla2scripts.py')
	directorioMgO = os.listdir(directorioProporcion)
	directorioMgO.sort()

	for caso in directorioMgO:
		if(caso.endswith('1300') and not(caso.startswith('Rmin_100'))):
			os.chdir(directorioProporcion + '/' + caso)
			os.system('python ejecuta.py')
			# archivos dump para posible renderizado posterior
			os.system('mv dump1 ../../../dumps/dump1%s-F_%sN' % (caso, str(fuerza)))
			os.system('mv dump2 ../../../dumps/dump2%s-F_%sN' % (caso, str(fuerza)))
			# Vuelve a directorio simulaciones
			os.chdir('../../../')


print 'Tareas completadas! :D'
# Apaga el equipo si se ejecuta en un servidor
#os.system('sudo shutdown -h now')
