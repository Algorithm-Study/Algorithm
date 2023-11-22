import sys
INF = sys.maxsize
n = int(input())
m = int(input())
distance = [[INF]*(n+1) for _ in range(n+1)]
routes = [[[] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    distance[i][i] = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    distance[a][b] = min(distance[a][b],cost)
    routes[a][b] = [a,b]
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
                routes[i][j] = routes[i][k] + routes[k][j][1:]
for i in range(1,n+1):
    temp = [x if x != INF else 0 for x in distance[i]]
    print(*temp[1:])
for i in range(1,n+1):
    for j in range(1,n+1):
        if distance[i][j] in [0,INF]:
            print(0)
        else:
            print(len(routes[i][j]), *routes[i][j])