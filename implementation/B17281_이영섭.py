from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())
result = [list(map(int, input().split())) for _ in range(n)]
ans = 0
bf = list(permutations([1, 2, 3, 4, 5, 6, 7, 8]))

for case in bf:  # 모든 타순에 대해
    case = list(case[:3]) + [0] + list(case[3:])
    hitter = 0
    score = 0

    for r in result:  # n번의 이닝을 진행
        out = 0  # 3번의 아웃을 당하면 이닝 종료
        base = [0, 0, 0, 0]
        while out < 3:
            hit = r[case[hitter]]
            if hit == 0:
                # hitter: 현재 타순, case[hitter]: 타석에 선 선수 번호,
                # result[i][case[hitter]]: 현재 이닝에서 타석에 선 선수가 얻을 결과
                out += 1
            elif hit == 1:
                score += base[3]
                base = [0, 1, base[1], base[2]]
            elif hit == 2:
                score += base[2] + base[3]
                base = [0, 0, 1, base[1]]
            elif hit == 3:
                score += base[1] + base[2] + base[3]
                base = [0, 0, 0, 1]
            elif hit == 4:
                score += 1 + base[1] + base[2] + base[3]
                base = [0, 0, 0, 0]
            hitter = (hitter + 1) % 9

    if score > ans:
        ans = score
print(ans)
