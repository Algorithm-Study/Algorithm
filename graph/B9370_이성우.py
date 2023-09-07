import heapq

def dijkstra(start):
    heap = []
    distance = [10**9]*(n+1)
    
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    
    while heap:
        dist, now = heapq.heappop(heap)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))   
    return distance


for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        arr[a].append((b, d))
        arr[b].append((a, d))
        
    dadi = [int(input()) for _ in range(t)] 
    
    s_dist = dijkstra(s)
    g_dist = dijkstra(g)
    h_dist = dijkstra(h)

    answer = []
    for d in dadi:
        if s_dist[g] + g_dist[h] + h_dist[d] == s_dist[d] \
        or s_dist[h] + h_dist[g] + g_dist[d] == s_dist[d]:
            answer.append(d)
                
    answer.sort()
    print(*answer)