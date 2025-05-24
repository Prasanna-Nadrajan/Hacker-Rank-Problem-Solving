import numpy
numpy.set_printoptions(legacy='1.13')
l=numpy.array(list(map(float,input().strip().split())))
print(numpy.floor(l),numpy.ceil(l),numpy.rint(l),sep='\n')
