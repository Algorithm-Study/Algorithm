import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
inning = [list(map(int, input().split())) for _ in range(n)]

def game(orders):
    idx = 0
    point = 0
    for i in inning:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if i[orders[idx]] == 0:
                out += 1
            elif i[orders[idx]] == 1:
                point += b3
                b1, b2, b3 = 1, b1 ,b2
            elif i[orders[idx]] == 2:
                point += b2 + b3
                b1, b2, b3 = 0, 1 ,b1
            elif i[orders[idx]] == 3:
                point += b1 + b2 + b3
                b1, b2, b3 = 0, 0 ,1
            elif i[orders[idx]] == 4:
                point += 1 + b1 + b2 + b3
                b1, b2, b3 = 0, 0 ,0

            idx = (idx+1)%9
    return point

answer = 0
for cases in permutations(range(1, 9)):
    orders = list(cases)[:3] + [0] + list(cases)[3:]
    answer = max(answer, game(orders))

print(answer)