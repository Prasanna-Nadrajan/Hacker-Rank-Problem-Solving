# Enter your code here. Read input from STDIN. Print output to STDOUT
sst=list(map(int,input().split()))
n=sst[0]
x=sst[1]
ll=[]
temp=[]
for i in range(x):
    temp=list(map(float,input().split()))
    ll.append(temp)
llz=list(zip(*ll))
for i in llz:
    print(round((sum(i)/len(i)),1))
