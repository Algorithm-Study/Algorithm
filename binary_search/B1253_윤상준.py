n = int(input())
nums = sorted(list(map(int, input().split())))
total = 0
for i in range(n):
    if n <= 2:
        break
    left, right = 0, n-1
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        if nums[left] + nums[right] == nums[i]:
            total += 1
            break
        elif nums[left] + nums[right] > nums[i]:
            right -= 1
        else:
            left += 1
print(total)
# 투 포인터만 사용해도 문제 해결 가능
# 음수도 들어온다는 점을 유의할 것