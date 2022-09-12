# Enter your code here. Read input from STDIN. Print output to STDOUT
# Poissoin Distribution pdf: P(X=k) = (lam**k) * (e**(-lam)) / k!
import math
lam = float(input())
k = int(input())
p = ((math.pow(lam,k) * math.exp(-lam))/math.factorial(k))
print("{:.3f}".format(p))
