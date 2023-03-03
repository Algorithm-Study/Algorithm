def solution(msg):
    alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lzw = [ _ for _ in alp]
    answer = []
    msg += '0'
    start, end = 0, 1
    while end < len(msg):
        while msg[start:end] in lzw:
            end += 1

        lzw.append(msg[start:end])
        answer.append(lzw.index(msg[start:end-1])+1)
        start, end = end - 1, end

    return answer