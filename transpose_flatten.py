import numpy
n,m=map(int,input().split())
l=[]
for i in range(n):
    t=list(map(int,input().split()))
    l.append(t)
    
l=numpy.array(l)
print(l.transpose())
print(l.flatten())
