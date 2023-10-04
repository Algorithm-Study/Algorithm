from collections import defaultdict
import heapq

N, M = map(int, input().split())
board = defaultdict(list)
ready = [0] * (N+1)
pq = []

for _ in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    ready[b] += 1

for i in range(1, N + 1):
    if ready[i] == 0:
        heapq.heappush(pq, i)

ans = []
while pq:
    tp = heapq.heappop(pq)
    ans.append(tp)
    for nxt in board[tp]:
        ready[nxt] -= 1
        if ready[nxt] == 0:
            heapq.heappush(pq, nxt)

print(*ans)
