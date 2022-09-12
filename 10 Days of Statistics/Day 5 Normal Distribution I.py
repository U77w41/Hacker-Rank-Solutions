# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import statistics as s


mu, sigma = [float(num) for num in input().split()]
a = float(input())
b, c = [float(num) for num in input().split()]



time = s.NormalDist(mu, sigma)



print(round(time.cdf(a), 3))
print(round((time.cdf(c)-time.cdf(b)), 3))