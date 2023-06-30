import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0 ,1]
dy = [0, -1, 1, 0]
dp = [[0 for _ in range(n)] for _ in range(n)]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[x][y] < arr[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny) + 1)
    return dp[x][y]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))
        
print(answer)