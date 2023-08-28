import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

k = int(input())

def dfs(start, group):
    visited[start] = group
    for i in graph[start]:
        if not visited[i]:
            tmp = dfs(i, -group)
            if not tmp:
                return False
        elif visited[i] == visited[start]:
            return False
    return True

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    visited = [False]*(v+1)
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print("YES" if result else "NO")