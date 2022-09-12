# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial as f
p,n=map(int,input().split())
p=p/100
q=1-p
def comb(n,r):
    return f(n)/(f(r)*f(n-r))
print(format(sum(comb(n,r)*(p**r)*(q**(n-r))for r in range (0,3)),'.3f'))
print(format(sum(comb(n,r)*(p**r)*(q**(n-r))for r in range (2,11)),'.3f'))