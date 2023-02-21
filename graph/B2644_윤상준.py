n = int(input())
X, Y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
result = []

for _ in range(m):
  x, y = map(int, input().split())  
  graph[x].append(y)
  graph[y].append(x)

def dfs(v, num):
    num += 1
    visited[v] = True

    if v == Y:
        result.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)
    return result


result = dfs(X, 0)
if len(result) == 0:
  print(-1)
else:
  print(result[0]-1)