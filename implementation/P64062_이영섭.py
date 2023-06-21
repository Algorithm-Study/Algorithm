from collections import deque

def solution(stones, k):
    answer = 200000001
    dq = deque()
    for idx, i in enumerate(stones):
        while dq:
            if i > dq[-1][0]:
                dq.pop()
            else:
                break
        # print('len', len(dq))
        if dq and (idx-k >= dq[0][1] or len(dq) == k):
            dq.popleft()
        dq.append((i, idx))
        if idx >= k-1 and dq:
            answer = min(answer, dq[0][0])
        # print(dq, answer, len(dq))
    return answer