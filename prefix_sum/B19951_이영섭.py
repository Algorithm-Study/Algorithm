N, M = map(int, input().split())
H = list(map(int, input().split()))
order, dp = [0]*(N+1), [0]*(N+1)

for _ in range(M):
    a, b, k = map(int, input().split())
    order[a-1] += k
    order[b] -= k

dp[0] = order[0]
for i in range(1, N+1):
    dp[i] = dp[i-1] + order[i]

for i in range(N):
    print(H[i] + dp[i], end=" ")
