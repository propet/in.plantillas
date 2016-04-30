import os
import glob
import math
import numpy as np

MgO = '75.0'
directorioProporcion = 'input_MgO' + MgO
fuerzas = [10000, 100000, 1000000] # Newtons

for fuerza in fuerzas:
	os.system("sed -e 's/FUERZA/%d/g' in.plantilla1.0 > in.plantilla1" % (fuerza))
	os.system("sed -e 's/PROPMGO/%d/g' -e 's/FUERZA/%d/g' ejecuta0.py > ejecuta.py")
	os.system('python plantilla2scripts.py')
	directorioMgO = os.listdir(directorioProporcion)

	for caso in directorioMgO:
		if(caso.endswith('1300'))
		os.system('python ./scripts/%s/%s/ejecuta.py' % (directorioProporcion, caso))
		os.system('python PostProc.py')

	os.system('cd %ds' % directorios[0])

