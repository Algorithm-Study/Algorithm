n, m, r = map(int, input().split())
item = list(map(int, input().split()))
road = [[float('inf')]*(n+1) for _ in range(n+1)]
dist = [[0]*(n+1) for _ in range(n+1)]
ans = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    road[a][b] = l
    road[b][a] = l

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            dist[i][j] = 0
        elif road[i][j] != float('inf'):
            dist[i][j] = road[i][j]
        else:
            dist[i][j] = float('inf')

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            cnt += item[j-1]
    if cnt > ans:
        ans = cnt
print(ans)
