import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
answer = []

for i in range(n):
    num = int(input())

    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))

    if right_heap and left_heap[0][1] > right_heap[0][1]:
        min_num = heapq.heappop(right_heap)[1]
        max_num = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-min_num, min_num))
        heapq.heappush(right_heap, (max_num, max_num))
        
    answer.append(left_heap[0][1])

for _ in answer:
    print(_)