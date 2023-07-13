import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
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
t = int(input())
for i in range(t):
    n = int(input())
    k = int(input())
    parent = [x for x in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        union(x,y)
    m = int(input())
    print(f'Scenario {i+1}:')
    for _ in range(m):
        x,y = map(int, input().split())
        if find(x) == find(y):
            print(1)
        else:
            print(0)
    print()
# 유니온 파인드 기본 유형
# sys 사용이 필수