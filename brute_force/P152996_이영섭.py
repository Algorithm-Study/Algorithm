from collections import Counter
from itertools import combinations
def solution(weights):
    answer = 0
    siso = {}
    mul = [(2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3)]
    w_counter = Counter(weights)
    for wc in w_counter:
        if w_counter[wc] > 1:
            w_counter[wc] * (w_counter[wc] - 1) // 2
            answer += w_counter[wc] * (w_counter[wc] - 1) // 2
    bf = list(combinations(w_counter, 2))
    for comb in bf:
        for i, j in mul:
            if comb[0] * i == comb[1] * j:
                answer += w_counter[comb[0]] * w_counter[comb[1]]
                break
    return answer

# 문제 접근 방법
# # O(n^2)으로 접근하면 무조건 터짐
# # dict로 조합의 결과를 모은 후에 곱할 수 있는 모든 경우의 수를 탐색