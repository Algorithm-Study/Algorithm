import heapq

v, e, p = map(int, input().split())
graph = [[] for _ in range(v+1)]
dist = [float('inf') for _ in range(v+1)]


def dijkstra(s):
    pq = []
    heapq.heappush(pq, [0, s])
    dist = [float('inf') for _ in range(v+1)]
    dist[s] = 0
    while pq:
        val, cur = heapq.heappop(pq)
        for nxt, cost in graph[cur]:
            total = val + cost
            if dist[nxt] > total:
                dist[nxt] = total
                heapq.heappush(pq, [total, nxt])
    return dist


for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


if dijkstra(1)[v] == dijkstra(1)[p] + dijkstra(p)[v]:
    print("SAVE HIM")
else:
    print("GOOD BYE")
