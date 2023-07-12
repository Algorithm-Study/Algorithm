import sys
sys.setrecursionlimit(10**5)
n, m = map(int, input().split())
parent = [x for x in range(n+1)]
def find(x):
    if parent[x] == x:
        return x
    p = find(parent[x])
    parent[x] = p
    return parent[x]

def union(a,b):
    p1, p2 = find(a), find(b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2 
for _ in range(m):
    op,x,y = map(int, input().split())
    if op == 0:
        union(x,y)
    else:
        if find(x) != find(y):
            print('NO')
        else:
            print('YES')

# union find를 진행하는 중간에 요청이 들어오면 같은 부모를 가지고 있는지 체크하여 출력하면 됨.