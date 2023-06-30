n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()

left = 1
right = arr[-1] - arr[0]
answer = 0

while left <= right:
    mid = (left+right) // 2
    now = arr[0]
    cnt = 1
    
    for i in range(1, n):
        if arr[i] >= now + mid:
            cnt += 1
            now = arr[i]
    
    if cnt >= c:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
        
print(answer)
    