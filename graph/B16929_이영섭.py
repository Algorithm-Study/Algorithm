N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
ans = False
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]


def dfs(val, x, y, cnt):
    global ans
    if ans:
        print("Yes")
        exit()
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue
        if cnt >= 4 and nx == sr and ny == se:
            ans = True
            print("Yes")
            exit()
        if board[nx][ny] == val and not visit[nx][ny]:
            visit[nx][ny] = 1
            dfs(val, nx, ny, cnt+1)
            visit[nx][ny] = 0


for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        sr, se = i, j
        dfs(board[i][j], i, j, 1)
        visit[i][j] = 0
print("No")
