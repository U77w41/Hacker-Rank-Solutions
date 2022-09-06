#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#



def rotation(r1,c1,r2,c2,a,k):
    temp=[]
    for i in range(c1,c2+1):
        temp.append(a[r1][i])
    for i in range(r1+1,r2+1):
        temp.append(a[i][c2])
    for i in range(c2-1,c1-1,-1):
        temp.append(a[r2][i])
    for i in range(r2-1,r1,-1):
        temp.append(a[i][c1])
    #print(temp)
    temp=temp[k%len(temp):]+temp[:k%len(temp)]
    #print(temp)
    t=0
    for i in range(c1,c2+1):
        a[r1][i]=temp[t]
        t+=1
    for i in range(r1+1,r2+1):
        a[i][c2]=temp[t]
        t+=1
    for i in range(c2-1,c1-1,-1):
        a[r2][i]=temp[t]
        t+=1
    for i in range(r2-1,r1,-1):
        a[i][c1]=temp[t]
        t+=1
    
    return a


    

def fullrotation(a,k):
    c=len(a[0])
    r=len(a)
    x=min(r,c)//2
    for i in range(0,x):
        a=rotation(i,i,r-1-i,c-i-1,a,k)
    return a


def matrixRotation(arr, k):
    arr=fullrotation(arr,k)
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

        
        
        
        
        
##############################################        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
