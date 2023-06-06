import heapq
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N+1)]
    distance = [float('inf')]*(N+1)
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            
            for i in graph[now]:
                cost = dist + i[1]
                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
                    
    dijkstra(1)

    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer