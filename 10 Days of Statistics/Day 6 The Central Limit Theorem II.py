# Enter your code here. Read input from STDIN. Print output to STDOUT


from math import erf
max_num = float(input())
n = int(input())
mu = float(input())
std = float(input())
mean = n*mu
stan = std*(n**0.5)
f = lambda x : 0.5*(1+erf((x-mean)/(stan*(2**0.5))))
pro = f(max_num)
pro = round(pro, 4)
print(pro)