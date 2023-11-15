import sys
INF = sys.maxsize
n, m = map(int, input().split())
graph = [[INF]*n for _ in range(n)]
for i in range(n):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
possible = []
for i in range(n):
    for j in range(i+1,n):
        count = 0
        if i != j:
            for k in [x for x in range(n) if x not in [i,j]]:
                count += min(graph[k][i], graph[k][j])
            count *= 2
            possible.append((count,i,j))
possible.sort(key = lambda x : (x[0], x[1], x[2]))

print(possible[0][1]+1, possible[0][2]+1, possible[0][0])