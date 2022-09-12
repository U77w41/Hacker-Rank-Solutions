# Poissoin Distribution pdf: P(X=k) = λk * e– λ / k!
import math
m = float(input())
p = float(input())
print(f"{(m *p)* 2.71828 **(-m)/math.factorial(p) :.3f}")