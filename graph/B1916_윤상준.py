import heapq
import sys
INF = sys.maxsize
n = int(input())
m = int(input())
nodes = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    x,y,cost = map(int, input().split())
    nodes[x].append((y,cost))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in nodes[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

start, end = map(int, input().split())            
dijkstra(start)

if distance[end] == INF:
    print('INF')
else:
    print(distance[end])

# sys.maxsize -> 정수 최대값