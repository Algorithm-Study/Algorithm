from collections import deque

def check(s):
    list = []
    for ch in s:
        if ch == "(" or ch == "{" or ch == "[":
            list.append(ch)
        elif len(list) > 0 and list[-1] == "(" and ch == ")":
            list.pop()
        elif len(list) > 0 and list[-1] == "{" and ch == "}":
            list.pop()
        elif len(list) > 0 and list[-1] == "[" and ch == "]":
            list.pop()
        else:
            return 0
    if len(list) != 0:
        return 0
    return 1

def solution(s):
    dq = deque(s)
    answer = 0
    length = len(dq)
    answer += check(dq)
    for i in range(1, length):
        dq.rotate(-1)
        answer += check(dq)
    return answer

# 문제 접근 방식
# # s의 길이가 1000이므로 완전 탐색으로 풀어도 백만
# # runtime error: 생성 함수의 return 값이 없는 경우가 있는지 고려
# # test 13: stack이 비었는지 확인 해줘야 함
# 새로 배운 python
# # deque에는 rotate라는 함수가 존재하여 -는 왼쪽꺼를 빼서 오른쪽으로 넣고 
# # +는 오른쪽꺼를 빼서 왼쪽에 넣음