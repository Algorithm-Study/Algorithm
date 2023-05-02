# 변수 초기화
n = int(input())
arr = list(map(int, input().split()))
rev_arr = arr[::-1]
inc_dp = [1]*n
dec_dp = [1]*n

for i in range(n):
    for j in range(i):
        # 증가하는 부분 수열 계산
        if arr[i] > arr[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j]+1)
        # 뒤집어서 감소하는 부분 수열 계산
        if rev_arr[i] > rev_arr[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j]+1)

# 만나는 지점들중에서 최대값 계산
print(max([inc_dp[i]+dec_dp[n-i-1] for i in range(n)])-1)