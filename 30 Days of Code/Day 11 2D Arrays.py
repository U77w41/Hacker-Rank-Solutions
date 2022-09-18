#!/bin/python3

import math
import os
import random
import re
import sys

def get_hourglass_sum(arr, i, j):
    return (
        arr[i][j] + arr[i][j+1] + arr[i][j+2] +
        arr[i+1][j+1] +
        arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
    )


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    
    max_hourglass_sum = float('-inf')
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            hourglass_sum = get_hourglass_sum(arr, i, j)
            if hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = hourglass_sum
    
    print(max_hourglass_sum)