# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
l=list(map(int,input().split()))
ll=[False]*len(l)
lk=[False]*len(l)
for i in range(len(l)):
    if (str(l[i])==str(l[i])[::-1]):
        ll[i]=True
    if (l[i]>=0):
        lk[i]=True
print(any(ll)and all(lk))
