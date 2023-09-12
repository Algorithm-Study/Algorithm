from collections import defaultdict


def dfs_up(i):
    global visit
    cnt = 0
    for idx in board_up[i]:
        if not visit[idx]:
            cnt += 1
            visit[idx] = True
            cnt += dfs_up(idx)
    return cnt


def dfs_down(i):
    global visit
    cnt = 0
    for idx in board_down[i]:
        if not visit[idx]:
            cnt += 1
            visit[idx] = True
            cnt += dfs_down(idx)
    return cnt


N, M = map(int, input().split())
board_up = defaultdict(list)
board_down = defaultdict(list)
visit = defaultdict(bool)

for _ in range(M):
    a, b = map(int, input().split())
    board_up[a].append(b)
    board_down[b].append(a)
ans = 0
for i in range(1, N+1):
    up = dfs_up(i)
    down = dfs_down(i)
    if up + down == N - 1:
        ans += 1
    visit.clear()
print(ans)