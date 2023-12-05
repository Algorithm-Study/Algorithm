import sys
input = sys.stdin.readline
INF = sys.maxsize

#초기값 설정
n, m = map(int, input().split())
dp = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = c 
k = int(input())
c = list(map(int, input().split()))

# 최단거리 탐색
for k in range(1, n+1):
    dp[k][k] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

# 왕복시간 최대값 탐색   
city = [0]*(n+1)
for i in range(1, n+1):
    max_val = 0
    for j in c:
        if j != i and dp[j][i] != INF and dp[i][j] != INF:
            max_val = max(max_val, dp[i][j]+dp[j][i])
    city[i] = max_val

# 최대값의 최소값 탐색 후 출력
min_val = min(city[1:])
for i in range(1, n+1):
    if city[i] == min_val:
        print(i, end=' ')