from collections import Counter

def solution(topping):
    topping_dict = Counter(topping)
    answer = set()
    cnt = 0
    for i in topping:
        topping_dict[i] -= 1
        if topping_dict[i] == 0:
            del topping_dict[i]
        answer.add(i)
        if len(answer) == len(topping_dict):
            cnt += 1

    return cnt