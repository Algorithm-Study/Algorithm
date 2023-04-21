from collections import deque

def solution(queue1, queue2):
    sq1, sq2 = sum(queue1), sum(queue2)
    if (sq1 + sq2) % 2 != 0:
        return -1
    queue1, queue2 = deque(queue1), deque(queue2)
    
    for i in range(len(queue1)*2 + len(queue2)*2 + 1):
        if sq1 > sq2:
            temp = queue1.popleft()
            queue2.append(temp)
            sq1, sq2 = sq1-temp, sq2+temp
        elif sq1 < sq2:
            temp = queue2.popleft()
            queue1.append(temp)
            sq1, sq2 = sq1+temp, sq2-temp
        else:
            return i
        
    return -1