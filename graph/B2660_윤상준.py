import sys
INF = sys.maxsize
n = int(input())
distance = [[INF]*(n+1) for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    distance[a][b] = 1
    distance[b][a] = 1
for i in range(1,n+1):
    distance[i][i] = 0
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                continue
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]
scores = []
for i in range(1,n+1):
    scores.append(max(distance[i][1:]))
president = min(scores)
print(president, scores.count(president))
print(*[x+1 for x in range(n) if scores[x] == president])