from collections import deque
def solution(queue1, queue2):
    q1 = deque(queue1[:])
    q2 = deque(queue2[:])
    sumq1 = sum(q1)
    sumq2 = sum(q2)
    cnt = 0
    
    while sumq1 != sumq2:

        if sumq1 < sumq2 :
            num = q2.popleft()
            sumq2 -= num
            q1.append(num)
            sumq1 += num

        else:
            num = q1.popleft()
            sumq1 -= num
            q2.append(num)
            sumq2 += num
            
        cnt += 1
        
        if cnt > len(queue1)*3-3:
            return -1
        
    return cnt