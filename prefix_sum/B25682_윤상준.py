import sys
n,m,k = map(int, input().split())
field = [list(input()) for _ in range(n)]
dp =[[0]*(m+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        if (i+j)%2 == 0:
            if field[i-1][j-1] == 'B':
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + 1
        else:
            if field[i-1][j-1] == 'W':
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + 1
min_select, max_select = sys.maxsize, -1
for i in range(k,n+1):
    for j in range(k,m+1):
        min_select = min(min_select, dp[i][j] - dp[i-k][j] - dp[i][j-k] + dp[i-k][j-k])
        max_select = max(max_select, dp[i][j] - dp[i-k][j] - dp[i][j-k] + dp[i-k][j-k])
print(min(min_select, k**2 - max_select))
# 정사각형에 대한 DP 구하기