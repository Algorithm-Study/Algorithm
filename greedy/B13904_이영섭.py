import heapq

N = int(input())
assignment = []
for _ in range(N):
    d, w = map(int, input().split())
    heapq.heappush(assignment, (-w, d))
day = [0] * (max([i[1] for i in assignment])+1)
for _ in range(N):
    w, d = heapq.heappop(assignment)
    while day[d] != 0 and d > 0:
        d -= 1
    day[d] = -w
print(sum(day[1:]))