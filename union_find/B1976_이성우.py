N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parents = list(range(N))
path = list(map(int, input().split()))


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]
    
    
def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        parents[x] = y
    else:
        parents[y] = x
        
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            union(i, j)
            
answer = 'YES'
for i in range(1, M):
    if parents[path[i] - 1] != parents[path[0] - 1]:
        answer = 'NO'
        break

print(answer)