#!/bin/python3

import math
import os
import random
import re
import sys

def introTutorial(V, arr):
    # Write your code here
    try:
        ind=arr.index(V)
    except ValueError:
        return -1
    return ind

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input().strip())

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
