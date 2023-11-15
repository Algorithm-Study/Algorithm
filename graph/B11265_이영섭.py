N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dist = [[float('inf')]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = graph[i][j]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for _ in range(M):
    a, b, c = map(int, input().split())
    if dist[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
