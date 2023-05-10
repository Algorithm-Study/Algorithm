import heapq
def solution(n, works):
    works_heapq = [-i for i in works]
    heapq.heapify(works_heapq)
    
    while n:
        num = heapq.heappop(works_heapq)
        if num == 0:
            break
        else:
            num += 1
            n -= 1
            heapq.heappush(works_heapq, num)

    return sum([i**2 for i in works_heapq])