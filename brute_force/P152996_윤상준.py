from collections import Counter
from itertools import combinations
import math
def solution(weights):
    weights_list = Counter(weights)
    answer = 0
    for weight in weights_list:
        if weights_list[weight] > 1:
            answer += weights_list[weight] * (weights_list[weight]-1)/2
        for key in weights_list.keys():
            if key <= weight:
                continue
            case1 = set([weight * x for x in range(2,5)])
            case2 = set([key * x for x in range(2,5)])
            if case1 & case2:
                answer+= weights_list[weight] * weights_list[key]
        
    return answer