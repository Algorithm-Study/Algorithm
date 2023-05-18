import heapq

N = int(input())
data = []
for _ in range(N):
    num = map(int, input().split())
    for n in num:
        heapq.heappush(data, -n)
for _ in range(N):
    ans = heapq.heappop(data)
print(-ans)