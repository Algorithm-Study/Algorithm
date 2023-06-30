k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

left = 1 # 0이면 ZeroDivisionError가 발생할 수 있음
right = max(arr)

while left <= right:
    mid = (left+right)//2
    cnt = 0
    for num in arr:
        cnt += num//mid
    
    if cnt < n:
        right = mid - 1
    else:
        left = mid + 1

print(right) # 최대값을 찾기때문에 right 출력