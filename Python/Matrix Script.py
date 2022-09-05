import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []


for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
mm = 0
mn = 0
mmatrix = []
alpham = []


for _1 in range(m):
    for _ in range(n):
        mmatrix.append(matrix[_][_1])
        alpham.append(matrix[_][_1].isalpha())
ret = []
cond = 0
end = []
start = []


for i in range(len(mmatrix)-1, -1, -1):
    cond += alpham[i]
    cond or end.append(mmatrix[i])
cond = 0

for i in range(len(mmatrix)):
    cond += alpham[i]
    cond or start.append(mmatrix[i])
cond = 0


for i in range(len(start), len(mmatrix) - len(end)):
    alpham[i] or ret.append(" ")
    (not alpham[i]) or ret.append(mmatrix[i])

st = "".join(start)+"".join(ret)+"".join(reversed(end))
len(ret) > 0 or print("".join(start))
len(ret) == 0 or print(st)