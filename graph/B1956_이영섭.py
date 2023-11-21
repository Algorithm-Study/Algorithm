import sys
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[float('inf')] * V for _ in range(V)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = c

for k in range(V):
    for i in range(V):
        for j in range(V):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

ans = float('inf')
for i in range(V):
    for j in range(V):
        ans = min(ans, graph[i][j] + graph[j][i])

if ans == float('inf'):
    print('-1')
else:
    print(ans)