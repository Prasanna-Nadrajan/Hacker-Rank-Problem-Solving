#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palin(s):
    l=0
    r=len(s)-1
    while(l<r):
        if(s[l]!=s[r]):
            return [l,r]
        l+=1
        r-=1
    return True

def palindromeIndex(s):
    # Write your code here
    if(palin(s)==True):
        return -1
    else:
        res=palin(s)
        l=res[0]
        r=res[1]
        if(palin(s[0:l]+s[l+1:len(s)])==True):
            return l
        else:
            return r
    return -1
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
