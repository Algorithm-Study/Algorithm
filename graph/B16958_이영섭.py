import sys
input = sys.stdin.readline

N, T = map(int, input().split())
graph = [[10000]*N for _ in range(N)]
city = []
for _ in range(N):
    s, x, y = map(int, input().split())
    city.append((x, y, s))

for i in range(N):
    for j in range(N):
        if i == j:
            graph[i][j] = 0
        else:
            if city[i][2] == city[j][2] == 1:
                graph[i][j] = min(T, abs(city[i][0] - city[j][0]) + abs(city[i][1] - city[j][1]))
            else:
                graph[i][j] = abs(city[i][0] - city[j][0]) + abs(city[i][1] - city[j][1])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

M = int(input())
for _ in range(M):
    A, B = map(int, input().split())
    print(graph[A-1][B-1])
