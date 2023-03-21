def solution(triangle):
    N = len(triangle)
    dp = [[0]*(i+1) for i in range(N)]
    dp[0][0] = triangle[0][0]
    for i in range(1,N):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) + triangle[i][j]
    # print(dp)
    answer = max(dp[N-1])
    return answer