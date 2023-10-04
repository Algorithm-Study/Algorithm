import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
q = []

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1
    
for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

answer = []
while q:
    x = heapq.heappop(q)
    answer.append(x)
    for i in arr[x]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(*answer)