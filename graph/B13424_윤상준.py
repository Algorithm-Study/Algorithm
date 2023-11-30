import sys
INF = sys.maxsize
t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    distance = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        distance[i][i] = 0
    for _ in range(m):
        a,b,cost = map(int, input().split())
        distance[a][b] = cost
        distance[b][a] = cost
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    continue
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    min_distance = INF
    result = -1
    friends = int(input())
    rooms = list(map(int, input().split()))
    for i in range(1,n+1):
        temp = sum([distance[i][x] for x in rooms])
        if temp < min_distance:
            result = i
            min_distance = temp
    print(result)