from collections import Counter
def solution(topping):
    answer = 0
    topping_list = Counter(topping)
    left = set()
    for top in topping:
        left.add(top)
        topping_list[top] -= 1
        if topping_list[top] == 0:
            del topping_list[top]
        if len(topping_list) == len(left):
            answer += 1
    
    return answer