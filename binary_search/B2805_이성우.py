n, m = list(map(int, input().split()))

arr = list(map(int, input().split()))

start, end = 0, max(arr) # 2000000000

result = 0
while start <= end:

    mid = (start + end) // 2
    total = sum([x - mid if x > mid else 0 for x in arr])
    # 아래 보다 위의 List Comprehension이 더 빠름
    # total = 0
    # for x in arr:
    #     if x > mid:
    #         total += x - mid
            
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)