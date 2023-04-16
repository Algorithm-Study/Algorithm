def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[0])
    prev_range = targets[0]
    for target in targets[1:]:
        if target[0] >= prev_range[1]:
            answer += 1
            prev_range = target
        else:
            prev_range = [max(prev_range[0],target[0]), min(prev_range[1], target[1])]
    return answer