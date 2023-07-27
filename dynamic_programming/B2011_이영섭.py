word = ['0'] + list(input())

if word[1] == '0':
    print(0)
    exit()

length = len(word)
dp = [0] * length
dp[0], dp[1] = 1, 1

for i in range(2, length):
    num = int(word[i])
    deci = int(word[i-1])*10 + int(word[i])
    if num > 0:
        dp[i] += dp[i-1]
    if 10 <= deci <= 26:
        dp[i] += dp[i-2]

print(dp[length-1] % 1000000)
