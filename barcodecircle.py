# Ejecutar con Jython, pues JAVAPLEX necesita Java
from edu.stanford.math.plex4 import *
import cPickle as cp
from java.lang import Runtime
import math
import random

def barcodes(path,filename):
    max_dimension = 3;
    resolution = 100;
    num_landmark_points = 50;
    nu = 1;
    num_divisions = 100;
    Dintervals = [];
    cloud = [(math.cos(2*x*math.pi/resolution)+random.uniform(-.2,.2),
              math.sin(2*x*math.pi/resolution)+random.uniform(-.2,.2)) for x in xrange(100)];
    print "Creating maxmin landmark selector"
    print "Total available memory: " + str(Runtime.getRuntime().totalMemory())
    # create a sequential maxmin landmark selector
    landmark_selector = api.Plex4.createMaxMinSelector(cloud, num_landmark_points);
    #R = landmark_selector.getMaxDistanceFromPointsToLandmarks()
    max_filtration_value = 1.2  # R*.7;
    
    print "Constructing lazy witness stream"
    # create a lazy witness stream
    stream = streams.impl.LazyWitnessStream(landmark_selector.getUnderlyingMetricSpace(),
                                            landmark_selector,
                                            max_dimension,
                                            max_filtration_value,
                                            nu,
                                            num_divisions);
    stream.finalizeStream()
    print "Lazy witness stream construction complete"
    # print out the size of the stream
    #num_simplices = stream.getSize()

    # get persistence algorithm over Z/2Z
    persistence = api.Plex4.getModularSimplicialAlgorithm(max_dimension, 2);
    print "Computing intervals"
    # compute the intervals
    intervals = persistence.computeIntervals(stream);
    
    # process and pickle the intervals
    for dimension in xrange(max_dimension):
        temp = []                                               # collection of intervals at dimension
        temp0 = intervals.getIntervalsAtDimension(dimension)
        for ninterval in xrange(len(temp0)):
            temp.append([temp0[ninterval].getStart(),
                         temp0[ninterval].getEnd()])            # intervals as pairs [start,end]
        Dintervals.append([dimension, temp])                    # adds dimension information for the collection of intervals
        
    #====================================================================
    # Dintervals are in the format: 
    # [[dim_1,listofintervalsofdim_1],...,[dim_k,listofintervalsofdim_k]]
    #====================================================================
    cp.dump(Dintervals, open(path + filename, 'wb'))
    cp.dump(cloud,open(path + filename +"cloud",'wb'))
    print "Intervals saved."


if __name__ == "__main__":
    path = './'
    filename='barcodecircle'
    barcodes(path,
             filename)
