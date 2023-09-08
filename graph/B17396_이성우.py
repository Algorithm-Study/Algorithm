import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
vision = list(map(int, input().split()))
vision[-1] = 0
arr = [[] for _ in range(n)]
distance = [INF]*n

for _ in range(m):
    a, b, t = map(int, input().split())
    if vision[a] != 1 and vision[b] != 1:
        arr[a].append((t, b))
        arr[b].append((t, a))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = i[0] + dist
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
                
dijkstra(0)
print(distance[n-1] if distance[n-1] != INF else -1)