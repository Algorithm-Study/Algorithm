N = int(input())
P = list(map(int, input().split()))
M = int(input())

dp = [-1] * (M+1)
for i in range(N-1, -1, -1):
    x = P[i]
    for j in range(x, M+1):
        dp[j] = max(dp[j-x]*10 + i, i, dp[j])
print(dp[M])
