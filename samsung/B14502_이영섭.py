from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

def bfs(new_board, dq):
    while dq:
        cx, cy = dq.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if new_board[nx][ny] != 0: continue
            dq.append((nx, ny))
            new_board[nx][ny] = 2
    cnt = 0
    for i in range(N):
        for j in range(M):
            if new_board[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
blank, start = [], []
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blank.append((i, j))
        elif board[i][j] == 2:
            start.append((i, j))
bf = list(combinations(blank, 3))

max_val = 0
for case in bf:
    dq = deque()
    new_board = [board[i][:] for i in range(N)]
    for px, py in case:
        new_board[px][py] = 1
    for sx, sy in start:
        dq.append((sx, sy))
    bfs_val = bfs(new_board, dq)
    max_val = max(max_val, bfs_val)
# print(case, bfs_val)
print(max_val)

# 문제 접근 방법
# # 공란 3개를 골라 벽을 세웠을 때, 안전지대의 최댓값
# # 완전탐색 -> 케이스 별로 bfs