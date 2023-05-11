from collections import deque
def solution(begin, target, words):
    length = len(begin)
    queue = deque()
    queue.append([begin, 0])
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        new_words = []
        for word in words:
            compare = sum([0 if word[x] == current[x] else 1 for x in range(length)])
            if compare == 1:
                queue.append([word, count+1])
            else:
                new_words.append(word)
        words = new_words[:]
    return 0
# 탐색해서 하나만 변경된 단어인 경우 덱에 추가
# 아닌 경우는 new_words에 임시저장한 이후 갱신