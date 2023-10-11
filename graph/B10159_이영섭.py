n, m = int(input()), int(input())
board = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    board[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][k] and board[k][j]:
                board[i][j] = 1

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if not board[i][j] and not board[j][i]:
            cnt += 1
    print(cnt - 1)
