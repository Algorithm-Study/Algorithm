def solution(board):
    answer = 0
    max_val = 0
    new_board = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    new_board[0] = board[0]
    for i in range(len(board)):
        new_board[i][0] = board[i][0]
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] != 0:
                new_board[i][j] = min(new_board[i-1][j-1], new_board[i-1][j], new_board[i][j-1]) + 1
    for i in new_board:
        if max(i) > max_val:
            max_val = max(i)
    answer = max_val ** 2
    return answer

# 문제 접근 방법
# # dp로 접근