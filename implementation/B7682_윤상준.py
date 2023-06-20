n = input()
while n != 'end':
    x_cross, o_cross = 0, 0
    x = n.count('X')
    o = n.count('O')
    # 갯수는 항상 X가 O와 같거나 하나 더 많아야 함
    if o > x or x-1 > o:
        print('invalid')
    # 가로 빙고 체크
    else:
        for i in range(0,9,3):
            if n[i:i+3] == 'XXX':
                x_cross += 1
            elif n[i:i+3] == 'OOO':
                o_cross += 1
        # 세로 빙고 체크
        for i in range(3):
            if n[i::3] == 'XXX':
                x_cross += 1
            elif n[i::3] == 'OOO':
                o_cross += 1
        # 대각 빙고 체크
        if n[0::4] == 'XXX':
            x_cross += 1
        elif n[0::4] == 'OOO':
            o_cross += 1
        if n[2:7:2] == 'XXX':
            x_cross += 1
        elif n[2:7:2] == 'OOO':
            o_cross += 1
        # 조건에 맞는지 체크
        # x가 2개 빙고를 만든 경우(성공 케이스)
        if x_cross > 1 and x-o == 1:
            print('valid')
        # 빙고가 2개 이상인 경우(부적합)
        elif x_cross + o_cross > 1:
            print('invalid')
        # x가 먼저 빙고를 달성했는데 x와o의 갯수가 같은 경우(부적합)
        elif x_cross == 1 and x == o:
            print('invalid')
        # o가 먼저 빙고를 달성했는데 x가 o의 갯수보다 많은 경우(부적합)
        elif o_cross == 1 and x > o:
            print('invalid')
        # 빙고 갯수가 0개 이지만 빈 공간이 있는 경우(종료 상태 아님)
        elif x_cross + o_cross == 0 and x+o != 9:
            print('invalid')
        else:
            print('valid')
            
    n = input()
# 프로그래머스 혼자서 하는 틱택토와 동일한 문제
# https://school.programmers.co.kr/learn/courses/30/lessons/160585