# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    strn = input()
    print(strn[::2],strn[1::2])