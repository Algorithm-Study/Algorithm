num = int(input())

dp = []
for _ in range(num):
    dp.append(list(map(int, input().split())))


for i in range(1,num):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + dp[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + dp[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + dp[i][2]
print(min(dp[num - 1][0], dp[num - 1][1], dp[num - 1][2]))