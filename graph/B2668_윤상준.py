n = int(input())
field = [0]*(n+1)
for i in range(1,n+1):
    field[i] = int(input())
result = []
def dfs(x,start):
    visited[x] = 1
    if not visited[field[x]]:
        dfs(field[x],start)
    elif visited[field[x]] and field[x] == start:
        result.append(field[x])
        print(start, result)
    
for i in range(1,n+1):
    visited = [0]*(n+1)
    dfs(i, i)
print(len(result))
for r in result:
    print(r)
# 출발해서 자신에게 돌아올 수 있는 값들만 구하면 되는 문제