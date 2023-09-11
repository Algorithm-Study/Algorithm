from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def set_it_path():
    move_num_a, move_num_b = [], []
    cnt, d_idx = 0, 0
    for i in range(1, n*2):
        if i % 2 == 1 and i != n * 2 - 1:
            cnt += 1
        move_num_a.append(cnt)
    for i in range(n*2 - 1, 0, -1):
        if i % 2 == 0 and i != n * 2 - 2:
            cnt -= 1
        move_num_b.append(cnt)

    sx, sy, sd = n // 2, n // 2, -2
    dq = deque([(sx, sy, sd)])
    for i, move in enumerate(move_num_a):
        for idx in range(move):
            cx, cy, di = dq.popleft()
            it_path.append((cx, cy, di))
            if idx == move - 1:
                break
            dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], di))
        if i == len(move_num_a) - 1:
            dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], rev_dict[(dir_dict[di] + 2) % 4]))
            break
        dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], rev_dict[(dir_dict[di] + 1) % 4]))

    for i, move in enumerate(move_num_b):
        for idx in range(move):
            cx, cy, di = dq.popleft()
            it_path.append((cx, cy, di))
            if idx == move - 1:
                break
            dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], di))
        if i == len(move_num_b) - 1:
            dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], rev_dict[(dir_dict[di] - 2) % 4]))
            break
        dq.append((cx + dx[dir_dict[di]], cy + dy[dir_dict[di]], rev_dict[(dir_dict[di] - 1) % 4]))


def move_hider(turn):
    for idx, (hx, hy, hd) in enumerate(hider):
        if abs(it_path[turn][0] - hx) + abs(it_path[turn][1] - hy) > 3:
            continue
        nx, ny = hx + dx[dir_dict[hd]], hy + dy[dir_dict[hd]]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            hd = -hd
            nx, ny = hx + dx[dir_dict[hd]], hy + dy[dir_dict[hd]]
        if not (it_path[turn][0] == nx and it_path[turn][1] == ny):
            hider[idx] = (nx, ny, hd)


def get_point(turn):
    global hider
    point = 0
    cx, cy = it_path[turn][0], it_path[turn][1]
    out_idx = []
    for idx, (hx, hy, hd) in enumerate(hider):
        if cx == hx and cy == hy:
            if (cx, cy) in tree and tree[(cx, cy)] == 0:
                point += turn
                out_idx.append(idx)
    new_hider = []
    for i, h in enumerate(hider):
        if i in out_idx:
            continue
        new_hider.append(h)
    hider = new_hider

    out_idx = []
    for i in range(2):
        cx, cy = cx + dx[dir_dict[it_path[turn][2]]], cy + dy[dir_dict[it_path[turn][2]]]
        for idx, (hx, hy, hd) in enumerate(hider):
            if cx == hx and cy == hy:
                if (cx, cy) in tree and tree[(cx, cy)] == 0:
                    point += turn
                    out_idx.append(idx)
    new_hider = []
    for i, h in enumerate(hider):
        if i in out_idx:
            continue
        new_hider.append(h)
    hider = new_hider

    return point


# 입력
n, m, h, k = map(int, input().split())
hider, tree = [], {(i, j): 0 for i in range(n) for j in range(n)}
dir_dict, rev_dict = {-2: 0, 1: 1, 2: 2, -1: 3}, {0: -2, 1: 1, 2: 2, 3: -1}
# 1은 좌우, 2는 상하
for _ in range(m):
    x, y, d = map(int, input().split())
    hider.append((x-1, y-1, d))
for _ in range(h):
    x, y = map(int, input().split())
    tree[(x-1, y-1)] = 1
# k번 째 턴의 술래의 위치
it_path = []
set_it_path()
while len(it_path) < 101:
    it_path += it_path
it_path = it_path[:101]

# 턴을 진행
ans = 0
for t in range(k):
    if t != 0:
        ans += get_point(t)
    move_hider(t)
ans += get_point(k)
print(ans)
