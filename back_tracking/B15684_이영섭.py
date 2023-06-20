N, M, H = map(int, input().split())
board = [[False]*(N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = True


def check(bd):
    for i in range(1, N):
        temp = i
        for j in range(1, H+1):
            if bd[j][temp]:
                temp += 1
            elif bd[j][temp-1]:
                temp -= 1
        if temp != i:
            return False
    return True


def dfs(cnt, bd, x, y):
    global ans
    if cnt >= ans:
        return
    if check(bd):
        ans = min(ans, cnt)
        return
    if cnt == 3:
        return

    for i in range(x, H+1):
        if x == i:
            k = y
        else:
            k = 0
        for j in range(k, N):
            if not bd[i][j] and not bd[i][j+1] and not bd[i][j-1]:
                bd[i][j] = True
                dfs(cnt+1, bd, i, j+2)
                bd[i][j] = False


ans = 4
dfs(0, board, 1, 1)
if ans == 4:
    ans = -1
print(ans)
