n = int(input())
data = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
dp[0][0] = data[0]
answer = data[0]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1]+ data[i], data[i])
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + data[i])
    answer = max(answer, dp[0][i], dp[1][i])
print(answer)