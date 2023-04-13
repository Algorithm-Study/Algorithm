from collections import deque

def move(x, y, dx, dy, board):
    while(board[x+dx][y+dy] != 'D'):
        x += dx
        y += dy
    return x, y

def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                end = (i, j)
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    dq = deque()
    dq.append(start)
    visit = [[0]*len(board[0]) for _ in range(len(board))]
    visit[start[0]][start[1]] = 1
    while dq:
        cx, cy = dq.popleft()
        for dir in range(4):
            nx, ny = cx + dx[dir], cy + dy[dir]
            while True:
                if nx < 0 or ny < 0 or nx >= len(board) or ny >= len(board[0]) or board[nx][ny] == 'D':
                    nx -= dx[dir]
                    ny -= dy[dir]
                    break
                nx += dx[dir]
                ny += dy[dir]
            if visit[nx][ny] > 0:
                continue
            if board[nx][ny] == 'G':
                return visit[cx][cy]
            dq.append((nx, ny))
            visit[nx][ny] = visit[cx][cy] + 1
    return -1

# 문제 접근 방법
# # bfs인데 구슬탈출과 같이 끝까지 굴러가는 bfs