n = int(input())
p = list(map(int, input().split()))
m = int(input())
dp = [0]*(m+1)
for i in range(n-1, -1, -1):
    i_cost = p[i]
    for now_cost in range(i_cost, m+1):
        dp[now_cost] = max(dp[now_cost], i, dp[now_cost-i_cost]*10+i)

print(dp[m])