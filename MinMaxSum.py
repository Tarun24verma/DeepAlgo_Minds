#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    a=0
    for i in arr:
        a+=i
    i=m=0
    n=arr[1]
    for i in range(len(arr)):
        m=m if m>arr[i] else arr[i]
        n=n if n<arr[i] else arr[i]
    print(a-m, a-n)
            
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
