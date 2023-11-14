import sys
import heapq
input = sys.stdin.readline

# 초기값 설정
v, e, p = map(int, input().split())
arr = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

# 다익스트라 탐색
def dijkstra(start):
    h = []
    heapq.heappush(h, (0, start))
    distance = [sys.maxsize for _ in range(v+1)]
    distance[start] = 0
    while h:
        dist, now = heapq.heappop(h)
        
        if distance[now] < dist:
            continue
        
        for i in arr[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(h, (cost, i[0]))
        
    return distance

# 최단거리와 건우를 들리는 경로 거리와 같은지 확인
if dijkstra(1)[v] == dijkstra(1)[p] + dijkstra(p)[v]:
    print('SAVE HIM')
else:
    print('GOOD BYE')