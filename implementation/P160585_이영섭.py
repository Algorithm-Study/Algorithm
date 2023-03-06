from collections import Counter

chk_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

def check_end_game(board, x):
    for chk in chk_list:
        if x == board[chk[0]]+board[chk[1]]+board[chk[2]]:
            return True
    return False

def solution(board):
    answer = 1
    split_board = []
    for line in board:
        split_board.extend(list(line))
    counter = Counter(split_board)
    if counter["O"] - counter["X"] == 1:
        if check_end_game(split_board, "XXX"):
            answer = 0
    elif counter["O"] == counter["X"]:
        if check_end_game(split_board, "OOO"):
            answer = 0
    else:
        answer = 0
    return answer

# 문제 접근 방법
# O가 X보다 같거나 1개 많아야 함
# # 같다면 O나 X가 3개가 만들어지면 안됨
# # 1개 많다면 X가 3개 만들어지면 안됨
# 새로 배운 python
# # 문자열에 list 함수를 취하면 한글자씩 나눠짐(공백도 포함하므로 공백을 제거하려면 split)