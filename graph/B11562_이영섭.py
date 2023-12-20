n, m = map(int, input().split())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, v, b = map(int, input().split())
    if b:
        graph[u][v] = 0
        graph[v][u] = 0
    else:
        graph[u][v] = 0
        graph[v][u] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(n+1):
    graph[i][i] = 0

for _ in range(int(input())):
    s, e = map(int, input().split())
    print(graph[s][e])
