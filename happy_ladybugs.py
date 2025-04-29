#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    # Write your code here
    d=dict(Counter(b))
    if "_" in d.keys():
        d.pop("_")
    else:
        ll=list(d.values())
        flag=1
        for i in ll:
            if i==1:
                flag=0
                break
        if(not flag):
            return "NO"
        else:
            for i in range(1,len(b)-1):
                if not(b[i-1]==b[i] or b[i+1]==b[i]):
                    return "NO"
            return "YES"
    ll=list(d.values())
    flag=1
    for i in ll:
        if i==1:
            flag=0
            break
    if(not flag):
        return "NO"
    return "YES"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
