import sys
from collections import deque
input = sys.stdin.readline


def bfs(val):
    dq = deque()
    dq.append(X)
    visit = [False] * (N+1)
    visit[X] = True
    while dq:
        x = dq.popleft()
        if x == Y:
            return True
        for y, cost in board[x]:
            if visit[y] or cost < val:
                continue
            dq.append(y)
            visit[y] = 1
    return False


N, M = map(int, input().split())
board = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    board[A].append((B, C))
    board[B].append((A, C))
X, Y = map(int, input().split())
low, high = 0, 1_000_000_000
while low <= high:
    mid = (low + high) // 2
    if bfs(mid):
        low = mid + 1
    else:
        high = mid - 1
print(high)
