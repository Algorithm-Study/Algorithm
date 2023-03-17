from itertools import combinations
from collections import Counter

def solution(orders, course):
    tmp = []
    answer = []
    for order in orders:
        for c in course:
            tmp += list(combinations(sorted(order), c))
    order_dict = Counter([ "".join(i) for i in tmp])

    order_dict = sorted(order_dict.items(), key = lambda x: (x[1], len(x[0])) ,reverse = True)
    for course_number in course:
        filtered_order = list(filter(lambda x : x[1] > 1 and len(x[0]) ==course_number, order_dict))
        filtered_order = list(filter(lambda x : x[1] == max(i[1] for i in filtered_order), filtered_order))
        answer += [i[0] for i in filtered_order]
    return sorted(answer)