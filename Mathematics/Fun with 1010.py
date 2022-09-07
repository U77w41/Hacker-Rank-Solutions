# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys

mod = 2000003
factorial_cache = [1, 1]
inverted_factorial_cache = [1, 1]
cache_two = {}
cache_ss = {}

def f(n):
    global factorial_cache
    if n >= len(factorial_cache):
        old_len = len(factorial_cache)
        new_len = max(1 + n, len(factorial_cache) * 11 // 10)   
        factorial_cache += [0] * (new_len - old_len)
        for i in range(old_len, new_len):
            factorial_cache[i] = factorial_cache[i - 1] * i % mod
    return factorial_cache[n]

def inv_f(n):
    global inverted_factorial_cache
    if n >= len(inverted_factorial_cache):
        old_len = len(inverted_factorial_cache)
        new_len = max(1 + n, len(inverted_factorial_cache) * 11 // 10)   
        inverted_factorial_cache += [-1] * (new_len-old_len)
    if inverted_factorial_cache[n] < 0:
        inverted_factorial_cache[n] = pow(f(n), mod - 2, mod)
    return inverted_factorial_cache[n]
        
def Cnk(n, k):
    if n < k:
        return 0
    return f(n) * inv_f(k) * inv_f(n - k) % mod 

def CnkBigP(n, k):
    zero = False
    N = n
    K = k
    while N > 0:
        NN = N % mod
        KK = K % mod
        if NN < KK:
            zero = True
            break
        N //= mod
        K //= mod
    if zero:
        return 0
    result = 1
    N = n
    K = k
    while N > 0:
        NN = N % mod
        KK = K % mod
        result *= Cnk(NN, KK)
        result %= mod
        N //= mod
        K //= mod
    return result

def t(n):
    global cache_two
    if n not in cache_two:
        cache_two[n] = pow(2, n, mod)
    return cache_two[n]

def ss(n):
    if n in cache_ss:
        return cache_ss[n]
    n2 = n + n
    n3 = n2 + n
    result = (n * t(n2 - 1) - (n2 - 1) * CnkBigP(n2 - 2, n - 1)) % mod
    cache_ss[n] = (3 * (t(n - 1) - 1) * result - n * t(n3 - 2) + t(n - 1) * n3 - n, (t(n3) - 3 * t(n2) + 3 * t(n) - 1))
    return cache_ss[n]

    
    
T = int(sys.stdin.readline())




for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    n = N - 1
    s, c = ss(n)
    result = (s + c * (M + 1 - n)) % mod
    print(result)