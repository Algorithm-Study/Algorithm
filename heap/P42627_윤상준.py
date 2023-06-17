import heapq
def solution(jobs):
    answer = []
    heap = []
    before, current = 0, 0
    while len(answer) < len(jobs):
        for job in jobs:
            if before <= job[0] and job[0] <= current:
                heapq.heappush(heap,(job[1], job[0]))
        if heap:
            time, query = heapq.heappop(heap)
            answer.append(current + time - query)
            before = current+1
            current += time
        else:
            current += 1
    return sum(answer)//len(answer)
# 해당 시간에 처리해야하는 요청 중 짧은 것부터 처리하면 되는 문제