# 조건에 맞게 구현하면 끝
def solution(n, words):
    prev = words[0]
    record = [words[0]]
    idx = 0
    for word in words[1:]:
        if prev[-1] != word[0]:
            return [(idx+1)%n + 1, (idx+1)//n+1]
        if word in record:
            return [(idx+1)%n + 1, (idx+1)//n+1]
        record.append(word)
        idx += 1
        prev = word
    return [0,0]