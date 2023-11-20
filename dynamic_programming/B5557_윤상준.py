n = int(input())
data = list(map(int, input().split()))
dp = [[0]*21 for i in range(n-1)]
dp[0][data[0]] = 1
for i in range(1, n-1):
    for j in range(21):
        # n번째 값을 빼도 양수인 경우
        if j-data[i]>=0: 
            dp[i][j-data[i]] += dp[i-1][j]
        # n번째 값을 더해도 20을 넘지 않는 경우
        if j+data[i]<=20: 
            dp[i][j+data[i]] += dp[i-1][j]
# 마지막 숫자가 나오는 경우의 수 출력
print(dp[-1][data[-1]])