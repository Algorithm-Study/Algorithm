n, m = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, max(data)
answer = 0
while start <= end:
    mid = (start + end)//2
    min_val, max_val = data[0], data[0]
    count = 1
    for i in range(1,n):
        min_val = min(min_val, data[i])
        max_val = max(max_val, data[i])
        if max_val - min_val > mid:
            count += 1
            max_val = data[i]
            min_val = data[i]
    if count <= m:
        end = mid -1
        answer = mid
    else:
        start = mid + 1
print(answer)