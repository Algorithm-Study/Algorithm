x = int(input())
arr = list(map(int, input().split()))
dp = [1 for i in range(x)]
for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
# 현재 기준으로 이전 값들을 순차적으로 비교하면서 dp table 갱신