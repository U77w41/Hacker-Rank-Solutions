import math

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))



##############   The below code not working on HackerRank    ##################



# # Enter your code here. Read input from STDIN. Print output to STDOUT
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# from scipy.stats import norm
# import math

# max_wt = float(input())
# n_b = int(input())
# mn_wt = float(input())
# sd = float(input())



# # We need to find the maximum average weight of each box to have 49 of them in the elavator
# max_possible_weight = max_wt / n_b
# # >>> max_possible_weight = 200

# # In the population of all boxes, mu=205 and stdev=25
# # we need to estimate the parameters of the distribution of all sample means using the one sample
# sample_size = n_b

# pop_mu = mn_wt
# pop_stdev = sd

# sample_dist_mu = pop_mu
# sample_dist_stdev = pop_stdev / math.sqrt(sample_size)

# # Now find the probabilty that our sample has the mean samller than 200
# x = 200
# p = norm.cdf(max_possible_weight, sample_dist_mu, sample_dist_stdev)
# print(f'The probability that all 49 boxes can be safely loaded into the freight elevator \
# and transported is {int(round(p, 3)*100)}%')

# # >>> The probability that all 49 boxes can be safely loaded into the freight elevator and transported is 1%
