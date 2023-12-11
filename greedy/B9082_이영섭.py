T = int(input())
for _ in range(T):
    N = int(input())
    board = [list(input()) for _ in range(2)]
    ans = 0
    for i in range(N):
        board[0][i] = int(board[0][i])

    for i in range(N):
        if i == 0:
            if board[0][i] != 0 and board[0][i+1] != 0:
                board[0][i] -= 1
                board[0][i+1] -= 1
                ans += 1
        elif i == N - 1:
            if board[0][i] != 0 and board[0][i-1] != 0:
                board[0][i-1] -= 1
                board[0][i-2] -= 1
                ans += 1
        else:
            if board[0][i-1] != 0 and board[0][i] != 0 and board[0][i+1] != 0:
                board[0][i-1] -= 1
                board[0][i] -= 1
                board[0][i+1] -= 1
                ans += 1
    print(ans)
