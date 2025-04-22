# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
num=int(input())
l=list(map(int,input().split()))
cl=Counter(l)
c_d=dict(cl)
for i,j in enumerate(list(c_d.values())):
    if j==1:
        c_i=i
for i,j in enumerate(list(c_d.keys())):
    if i==c_i:
        c_r=j
print(c_r)
