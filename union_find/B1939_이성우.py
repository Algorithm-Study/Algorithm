import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a
    
    
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

def check(a, b):
    return find(a) == find(b)


parent = [_ for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([-c, a, b])

s, e = map(int, input().split())

arr.sort()
for i in arr:
    c, a, b = i[0], i[1], i[2]
    c = abs(c)
    union(a, b)
    if check(s, e):
        print(c)
        break
        