# Enter your code here. Read input from STDIN. Print output to STDOUT




read_ints = lambda: list(map(int, input().split()))



def solve(rect, mat_len):
    l = len(rect)
    ret = [0 for i in range(l)]
    pos = 0
    for i in range(l):
        while True:
            find = False
            for j in range(i, l):
                if rect[j][pos] == 1:
                    rect[i], rect[j] = rect[j], rect[i]
                    find = True
                    break
            if find:
                break
            else:
                pos += 1
                if pos == l:
                    break
        if pos == l:
            break
        for j in range(i + 1, l):
            if rect[j][pos]:
                for k in range(pos, l + 1):
                    rect[j][k] ^= rect[i][k]
        pos += 1
        if pos == l:
            break
    rect.reverse()
    for i in range(l):
        pos = -1
        for j in range(l + 1):
            if rect[i][j]:
                pos = j
                break
        if pos == l:
            print('Impossible')
            return
        if pos == -1:
            continue
        ret[pos] = rect[i][l]
        for j in range(i + 1, l):
            if rect[j][pos]:
                for k in range(pos, l + 1):
                    rect[j][k] ^= rect[i][k]
    print('Possible')
    print(sum(ret))
    k = 0
    for i in range(mat_len):
        for j in range(mat_len):
            if (ret[k]):
                print(i, j)
            k += 1

            
            
if __name__ == "__main__":
    [r, d] = read_ints()
    mat = []
    for i in range(r):
        mat.append(read_ints())
    rect = []
    k = 0
    for i in range(r):
        for j in range(r):
            rect.append([])
            for iter_i in range(r):
                for iter_j in range(r):
                    if abs(i - iter_i) + abs(j - iter_j) <= d:
                        rect[k].append(1)
                    else:
                        rect[k].append(0)
            if mat[i][j]:
                rect[k].append(1)
            else:
                rect[k].append(0)
            k += 1
    solve(rect, r)