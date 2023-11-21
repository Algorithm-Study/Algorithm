import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
arr = [_ for _ in range(n+1)]

def find_parent(x):
    if arr[x] != x:
        arr[x] = find_parent(arr[x])
        
    return arr[x]


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        if cost[x] <= cost[y]:
            arr[y] = x
        else: # x > y 일 때
            arr[x] = y


for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

answer = 0
for idx, root in enumerate(arr):
    if idx == root:
        answer += cost[idx]
        
if answer <= k:
    print(answer)
else:
    print("Oh no")
