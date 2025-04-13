# Enter your code here. Read input from STDIN. Print output to 
num1=int(input())
l1=set(map(int,input().split()))
num2=int(input())
l2=set(map(int,input().split()))
c=len(l1&l2)
print(c)


