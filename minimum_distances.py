#!/bin/python3

import math
import os
import random
import re
import sys

def minimumDistances(a):
    # Write your code here
    d=dict()
    distance=[]
    for i,val in enumerate(a):
        if val in d.keys():
            distance.append(i-d[val])
        else:
            d[val]=i
    if not distance:
        return -1
    else:
        return min(distance)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
 
