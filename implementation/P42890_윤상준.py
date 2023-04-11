from itertools import combinations
def solution(relation):
    row, col = len(relation), len(relation[0])
    #가능한 모든 조합 경우의 수 계산
    cases = []
    for i in range(1,col+1):
        cases.extend(combinations(range(col), i))
    possible = []
    for case in cases:
        temp = set([tuple(relate[i] for i in case) for relate in relation])
        if len(temp) == row:
            possible.append(case)
    result = set(possible)
    for i in range(len(possible)):
        for j in range(i+1, len(possible)):
            if len(possible[i]) == len(set(possible[i]) & set(possible[j])):
                result.discard(possible[j])
    return len(result)