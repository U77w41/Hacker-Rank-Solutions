import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    l = len(arr)
    p =  0
    neg = 0
    z = 0
    for ele in arr:
        if ele >0:
            p +=1
        elif ele <0:
            neg += 1
        else:
            z +=1
   
    
    print(f"{p/l :.6f}")
    print(f"{neg/l :6f}")
    print(f"{z/l :.6f}")
        
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
