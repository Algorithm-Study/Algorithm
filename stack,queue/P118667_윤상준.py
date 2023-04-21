# 불가능하다고 생각되는 Count의 최대값?
from collections import deque
def solution(queue1, queue2):
    count = 0
    mean = sum(queue1) + sum(queue2)
    if mean/2 != mean//2:
        return -1
    mean = mean//2
    if max(max(queue1), max(queue2)) > mean:
        return - 1
    que1= deque(queue1)
    que2= deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    while True:
        if count > 300_000:
            return - 1
        if s1 == s2:
            return count
        if s1 > s2:
            temp = que1.popleft()
            s1 -= temp
            s2 += temp
            que2.append(temp)
            count += 1
        elif s2 > s1:
            temp = que2.popleft()
            s1 += temp
            s2 -= temp
            que1.append(temp)
            count += 1
    return count