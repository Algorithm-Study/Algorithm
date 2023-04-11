n = int(input())
m = [list(map(int, input().split()))for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(n-i):
        x = j + i
        dp[j][x] = float('inf')
        for k in range(j, x):
            dp[j][x] = min(dp[j][x],
                           dp[j][k] + dp[k+1][x] + m[j][0]*m[k][1]*m[x][1])

print(dp[0][n-1])
# for _ in dp:
#     print(*_)
