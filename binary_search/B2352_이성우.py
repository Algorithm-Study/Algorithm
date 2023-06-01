from bisect import bisect
import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
dp = [s[0]]
for i in range(1, n):
    if s[i] > dp[-1]:
        dp.append(s[i])
    else:
        dp[bisect(dp, s[i])] = s[i]
print(dp)
print(len(dp))