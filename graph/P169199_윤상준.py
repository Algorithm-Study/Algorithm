from collections import deque
def solution(board):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = len(board)
    m = len(board[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for idx, line in enumerate(board):
        if 'R' in line:
            x, y = idx, line.index('R')
        if 'G' in line:
            gx, gy = idx, line.index('G')
    queue = deque()
    queue.append([x,y,0])
    while queue:
        x, y, count = queue.popleft()
        if x == gx and y == gy:
            return count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx< 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 'D':
                continue
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx< 0 or ny < 0 or nx >= n or ny >= m or board[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    if visited[nx][ny] == 0: 
                        queue.append([nx,ny,count+1])
                        visited[nx][ny] = 1
                    break
    return -1