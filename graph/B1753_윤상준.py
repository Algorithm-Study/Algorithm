import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)
start = int(input())
for _ in range(E):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
dijkstra(start)

for d in range(1,len(distance)):
    if distance[d] == INF:
        print('INF')
    else:
        print(distance[d])
