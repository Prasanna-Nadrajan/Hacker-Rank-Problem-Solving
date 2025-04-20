#!/bin/python3

import math
import os
import random
import re
import sys
import math
# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    c.sort()
    max_distance = 0

    max_distance = max(max_distance, c[0])

    max_distance = max(max_distance, n - 1 - c[-1])

    for i in range(1, len(c)):
        gap = c[i] - c[i - 1]
        max_distance = max(max_distance, gap // 2)

    return max_distance
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
