import sys
INF = sys.maxsize
n, m = map(int, input().split())
distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    distance[i][i] = 0
for _ in range(m):
    u,v,b = map(int, input().split())
    distance[u][v] = 0
    if b == 1:
        distance[v][u] = 0
    else:
        distance[v][u] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if distance[i][k] + distance[k][j] < distance[i][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
k = int(input())
for _ in range(k):
    s,e = map(int, input().split())
    print(distance[s][e])