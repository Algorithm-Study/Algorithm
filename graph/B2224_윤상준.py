import sys
INF = sys.maxsize
n,m = map(int, input().split())
distance = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b, dist = map(int, input().split())
    distance[a][b] = dist
for i in range(1,n+1):
    distance[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
_ = int(input())
friends = list(map(int, input().split()))
answer = []
for i in range(1,n+1):
    temp = 0
    for f in friends:
        if f == i or distance[f][i] == INF or distance[i][f] == INF:
            continue
        temp = max(temp ,distance[f][i] + distance[i][f])
    answer.append(temp)
min_time = min(answer)
for i in range(n):
    if answer[i] == min_time:
        print(i+1, end = ' ')