import sys
import heapq
from collections import deque
input = sys.stdin.readline

N, M, K, S = map(int, input().split())
p, q = map(int, input().split())

risk = [0]*N # 0 : 안전, 1 : 위험, 2 : 좀비
dq = deque()
for _ in range(K):
    i = int(input()) - 1
    risk[i] = 2
    dq.append((i, 0))

graph = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)
    graph[j-1].append(i-1)

# 위험한 도시 체크
while dq:
    i, s = dq.popleft()
    if s == S:
        continue
    for j in graph[i]:
        if risk[j]:
            continue
        risk[j] = 1
        dq.append((j, s + 1))


dist = [float('inf')]*N
dist[0] = 0
pq = [(0, 0)]
while pq:
    d, i = heapq.heappop(pq)
    if dist[i] < d:
        continue
    for j in graph[i]:
        cost = p if risk[j] == 0 else q if risk[j] == 1 else float('inf')
        if dist[j] > d + cost:
            dist[j] = d + cost
            heapq.heappush(pq, (dist[j], j))

print(dist[N - 1] - (p if risk[N - 1] == 0 else q))