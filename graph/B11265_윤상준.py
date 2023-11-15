n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
for _ in range(m):
    a,b,time = map(int, input().split())
    if graph[a-1][b-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')

