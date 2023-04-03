def solution(name, yearning, photo):
    answer = []
    chain = {}
    for n, y in zip(name, yearning):
        chain[n] = y
    for ph in photo:
        temp = 0
        for p in ph:
            if p in name:
                temp += chain[p]
        answer.append(temp)
    return answer