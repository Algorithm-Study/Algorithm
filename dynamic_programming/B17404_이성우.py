n = int(input())

maps = [list(map(int, input().split())) for _ in range(n)]

answer = float('inf')

for k in range(3):
    dp = [[float('inf') for _ in range(3)] for _ in range(n)]
    dp[0][k] = maps[0][k]
    for i in range(1, n):
        for j in range(3):
            dp[i][j] = maps[i][j] + min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
    # print(dp)
    answer = min(answer, dp[n-1][(k+1)%3], dp[n-1][(k+2)%3])

print(answer)

# 시작을 정하고 시작할 때는 나머지 값을 inf로 만들어줘서 고르지 않게 한다