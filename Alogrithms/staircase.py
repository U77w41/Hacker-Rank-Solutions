#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    h = '#'
    s = " "
    n = int(n)
    
    if n == 0:
        print('')
    if n ==1:
        print('#')
    if n >1:
        for i in range(1 , n+1):
            print(((s * (n - i))) + (i * h))
        
    
    
    
# def staircase(n):
#     tag = "#"
#     spa = " "
#     # Write your code here
#     for i in range(n):
#         if((n-1) - i == 0):
#             print(((i +1) * tag))
#         else:   
#             print((spa * ((n -1) - i)) +((i +1) * tag))
    
    

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
