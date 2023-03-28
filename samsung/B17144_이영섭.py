import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
point = []
for i in range(R):
    if board[i][0] == -1:
        point.append(i)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dust_diffusion(board):
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == -1: 
                new_board[i][j] = -1
                continue
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]): continue
                if board[nx][ny] == -1: continue
                new_board[nx][ny] += board[i][j]//5
                cnt += 1
            board[i][j] -= cnt * (board[i][j]//5)
            
    for i in range(len(board)):
        for j in range(len(board[0])):
            if new_board[i][j] == -1: continue
            new_board[i][j] += board[i][j]
    return new_board

def air_cleaner(board, point):
    # 위쪽
    for i in range(point[0]-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(point[0]):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[point[0]][i] = board[point[0]][i-1]
    board[point[0]][1] = 0
    # 아래쪽
    for i in range(point[1]+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, point[1], -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[point[1]][i] = board[point[1]][i-1]
    board[point[1]][1] = 0
    return board

def solution(board, point):
    for i in range(T):
        board = dust_diffusion(board)
        board = air_cleaner(board, point)
    return sum(map(sum, board)) + 2
print(solution(board, point))