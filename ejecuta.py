import os
import glob
import math
import numpy as np

os.system('mpirun -np 4 liggghts < in.plantilla1')
#os.system('mpirun -np 4 liggghts < in.plantilla2')
os.system('mpirun -np 4 liggghts < in.plantilla3')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime) # particulas antes de retirar paredes
os.system('mv %s ./dump1' % (newest))
os.system('mpirun -np 4 liggghts < in.plantilla4')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime) # particulas en reposos sin paredes
os.system('mv %s ./dump2' % (newest))
