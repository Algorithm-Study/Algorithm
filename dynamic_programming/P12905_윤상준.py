def solution(board):
    max_size = min(len(board), len(board[0]))
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]!= 0:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1])+1
    return max(map(max, board))**2