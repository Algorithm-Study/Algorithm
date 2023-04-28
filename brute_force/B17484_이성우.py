N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf'),float('inf'),float('inf')] for _ in range(M)] for _ in range(N+1)]

dp[0] = [[0, 0, 0] for _ in range(M)]
    
for i in range(1,N+1):
    for j in range(M):
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1],dp[i-1][j+1][2]) + maps[i-1][j]
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1],dp[i-1][j-1][0]) + maps[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0],dp[i-1][j][2]) + maps[i-1][j]
    
answer = float('inf')
for cases in dp[N]:
    for case in cases:
        answer = min(answer,case)
print(answer)