import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewerly = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewerly.sort()
bags.sort()
result = 0
tmp = []

for bag in bags:
    while jewerly and jewerly[0][0] <= bag:
        heapq.heappush(tmp, -jewerly[0][1])
        heapq.heappop(jewerly)
    if tmp:
        result -= heapq.heappop(tmp)
print(result)