# Enter your code here. Read input from STDIN. Print output to STDOUT
ss=set(map(int,input().split()))
num=int(input())
flag=True
for i in range(num):
    s=set(map(int,input().split()))
    if not (s.issubset(ss)):
        flag=False
        break
print(flag)
