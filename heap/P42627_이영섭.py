import heapq

def solution(jobs):
    answer = 0
    time, idx, idx_j = 0, 0, 0
    jobs.sort()
    pq = []
    while idx_j < len(jobs):
        while idx < len(jobs) and jobs[idx][0] <= time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))
            idx += 1
        if pq:
            jtime, stime = heapq.heappop(pq)
            time += jtime
            answer += time - stime
            idx_j += 1
        else:
            time += 1
    return answer//len(jobs)