import sys
input = sys.stdin.readline
n = int(input().rstrip())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1
    if i < n-1 and arr[i] == arr[i+1]:
        dp[i][i+1] = 1
        
for k in range(n-2):
    for i in range(n-2-k):
        j = i+2+k
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for _ in range(int(input().rstrip())):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])