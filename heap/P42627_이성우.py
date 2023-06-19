import heapq
def solution(jobs):
    h = []
    answer = 0
    start = -1
    now = i = 0
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(h, [j[1], j[0]])
            
        if len(h) > 0:
            cur = heapq.heappop(h)
            start = now
            now += cur[0]
            answer += now - cur[1]
            i +=1
        else:
            now += 1
                
    return answer//len(jobs)