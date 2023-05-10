T = int(input())
for _ in range(T):
    K = int(input())
    data = list(map(int, input().split()))
    dp = [[0]*K for i in range(K)]
    sum = [0]
    for dt in data:
        sum.append(sum[-1] + dt)
    for d in range(1, K):
        for i in range(K-d):
            j = d + i
            dp[i][j] = float("inf")
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + sum[j+1] - sum[i])
    print(dp[0][K-1])
    
# 문제 접근 방법
# # 연쇄 행렬 최소 곱셈 알고리즘의 변형
# # prefix sum과 나눠지는 값인 k를 선정하는 for문을 작성할 수 있어야 풀 수 있음