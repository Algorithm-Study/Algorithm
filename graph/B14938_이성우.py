n, m, r = map(int, input().split())
item = list(map(int, input().split()))
arr = [[float('inf')]*n for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1], c)
    arr[b-1][a-1] = min(arr[b-1][a-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
            if i == j:
                arr[i][j] = 0
   
answer = 0

for i in range(n):
    tmp = 0
    for j in range(n):
        if arr[i][j] <= m:
            tmp += item[j]
            
    answer = max(answer, tmp)
    
print(answer)