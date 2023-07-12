import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [i for i in range(N+1)]

def find(a):
    if arr[a] == a:
        return a
    x = find(arr[a])
    arr[a] = x
    return arr[a]
        
        
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b:
        return
    if a < b:
        arr[b] = a
    else:
        arr[a] = b
        
        
for _ in range(M):
    c, a, b = map(int, input().split())
    if c == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')