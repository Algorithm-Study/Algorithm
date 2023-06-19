import heapq
def solution(n, s, a, b, fares):
    answer = float('inf')
    arr = [[] for _ in range(n+1)]
    for x, y, c in fares:
        arr[x].append((y, c))
        arr[y].append((x, c))
    
    def dijkstra(start):
        h = []
        distance = [float('inf')]*(n+1)
        route = [[] for _ in range(n+1)]
        distance[start] = 0
        heapq.heappush(h, (0, start))
        while h:
            d, now = heapq.heappop(h)
            
            if distance[now] < d:
                continue
            
            for i in arr[now]:
                cost =  d + i[1]
                if distance[i[0]] > cost:
                    distance[i[0]] = cost
                    heapq.heappush(h, (cost, i[0]))
                    route[i[0]] = now
        return distance
    
    d1 = dijkstra(s)
    for i in range(1, n+1):
        d2 = dijkstra(i)
        answer = min(answer, d2[a] + d2[b] + d1[i])
    return answer