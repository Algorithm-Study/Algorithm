n = int(input())
m = int(input())
x = list(map(int, input().split()))
arr = list(range(n))

left, right = 1, 100_000
answer = float('inf')
while left <= right:
    pos = 0
    mid = (left+right)//2
    for num in x:
        if num - mid <= pos:
            pos = num + mid
        else:
            left = mid + 1
            break
    else:
        if pos >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    
print(answer)