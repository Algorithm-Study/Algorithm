import heapq
import sys
INF = sys.maxsize
t = int(input())
def dijkstra():
    queue = [(0,0)]
    distance[0] = 0
    while queue:
        cost, current = heapq.heappop(queue)
        if distance[current] < cost:
            continue
        for next_node, price in graph[current]:
            new_cost = price + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(queue, (new_cost, next_node))
                route[next_node] = current 
for _ in range(1,t+1):
    m, n = map(int, input().split())
    graph = [[] for _ in range(n)]
    distance = [INF]*n
    route = [-1] *n
    for __ in range(m):
        a,b,cost = map(int, input().split())
        graph[a].append((b,cost))
        graph[b].append((a,cost))
    dijkstra()
    if distance[-1] == INF:
        print(f'Case #{_}: -1')
    else:
        routes = []
        current = n -1
        while current != -1:
            routes.append(current)
            current = route[current]
        routes = routes[::-1]
        print(f'Case #{_}:', *routes)