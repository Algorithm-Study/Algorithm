import heapq, sys
input = sys.stdin.readline
INF = sys.maxsize

# 다익스트라 구현
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


# 초기값 설정
n, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(v):
    a, b, t = map(int, input().split())
    arr[a].append((t, b))
    arr[b].append((t, a))
     
start, end = map(int, input().split())     
dijkstra(start)
print(distance[end])