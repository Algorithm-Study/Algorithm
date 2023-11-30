import heapq
import sys
INF = sys.maxsize
n, m = map(int, input().split())
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
start, end = map(int, input().split())
distance[start] = 0
queue = []
heapq.heappush(queue,(0,start))
while queue:
    cost, node = heapq.heappop(queue)
    if distance[node] < cost:
        continue
    for next_node, price in graph[node]:
        new_cost = cost + price
        if new_cost < distance[next_node]:
            distance[next_node] = new_cost
            heapq.heappush(queue,(new_cost, next_node))
print(distance[end])