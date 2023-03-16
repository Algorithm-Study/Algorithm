from itertools import combinations
from collections import Counter, OrderedDict
def solution(orders, course):
    answer = []    
    for c in course:
        choice = []
        for order in orders:
            str2list = sorted(list(order))
            if len(str2list) < c:
                continue
            choice += list(combinations(str2list,c))
            #print(list(combinations(str2list,3)))
        if len(choice) == 0:
            break
        counter = Counter(choice)
        counter = OrderedDict(counter.most_common())
        #print(counter)
        #print('='*30)
        max_count = 2
        for count in counter:
            #print(count)
            if counter[count] >= max_count:
                answer.append(''.join(list(count)))
                max_count = counter[count]
    answer.sort()
    return answer