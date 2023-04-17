from math import sqrt, ceil, floor

def solution(r1, r2):
    answer = 0
    for i in range(1, r1+1):
        y = len(range(ceil(sqrt(r1**2 - i**2)), floor(sqrt(r2**2 - i**2))))
        answer += y + 1
    for i in range(r1+1, r2+1):
        y = floor(sqrt(r2**2 - i**2))
        answer += y + 1
    
    return answer*4

# 문제 접근 방법
# # i, j 모든 점을 살펴보면 시간초과 발생할 것 같아 i일때 r1, r2의 y좌표를 구함
# # 1사분면만 구한 뒤, 4배