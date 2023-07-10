N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
pipe = [[[0]*3 for _ in range(N)] for _ in range(N)]
pipe[0][1][0] = 1

for i in range(N):
    for j in range(2, N):
        if board[i][j] != 1:
            pipe[i][j][0] = pipe[i][j-1][0] + pipe[i][j-1][2]
            pipe[i][j][1] = pipe[i-1][j][1] + pipe[i-1][j][2]
            if board[i-1][j] == 0 and board[i][j-1] == 0:
                pipe[i][j][2] = pipe[i-1][j-1][0] + pipe[i-1][j-1][1] + pipe[i-1][j-1][2]

print(sum(pipe[N-1][N-1]))
