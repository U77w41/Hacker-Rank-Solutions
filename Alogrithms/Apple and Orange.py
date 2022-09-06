#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#



def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    dis_a = []
    dis_b = []
    c_a = 0
    c_o = 0
    
    
    
    for ap in apples:
        dis_a.append(ap + a)
    for orn in oranges:
        dis_b.append(orn + b)
        
    for n_a in dis_a:
        if n_a in range(s,t+1):
            c_a +=1
            
    for n_o in dis_b:
        if n_o in range(s ,t+1):
            c_o +=1
            
    print(c_a)
    print(c_o)
    
    
    
    
    
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
