import sys
INF = sys.maxsize
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(r):
    a,b, far = map(int, input().split())
    dist[a][b], dist[b][a] = far,far
# 자기 자신 0으로 설정
for i in range(1,n+1):
    dist[i][i] = 0
# 플로이드 워셜 진행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
max_item = 0
# 각 시작 위치에서의 아이템 획득 수 체크
for i in range(1,n+1):
    temp = sum([items[x-1] if dist[i][x] <= m else 0 for x in range(1,n+1)])
    max_item = max(max_item,temp)
print(max_item)