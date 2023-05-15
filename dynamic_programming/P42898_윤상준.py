def solution(m, n, puddles):
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] += dp[i-1][j] + dp[i][j-1]

    return dp[n][m] % 1_000_000_007

# m과 n 입력인 것처럼 puddles의 입력도 반대라서 이 점을 고려해야 함
# dp 크기를 행과 열 모두 1씩 늘리면 edge에 대한 고려 필요 X