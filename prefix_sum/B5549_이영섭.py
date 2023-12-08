import sys
input = sys.stdin.readline

M, N = map(int, input().split())
K = int(input())
planet = [list(input()) for _ in range(M)]
board = [[[0]*3 for _ in range(N+1)] for _ in range(M+1)]

for i in range(M):
    for j in range(N):
        for k in range(3):
            board[i+1][j+1][k] = board[i+1][j][k] + board[i][j+1][k] - board[i][j][k]
        if planet[i][j] == 'J':
            board[i+1][j+1][0] += 1
        elif planet[i][j] == 'O':
            board[i+1][j+1][1] += 1
        elif planet[i][j] == 'I':
            board[i+1][j+1][2] += 1

for _ in range(K):
    a, b, c, d = map(int, input().split())
    ans = [0, 0, 0]
    for i in range(3):
        ans[i] = board[c][d][i] - board[a-1][d][i] - board[c][b-1][i] + board[a-1][b-1][i]
    print(*ans)
