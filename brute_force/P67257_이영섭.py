from itertools import permutations
from collections import deque

def solution(expression):
    answer = 0
    temp = ''
    expression_list = []
    cnt = 0
    for ep in expression:
        if not (ep == "+" or ep == "-" or ep == "*"):
            temp += ep
        else:
            expression_list.append(temp)
            expression_list.append(ep)
            temp = ''
    expression_list.append(temp)
    oper = ["+", "-", "*"]
    for op in oper:
        if op not in expression_list:
            oper.remove(op)
    bf = list(permutations(oper))
    for case in bf:
        new_ep = deque(expression_list[:])
        idx = 0
        for op in case:
            temp = deque()
            while new_ep:
                if new_ep[0] == op:
                    fir = temp.pop()
                    ope = new_ep.popleft()
                    two = new_ep.popleft()
                    temp.append(eval(str(fir)+str(ope)+str(two)))
                else:
                    val = new_ep.popleft()
                    temp.append(val)
            new_ep = temp
        answer = max(answer, abs(int(new_ep[0])))
    return answer