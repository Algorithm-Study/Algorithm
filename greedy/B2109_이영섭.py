import heapq

n = int(input())
univ = []
for _ in range(n):
    p, d = map(int, input().split())
    univ.append((p, d))
univ.sort(key=lambda x: (x[1], -x[0]))

pq = []
for p, d in univ:
    heapq.heappush(pq, p)
    if len(pq) > d:
        heapq.heappop(pq)
print(sum(pq))
