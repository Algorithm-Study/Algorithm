from collections import deque

def move_shark(board):
    temp_board = [[[0, 0, 0] for i in range(C)] for j in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != [0, 0, 0]:
                # print(i, j, board[i][j])
                if board[i][j][1] <= 2:
                    if board[i][j][1] == 2: rem = (i + board[i][j][0]) % ((R-1) * 2)
                    else: rem = (2*(R-1)-i + board[i][j][0]) % ((R-1) * 2)
                    if rem >= R-1 and board[i][j][2] > temp_board[2*(R-1) - rem][j][2]:
                        temp_board[2*(R-1) - rem][j] = [board[i][j][0], 1, board[i][j][2]]
                    elif rem < R-1 and board[i][j][2] > temp_board[rem][j][2]:
                        temp_board[rem][j] = [board[i][j][0], 2, board[i][j][2]]
                elif board[i][j][1] >= 3:
                    if board[i][j][1] == 3: rem = (j + board[i][j][0]) % ((C-1) * 2)
                    else: rem = (2*(C-1)-j + board[i][j][0]) % ((C-1) * 2)
                    if rem >= C-1 and board[i][j][2] > temp_board[i][2*(C-1) - rem][2]:
                        temp_board[i][2*(C-1) - rem] = [board[i][j][0], 4, board[i][j][2]]
                    elif rem < C-1 and board[i][j][2] > temp_board[i][rem][2]:
                        temp_board[i][rem] = [board[i][j][0], 3, board[i][j][2]]
    return temp_board

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

R, C, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
board = [[[0, 0, 0] for _ in range(C)] for _ in range(R)]
for sk in shark:
    board[sk[0]-1][sk[1]-1] = [sk[2], sk[3], sk[4]]
# 낚시왕 이동
shark_size = 0
for i in range(C):
    # 상어 잡기
    for j in range(R):
        if board[j][i][2] != 0:
            shark_size += board[j][i][2]
            board[j][i] = [0, 0, 0]
            break
    # 상어 이동
    board = move_shark(board)
    # print_board()
    # print()

print(shark_size)

# 문제 접근 방법
# # bfs로 접근하면 시간초과라서 좌표 값을 수식으로 업데이트