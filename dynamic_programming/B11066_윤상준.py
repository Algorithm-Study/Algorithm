# 합치는 과정에서 소설 챕터의 연속성이 보장되어야 함
# 파일 합치기3(13975)와 다른 방식
t = int(input())
for _ in range(t):
    total = 0
    k = int(input())
    files = [0] + list(map(int, input().split()))
    culsum = [0 for _ in range(k+1)]
    for i in range(1,k+1):
        culsum[i] = culsum[i-1] + files[i]
    dp = [[0]*(k+1) for _ in range(k+1)]
    for i in range(2, k+1):
        for j in range(1, k - i + 2):
            dp[j][j+i-1] = min([dp[j][j+l] + dp[j+l+1][j+i-1] for l in range(i-1)]) + (culsum[j+i-1] - culsum[j-1])
    print(dp[1][k])
    
