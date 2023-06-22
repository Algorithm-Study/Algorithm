from collections import defaultdict

N = int(input())
graph = defaultdict(list)
visit = [0 for _ in range(N+1)]
for idx in range(N):
    graph[int(input())].append(idx+1)


def dfs(i, node):
    node.add(i)
    visit[i] = 1
    for g in graph[i]:
        if g not in node:
            dfs(g, node.copy())
        else:
            ans.extend(list(node))
            return


ans = []
for i in range(1, N+1):
    if not visit[i]:
        dfs(i, set([]))

ans.sort()
print(len(ans))
for i in ans:
    print(i)