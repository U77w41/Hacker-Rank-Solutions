# Enter your code here. Read input from STDIN. Print output to STDOUT
# from scipy.stats import geom

# a,b=input().split(' ')
# a=int(a)
# b=int(b)
# c=int(input())


# # k: number of trials to have the 1st success
# # p: prbability of success in each trial 



# geom.pmf(k=c, p=(a/b))





a,b=input().split(' ')
a=int(a)
b=int(b)
c=int(input())

pd=a/b   #probability of defective
pd=round(pd,3)

pnd=1-pd  #probability of non-defective

s=pow(pnd,(c-1))*pd
s=round(s,3)
print(s)