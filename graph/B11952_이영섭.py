import heapq
from collections import defaultdict, deque

N, M, K, S = map(int, input().split())
p, q = map(int, input().split())
dq, graph = deque(), defaultdict(list)
visit = [-1]*(N+1)

# bfs용
for _ in range(K):
    ip = int(input())
    visit[ip] = 0
    dq.append((ip, 0))

# graph 입력
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# bfs
while dq:
    cp, vis = dq.popleft()
    if vis == S:
        continue
    for g in graph[cp]:
        if visit[g] > -1:
            continue
        dq.append((g, vis+1))
        visit[g] = vis + 1

# dijkstra
heap = []
heapq.heappush(heap, [0, 1])
stay = [float('INF')]*(N+1)
stay[1] = 0
while heap:
    cur_cost, cp = heapq.heappop(heap)
    if stay[cp] < cur_cost:
        continue
    for g in graph[cp]:
        if visit[g] == 0:
            new_cost = float('INF')
        elif visit[g] > 0:
            new_cost = q
        else:
            new_cost = p
        cost = cur_cost + new_cost
        if cost < stay[g]:
            stay[g] = cost
            heapq.heappush(heap, [cost, g])

print(stay[N] - (p if visit[N] == -1 else q))