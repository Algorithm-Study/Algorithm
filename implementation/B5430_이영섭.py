from collections import deque
import ast

first = True
error = False

def reverse():
    global first
    if first == True:
        first = False
    else:
        first = True

T = int(input())

for _ in range(T):
    first = True
    error = False
    p = input()
    n = int(input())
    dq = deque(ast.literal_eval(input()))
    for chr in p:
        if chr == 'R':
            reverse()
        else:
            if len(dq) == 0:
                print("error")
                error = True
                break
            if first == True:
                dq.popleft()
            else:
                dq.pop()
    if len(dq) == 0 and error == False:
        print("[]")
    elif first == True and error != True:
        print(f"[{dq[0]}", end="")
        for val in list(dq)[1:]:
            print(f",{val}", end="")
        print("]")
    elif first == False and error != True:
        dq.reverse()
        print(f"[{dq[0]}", end="")
        for val in list(dq)[1:]:
            print(f",{val}", end="")
        print("]")
        
# 문제 접근 방법
# # C++로 풀었던 문제 -> 배열을 직접 돌리면 시간초과 발생
# # 배열의 앞 부분이 어디인지 파악할 수 있는 boolean 자료형이 있으면 됨
# 새로 배운 python
# # deque은 slicing이 불가능하다 -> slicing을 위해서는 list로 변환해야함