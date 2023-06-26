import sys
from collections import deque
import heapq
INF = sys.maxsize
n,m,k,s = map(int, input().split())
p, q = map(int, input().split())
zombies = [0]*(n+1)
danger = [0]*(n+1)
graphs = [[] for _ in range(n+1)]
queue = deque()
for _ in range(k):
    city = int(input())
    zombies[city] = 1
    queue.append((city, 0))
for _ in range(m):
    a,b = map(int, input().split())
    # 비용은 bfs 결과에 따라 달라지므로 연결관계만 저장
    graphs[a].append(b)
    graphs[b].append(a)
while queue:
    start, route = queue.popleft()
    if route == s:
        continue
    for g in graphs[start]:
        # 이미 위험도시 거나 좀비에 점령당한 곳이면 반복 필요 X
        if zombies[g] or danger[g]:
            continue
        danger[g] = 1
        queue.append((g, route + 1))
distance = [INF] *(n+1)
distance[1] = 0
heap = [(0,1)]
while heap:
    cost, start = heapq.heappop(heap)
    if distance[start] < cost:
        continue
    for g in graphs[start]:
        if zombies[g]:
            new_cost = INF
        elif danger[g]:
            new_cost = cost + q
        else:
            new_cost = cost + p
        if distance[g] > new_cost:
            distance[g] = new_cost
            heapq.heappush(heap, (new_cost, g))

if danger[n]:
    print(distance[n]- q)
else:
    print(distance[n]- p)
# 1.bfs로 위험도시 목록을 구한다.
# 2. 다익스트라로 최소 비용 계산한다.
# 단 도착지점에 도달하면 끝이므로 도착 도시의 숙박비는 빼고 출력한다.