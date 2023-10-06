import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

arr = [[INF if i != j else 0 for i in range(n+1)] for j in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 or b == -1:
        break
    arr[a][b] = 1
    arr[b][a] = 1
    
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
                arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
answer = []
for i in range(1, n+1):
    answer.append(max([i for i in arr[i] if i != INF]))
tmp = min(answer)
print(tmp, answer.count(tmp))
print(*[i+1 for i in range(n) if answer[i] == tmp])