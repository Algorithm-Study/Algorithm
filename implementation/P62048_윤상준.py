# 규칙찾기 -> 각 정수 x 좌표 간 차로 갯수를 뺄 경우 시간 초과
# 규칙성을 찾아야 함 -> 직선이 x,y가 정수인 갯수는 2 + gcd - 1 개
# 최데공약수로 나눈 정수 크기의 사각형 최대공약수의 갯수 만큼 생성
import math
def solution(w,h):
    answer = w*h - (w + h - math.gcd(w,h))
    return answer

# 시간 초과 코드
from math import ceil
def solution(w,h):
    answer = w*h
    temp = h
    for i in range(w):
        left = -h/w*i + h
        right = -h/w*(i+1) + h
        answer -= ceil(left - right)
    return answer