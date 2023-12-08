import sys
input = sys.stdin.readline

n = int(input())
edge = [list(map(int, input().split())) for _ in range(n)]
edge.sort()
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if edge[j][1] < edge[i][1]:
            dp[i] = max(dp[i], dp[j]+1)
print(n-max(dp))