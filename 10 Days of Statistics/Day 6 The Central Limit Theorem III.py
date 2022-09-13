# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input
sample_size = int(input())
mu = float(input())
sigma = float(input())
cc = float(input())
z = float(input())

# Calculating Standerd error
se = sigma / (sample_size**0.5)

# Results
print(mu-(z*se))
print(mu+(z*se))