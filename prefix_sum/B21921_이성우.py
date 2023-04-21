n, x = map(int, input().split())

nums = list(map(int,input().split()))

dp = [0]*(n+1)
dp[x] = sum(nums[:x])
for i in range(x+1,n+1):
    dp[i] = dp[i-1] - nums[i-x-1] + nums[i-1]

max_dp = max(dp)
if max_dp == 0:
    print('SAD')
else:
    print(f'{max_dp}\n{dp.count(max_dp)}')