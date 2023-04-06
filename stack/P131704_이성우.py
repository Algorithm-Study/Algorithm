def solution(order):
    box = 1
    stack = []
    i = 0
    while box <= len(order):   
        stack.append(box)
        box += 1
        while stack[-1] == order[i]:
            stack.pop()
            i += 1
            if stack == []:
                break
        # print('truck :',truck, 'stack :',stack)
    return i

# 박스 배열을 만들면 시간초과
# order 길이가 길어져서 미리 만들면 느려진다
# while문 조건을 잘 설정하지 않으면 index error가 떠서 조금 어려웠던 문제