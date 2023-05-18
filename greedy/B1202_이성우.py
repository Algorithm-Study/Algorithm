import sys
import heapq
input=sys.stdin.readline
n, k = map(int, input().split())
juwelry = []
for _ in range(n):
    heapq.heappush(juwelry, list(map(int, input().split())))
bag = [int(input().rstrip()) for _ in range(k)]
bag.sort()
answer = 0
tmp = []

for b in bag:
    while juwelry:
        if b >= juwelry[0][0]:
            weight, cost = heapq.heappop(juwelry)
            heapq.heappush(tmp, -cost)
        else:
            break
    if tmp:
        answer -= heapq.heappop(tmp)
        
print(answer)