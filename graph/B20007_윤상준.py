import sys
import heapq
INF = sys.maxsize
n, m, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
distance = [INF]*n
distance[y] = 0
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
queue = []
heapq.heappush(queue, (0,y))
while queue:
    c_cost, c_node = heapq.heappop(queue)
    if distance[c_node] < c_cost:
        continue
    for n_node, n_cost in graph[c_node]:
        new_cost = c_cost + n_cost
        if new_cost < distance[n_node]:
            distance[n_node] = new_cost
            heapq.heappush(queue,(new_cost, n_node))
result = sorted([(dist, idx) for idx, dist in enumerate(distance)])
if result[-1][0] * 2 > x:
    print(-1)
else:
    answer = 1
    c_dist = 0
    for dist, idx in result:
        if c_dist + 2*dist <= x:
            c_dist += 2 * dist
        else:
            answer += 1
            c_dist = 2* dist
    print(answer) 
