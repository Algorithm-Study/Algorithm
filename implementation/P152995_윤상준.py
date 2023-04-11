# 4,4 2,5 2,4 -> 판별 가능해야 함
def solution(scores):
    wanho = scores[0]
    scores = scores[1:]
    scores.sort(key = lambda x: (-x[0], x[1]))
    answer = 1
    max_val = 0
    for score in scores:
        if sum(wanho) >= sum(score):
            continue
        if wanho[0] < score[0] and wanho[1] < score[1]:
                return -1
        if max_val <= score[1]:
            if sum(wanho) < sum(score):
                answer += 1
            max_val = score[1]
    return answer