import heapq, sys
input = sys.stdin.readline
INF = sys.maxsize

n, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF]*(n+1)
parent = [0]*(n+1)

for _ in range(v):
    a, b, t = map(int, input().split())
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
                parent[i[1]] = now

dijkstra(1)
print(n-1)
for i in range(2, n+1):
    print(i, parent[i])