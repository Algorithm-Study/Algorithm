from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
prefix_sum = defaultdict(int)
temp, ans = 0, 0
for i in A:
    temp += i
    if temp == K:
        ans += 1
    ans += prefix_sum[temp - K]
    prefix_sum[temp] += 1
print(ans)