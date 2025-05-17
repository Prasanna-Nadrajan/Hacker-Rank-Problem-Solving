import numpy
n,m=map(int,input().strip().split())
l=[]
for i in range(n):
    l.append(list(map(int,input().strip().split())))
ln=numpy.array(l)
res=numpy.prod(numpy.sum(ln,axis=0))
print(res) 
