from struct import unpack

with  open("./train-images.idx3-ubyte","rb") as input:
        magicnumber = unpack(">i",input.read(4))[0]
        numberofimages = unpack(">i",input.read(4))[0]
        print magicnumber
        print numberofimages
        nrows = unpack(">i",input.read(4))[0]
        ncolumns = unpack(">i",input.read(4))[0]
        images = [[[unpack(">B",input.read(1))[0] for j in xrange(ncolumns)] for k in xrange(nrows)] for l in xrange(numberofimages) ]
print images[0]   
