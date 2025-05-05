# Enter your code here. Read input from STDIN. Print output to STDOUT
def check_float(num):
    if '.' in num and not(num.count('.')>1):
        flag=0
        for j,i in enumerate(num):
            # print(j,i)
            if (not(i.isdigit()) and i!='.' and i!='+' and i!='-')or((i=='+' or i=='-') and j!=0):
                flag=1
                break
        if(flag):
            print(False)
        else:
            print(True)
    else:
        print(False)

num=int(input())
for i in range(num):
    check_float(input())
