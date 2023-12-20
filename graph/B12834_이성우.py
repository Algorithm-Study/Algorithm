import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 초기값 설정
n, v, e = map(int, input().split())
a, b = map(int, input().split())
h = list(map(int, input().split()))
arr = [[] for _ in range(v+1)]
for _ in range(e):
    x, y, l = map(int, input().split())
    arr[x].append((l, y))
    arr[y].append((l, x))
answer = 0

# 다익스트라 구현
def dijkstra(start):
    q = [(0, start)]
    distance = [INF]*(v+1)
    distance[start] = 0
    
    while q:
        cost, now = heapq.heappop(q)
        
        if distance[now] < cost:
            continue
        
        for node in arr[now]:
            new_cost = cost + node[0]
            
            if new_cost < distance[node[1]]:
                heapq.heappush(q, (new_cost, node[1]))
                distance[node[1]] = new_cost
                
    return distance

# KIST, 푸드씨알에서 각 집까지 거리 계산
dist_a = dijkstra(a)
dist_b = dijkstra(b)
for member in h:
    x = dist_a[member]
    y = dist_b[member]
    if x == INF:
        answer -= 1
    else:
        answer += x
    if y == INF:
        answer -= 1
    else:
        answer += y
print(answer)