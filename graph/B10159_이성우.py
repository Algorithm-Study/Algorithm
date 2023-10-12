n = int(input())
m = int(input())

dp = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = -1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][k] == 1 and dp[k][j] == 1:
                dp[i][j] = 1
            elif dp[i][k] == -1 and dp[k][j] == -1:
                dp[i][j] = -1

for i in range(1, n+1):
    print(dp[i].count(0)-2)