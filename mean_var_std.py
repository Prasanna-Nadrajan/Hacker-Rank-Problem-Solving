import numpy

n,m=map(int,input().strip().split())
ll=[]
for i in range(n):
    ll.append(list(map(int,input().strip().split())))
ll=numpy.array(ll)
print(numpy.mean(ll,axis=1))
print(numpy.var(ll,axis=0))
print(round(numpy.std(ll),11))


