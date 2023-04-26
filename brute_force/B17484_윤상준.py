# 이전 값을 확인할 때 셋 모두 소모 연료량이 같은 경우를 고려해야 함
# 이전 값이 선택한 왼쪽, 위, 오른쪽에 대한 모든 경우의 수를 고려해야 함
# 입력 값 양쪽애 값을 넣어서 위치에 상관 없이 dp 계산되도록 처리
n, m = map(int, input().split())

INF = 100*7
dp = [[INF]*3] + [[x]*3 for x in list(map(int, input().split()))] + [[INF]*3]

for i in range(n-1):
    fuel = [INF]+list(map(int, input().split()))+[INF]
    temp = [[INF]*3] + [[0]*3 for _ in range(m)] + [[INF]*3]
    for j in range(1, m+1):
        temp[j][0] = min(dp[j + 1][1], dp[j + 1][2]) + fuel[j]
        temp[j][1] = min(dp[j][0], dp[j][2]) + fuel[j]
        temp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + fuel[j]
    dp = temp

print(min(map(min, dp)))