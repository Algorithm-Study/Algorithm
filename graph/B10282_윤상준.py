import heapq
import sys
INF = sys.maxsize
t = int(input())
for _ in range(t):
    n,d,c = map(int, input().split())
    distance = [INF]* (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int, input().split())
        graph[b].append((a,s))
    queue = [(0,c)]
    distance[c] = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if distance[node] < cost:
            continue
        for g, dist in graph[node]:
            new_cost = cost + dist
            if new_cost < distance[g]:
                distance[g] = new_cost
                heapq.heappush(queue,(new_cost,g))
    result = [x for x in distance if x != INF]
    print(len(result), max(result))