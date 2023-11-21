import sys
input = sys.stdin.readline

v, e = map(int, input().split())
dp = [[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a][b] = c
    
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]
                
                
answer = sys.maxsize
for i in range(1, v+1):
    answer = min(answer, dp[i][i])

if answer != sys.maxsize:  
    print(answer)
else:
    print(-1)