n, k = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
nums = [0]*100_001
ans = 0
while right < n:
    nums[arr[right]] += 1
    if nums[arr[right]] == k + 1:
        while True:
            nums[arr[left]] -= 1
            left += 1
            if arr[left-1] == arr[right]:
                break
    ans = max(ans, right - left + 1)
    right += 1
print(ans)