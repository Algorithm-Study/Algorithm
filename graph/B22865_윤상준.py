import heapq
import sys
INF = sys.maxsize
n = int(input())
a,b,c = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, cost = map(int, input().split())
    graph[x].append((y,cost))
    graph[y].append((x,cost))
def dijkstra(start):
    distance = [INF]*(n+1)
    distance[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_node, dist in graph[node]:
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue,(distance[next_node], next_node))
    return distance
max_distance = -1
answer = -1
dista = dijkstra(a)
distb = dijkstra(b)
distc = dijkstra(c)
for i in range(1,n+1):
    result = min([dista[i], distb[i], distc[i]])
    if result > max_distance:
        max_distance = result
        answer = i
print(answer)
