from collections import Counter

point = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def check_end_game(board, x):
    for chk in point:
        if x == board[chk[0]]+board[chk[1]]+board[chk[2]]:
            return True
    return False


while True:
    tc = input()
    if tc == 'end':
        break
    tc = list(tc)
    tcCounter = Counter(tc)
    if tcCounter['O'] == tcCounter['X']:
        if check_end_game(tc, 'OOO') and not check_end_game(tc, 'XXX'):
            print('valid')
        else:
            print('invalid')
    elif tcCounter['X'] == 5 and tcCounter['O'] == 4:
        if check_end_game(tc, 'OOO'):
            print('invalid')
        else:
            print('valid')
    elif tcCounter['O'] + 1 == tcCounter['X']:
        if check_end_game(tc, 'XXX') and not check_end_game(tc, 'OOO'):
            print('valid')
        else:
            print('invalid')
    else:
        print('invalid')

# 최종 상태 = 3칸을 이어져 있으며, O가 X보다 같거나 1 작아야 함
