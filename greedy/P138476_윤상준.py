from collections import Counter, OrderedDict
def solution(k, tangerine):
    answer = 0
    tangerine.sort()
    stock = Counter(tangerine)
    stock = OrderedDict(stock.most_common())
    for s in stock:
        if k -stock[s] <= 0:
            answer += 1
            return answer
        else:
            k -= stock[s]
            answer += 1
    return answer