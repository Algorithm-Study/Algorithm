import sys
input = sys.stdin.readline

# 변수 초기화
n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]

# 프로이드 워셜 탐색
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

# dp값과 시간 비교 후 결과 출력
for _ in range(m):
    a, b, c = map(int, input().split())
    if dp[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")