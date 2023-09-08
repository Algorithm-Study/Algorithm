from collections import defaultdict
import heapq

n, m = map(int, input().split())
ward = list(map(int, input().split()))
dist = [float('inf')]*n
board = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, input().split())
    board[a].append((b, t))
    board[b].append((a, t))

pq = [(0, 0)]
dist[0] = 0
while pq:
    dis, idx = heapq.heappop(pq)
    if dist[idx] < dis:
        continue
    for nxt, ndis in board[idx]:
        if nxt != n-1 and ward[nxt]:
            continue
        new_dis = ndis + dis
        if dist[nxt] > new_dis:
            dist[nxt] = new_dis
            heapq.heappush(pq, (new_dis, nxt))

if dist[-1] == float('inf'):
    print(-1)
else:
    print(dist[-1])
