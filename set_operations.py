# Enter your code here. Read input from STDIN. Print output to STDOUT
num1=int(input())
l1=set(map(int,input().split()))
num2=int(input())
l2=set(map(int,input().split()))
res=len(l1.difference(l2))
print(res)
