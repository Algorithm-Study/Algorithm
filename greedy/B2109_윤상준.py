import heapq
n = int(input())
request = []
for _ in range(n):
    request.append(list(map(int, input().split())))
request.sort(key=lambda x: x[1])
result = []
for r in request:
    heapq.heappush(result,r[0])
    if r[1] < len(result):
        heapq.heappop(result)
print(sum(result))