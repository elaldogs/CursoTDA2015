import cPickle as cp
import matplotlib.pyplot as pplt

nubeleida=cp.load(open("./salidadepickle","rb"))
nubeleidax=[x[0] for x in nubeleida]
nubeleiday=[x[1] for x in nubeleida]
pplt.plot(nubeleidax,nubeleiday,'.')
pplt.show()