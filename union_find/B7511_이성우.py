import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def find(a):
    if arr[a] != a:
        arr[a] = find(arr[a])
    return arr[a]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        arr[b] = a
    else:
        arr[a] = b
        

for i in range(int(input())):
    N = int(input())
    K = int(input())
    arr = list(range(N))
    
    for _ in range(K):
        a, b = map(int, input().split())
        if find(a) != find(b):
            union(a, b)
            
    print(f'Scenario {i+1}:')
    
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()
    