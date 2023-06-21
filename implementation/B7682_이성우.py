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

while True:
    board = input()
    if board == 'end':
        break

    O = board.count('O')
    X = board.count('X')
    dot = board.count('.')
        
    if X - O >= 2 or O - X >= 1:
        print('invalid')
        continue
    if is_win(board, 'X') and O == X:
        print('invalid')
        continue
    if is_win(board, 'O') and O != X:
        print('invalid')
        continue
    if is_win(board, 'O') == False and is_win(board, 'X') == False and dot >= 1:
        print('invalid')
        continue
    print('valid')