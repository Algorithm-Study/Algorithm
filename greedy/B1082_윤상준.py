n = int(input())
price = list(map(int, input().split()))
m = int(input())
dp = [-1 for _ in range(m+1)]
for i in range(n-1,-1,-1):
    temp = price[i]
    for j in range(temp,m+1):
        dp[j] = max(dp[j],i, dp[j-temp]*10 + i)
print(dp[-1])