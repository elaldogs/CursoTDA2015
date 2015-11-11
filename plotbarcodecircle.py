# Ejecutar con Python
import matplotlib.pyplot as plt
import numpy as np
import cPickle as cp
import math

if __name__ == "__main__":
    x = cp.load(open('./barcodecircle', 'rb'))
    x = np.asanyarray(x)
    MAX_X = 1.2; #Upper limit of X values
    resolution = 100
    cloud = cp.load(open("./barcodecirclecloud",'rb'))
    plt.figure(1)
    for i in xrange(len(x)):
        ax = plt.subplot(len(x), 1, i + 1)
        ax.set_title('Dimension '+str(i)+'')
        ax.margins(0, .2)                   # padding in x and y axis, respectively 
        ax.set_xlim(0, MAX_X)               # limits of graph in axis x
        ax.set_yticks([])                   # removes ticks and labels along the y-axis
        for j in xrange(len(x[i][1])):
            print str(i) + ": " + str(x[i][1][j])
            plt.plot(x[i][1][j], [j * .1 + 1, j * .1 + 1])
            if x[i][1][j][1] == None:
                plt.plot([x[i][1][j][0], MAX_X], [j * .1 + 1, j * .1 + 1])
    plt.suptitle("Barcodes for the circle cloud:")
    plt.savefig('barcodecircle.png')
    plt.tight_layout()
    plt.subplots_adjust(top=.89)
    plt.figure(2)
    plt.plot([x[0] for x in cloud], [x[1] for x in cloud],'.')
    plt.show()