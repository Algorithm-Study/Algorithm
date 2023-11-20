N = int(input())
ip = list(map(int, input().split()))
dp = [[0]*21 for _ in range(N)]
dp[0][ip[0]] += 1

for i in range(1, N-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + ip[i] <= 20:
                dp[i][j + ip[i]] += dp[i-1][j]
            if j - ip[i] >= 0:
                dp[i][j - ip[i]] += dp[i-1][j]
print(dp[N-2][ip[N-1]])
