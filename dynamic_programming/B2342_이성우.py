#  0 1 2 3 4 to
#0 0 2 2 2 2
#1 0 1 3 4 3
#2 0 3 1 3 4
#3 0 4 3 1 3
#4 0 3 4 3 1
# from
maps = [[0,2,2,2,2],[0,1,3,4,3],[0,3,1,3,4],[0,4,3,1,3],[0,3,4,3,1]]
INF = 1e8
l = list(map(int, input().split()))
# dp[n 번째 움직임][왼발위치][오른발위치]
dp = [[[INF for _ in range(5)] for _ in range(5)] for _ in range(len(l)+1)]
dp[0][0][0] = 0

for i in range(1, len(l)) :
    move = l[i-1]
    for left in range(5) :
        for right in range(5) :
            dp[i][move][right] = min(dp[i][move][right], dp[i-1][left][right] + maps[left][move])
            dp[i][left][move] = min(dp[i][left][move], dp[i-1][left][right] + maps[right][move])

result = INF
for i in range(5) :
    for j in range(5) :
        result = min(result, dp[len(l)-1][i][j])

print(result)

# 1 4 1 4 1 4 1 4
# 10
# 1 4 1 4 2 3 4
# 13