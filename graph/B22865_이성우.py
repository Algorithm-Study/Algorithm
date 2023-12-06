import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 초기값 설정
n = int(input())
a, b, c = list(map(int, input().split()))
m = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    d, e, l = map(int, input().split())
    arr[d].append((l, e))
    arr[e].append((l, d))

# 다익스트라 구현
def dijkstra(start):
    q = []
    distance = [INF]*(n+1)
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
                
    return distance


max_ = 0
answer = 0
# 각 집에서의 거리
a = dijkstra(a)
b = dijkstra(b)
c = dijkstra(c)

# 최소값의 최대값 탐색
for i in range(1, n+1):
    if max_ < min(a[i], b[i], c[i]):
        max_ = min(a[i], b[i], c[i])
        answer = i
print(answer)