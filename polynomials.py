import numpy

ll=list(map(float,input().split()))
s=float(input())
ll=numpy.array(ll)
res=numpy.polyval(ll,s)
print(res)
