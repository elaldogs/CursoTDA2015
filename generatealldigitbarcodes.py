import cPickle as cp
from edu.stanford.math.plex4 import *
from java.lang import Runtime


def generatebarcode(singledigit, label):
    max_dimension = 2
    verticesnumbers = 1
    verticesdict = dict()
    digitcomplex = api.Plex4.createExplicitSimplexStream()
    for i in xrange(len(singledigit)):
        for j in xrange(len(singledigit[i])):
            if singledigit[i][j]>0:
                verticesdict[(i,j)]=verticesnumbers
                digitcomplex.addVertex(verticesnumbers,i)
                verticesnumbers = verticesnumbers + 1
    for i in xrange(len(singledigit)):
        for j in xrange(len(singledigit[i])):
            localvertexcount = 0
            localedge = []
            for x in [(i-1,j-1),(i-1,j),(i,j-1),(i,j)]:
                if x in verticesdict:
                    localedge.append(x)
                    localvertexcount = localvertexcount + 1
            if localvertexcount == 4:
                digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i,j)]],i)
                digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j)]],i)
                digitcomplex.addElement([verticesdict[(i,j-1)], verticesdict[(i,j)]],i)
                digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i,j-1)], verticesdict[(i,j)]],i)
                digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i-1,j)], verticesdict[(i,j)]],i)
            if localvertexcount == 3:
                if not (i-1,j-1) in verticesdict:
                    digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j-1)]],i)
                    digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j)]],i)
                    digitcomplex.addElement([verticesdict[(i,j-1)], verticesdict[(i,j)]],i)    
                    digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j-1)], verticesdict[(i,j)]],i)
                if not (i-1,j) in verticesdict:
                    digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i,j)]],i)
                    digitcomplex.addElement([verticesdict[(i,j-1)], verticesdict[(i,j)]],i)    
                    digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i,j-1)], verticesdict[(i,j)]],i)
                if not (i,j-1) in verticesdict:
                    digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i,j)]],i)
                    digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j)]],i)
                    digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i-1,j)], verticesdict[(i,j)]],i)
                if not (i,j) in verticesdict:
                    digitcomplex.addElement([verticesdict[(i-1,j)], verticesdict[(i,j-1)]],i)
                    digitcomplex.addElement([verticesdict[(i-1,j-1)], verticesdict[(i-1,j)], verticesdict[(i,j-1)]],i)
            if localvertexcount == 2:
                if not (localedge[0]==(i-1,j-1) and (localedge[1]==(i-1,j) or localedge[1]==(i,j-1))):
                    digitcomplex.addElement([verticesdict[localedge[0]], verticesdict[localedge[1]]],i)
    digitcomplex.finalizeStream()
    persistence = api.Plex4.getModularSimplicialAlgorithm(max_dimension,2)
    intervals = persistence.computeIntervals(digitcomplex)
    Dintervals = []
    for dimension in xrange(max_dimension):
        temp = []
        temp0 = intervals.getIntervalsAtDimension(dimension)
        for ninterval in xrange(len(temp0)):
            temp.append([temp0[ninterval].getStart(), temp0[ninterval].getEnd()])
        Dintervals.append([dimension,temp])
    #with open("./barcodes/intervalsdigit" + label + ".p","wb") as outputfile:
    #    cp.dump(Dintervals,outputfile)
    return Dintervals

def downup(matrix):
    result = [[ 0 for j in xrange(len(matrix[i]))] for i in xrange(len(matrix))]
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            result[i][j] = matrix[len(matrix) - 1 - i][j]
    return result

def leftright(matrix):
    result = [[ 0 for j in xrange(len(matrix[i]))] for i in xrange(len(matrix))]
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[i])):
            result[i][j] = matrix[j][i]
    return result

def rightleft(matrix):
    return downup(leftright(matrix))

if __name__ == '__main__':
    allintervals = []
    with open("./images.p","rb") as inputfile:
        images = cp.load(inputfile)
    for x in xrange(len(images)):
        allintervals.append(generatebarcode(images[x], str(x) + "ud"))
        allintervals.append(generatebarcode(downup(images[x]), str(x) + "du"))
        allintervals.append(generatebarcode(leftright(images[x]), str(x) + "lr"))
        allintervals.append(generatebarcode(rightleft(images[x]), str(x) + "rl"))
    with open("./allintervals.p", "wb") as outputfile:
        cp.dump(allintervals,outputfile)
        
        