#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
ones=["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]
teens=["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["ten","twenty"]
def timeInWords(h, m):
    res=""
    if m==0:
        res=ones[h-1]+" o' clock"
    def find_m(minutes,h):
        res=""
        if 1<=m<10:
            res+=ones[m-1]
        elif m==10:
            res+=tens[0]
        elif m==15:
            res="quarter past "+ones[h-1]
            return res
        elif 11<=m<=19 and m!=15:
            res+=teens[int(str(m)[1])-1]
        elif m==20:
            res+=tens[1]
        elif 20<m<=29:
            res+=tens[1]+" "+ones[int(str(m)[1])-1]
        res+=" minutes past "+ones[h-1]
        if m==1:
            res=res.replace("minutes","minute")
        return res
    if 0<m<30:
        res=find_m(m,h)
    elif m==30:
        res+="half past "+ones[h-1]
    elif 31<=m<=59:
        m=60-m
        res=find_m(m,h+1)
        res=res.replace("past","to")
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
