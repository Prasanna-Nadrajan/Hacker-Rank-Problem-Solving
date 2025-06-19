#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    lc=1
    uc=1
    d=1
    sp=1
    for i in password:
        if i.isdigit():
            d=0
        elif i.isupper():
            uc=0
        elif i.islower():
            lc=0
        else:
            sp=0
    req=lc+uc+d+sp
    
    if(len(password)<6):
        res=6-len(password)
        if res>req:
            return res
        else:
            return req
    else:
        return req
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
