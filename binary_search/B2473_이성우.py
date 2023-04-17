import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
# print(nums)
ref = 3e9
answer = []

for i in range(n-2):
    start = i+1
    end = n-1
    
    while start < end:
        num_sum = nums[i] + nums[start] + nums[end]
        if abs(ref) >= abs(num_sum):
            ref = num_sum
            answer = [nums[i], nums[start], nums[end]]

        if num_sum < 0:
            start += 1
        elif num_sum > 0:
            end -= 1
        else:
            print(*answer)
            exit(0)

print(*answer)

#PyPy3로 제출해야함