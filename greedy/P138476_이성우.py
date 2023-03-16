from collections import Counter
def solution(k, tangerine):
    tangerine = Counter(tangerine)
    tangerine_values = tangerine.values()
    tangerine_values = sorted(tangerine_values, reverse = True)
    answer = search(k, tangerine_values)
    return answer

def search(k, tangerine):
    count = 0
    for i in tangerine:
        k -= i
        count += 1
        if k <= 0:
            return count
    # else:
    #     tangerine.pop(0)
    #     return search(k, tangerine)