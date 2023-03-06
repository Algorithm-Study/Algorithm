def is_win(board, alp):
    wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
    ]
    for win in wins:
        i, j, k = win
        if board[i] == alp and board[j] == alp and board[k] == alp:
            return True
    return False

def solution(board):
    board = "".join(board)
    O = board.count('O')
    X = board.count('X')
        
    if O - X >= 2 or X - O >= 1:
        return 0
    if is_win(board, 'O') and is_win(board, 'X'):
        return 0
    if is_win(board, 'O') and O == X:
        return 0
    if is_win(board, 'X') and O != X:
        return 0
    return 1