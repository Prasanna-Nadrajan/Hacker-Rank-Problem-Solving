#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import product
#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones(n, a, b):
    # Write your code here
    if a>b:
        a,b=b,a
    if a==b:
        return [a*(n-1)]
    return [i for i in range(a*(n-1),b*(n-1)+1,b-a)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())
        a = int(input().strip())
        b = int(input().strip())
        result = stones(n, a, b)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
