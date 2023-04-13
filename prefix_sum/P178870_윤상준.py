# 덱 활용해서 진행해도 시간 초과 발생 -> 모든 경우의 수를 구하면 안 됨
from collections import deque
def solution(sequence, k):
    cases = []
    total = 0 
    point = 0
    for i in range(len(sequence)):
        for j in range(point, len(sequence)):
            if total >= k:
                break
            total += sequence[j]
            point += 1
        if total == k:
            cases.append([i,point-1])
        total -= sequence[i]
    cases.sort(key = lambda x: (x[1])- x[0])
    return cases[0]