from itertools import permutations
import sys
input = sys.stdin.readline
n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]
max_score = 0
for case in permutations(range(1,9), 8):
    case = list(case[:3]) + [0] + list(case[3:])
    score, idx = 0, 0
    # 1루 2루 3루
    for i in range(n):
        out = 0
        b1,b2,b3 = 0,0,0
        while out < 3:
            if innings[i][case[idx]] == 0:
                out += 1
            elif innings[i][case[idx]] == 1:
                # 3루에 있는 사람은 홈에 도착
                score += b3
                b1,b2,b3 = 1,b1,b2
            elif innings[i][case[idx]] == 2:
                # 2,3루에 있는 사람은 홈에 도착
                score += b2 + b3
                b1,b2,b3 = 0,1,b1
            elif innings[i][case[idx]] == 3:
                # 1,2,3루 모두 도착
                score += b1 + b2 + b3
                b1,b2,b3 = 0,0,1
            else:
                # 모두 홈에 도착
                score += b1 + b2 + b3 + 1
                b1,b2,b3 = 0,0,0
            idx = (idx + 1)%9 
    max_score = max(max_score, score)
print(max_score)
# 파이썬은 시간 제약이 심한 문제