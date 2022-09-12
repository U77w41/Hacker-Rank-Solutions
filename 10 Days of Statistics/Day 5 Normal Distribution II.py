# Enter your code here. Read input from STDIN. Print output to STDOUT
import statistics as st

n = input().rstrip().split()
mu = float(n[0])
sigma = float(n[1])

a, b = float(input()), float(input())


grades = st.NormalDist(mu, sigma)


print(round((1-grades.cdf(a))*100, 2))
print(round((1-grades.cdf(b))*100, 2))
print(round((grades.cdf(b))*100, 2))