# 1/4만 구하는 방식으로 해결 가능
from math import sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        hy = int(sqrt(r2**2-i**2))
        if i > r1:
            ly = 0
        else:
            if sqrt(r1**2-i**2) - int(sqrt(r1**2-i**2)) > 0:
                ly = int(sqrt(r1**2-i**2)) + 1
            else:
                ly = int(sqrt(r1**2-i**2))
        answer += hy -ly + 1
    return answer*4