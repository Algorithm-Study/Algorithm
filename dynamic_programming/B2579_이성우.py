n = int(input())

nums = [0]*301
for i in range(1,n+1):
    nums[i] = int(input())
    

dp = [0]*301
dp[1] = nums[1]
dp[2] = nums[2] + nums[1]
dp[3] = max(nums[3] + nums[2],
            nums[3] + nums[1])

for i in range(4,n+1):
    dp[i] = nums[i] + max(nums[i-1] + dp[i-3], dp[i-2])
    
print(dp[n])

# 미리 공간을 안만들고 n개 만큼 공간을 맞춰서 만들면 n이 3보다 작을 때 IndexError발생
