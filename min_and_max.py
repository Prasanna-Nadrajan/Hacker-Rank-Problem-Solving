import numpy as np
n,m=map(int,input().strip().split())
arr=[]
for i in range(n):
    ar=list(map(int,input().split()))
    arr.append(ar)
arr=np.array(arr)
print(np.max(np.min(arr,axis=1)))

