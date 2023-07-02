n = int(input())
# 0: horizontal 1: vertical 2:  diagonal
field = []
dp = [[[0]*n for _ in range(n)] for _ in range(3)]
for _ in range(n):
    field.append(list(map(int, input().split())))
dp[0][0][1] = 1
for i in range(2,n):
    if field[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]
for i in range(1,n):
    for j in range(1,n):
        if field[i][j] == 0:
            # 가로(이전이 대각 or 가로)
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            # 세로(이전이 대각 or 세로)
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
        if field[i][j] == 0 and field[i-1][j] == 0 and field[i][j-1] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]

print(dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1])

# 시작 조건으로 인해 경우의 수가 많이 감소(처음은 가로 파이프로 시작)
# 현재 위치로 도달할 수 있는 방법이 3가지 존재하므로 이동방향에 대해 기록하기 위해서는 3차원 DP 필요
# 3치원 DP를 구성했다면 조건에 맞게 dp table 갱신하여 출력하면 되는 문제