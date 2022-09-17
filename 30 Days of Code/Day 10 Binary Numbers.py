#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = format(int(input().strip()), 'b')
    
    counter = 0
    counter_list = []
    
    for i in range(0, len(n)):
        if int(n[i]) == 1:
            counter +=1
        else:
            counter_list.append(counter)
            counter = 0

    counter_list.append(counter)
    print(max(counter_list))