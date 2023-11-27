import sys
INF = int(1e9)
# 벨만 포드 알고리즘의 특징
# 1. 음수 가중치가 있는 그래프의 시작 정점에서 다른 정점까지의 최단거리를 구할 수 있음
# 2. 음수 사이클의 존재 여부를 알 수 있음
# 시간복잡도 : O(VE)
n, m = map(int, input().split())
edges = []
distance = [INF]*(n+1)
distance[1] = 0
for _ in range(m):
    edges.append(tuple(map(int, input().split())))
cycle = 0
for i in range(n):
    for j in range(m):
        a, b, cost = edges[j]
        if distance[a] != INF and distance[b] > distance[a] + cost:
            distance[b] = distance[a] + cost
            if i == n-1:
                cycle = 1
if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        print(-1 if distance[i] == INF  else distance[i])