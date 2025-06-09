import numpy as np

n,m=map(int,input().split())
a=[]
b=[]

for j in range(n):
    a.append(list(map(int,input().split())))
for j in range(n):
    b.append(list(map(int,input().split())))

a=np.array(a)
b=np.array(b)
d=a/b
d=d.astype(int)
print(a+b,a-b,a*b,d,a%b,a**b,sep='\n')

