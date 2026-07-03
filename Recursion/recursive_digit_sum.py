#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    h=str(n)
    h=n*k
    return sup(h)
def sup(h):
    dig=0
    n=int(h)
    while n>0:
        dig+=n%10
        n//=10
    return check(dig)
def check(dig):
    if dig%10==dig:
        return dig
    else:
        return sup(dig)
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
