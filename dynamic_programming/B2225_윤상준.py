n, k = map(int, input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(0, n+1):
    for j in range(1,k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] %1_000_000_000)

# 점화식을 세워야 하는 문제