import heapq
import sys
INF = sys.maxsize
n, m = map(int, input().split())
is_visible = list(map(int, input().split()))
is_visible[-1]= 0
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int, input().split())
    graph[a].append((b,t))
    graph[b].append((a,t))
queue = [(0,0)]
dist = [INF]*n
dist[0] = 0
while queue:
    cost, next = heapq.heappop(queue)
    if dist[next] < cost:
        continue
    for g,distance in graph[next]:
        if is_visible[g] == 1:
            continue
        new_cost = cost + distance
        if dist[g] > new_cost:
            dist[g] = new_cost
            heapq.heappush(queue,(new_cost,g))
print(dist[-1] if dist[-1] != INF else -1)
