num1=int(input())
s=set(map(int,input().split()))
tc=int(input())
for i in range(tc):
    l=input().split()
    s_temp=set(map(int,input().split()))
    task=l[0]
    if(task=="intersection_update"):
        s&=s_temp
    elif(task=="symmetric_difference_update"):
        s^=s_temp
    elif(task=="update"):
        s|=s_temp
    elif(task=="difference_update"):
        s-=s_temp
print(sum(s))
