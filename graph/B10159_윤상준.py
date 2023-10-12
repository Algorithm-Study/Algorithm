import sys
INF = sys.maxsize
n = int(input())
m = int(input())
distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    distance[i][i] = 0
for _ in range(m):
    a,b = map(int, input().split())
    distance[a][b] = 1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if distance[i][j] == INF and distance[j][i] == INF:
            cnt += 1
    print(cnt)