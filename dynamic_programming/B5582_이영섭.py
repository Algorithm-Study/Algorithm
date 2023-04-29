A = input()
B = input()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1

print(max(map(max, dp)))

# 문제 접근 방법
# # 모든 경우에 대한 2차원 배열을 만들어서
# # dp로 값을 구하기