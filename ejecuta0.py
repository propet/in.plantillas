import os
import glob
import math
import numpy as np

os.system('mpirun -np * liggghts < in1.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
os.system('mpirun -np * liggghts < in2.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
os.system('mpirun -np * liggghts < in3.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s ./dump1' % (newest))
os.system('python PostProc.py >> MgO_PROPMGO-F_FUERZA')
os.system('mpirun -np * liggghts < in4.MgO_proporcion_Rmin_radioMinimo_Rmax_radioMaximo')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime)
os.system('mv %s ./dump2' % (newest))
os.system('python PostProc.py >> MgO_PROPMGO-F_FUERZA')
