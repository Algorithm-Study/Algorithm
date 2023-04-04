from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
magic = list(map(int, input().split()))

def rotate_90(l):
    global board
    sq = 2**l
    le = 2**N
    temp = [[0 for _ in range(le)] for _ in range(le)]
    for i in range(0, le, sq):
        for j in range(0, le, sq):
            for m in range(sq):
                for n in range(sq):
                    temp[i+n][j+sq-1-m] = board[i+m][j+n]
    board = [temp[i][:] for i in range(le)]
    
def check_ice(i, j):
    nx = i
    ny = j
    cnt = 4
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or nx >= 2**N or ny < 0 or ny >= 2**N or board[nx][ny] == 0: cnt -= 1
    if cnt <= 2: return True
    else: return False

def bfs():
    visit = [[0 for _ in range(2**N)] for _ in range(2**N)]
    cnt = 1
    for i in range(2**N):
        for j in range(2**N):
            dq = deque()
            if board[i][j] != 0 and visit[i][j] == 0:
                dq.append((i, j))
                visit[i][j] = cnt
                while dq:
                    cx, cy = dq.popleft()
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if nx < 0 or ny < 0 or nx >= 2**N or ny >= 2**N: continue
                        if board[nx][ny] == 0 or visit[nx][ny] > 0: continue
                        visit[nx][ny] = cnt
                cnt += 1
    val = {i:0 for i in range(1, cnt+1)}
    for i in range(2**N):
        for j in range(2**N):
            if visit[i][j] != 0:
                val[visit[i][j]] += 1
    max_val = 0
    for v in val:
        if val[v] > max_val:
            max_val = val[v]
    return max_val

for mg in magic:
    rotate_90(mg)
    idx = []
    temp = [[0 for _ in range(2**N)] for _ in range(2**N)]
    for i in range(2**N):
        for j in range(2**N):
            if check_ice(i, j) and board[i][j] > 0:
                idx.append((i, j, board[i][j]-1))
    for x, y, val in idx:
        board[x][y] = val

print(sum(map(sum, board)))
print(bfs())

# 문제 접근 방법
# # 회전, check_ice, bfs를 함수로 따로 구현