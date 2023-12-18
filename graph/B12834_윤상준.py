import heapq
import sys
INF = sys.maxsize
n, v, e = map(int, input().split())
a, b = map(int, input().split())
teammates = list(map(int, input().split()))
graph = [[] for _ in range(v+1)]
dist_a = [INF]*(v+1)
dist_b = [INF]*(v+1)
for _ in range(e):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

def dijkstra(distance,start):
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for next_node, price in graph[node]:
            new_cost = price + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue,(new_cost, next_node))
    return distance

dist_a = dijkstra(dist_a,a)
dist_b = dijkstra(dist_b,b)
answer = 0
for team in teammates:
    d1 = dist_a[team]
    d2 = dist_b[team]
    if d1 == INF:
        answer -= 1
    else:
        answer += d1
    if d2 == INF:
        answer -= 1
    else:
        answer += d2
print(answer)
