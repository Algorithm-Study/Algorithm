import sys
from itertools import combinations
n, m, d = map(int, input().split())
soldiers = 0
field = []
result = 0
for i in range(n):
    temp = list(map(int, input().split()))
    soldiers += temp.count(1)
    field.append(temp)
# 필드를 전치 후 반대로 뒤집어서 진행
field = list(map(list,zip(*field[::-1])))
for positions in combinations([x for x in range(m)],3):
    #복사
    count = 0
    t_field = [x[:] for x in field]
    t_soldiers = soldiers
    while t_soldiers:
        targets = []
        for pos in positions:
            # 거리, x,y 좌표
            target = [d,m+1,0]
            for i in range(m):
                for j in range(n):
                    if t_field[i][j] == 1:
                        distance = abs(pos - i) + j+1
                        if distance < target[0]:
                            target = [distance, i, j]
                        elif distance == target[0]:
                            if i < target[1]:
                                target = [distance, i, j]
            targets.append(target)
        # 타겟 제거
        for target in targets:
            dist, x, y = target
            # 사거리 안에 target이 없는 경우 생략
            if x == m+1:
                continue
            if t_field[x][y] == 1:
                t_field[x][y] = 0
                count += 1
                t_soldiers -= 1
        # 남은 병사 수 갱신
        t_soldiers -= sum([x[0] for x in t_field])
        # 맵 갱신
        for i in range(m):
            t_field[i] = t_field[i][1:] +[0]
    result = max(result, count)
print(result)

# 별첨: Combinations 직접 구현하기
def combinations(array, r):
    for i in range(len(array)):
        if r == 1:  # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i + 1:], r - 1):
                yield [array[i]] + next