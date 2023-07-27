n = list(map(int, input()))
dp = [0 for _ in range(len(n)+1)]

if (n[0] == 0):
    print('0')
else:
    n = [0] + n
    dp[0] = dp[1] = 1
    for i in range(2, len(n)):
        if n[i] > 0:
            dp[i] += dp[i-1]
        tmp = n[i-1]*10 + n[i]
        if 10 <= tmp <= 26:
            dp[i] += dp[i-2]
    print(dp[len(n)-1]%1_000_000)
    