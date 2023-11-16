from itertools import combinations
n, m = map(int, input().split())
dp = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1
    
for i in range(1, n+1):
    dp[i][i] = 0

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

answer = [0, 0, float('inf')]
for case in combinations(range(1, n+1), 2):
    one, two = case
    tmp = 0
    for i in range(1, n+1):
        tmp += min(dp[i][one], dp[i][two])*2
                    
    if answer[2] > tmp:
        answer = [one, two, tmp]

print(*answer)