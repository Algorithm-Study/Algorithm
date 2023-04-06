n, k = map(int, input().split())

dp = [float('INF')]*100003

for i in range(max(n,k)+2):
    if i <= n:
        dp[i] = n - i
    else:
        if i % 2 == 0:
            dp[i] = min(dp[i-1] + 1, dp[i+1] + 1, dp[i//2])
        else:
            dp[i] = min(dp[i-1] + 1, dp[i+1] + 1)
        dp[i+1] = min(dp[i+1], dp[i] + 1)
        dp[i-1] = min(dp[i-1], dp[i] + 1)

print(dp[k])

# 왜 100003, max(n,k)+2는 되고 100002, max(n,k)+1은 안되는지
# max+1 까지 봐야하는데 max+1까지 보려면 for문에서 max+2까지 본다 그래서 배열은 max+2까지 있어야한다
# 최대값이 100,000에다가 +2 니까 배열은 100,003개 있어야한다