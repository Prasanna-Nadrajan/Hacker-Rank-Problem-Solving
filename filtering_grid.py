#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    # Write your code here
    cons=[0,len(grid)-1]
    res=[]
    for i in range(len(grid)):
        l=list(grid[i])
        for j in range(1,len(grid[i])-1):
            if i not in cons and j not in cons:
                e=grid[i][j]
                print(e,end=" ")
                if e>grid[i][j-1] and e>grid[i-1][j] and e>grid[i+1][j] and e>grid[i][j+1]:
                    l[j]="X"
        print()
        res.append("".join(l))
    return(res)
    print(grid)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
