N, target = map(int, input().split())
arr = [ i for i in range(10001)]
shortcut = [list(map(int, input().split())) for _ in range(N)]

for i in range(1,target+1):
    arr[i] = min(arr[i], arr[i-1]+1)
    for start, end, cost in shortcut:
        arr[end] = min(arr[end], cost + arr[start])
        
print(arr[target])