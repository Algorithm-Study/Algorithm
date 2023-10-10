import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    p, d = map(int, input().split())
    q.append([p, d])
    
q.sort(key=lambda x : x[1])

answer = []
for p, d in q:
    heapq.heappush(answer, p)
    
    if len(answer) > d:
        heapq.heappop(answer)
        
print(sum(answer))