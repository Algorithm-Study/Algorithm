import sys
from itertools import combinations
from collections import deque
INF = sys.maxsize
n = int(input())
population = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
result = INF
def bfs(group):
    queue = deque()
    queue.append(group[0])
    visited = set([group[0]])
    num = 0
    while queue:
        current = queue.popleft()
        num += population[current]
        for node in graph[current]:
            if node not in visited and node in group:
                queue.append(node)
                visited.add(node)
    return num, len(visited)

for i in range(1, n+1):
    info = list(map(int, input().split()))
    graph[i] = info[1:]
for i in range(1, n // 2 +1):
    comb = list(combinations(range(1, n+1), i))
    for c in comb:
        t1, n1 = bfs(c)
        t2, n2 = bfs([x for x in range(1, n+1) if x not in c])
        if n1 + n2 == n:
            result = min(result, abs(t1-t2))

print(result if result != sys.maxsize else -1)