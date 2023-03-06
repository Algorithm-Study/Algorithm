def solution(board):
    b_list = []
    num_x = 0
    num_o = 0
    cross_x = 0
    cross_o = 0
    for i in range(3):
        b_list.append(list(board[i]))
        num_x += list(board[i]).count('X')
        num_o += list(board[i]).count('O')
        if list(board[i]).count('X') == 3:
            cross_x += 1
        if list(board[i]).count('O') == 3:
            cross_o += 1
    if num_x > num_o:
        return 0
    if num_o - 1 > num_x:
        return 0
    #대각선
    if b_list[0][0] == 'O' and b_list[1][1] == 'O' and b_list[2][2] == 'O':
            cross_o += 1
    if b_list[0][0] == 'X' and b_list[1][1] == 'X' and b_list[2][2] == 'X':
            cross_x += 1
    if b_list[0][2] == 'O' and b_list[1][1] == 'O' and b_list[2][0] == 'O':
            cross_o += 1
    if b_list[0][2] == 'X' and b_list[1][1] == 'X' and b_list[2][0] == 'X':
            cross_x += 1
    #세로
    if b_list[0][0] == 'O' and b_list[1][0] == 'O' and b_list[2][0] == 'O':
            cross_o += 1
    if b_list[0][0] == 'X' and b_list[1][0] == 'X' and b_list[2][0] == 'X':
            cross_x += 1
    if b_list[0][1] == 'O' and b_list[1][1] == 'O' and b_list[2][1] == 'O':
            cross_o += 1
    if b_list[0][1] == 'X' and b_list[1][1] == 'X' and b_list[2][1] == 'X':
            cross_x += 1
    if b_list[0][2] == 'O' and b_list[1][2] == 'O' and b_list[2][2] == 'O':
            cross_o += 1
    if b_list[0][2] == 'X' and b_list[1][2] == 'X' and b_list[2][2] == 'X':
            cross_x += 1
    if cross_x + cross_o > 1:
        if cross_o > 1 and num_o-num_x == 1:
            return 1
        return 0
    if cross_x == 1 and num_o > num_x:
        return 0
    if cross_o == 1 and num_o == num_x:
        return 0
    return 1