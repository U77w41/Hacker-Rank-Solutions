# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

c = list(map(float, input().split()))

def bd(condition):
    n = 6
    x = [3, 4, 5, 6]
    p = condition[0]/sum(condition)
    q = 1 - p
    _sum_ = 0
    for i in range(len(x)):
        b = (math.factorial(n)/(math.factorial(x[i])*math.factorial(n-x[i])))*p**x[i]*q**(n-x[i])
        _sum_ += b
    print(round(_sum_, 3))

bd(c)