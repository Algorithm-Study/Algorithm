from collections import deque
def solution(s):
    answer = 0
    s_queue = deque(s)
    for i in range(len(s)):
        if i != 0:
            temp = s_queue.popleft()
            s_queue.append(temp)
        status = []
        for q in s_queue:
            if status:
                if status[-1] == '[' and q == ']':
                    status.pop()
                elif status[-1] == '{' and q == '}':
                    status.pop()
                elif status[-1] == '(' and q == ')':
                    status.pop()
                else:
                    status.append(q)
            else:
                status.append(q)
        if len(status) ==0:
            answer += 1
    return answer