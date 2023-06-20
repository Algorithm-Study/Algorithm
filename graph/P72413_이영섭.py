import heapq

def solution(n, s, a, b, fares):
    answer = 0
    road = [[] for _ in range(n+1)]
    
    for f in fares:
        road[f[0]].append((f[1], f[2]))
        road[f[1]].append((f[0], f[2]))
    
    
    def dijkstra(n, s, e):
        pq = []
        dist = [float('INF') for _ in range(n+1)]
        heapq.heappush(pq, (0, s))
        dist[s] = 0
        while pq:
            val, point = heapq.heappop(pq)
            if dist[point] < val:
                continue
            for r in road[point]:
                cost = val + r[1]
                if cost < dist[r[0]]:
                    dist[r[0]] = cost
                    heapq.heappush(pq, (cost, r[0]))
        return dist[e]
    
    result = []
    for i in range(1, n+1):
        if i != s:
            result.append(dijkstra(n, s, i) + dijkstra(n, i, a) + dijkstra(n, i, b))
        else:
            result.append(dijkstra(n, s, a) + dijkstra(n, s, b))
    return min(result)