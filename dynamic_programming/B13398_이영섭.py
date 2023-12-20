n = int(input())
num = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = num[0]
dp[1][0] = -float('inf')
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1] + num[i], num[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + num[i])
print(max(max(dp[0]), max(dp[1])))