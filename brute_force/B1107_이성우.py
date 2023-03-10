target = int(input())
n = int(input())

if n != 0:
    broken = list(map(str, input().split()))
else:
    broken = []
    
min_click = abs(100 - target)

for nums in range(1000000):
    nums = str(nums)
    
    for i in nums:
        if i in broken:
            break
    else:
        min_click = min(min_click, abs(int(nums) - target) + len(nums))

print(min_click)