import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
new_board = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        new_board[i][j] = new_board[i][j-1] + new_board[i-1][j] - new_board[i-1][j-1] + board[i-1][j-1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    ans = new_board[x2][y2] - new_board[x1-1][y2] - new_board[x2][y1-1] + new_board[x1-1][y1-1]
    print(ans)