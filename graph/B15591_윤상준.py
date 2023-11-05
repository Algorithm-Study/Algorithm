import sys
from collections import deque
INF = sys.maxsize
N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))
for _ in range(Q):
    k, v = map(int, input().split())
    queue = deque()
    queue.append((v, INF))
    visited = [0]*(N+1)
    visited[v] = 1
    cost = 0
    while queue:
        node, usado = queue.popleft()
        for next_node, next_usado in graph[node]:
            next_usado = min(usado, next_usado)
            if visited[next_node]:
                continue
            if next_usado >= k:
                cost += 1
                queue.append((next_node, next_usado))
                visited[next_node] = 1
    print(cost)

