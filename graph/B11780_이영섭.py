n = int(input())
m = int(input())

dist = [[float('inf')]*n for _ in range(n)]
path = [[-1]*n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a-1][b-1] = min(dist[a-1][b-1], c)
    path[a-1][b-1] = a-1

for k in range(n):
    dist[k][k] = 0
    path[k][k] = -1
    for i in range(n):
        for j in range(n):
            di = dist[i][k] + dist[k][j]
            if dist[i][j] > di:
                dist[i][j] = di
                path[i][j] = path[k][j]

for i in range(n):
    for j in range(n):
        if dist[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()

for i in range(n):
    for j in range(n):
        if path[i][j] == -1:
            print(0)
            continue
        v = j
        ans = []
        while True:
            if v == i:
                break
            ans.append(v+1)
            v = path[i][v]
        print(len(ans)+1, i + 1, *ans[::-1])

