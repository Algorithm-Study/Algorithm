import sys
n, m = map(int, input().split())
graph = [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
result = [['-']*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b, dist = map(int, input().split())
    graph[a][b] = dist
    graph[b][a] = dist
    result[a][b] = str(b)
    result[b][a] = str(a)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                result[i][j] = result[i][k]
for i in range(1,n+1):
    print(*result[i][1:])