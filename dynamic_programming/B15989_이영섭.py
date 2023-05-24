dp = [[0]*3 for _ in range(10001)]
for i in range(1, 4):
    for j in range(i):
        dp[i][j] = 1
for i in range(4, len(dp)):
    dp[i][0] = 1
    dp[i][1] = dp[i-2][0] + dp[i-2][1]
    dp[i][2] = dp[i-3][0] + dp[i-3][1] + dp[i-3][2]
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n][0] + dp[n][1] + dp[n][2])