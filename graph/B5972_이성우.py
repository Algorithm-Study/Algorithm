import heapq

# 초기 변수값
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [float('inf')]*(n+1)

# 간선 연결
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

# 최단 경로 탐색
def dijkstra(start: int) -> None:
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1)
print(distance[-1])