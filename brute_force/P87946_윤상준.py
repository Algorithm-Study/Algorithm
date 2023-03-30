from itertools import permutations
def solution(k, dungeons):
    answer = -1
    cases = []
    for i in range(len(dungeons),0, -1):
        for p in permutations(dungeons, i):
            cases.append(list(p))
    for case in cases:
        current_visit = 0
        temp = k
        for c in case:
            if c[0] <= temp:
                temp -= c[1]
                current_visit +=1
        #print(case, current_visit)
        answer = max(answer, current_visit)
    return answer
        