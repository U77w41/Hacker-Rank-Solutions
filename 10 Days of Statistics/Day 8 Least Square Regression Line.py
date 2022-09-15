# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    scores = []
    for i in range(5):
        scores.append(tuple(map(int, input().strip().split(' '))))
        
    sum_x = sum([i[0] for i in scores])
    sum_y = sum([i[1] for i in scores])
    sum_x2 = sum([i[0]**2 for i in scores])
    sum_xy = sum([i[0]*i[1] for i in scores])
    
    n = len(scores)
    
    m = ((n*sum_xy)-(sum_x*sum_y)) / ((n*sum_x2)-sum_x**2)
    b = (sum_y - m*sum_x)/n
    
    print(round(m*80+b, 3))