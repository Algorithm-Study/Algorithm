import sys
sys.setrecursionlimit(10**5)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y):
    if visit[x][y]:
        return visit[x][y]
    visit[x][y] = 1

    for di in range(4):
        nx = x + dx[di]
        ny = y + dy[di]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if board[x][y] < board[nx][ny]:
            visit[x][y] = max(visit[x][y], dfs(nx, ny) + 1)
    return visit[x][y]


ans = [1]
for i in range(n):
    for j in range(n):
        if not visit[i][j]:
            dfs(i, j)
print(max([max(visit[i]) for i in range(n)]))