import numpy
ll=input().strip().split()
n,m,p=map(int,ll)
l1=[]
l2=[]
for i in range(n):
    l1.append(list(map(int,input().strip().split())))
for i in range(m):
    l2.append(list(map(int,input().strip().split())))
l1=numpy.array(l1)
l2=numpy.array(l2)
l3=numpy.concatenate((l1,l2),axis=0)
print(l3)
