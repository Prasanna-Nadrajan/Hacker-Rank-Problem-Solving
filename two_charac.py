#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def check(st):
    if(len(set(st))!=2):
        return False
    else:
        if(len(st)%2!=0):
            if(st[0]==st[-1]):
                if(st[1]==st[-2]):
                    for i in range(2,len(st)):
                        if(st[i]!=st[i-2] or st[i]==st[i-1]):
                            return False
                else:
                    return False
            else:
                return False
        else:
            for i in range(len(st)):
                if(st[i]!=st[i-2] or st[i]==st[i-1]):
                    return False
        return True

def alternate(s):
    # Write your code here
    l=set(s)
    print(l)
    try:
        lk=list(combinations(l,len(l)-2))
    except:
        return 0
    print(lk)
    max_len=0
    for i in lk:
        t2=s
        t1=''
        for j in range(len(i)):
            t1=t2.replace(i[j],"")
            t2=t1 
        print(t2)   
        print(check(t2))
        if(check(t2) and max(len(t2),max_len)!=max_len):
            max_len=len(t2)
    return max_len
    
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
