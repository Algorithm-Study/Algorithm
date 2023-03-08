def solution(n, m, section):
    pos = 0
    answer = 0
    i = 0
    while pos <= section[-1]:
        if pos == section[i]:
            answer += 1
            pos += m
            i += 1
        elif pos > section[i]:
            i += 1
        else:
            pos += 1
    return answer