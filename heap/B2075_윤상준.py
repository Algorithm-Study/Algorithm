import heapq
n = int(input())
queue = list(map(int, input().split()))
heapq.heapify(queue)
for _ in range(n-1):
    line = list(map(int, input().split()))
    for l in line:
        heapq.heappush(queue, l)
        heapq.heappop(queue)
print(heapq.heappop(queue))
# 메모리 때문에 heapq 크기를 작게 유지해야 함