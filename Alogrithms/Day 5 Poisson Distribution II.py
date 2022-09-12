# Enter your code here. Read input from STDIN. Print output to STDOUT
input_ = input().rstrip().split()
lam_a = float(input_[0])
lam_b = float(input_[1])

# lam_a = 0.88
# lam_b =  1.55

# ca = 160 + 40X^2
# cb = 128 + 40Y^2
# Propert of random variables: E[X * Y] = muX * muY + Cov(X,Y)
exp_ca = 160 + 40 * (lam_a ** 2 + lam_a)
exp_cb = 128 + 40 * (lam_b ** 2 + lam_b)

print(f'{exp_ca:0.3f}')
print(f'{exp_cb:0.3f}')