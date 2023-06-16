import heapq


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
dis = [float('inf')] * (N+1)
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

pq = []
heapq.heappush(pq, (0, 1))
dis[1] = 0
while pq:
    d, now = heapq.heappop(pq)
    if dis[now] < d:
        continue
    for v, w in graph[now]:
        cost = d + w
        if cost < dis[v]:
            dis[v] = cost
            heapq.heappush(pq, (cost, v))

print(dis[N])