import os
import glob

os.system('mpirun -np * liggghts < in1.MgO_proporcion_muMU_sigmaSIGMA')
os.system('mpirun -np * liggghts < in2.MgO_proporcion_muMU_sigmaSIGMA')
os.system('mpirun -np * liggghts < in3.MgO_proporcion_muMU_sigmaSIGMA')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime) # particulas antes de retirar paredes
os.system('mv %s ./dump1' % (newest))
os.system('mpirun -np * liggghts < in4.MgO_proporcion_muMU_sigmaSIGMA')
newest = max(glob.iglob('./post/dump*.pruebas'), key=os.path.getctime) # particulas en reposos sin paredes
os.system('mv %s ./dump2' % (newest))
