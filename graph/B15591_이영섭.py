from collections import deque

n, Q = map(int, input().split())
board = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, q, r = map(int, input().split())
    board[p].append((q, r))
    board[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    visit = [False] * (n+1)
    visit[v] = True
    ans = 0
    dq = deque()
    dq.append((v, float('inf')))

    while dq:
        cx, val = dq.popleft()
        for nx, n_val in board[cx]:
            n_val = min(val, n_val)
            if n_val >= k and not visit[nx]:
                ans += 1
                dq.append((nx, n_val))
                visit[nx] = True
    print(ans)
