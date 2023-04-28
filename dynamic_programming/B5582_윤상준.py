#LCS 유형과 비슷하지만 해당 문제는 완전 연속인 경우만 카운트하기 때문에 더 간단
a = input()
b = input()
n, m = len(a), len(b)
dp = [0] * (m+1)
answer = 0
for i in range(n):
    temp = [0] * (m+1)
    for j in range(m):
        if a[i] == b[j]:
            temp[j+1] = dp[j] + 1
    answer = max(answer, max(temp))
    dp = temp[:]
print(answer)
#이차원 DP 구현 시 python으로는 메모리 초과 -> PyPy3로만 해결 가능
a = input()
b = input()
n, m = len(a), len(b)
dp = [[0]*(m+1) for _ in range(n + 1)]
answer = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
    answer = max(answer, max(dp[i]))
print(answer)