n, m = map(int, input().split())
board = [[(float('inf'), i) for i in range(n)] for _ in range(n)]

for i in range(n):
    board[i][i] = (0, '-')

for _ in range(m):
    a, b, cost = map(int, input().split())
    board[a - 1][b - 1] = (cost, b-1)
    board[b - 1][a - 1] = (cost, a-1)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if board[i][j][0] > board[i][k][0] + board[k][j][0]:
                board[i][j] = (board[i][k][0] + board[k][j][0], board[i][k][1])

for i in range(n):
    for j in range(n):
        if board[i][j][1] != '-':
            print(board[i][j][1] + 1, end=" ")
        else:
            print(board[i][j][1], end=" ")
    print()