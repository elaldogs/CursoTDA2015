import numpy as np
import math
import matplotlib.pyplot as pplt

resolucion=100
nube=np.asarray([(math.cos(x*2*math.pi/100),
                  math.sin(x*2*math.pi/100)) for x in range(0,resolucion)])
nubex=nube[:,0]     # primera columna de nube, lista de x's
nubey=nube[:,1]     # segunda columna de nube, lista de y's
pplt.plot(nubex,nubey,'r+')
pplt.show()
