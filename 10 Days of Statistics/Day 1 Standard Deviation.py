#!/bin/python3

import math
import os
import random
import re
import sys
from statistics import mean as mn
#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mu = mn(arr)
    var = 0
    for i in range(len(arr)):
        var += (arr[i] - mu)**2
    sd = (var/len(arr))**(1/2)
    print(f'{sd :.1f}')
        
        

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
