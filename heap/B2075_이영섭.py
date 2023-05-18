import heapq

N = int(input())
data = []
for i in range(N):
    num = list(map(int, input().split()))
    if i == 0:
        for n in num:
            heapq.heappush(data, n)
    else:
        for n in num:
            heapq.heappush(data, n)
            heapq.heappop(data)

print(heapq.heappop(data))