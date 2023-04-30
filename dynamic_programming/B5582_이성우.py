n = input()
m = input()

dp=[[0] * (len(m) + 1) for _ in range(len(n) + 1)]

for i in range(1, len(n)+1):
    for j in range(1, len(m)+1):
        if n[i-1] == m[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp)
print(max(map(max, dp)))