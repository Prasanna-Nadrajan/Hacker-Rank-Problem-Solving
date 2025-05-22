import numpy
num=int(input())
arr1=[]
for i in range(num):
    l=list(map(int,input().split()))
    arr1.append(l)
arr1=numpy.array(arr1)
arr2=[]
for i in range(num):
    l=list(map(int,input().split()))
    arr2.append(l)
arr2=numpy.array(arr2)
print(numpy.dot(arr1,arr2))
