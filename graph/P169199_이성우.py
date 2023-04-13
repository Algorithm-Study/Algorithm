from collections import deque

def solution(board):
    answer = 0
    r = len(board)
    c = len(board[0])
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                x0, y0 = i, j
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    def bfs():
        dq = deque()
        dq.append([x0, y0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        visited[x0][y0] = 1 
        while dq:
            x, y = dq.popleft()
            if board[x][y] == 'G':
                return visited[x][y] - 1

            for i in range(4):
                nx , ny = x, y
                while True:
                    nx, ny = nx+dx[i], ny+dy[i]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx >= r or ny < 0 or ny >= c:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    dq.append([nx, ny])
        return -1
    
    answer = bfs()
        
    return answer

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board))
board = [".D.R", "....", ".G..", "...D"]
print(solution(board))