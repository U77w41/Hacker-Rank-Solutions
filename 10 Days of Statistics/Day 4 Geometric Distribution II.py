# Enter your code here. Read input from STDIN. Print output to STDOUT
def g(n,p):
    q = 1-p
    g = q**(n-1)*p
    return g

if __name__ == '__main__':
    a,b = list(map(int,input().split(" ")))
    p = a/b
    
    n = int(input())
    
    result = []
    for i in range(1,n+1):
        a = g(i,p)
        result.append(a)
    
    print(round(sum(result),3))