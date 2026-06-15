#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X, N):
    return compute(X,N,1,0)
def compute(X,N,Start,Cur_Sum):
    if Cur_Sum==X:
        return 1
    if Start > math.sqrt(X) or Cur_Sum > X:
        return 0

    return compute(X, N, Start + 1, Cur_Sum + pow(Start, N)) + compute(X, N, Start + 1, Cur_Sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
