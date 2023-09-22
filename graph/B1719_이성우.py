n, m = map(int, input().split())

dp = [[float('inf')]*n for _ in range(n)]
answer = [['-']*n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a-1][b-1] = c
    dp[b-1][a-1] = c
    answer[a-1][b-1] = b
    answer[b-1][a-1] = a
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j and dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                answer[i][j] = answer[i][k]

for _ in answer:
    print(*_)