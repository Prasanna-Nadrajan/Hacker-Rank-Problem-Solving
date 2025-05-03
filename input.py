# Enter your code here. Read input from STDIN. Print output to STDOUT
num1,num2=map(int,input().split())
expr=input()
expr=eval(expr.replace('x',str(num1)))
print(expr==num2)
