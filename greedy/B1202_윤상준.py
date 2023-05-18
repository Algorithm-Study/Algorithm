import heapq
n, k = map(int, input().split())
jewels = []
for _ in range(n):
    heapq.heappush(jewels, list(map(int, input().split())))
bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()
total = 0
candidates = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        heapq.heappush(candidates, -heapq.heappop(jewels)[1])
    if candidates:
        total -= heapq.heappop(candidates)
print(total)

# 최대 힙과 최소 힙을 병행해서 문제 풀이
# 가방 안에 들어갈 수 있는 보석들 중에서 가장 가치가 큰 것을 넣는 방식으로 진행
# 작은 가방부터 시작해서 진행해야 문제 해결 가능