tc = int(input())

for i in range(tc):
    column = int(input())
    row1 = list(map(int,input().split()))
    row2 = list(map(int,input().split()))
    matrix = [row1, row2]
    dp = [[0]*column for _ in range(2)]
    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]
    if column > 1:
        dp[0][1] = dp[1][0] + matrix[0][1]
        dp[1][1] = dp[0][0] + matrix[1][1]
        for j in range(2,column):
            dp[0][j] = max(dp[1][j-1],dp[1][j-2]) + matrix[0][j]
            dp[1][j] = max(dp[0][j-1],dp[0][j-2]) + matrix[1][j]
    print(max(dp[0][column-1],dp[1][column-1]))