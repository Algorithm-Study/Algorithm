h, w = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
for idx in range(1, w-1):
    left = max(arr[:idx])
    right = max(arr[idx+1:])
    
    standard = min(left, right)
    if arr[idx] < standard:
        ans += standard - arr[idx]

print(ans)