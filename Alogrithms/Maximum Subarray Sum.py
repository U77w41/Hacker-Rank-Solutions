#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY a
#  2. LONG_INTEGER m
#


def maximumSum(a, m):
    # Create prefix array (1)
    prefix = [None] * len(a)
    
    # Fill prefix array (n)
    prefix[0] = a[0] % m
    for i in range(1, len(a)):
        prefix[i] = (prefix[i-1] + a[i]) % m
    
    # Find best candidate under prefixes (n)
    best = max(prefix)
    
    # Create tuples to save original index of value (n)
    numbered = enumerate(prefix)
    
    # Sort based on prefix value (n log(n))
    sort = sorted(numbered, key=lambda x: x[1])
    
    # find greatest vale when subtracting two consecutive values (smaller-greater one) of sorted prefix array. Check if indices allow this to be a candidate. Save largest candidate. (n)
    best = best - m
    for i in range(1, len(sort)):
        candidate_value = sort[i-1][1] - sort[i][1]
        if candidate_value < 0 and candidate_value > best:
            if sort[i-1][0] > sort[i][0]:
                best = candidate_value
                                
                                
                                

                                
                                
                
    return(best + m)







    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = maximumSum(a, m)

        fptr.write(str(result) + '\n')

    fptr.close()
