import sys
input = sys.stdin.readline
INF = 1e6

for _ in range(int(input())):
    n, m = map(int, input().split())
    dp = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        dp[a][b] = c
        dp[b][a] = c
        
    k = int(input())
    pos = list(map(int, input().split()))
    for k in range(1, n+1):
        dp[k][k] = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    
    cnt = [0]*(n+1)
    for p in pos:
        for idx in range(1, n+1):
            cnt[idx] += dp[p][idx]
            
    tmp = INF
    answer = 0
    for idx, c in enumerate(cnt):
        if idx > 0 and tmp > c:
            tmp = c
            answer = idx
        
    print(answer)