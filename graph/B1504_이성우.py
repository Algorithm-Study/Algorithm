import heapq

def dijkstra(start):
    distances = [float('inf')]*(N+1)
    distances[start] = 0
    q = [(0, start)]
    
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for node, d in graph[now]:
            cost = dist + d
            if cost < distances[node]:
                distances[node] = cost
                heapq.heappush(q, (cost, node))

    return distances

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
origin_d = dijkstra(1)
v1_d = dijkstra(v1)
v2_d = dijkstra(v2)

v1_path = origin_d[v1] + v1_d[v2] + v2_d[N]
v2_path = origin_d[v2] + v2_d[v1] + v1_d[N]

answer = min(v1_path, v2_path)
print(answer if answer < float('inf') else -1)