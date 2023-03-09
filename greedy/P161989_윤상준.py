#한번 칠한 경우 고려안하는 방식 채용
def solution(n, m, section):
    answer = 1
    start = min(section)
    end = max(section)
    while start < end:
        erase = start + m - 1
        if len(section) == 0:
            break
        current = section.pop(0)
        if current > erase:
            start = current
            answer += 1
    return answer