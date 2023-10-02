import heapq

n = int(input())
card = []
ans = 0
for _ in range(n):
    heapq.heappush(card, int(input()))
while len(card) > 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    ans += a + b
print(ans)
