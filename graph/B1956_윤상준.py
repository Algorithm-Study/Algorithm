import sys
INF = sys.maxsize
n, m = map(int, input().split())
distance = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b, cost = map(int, input().split())
    distance[a][b] = cost
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
answer = INF
for i in range(1,n+1):
    answer = min(answer, distance[i][i])
print(-1 if answer == INF else answer)