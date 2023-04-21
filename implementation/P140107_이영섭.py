from math import sqrt

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        answer += int(sqrt(d**2 - i**2) // k + 1)
    return answer