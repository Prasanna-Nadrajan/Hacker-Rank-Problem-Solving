import numpy

num=int(input())
ll=[]
for i in range(num):
    l=list(map(float,input().split()))
    ll.append(l)
ll=numpy.array(ll)
det=numpy.linalg.det(ll)
print(round(det,2))

