from collections import deque, defaultdict
def solution(begin, target, words):
    dq = deque([begin])
    visited = defaultdict(int)

    while dq:
        tmp = dq.popleft()
        if tmp == target:
            return visited[target]

        for word in words:
            cnt = 0
            for i in range(len(word)):
                if tmp[i] != word[i]:
                    cnt += 1
                    
            if cnt == 1 and visited[word] == 0:
                dq.append(word)
                visited[word] = visited[tmp] + 1

    return 0