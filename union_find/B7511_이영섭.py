import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


t = int(input())
for tc in range(1, t+1):
    print(f"Scenario {tc}:")
    n = int(input())
    k = int(input())
    parent = [i for i in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)
    print()