#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Write your code here
    loaves=0
    if(sum(B)%2!=0):
        return "NO"
    flag=1
    while(flag):
        for i,j in enumerate(B):
            if(j%2!=0):
                B[i]+=1
                B[i+1]+=1
                loaves+=2
        flag=0
        for i in B:
            if i%2!=0:
                flag=1
    return (str(loaves))
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
