#!/bin/python3

import math
import os
import random
import re
import sys


n, m=map(int, input().strip().split(" "))
dist=[[math.inf]*(n+1) for _ in range(n+1)]

for _ in range(m):
    i,j,w=map(int,input().strip().split(" "))
    dist[i][j]=w
for i in range(1,n+1):
    dist[i][i]=0

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])

q=int(input())

for _ in range(q):
    i, j=map(int, input().strip().split(" "))
    print(dist[i][j] if dist[i][j]!=math.inf else -1)