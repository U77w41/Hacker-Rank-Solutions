# Enter your code here. Read input from STDIN. Print output to STDOUT
d = []
N = int(input())

#-------------------- step1 --------------------
#x = 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2
#y = 200 44 32 24 22 17 15 12 8 4
x = list(map(float, input().split()))
y = list(map(float, input().split()))


#-------------------- step2 --------------------
#rx = 10 9 8 7 6 2 5 4 1 3
#ry = 10 9 8 7 6 5 4 3 2 1
rx = x.copy()
ry = y.copy()
rx.sort()
ry.sort()

#-------------------- step3 --------------------
#rx - ry = 0 0 0 0 0 -3 1 1 -1 2
for i in range(N):
    d.append((rx.index(x[i]) + 1) - (ry.index(y[i]) + 1))

#-------------------- step4 --------------------
#di^2 = 0 0 0 0 0 9 1 1 1 4
for i in range(N):
    d[i] = d[i] ** 2
    
#-------------------- step5 --------------------
# Answer = 1 - 0.09696969696 = 0.90303030303
# Answer rounded to a scale of three decimal places, we get 0.903
# Answer = 0.903
ans = 1 - ((6 * sum(d))/(N * ((N**2) -1)))
print("{:.3f}".format(ans))