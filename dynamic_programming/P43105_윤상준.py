def solution(triangle):
    height = len(triangle)
    for idx, line in enumerate(triangle):
        if idx == 0:
            continue
        for pos, val in enumerate(line):
            if pos == 0:
                line[pos] += triangle[idx-1][0]
            elif len(line)-1 == pos:
                line[pos] += triangle[idx-1][-1]
            else:
                line[pos] += max(triangle[idx-1][pos], triangle[idx-1][pos-1])
    answer = max(triangle[-1])
    return answer