    


def runner_up(arr):
    lst = list(arr)
    mx = max(lst)
    z = lst.remove(mx)
    print(mx)
    
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)