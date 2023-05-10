tc = int(input())

for _ in range(tc):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    # S[i]는 1~i번까지의 누적합
    S = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        S[i] = S[i-1] + arr[i]
        
    # dp[i][j]는 i~j까지 합치는데 필요한 최소 비용
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, n+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + (S[j+i-1] - S[j-1])

    print(dp[1][n])