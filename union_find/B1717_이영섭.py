import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(a):
    if parents[a] != a:
        parents[a] = find_parent(parents[a])
    return parents[a]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


n, m = map(int, input().rstrip().split())
parents = [i for i in range(n+1)]

for _ in range(m):
    x, a, b = map(int, input().rstrip().split())
    if x == 0:
        union(a, b)
    else:
        pa = find_parent(a)
        pb = find_parent(b)
        if pa == pb:
            print("YES")
        else:
            print("NO")