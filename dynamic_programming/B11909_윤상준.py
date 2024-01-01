import sys
INF = sys.maxsize
input = sys.stdin.readline
n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(1,n):
    dp[0][i] = dp[0][i-1] + (0 if field[0][i] < field[0][i-1] else field[0][i] - field[0][i-1] + 1)
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + (0 if field[i][0] < field[i-1][0] else field[i][0] - field[i-1][0] + 1)
for i in range(1,n):
    for j in range(1,n):
        left = dp[i][j-1] + (0 if field[i][j] < field[i][j-1] else field[i][j] - field[i][j-1] + 1)
        up =  dp[i-1][j] + (0 if field[i][j] < field[i-1][j] else field[i][j] - field[i-1][j] + 1)
        dp[i][j] = min(left, up)
print(dp[n-1][n-1])