n = int(input())
passengers = list(map(int, input().split()))
k = int(input())
dp = [[0]*(n+1) for _ in range(4)]
# 포함하지 않는 경우도 있으므로 0 추가
prefix = [0]
temp = 0
for passenger in passengers:
    temp += passenger
    prefix.append(temp)
for i in range(1,4):
    for j in range(i*k,n+1):
        if i == 1:
            dp[i][j] = max(dp[i][j-1], prefix[j] - prefix[j-k])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + prefix[j] - prefix[j-k])
print(dp[-1][-1])
# DP를 무조건 만들어야 함
# 객차의 순서나 조합은 고려하지 않아도 되기 때문에 이를 기반으로 점화식 구해야 함
# 이전 선택을 계속 유지하거나 이전 k이전 객차의 최대값과 k개 구간의 누적합의 합과 비교하는 방식으로 진행