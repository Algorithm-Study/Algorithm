import heapq
import sys
input = sys.stdin.readline

hq = []
N = int(input())

for i in range(N):
    x = int(input())
    
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if not hq:
            print(0)
        else:
            print(heapq.heappop(hq)[1])
            

# 문제 접근 방법
# # priority queue 구현
# 새로 배운 python
# # heapq와 PriorityQueue를 사용해 쉽게 우선순위 큐 구현 가능