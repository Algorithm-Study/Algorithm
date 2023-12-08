n = int(input())
ls = []
dp = [1]*n
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a, b))
ls.sort()
print(ls)
for i in range(1, n):
    for j in range(0, i):
        if ls[j][1] < ls[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
