import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[[False]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)
q = deque()

def init():
    rx, ry, bx, by = [0] * 4 # 초기화 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': # board에 빨간 구슬이라면 좌표 값 저장
                rx, ry = i, j
            elif board[i][j] == 'B': # board에 파란 구슬이라면 좌표 값 저장
                bx, by = i, j
    q.append((rx, ry, bx, by, 1)) # 위치 정보와 depth
    visited[rx][ry][bx][by] = True
    
def move(x, y, dx, dy):
    count = 0 # 이동한 칸 수 
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    init()
    while q: # BFS -> queue, while
        rx, ry, bx, by, depth = q.popleft() # FIFO
        if depth > 10: # 10 이하여야 한다.
            break
        for i in range(4): # 4방향으로 시도한다.
            next_rx, next_ry, r_count = move(rx, ry, dx[i], dy[i]) # RED
            next_bx, next_by, b_count = move(bx, by, dx[i], dy[i]) # BLUE
                        
            if board[next_bx][next_by] == 'O': # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if board[next_rx][next_ry] == 'O': # 빨간 구슬이 구멍에 떨어진다면(성공)
                print(depth)
                return
            if next_rx == next_bx and next_ry == next_by : # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count: # 이동 거리가 많은 구슬을 한칸 뒤로
                    next_rx -= dx[i]
                    next_ry -= dy[i]
                else:
                    next_bx -= dx[i]
                    next_by -= dy[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_rx][next_ry][next_bx][next_by]:
                visited[next_rx][next_ry][next_bx][next_by] = True
                q.append((next_rx, next_ry, next_bx, next_by, depth +1))
    print(-1) # 실패 

bfs()