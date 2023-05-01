from collections import defaultdict
def solution(n, words):
    answer = [0, 0]
    word = defaultdict(int)
    for idx, wd in enumerate(words):
        word[wd] += 1
        if idx == 0:
            last_char = wd[-1]
            continue
        if word[wd] > 1 or last_char != wd[0]:
            return [idx % n + 1, idx // n + 1]
        last_char = wd[-1]
    return answer