import heapq
import sys
INF = sys.maxsize
n, m, p = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((cost,b))
    graph[b].append((cost,a))

def dijkstra(start, end):
    queue = [(0,start)]
    distance = [INF]*(n+1)
    distance[start] = 0
    while queue:
        cost,node = heapq.heappop(queue)
        for price, next_node in graph[node]:
            new_cost = cost + price
            if new_cost <= distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue,(new_cost, next_node))
    return distance[end]
StoB = dijkstra(1,n)
StoG = dijkstra(1,p)
GtoB = dijkstra(p,n)
if StoB == StoG + GtoB:
    print('SAVE HIM')
else:
    print('GOOD BYE')