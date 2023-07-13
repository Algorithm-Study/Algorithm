import sys
n, m = map(int, input().split())
dp = []
max_value = -sys.maxsize
dp.append([0]*(m+1))
for i in range(n):
    dp.append([0]+list(map(int, input().split())))
for i in range(1,n+1):
    column_prefix = [0]*(m+1)
    for j in range(i,n+1):
        row_prefix = [0]*(m+1)
        for k in range(1,m+1):
            column_prefix[k] += dp[j][k]
            row_prefix[k] = max(row_prefix[k-1] + column_prefix[k], column_prefix[k])
            max_value = max(max_value,row_prefix[k])
print(max_value)
# 4중 for문 방식으로도 풀 수 있지만 3중 for문으로 줄일 수 있음