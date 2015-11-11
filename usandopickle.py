# Esto corre en Jython
import math
import cPickle as cp
import random

resolucion=100
#    random.uniform(a,b) genera un random entre a y b
nube=[(math.cos(x*2*math.pi/100)+random.uniform(-.2,.2),
                  math.sin(x*2*math.pi/100)+random.uniform(-.2,.2)) for x in range(0,resolucion)]
#    esto graba usando pickle y open
cp.dump(nube,open("./salidadepickle","wb"))
