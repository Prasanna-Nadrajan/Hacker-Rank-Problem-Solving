#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    # Write your code here
    pivot=arr[0]
    left=1
    right=len(arr)-1
    while(left<right):
        while(arr[left]<=pivot and right >=left):
            left+=1
        while(arr[right]>=pivot and right>=left):
            right-=1
        if(left<right):
            arr[left],arr[right]=arr[right],arr[left]
        else:
            break
    arr[0],arr[right]=arr[right],arr[0]
    return arr
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
