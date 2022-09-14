# Enter your code here. Read input from STDIN. Print output to STDOUT
from statistics import mean , pstdev
#  pstdev Calculates the standard deviation from an entire population
 
n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))


muX = mean(X)
muY = mean(Y)
sdX = pstdev(X)
sdY = pstdev(Y)

s = 0

for i in range(n):
    s+=(X[i]-muX)*(Y[i]-muY)
    
    
pearson = s/(n*sdX*sdY)

pearson = round(pearson, 3)


print(pearson)

