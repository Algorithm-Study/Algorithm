from math import floor, ceil

def solution(w,h):
    answer = 0
    if w == h:
        return sum(range(1,w))*2

    for i in range(1, w):
        answer += (h*i)//w
    return answer*2
    # out = 0
    # before_y = 0
    # for x in range(1, w+1):
    #     now_y = (h/w) * x
    #     out += ceil(now_y) - floor(before_y)
    #     before_y = now_y
    # return answer - out
    
# 문제 접근 방법
# # 일차 함수로 생각하여 out 개수를 구하고 전체에서 빼려고 했으나 시간초과
# # 빼지말고 함수 가장 아래 정수의 개수만 세주면 아래 타일이므로 * 2