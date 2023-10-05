import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [_ for _ in range(n+1)]
arr = []

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])
arr.sort(key = lambda x : x[2])

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]
    
    
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

answer = 0
for a, b, c in arr:
    if find_parent(a) != find_parent(b):
        union(a, b)
        answer += c
        
print(answer)