from typing import List
import heapq
def solution(stones: List[int], k: int) -> int:
    answer = []
    heap = []
    for i in range(k):
        heapq.heappush(heap, (-stones[i], i))
        
    answer.append(-heap[0][0])

    for i in range(k, len(stones)):
        heapq.heappush(heap, (-stones[i], i))
        
        while heap[0][1] <= i - k:
            heapq.heappop(heap)
            
        answer.append(-heap[0][0])
    return min(answer)