n = int(input())
m = int(input())
parents = [x for x in range(0,n+1)]
def parent(x):
    if parents[x] == x:
        return x
    p = parent(parents[x])
    parents[x] = p
    return parents[x]

def union(x,y):
    x = parent(x)
    y = parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y
for i in range(1,n+1):
    nodes = list(map(int, input().split()))
    for idx,node in enumerate(nodes):
        if node == 1:
            union(i,idx+1)

route = list(map(int, input().split()))
start = parents[route[0]]
for i in range(1,m):
    if parents[route[i]] != start:
        print('NO')
        break
else:
    print('YES')