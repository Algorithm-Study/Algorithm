def solution(order):
    answer = 0
    temp = []
    order = order[::-1]
    for i in range(1,len(order)+1):
        if len(order) == 0:
            break
        if i == order[-1]:
            answer += 1
            order.pop()
        else:
            temp.append(i)
        while len(temp) != 0:
            if temp[-1] == order[-1]:
                temp.pop()
                order.pop()
                answer += 1
            else:
                break
    return answer