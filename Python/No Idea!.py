# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
my_arr = list(map(int, input().split()))
my_arr = my_arr[:n]




a = set(map(int, input().split()))
b = set(map(int, input().split()))


happiness = 0


if len(a) <= m and len(b) <= m:
    for i in my_arr:
        if i in a:
            happiness += 1
        if i in b:
            happiness -= 1

print(happiness)