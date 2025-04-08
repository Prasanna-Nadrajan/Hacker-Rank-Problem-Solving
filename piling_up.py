# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
testcases=int(input())
while(testcases!=0):
    num=int(input())
    l=list(map(int,input().split()))
    res=[]
    for i in range(int(math.ceil(num/2))):
        if(l[i]>=l[num-1-i]):
            res.append(l[i])
        else:
            res.append(l[num-i-1])
    if(sorted(res,reverse=True)==res):
        print("Yes")
    else:
        print("No")
    testcases-=1
