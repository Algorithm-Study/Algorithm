n = int(input())
nums = list(map(int, input().split()))
budget = int(input())

### max_num = max(nums)면 아래 조건문 없어도 작동
# if sum(nums) <= budget:
#     print(max(nums))
# else:

min_num = 0
max_num = 100000
mid_num = (min_num + max_num)//2
while min_num <= max_num: # 등호 없어서 틀렸었음

    total = sum( num if num < mid_num else mid_num for num in nums )

    if total < budget:
        min_num = mid_num + 1
        mid_num = (min_num + max_num)//2
    elif total > budget:
        max_num = mid_num - 1
        mid_num = (min_num + max_num)//2
    else:
        break
print(mid_num)