n = int(input())
arr = list(map(int, input().split()))
k = int(input())

s = [0]
for num in range(n):
    s.append(s[num]+arr[num])

dp = [[0]*(n+1) for _ in range(4)]

for i in range(1,4):
    for j in range(i*k, n+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], s[j] - s[j-k])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + s[j] - s[j-k])

print(dp[3][n])