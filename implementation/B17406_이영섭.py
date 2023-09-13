from itertools import permutations


def val_a(bd):
    tp = []
    for i in range(n):
        tp.append(sum(bd[i]))
    return min(tp)


def rotate_op(temp, sx, sy, ex, ey):
    tp = [[temp[i][j] for j in range(m)] for i in range(n)]

    for k in range(min((ey-sy)//2+1, (ex-sx)//2+1)):
        for i in range(sy+k, ey-k):
            tp[sx+k][i+1] = temp[sx+k][i]
        for i in range(sx+k, ex-k):
            tp[i+1][ey-k] = temp[i][ey-k]
        for i in range(ey-k, sy+k, -1):
            tp[ex-k][i-1] = temp[ex-k][i]
        for i in range(ex-k, sx+k, -1):
            tp[i-1][sy+k] = temp[i][sy+k]
    return tp


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
op = [list(map(int, input().split())) for _ in range(k)]
ans = []
bf = list(permutations(op))

for case in bf:
    temp = [board[i][:] for i in range(n)]
    for cs in case:
        temp = rotate_op(temp, cs[0]-cs[2]-1, cs[1]-cs[2]-1, cs[0]+cs[2]-1, cs[1]+cs[2]-1)
    ans.append(val_a(temp))

print(min(ans))
