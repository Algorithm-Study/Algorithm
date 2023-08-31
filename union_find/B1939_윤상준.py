import heapq
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(a,b):
    p1,p2 = find(a),find(b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2 

n, m = map(int, input().split())
queue = []
for i in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, [-c, a, b]) 
c1, c2 = map(int, input().split())
answer = 1_000_000_001
parent = [i for i in range(n+1)]
while queue:
    c, a, b = heapq.heappop(queue)
    c = -c
    union(a, b)
    answer = min(answer, c)
    if find(c1) == find(c2):
        break
print(answer)

# MST + 분리집합 문제
# BFS + 이분탐색이나 DFS + 이분탐색 등 다른 풀이로도 문제 해결 가능