import sys
input = sys.stdin.readline

# 초기값 설정
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]
answer = 0

# dp 탐색
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            answer = max(answer, dp[i][j])
print(answer**2)